program tra_adv
  use iso_c_binding, only : c_int64_t
  integer, parameter :: wp = 8
  real(kind=wp), allocatable, dimension(:,:,:,:) :: t3sn
  real(kind=wp), allocatable, dimension(:,:,:,:) :: t3ns
  real(kind=wp), allocatable, dimension(:,:,:,:) :: t3ew
  real(kind=wp), allocatable, dimension(:,:,:,:) :: t3we
  real(kind=wp), allocatable, dimension(:,:,:) :: tsn
  real(kind=wp), allocatable, dimension(:,:,:) :: pun
  real(kind=wp), allocatable, dimension(:,:,:) :: pvn
  real(kind=wp), allocatable, dimension(:,:,:) :: pwn
  real(kind=wp), allocatable, dimension(:,:,:) :: mydomain
  real(kind=wp), allocatable, dimension(:,:,:) :: zslpx
  real(kind=wp), allocatable, dimension(:,:,:) :: zslpy
  real(kind=wp), allocatable, dimension(:,:,:) :: zwx
  real(kind=wp), allocatable, dimension(:,:,:) :: zwy
  real(kind=wp), allocatable, dimension(:,:,:) :: umask
  real(kind=wp), allocatable, dimension(:,:,:) :: vmask
  real(kind=wp), allocatable, dimension(:,:,:) :: tmask
  real(kind=wp), allocatable, dimension(:,:,:) :: zind
  real(kind=wp), allocatable, dimension(:,:) :: ztfreez
  real(kind=wp), allocatable, dimension(:,:) :: rnfmsk
  real(kind=wp), allocatable, dimension(:,:) :: upsmsk
  real(kind=wp), allocatable, dimension(:) :: rnfmsk_z
  real(kind=wp) :: zice
  real(kind=wp) :: zu
  real(kind=wp) :: z0u
  real(kind=wp) :: zzwx
  real(kind=wp) :: zv
  real(kind=wp) :: z0v
  real(kind=wp) :: zzwy
  real(kind=wp) :: ztra
  real(kind=wp) :: zbtr
  real(kind=wp) :: zdt
  real(kind=wp) :: zalpha
  real(kind=wp) :: r
  real(kind=wp) :: zw
  real(kind=wp) :: z0w
  integer :: jpi
  integer :: jpj
  integer :: jpk
  integer :: ji
  integer :: jj
  integer :: jk
  integer :: jt
  integer(kind=c_int64_t) :: it
  CHARACTER(LEN = 10) :: env

  call get_environment_variable('JPI', env)
  READ(env, '(i10)') jpi
  call get_environment_variable('JPJ', env)
  READ(env, '(i10)') jpj
  call get_environment_variable('JPK', env)
  READ(env, '(i10)') jpk
  call get_environment_variable('IT', env)
  READ(env, '(i10)') it
  ALLOCATE(mydomain(jpi, jpj, jpk))
  ALLOCATE(zwx(jpi, jpj, jpk))
  ALLOCATE(zwy(jpi, jpj, jpk))
  ALLOCATE(zslpx(jpi, jpj, jpk))
  ALLOCATE(zslpy(jpi, jpj, jpk))
  ALLOCATE(pun(jpi, jpj, jpk))
  ALLOCATE(pvn(jpi, jpj, jpk))
  ALLOCATE(pwn(jpi, jpj, jpk))
  ALLOCATE(umask(jpi, jpj, jpk))
  ALLOCATE(vmask(jpi, jpj, jpk))
  ALLOCATE(tmask(jpi, jpj, jpk))
  ALLOCATE(zind(jpi, jpj, jpk))
  ALLOCATE(ztfreez(jpi, jpj))
  ALLOCATE(rnfmsk(jpi, jpj))
  ALLOCATE(upsmsk(jpi, jpj))
  ALLOCATE(rnfmsk_z(jpk))
  ALLOCATE(tsn(jpi, jpj, jpk))
  r = jpi * jpj * jpk
  do jk = 1, jpk, 1
    do jj = 1, jpj, 1
      do ji = 1, jpi, 1
        umask(ji,jj,jk) = ji * jj * jk / r
        mydomain(ji,jj,jk) = ji * jj * jk / r
        pun(ji,jj,jk) = ji * jj * jk / r
        pvn(ji,jj,jk) = ji * jj * jk / r
        pwn(ji,jj,jk) = ji * jj * jk / r
        vmask(ji,jj,jk) = ji * jj * jk / r
        tsn(ji,jj,jk) = ji * jj * jk / r
        tmask(ji,jj,jk) = ji * jj * jk / r
      enddo
    enddo
  enddo
  r = jpi * jpj
  do jj = 1, jpj, 1
    do ji = 1, jpi, 1
      ztfreez(ji,jj) = ji * jj / r
      upsmsk(ji,jj) = ji * jj / r
      rnfmsk(ji,jj) = ji * jj / r
    enddo
  enddo
  do jk = 1, jpk, 1
    rnfmsk_z(jk) = jk / jpk
  enddo
  do jt = 1, it, 1
    do jk = 1, jpk, 1
      do jj = 1, jpj, 1
        do ji = 1, jpi, 1
          if (tsn(ji,jj,jk) <= ztfreez(ji,jj) + 0.1d0) then
            zice = 1.d0
          else
            zice = 0.d0
          end if
          zind(ji,jj,jk) = MAX(rnfmsk(ji,jj) * rnfmsk_z(jk), upsmsk(ji,jj), zice) * tmask(ji,jj,jk)
          zind(ji,jj,jk) = 1 - zind(ji,jj,jk)
        enddo
      enddo
    enddo
    !$acc data copyin(pun,pvn,pwn,tmask,umask,vmask,zind) copyout(zslpx,zslpy,zwx,zwy) copy(mydomain)
    !$acc kernels default(present)
    zwx(:,:,jpk) = 0.e0
    zwy(:,:,jpk) = 0.e0
    do jk = 1, jpk - 1, 1
      do jj = 1, jpj - 1, 1
        do ji = 1, jpi - 1, 1
          zwx(ji,jj,jk) = umask(ji,jj,jk) * (mydomain(ji + 1,jj,jk) - mydomain(ji,jj,jk))
          zwy(ji,jj,jk) = vmask(ji,jj,jk) * (mydomain(ji,jj + 1,jk) - mydomain(ji,jj,jk))
        enddo
      enddo
    enddo
    zslpx(:,:,jpk) = 0.e0
    zslpy(:,:,jpk) = 0.e0
    do jk = 1, jpk - 1, 1
      do jj = 2, jpj, 1
        do ji = 2, jpi, 1
          zslpx(ji,jj,jk) = (zwx(ji,jj,jk) + zwx(ji - 1,jj,jk)) * (0.25d0 + SIGN(0.25d0, zwx(ji,jj,jk) * zwx(ji - 1,jj,jk)))
          zslpy(ji,jj,jk) = (zwy(ji,jj,jk) + zwy(ji,jj - 1,jk)) * (0.25d0 + SIGN(0.25d0, zwy(ji,jj,jk) * zwy(ji,jj - 1,jk)))
        enddo
      enddo
    enddo
    do jk = 1, jpk - 1, 1
      do jj = 2, jpj, 1
        do ji = 2, jpi, 1
          zslpx(ji,jj,jk) = SIGN(1.d0, zslpx(ji,jj,jk)) * MIN(ABS(zslpx(ji,jj,jk)), 2.d0 * ABS(zwx(ji - 1,jj,jk)), 2.d0 * &
&ABS(zwx(ji,jj,jk)))
          zslpy(ji,jj,jk) = SIGN(1.d0, zslpy(ji,jj,jk)) * MIN(ABS(zslpy(ji,jj,jk)), 2.d0 * ABS(zwy(ji,jj - 1,jk)), 2.d0 * &
&ABS(zwy(ji,jj,jk)))
        enddo
      enddo
    enddo
    do jk = 1, jpk - 1, 1
      zdt = 1
      do jj = 2, jpj - 1, 1
        do ji = 2, jpi - 1, 1
          z0u = SIGN(0.5d0, pun(ji,jj,jk))
          zalpha = 0.5d0 - z0u
          zu = z0u - 0.5d0 * pun(ji,jj,jk) * zdt
          zzwx = mydomain(ji + 1,jj,jk) + zind(ji,jj,jk) * (zu * zslpx(ji + 1,jj,jk))
          zzwy = mydomain(ji,jj,jk) + zind(ji,jj,jk) * (zu * zslpx(ji,jj,jk))
          zwx(ji,jj,jk) = pun(ji,jj,jk) * (zalpha * zzwx + (1. - zalpha) * zzwy)
          z0v = SIGN(0.5d0, pvn(ji,jj,jk))
          zalpha = 0.5d0 - z0v
          zv = z0v - 0.5d0 * pvn(ji,jj,jk) * zdt
          zzwx = mydomain(ji,jj + 1,jk) + zind(ji,jj,jk) * (zv * zslpy(ji,jj + 1,jk))
          zzwy = mydomain(ji,jj,jk) + zind(ji,jj,jk) * (zv * zslpy(ji,jj,jk))
          zwy(ji,jj,jk) = pvn(ji,jj,jk) * (zalpha * zzwx + (1.d0 - zalpha) * zzwy)
        enddo
      enddo
    enddo
    do jk = 1, jpk - 1, 1
      do jj = 2, jpj - 1, 1
        do ji = 2, jpi - 1, 1
          zbtr = 1.
          ztra = -zbtr * (zwx(ji,jj,jk) - zwx(ji - 1,jj,jk) + zwy(ji,jj,jk) - zwy(ji,jj - 1,jk))
          mydomain(ji,jj,jk) = mydomain(ji,jj,jk) + ztra
        enddo
      enddo
    enddo
    zwx(:,:,1) = 0.e0
    zwx(:,:,jpk) = 0.e0
    do jk = 2, jpk - 1, 1
      zwx(:,:,jk) = tmask(:,:,jk) * (mydomain(:,:,jk - 1) - mydomain(:,:,jk))
    enddo
    zslpx(:,:,1) = 0.e0
    do jk = 2, jpk - 1, 1
      do jj = 1, jpj, 1
        do ji = 1, jpi, 1
          zslpx(ji,jj,jk) = (zwx(ji,jj,jk) + zwx(ji,jj,jk + 1)) * (0.25d0 + SIGN(0.25d0, zwx(ji,jj,jk) * zwx(ji,jj,jk + 1)))
        enddo
      enddo
    enddo
    do jk = 2, jpk - 1, 1
      do jj = 1, jpj, 1
        do ji = 1, jpi, 1
          zslpx(ji,jj,jk) = SIGN(1.d0, zslpx(ji,jj,jk)) * MIN(ABS(zslpx(ji,jj,jk)), 2.d0 * ABS(zwx(ji,jj,jk + 1)), 2.d0 * &
&ABS(zwx(ji,jj,jk)))
        enddo
      enddo
    enddo
    zwx(:,:,1) = pwn(:,:,1) * mydomain(:,:,1)
    zdt = 1
    zbtr = 1.
    do jk = 1, jpk - 1, 1
      do jj = 2, jpj - 1, 1
        do ji = 2, jpi - 1, 1
          z0w = SIGN(0.5d0, pwn(ji,jj,jk + 1))
          zalpha = 0.5d0 + z0w
          zw = z0w - 0.5d0 * pwn(ji,jj,jk + 1) * zdt * zbtr
          zzwx = mydomain(ji,jj,jk + 1) + zind(ji,jj,jk) * (zw * zslpx(ji,jj,jk + 1))
          zzwy = mydomain(ji,jj,jk) + zind(ji,jj,jk) * (zw * zslpx(ji,jj,jk))
          zwx(ji,jj,jk + 1) = pwn(ji,jj,jk + 1) * (zalpha * zzwx + (1. - zalpha) * zzwy)
        enddo
      enddo
    enddo
    zbtr = 1.
    do jk = 1, jpk - 1, 1
      do jj = 2, jpj - 1, 1
        do ji = 2, jpi - 1, 1
          ztra = -zbtr * (zwx(ji,jj,jk) - zwx(ji,jj,jk + 1))
          mydomain(ji,jj,jk) = ztra
        enddo
      enddo
    enddo
    !$acc end kernels
    !$acc end data
  enddo
  OPEN(UNIT = 4, FILE = 'output.dat', FORM = 'formatted')
  do jk = 1, jpk - 1, 1
    do jj = 2, jpj - 1, 1
      do ji = 2, jpi - 1, 1
        WRITE(4, *) mydomain(ji, jj, jk)
      enddo
    enddo
  enddo
  CLOSE(UNIT = 4)
  DEALLOCATE(mydomain)
  DEALLOCATE(zwx)
  DEALLOCATE(zwy)
  DEALLOCATE(zslpx)
  DEALLOCATE(zslpy)
  DEALLOCATE(pun)
  DEALLOCATE(pvn)
  DEALLOCATE(pwn)
  DEALLOCATE(umask)
  DEALLOCATE(vmask)
  DEALLOCATE(tmask)
  DEALLOCATE(zind)
  DEALLOCATE(ztfreez)
  DEALLOCATE(rnfmsk)
  DEALLOCATE(upsmsk)
  DEALLOCATE(rnfmsk_z)
  DEALLOCATE(tsn)

end program tra_adv
