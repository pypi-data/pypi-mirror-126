PROGRAM tra_adv
 USE dl_timer , ONLY: timer_init , timer_register , timer_start , timer_stop , timer_report
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: t3sn ( : , : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: t3ns ( : , : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: t3ew ( : , : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: t3we ( : , : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: tsn ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: pun ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: pvn ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: pwn ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: mydomain ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: zslpx ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: zslpy ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: zwx ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: zwy ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: umask ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: vmask ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: tmask ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: zind ( : , : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: ztfreez ( : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: rnfmsk ( : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: upsmsk ( : , : )
 REAL ( KIND= 8 ) , SAVE , ALLOCATABLE :: rnfmsk_z ( : )
 REAL ( KIND= 8 ) :: zice
 REAL ( KIND= 8 ) :: zu
 REAL ( KIND= 8 ) :: z0u
 REAL ( KIND= 8 ) :: zzwx
 REAL ( KIND= 8 ) :: zv
 REAL ( KIND= 8 ) :: z0v
 REAL ( KIND= 8 ) :: zzwy
 REAL ( KIND= 8 ) :: ztra
 REAL ( KIND= 8 ) :: zbtr
 REAL ( KIND= 8 ) :: zdt
 REAL ( KIND= 8 ) :: zalpha
 REAL ( KIND= 8 ) :: r
 REAL ( KIND= 8 ) :: zw
 REAL ( KIND= 8 ) :: z0w
 INTEGER :: jpi
 INTEGER :: jpj
 INTEGER :: jpk
 INTEGER :: ji
 INTEGER :: jj
 INTEGER :: jk
 INTEGER :: jt
 INTEGER ( KIND= 8 ) :: it
 CHARACTER ( LEN= 10 ) :: env
 INTEGER :: init_timer
 INTEGER :: step_timer

 CALL get_environment_variable ("JPI" , env )
 READ ( unit = env , fmt ="(i10)" ) jpi
 CALL get_environment_variable ("JPJ" , env )
 READ ( unit = env , fmt ="(i10)" ) jpj
 CALL get_environment_variable ("JPK" , env )
 READ ( unit = env , fmt ="(i10)" ) jpk
 CALL get_environment_variable ("IT" , env )
 READ ( unit = env , fmt ="(i10)" ) it
 CALL timer_init ( )
 CALL timer_register ( init_timer , label ="Initialisation" )
 CALL timer_register ( step_timer , label ="Time-stepping" , num_repeats = it )
 CALL timer_start ( init_timer )
 ALLOCATE ( mydomain ( jpi , jpj , jpk ) )
 ALLOCATE ( zwx ( jpi , jpj , jpk ) )
 ALLOCATE ( zwy ( jpi , jpj , jpk ) )
 ALLOCATE ( zslpx ( jpi , jpj , jpk ) )
 ALLOCATE ( zslpy ( jpi , jpj , jpk ) )
 ALLOCATE ( pun ( jpi , jpj , jpk ) )
 ALLOCATE ( pvn ( jpi , jpj , jpk ) )
 ALLOCATE ( pwn ( jpi , jpj , jpk ) )
 ALLOCATE ( umask ( jpi , jpj , jpk ) )
 ALLOCATE ( vmask ( jpi , jpj , jpk ) )
 ALLOCATE ( tmask ( jpi , jpj , jpk ) )
 ALLOCATE ( zind ( jpi , jpj , jpk ) )
 ALLOCATE ( ztfreez ( jpi , jpj ) )
 ALLOCATE ( rnfmsk ( jpi , jpj ) )
 ALLOCATE ( upsmsk ( jpi , jpj ) )
 ALLOCATE ( rnfmsk_z ( jpk ) )
 ALLOCATE ( tsn ( jpi , jpj , jpk ) )
 r = jpi * jpj * jpk
!$omp parallel do default(shared), private(jk,jj,ji), schedule(static)
 DO jk = 1 , jpk , 1
  DO jj = 1 , jpj , 1
   DO ji = 1 , jpi , 1
    umask ( ji , jj , jk ) = ji * jj * jk / r
    mydomain ( ji , jj , jk ) = ji * jj * jk / r
    pun ( ji , jj , jk ) = ji * jj * jk / r
    pvn ( ji , jj , jk ) = ji * jj * jk / r
    pwn ( ji , jj , jk ) = ji * jj * jk / r
    vmask ( ji , jj , jk ) = ji * jj * jk / r
    tsn ( ji , jj , jk ) = ji * jj * jk / r
    tmask ( ji , jj , jk ) = ji * jj * jk / r
   END DO
  END DO
 END DO
!$omp end parallel do
 r = jpi * jpj
 DO jj = 1 , jpj , 1
  DO ji = 1 , jpi , 1
   ztfreez ( ji , jj ) = ji * jj / r
   upsmsk ( ji , jj ) = ji * jj / r
   rnfmsk ( ji , jj ) = ji * jj / r
  END DO
 END DO
!$omp parallel do default(shared), private(jk), schedule(static)
 DO jk = 1 , jpk , 1
  rnfmsk_z ( jk ) = jk / jpk
 END DO
!$omp end parallel do
 CALL timer_stop ( init_timer )
 CALL timer_start ( step_timer )
 DO jt = 1 , it , 1
!$omp parallel do default(shared), private(jk,jj,ji,zice), schedule(static)
  DO jk = 1 , jpk , 1
   DO jj = 1 , jpj , 1
    DO ji = 1 , jpi , 1
     IF ( tsn ( ji , jj , jk ) <= ztfreez ( ji , jj ) + 0.1d0 ) THEN
      zice = 1.d0
     ELSE
      zice = 0.d0
     END IF
     zind ( ji , jj , jk ) = max ( rnfmsk ( ji , jj ) * rnfmsk_z ( jk ) , upsmsk ( ji , jj ) , zice ) * tmask ( ji , jj , jk )
     zind ( ji , jj , jk ) = 1 - zind ( ji , jj , jk )
    END DO
   END DO
  END DO
!$omp end parallel do
  zwx ( : , : , jpk ) = 0.e0
  zwy ( : , : , jpk ) = 0.e0
!$omp parallel do default(shared), private(jk,jj,ji), schedule(static)
  DO jk = 1 , jpk - 1 , 1
   DO jj = 1 , jpj - 1 , 1
    DO ji = 1 , jpi - 1 , 1
     zwx ( ji , jj , jk ) = umask ( ji , jj , jk ) * ( mydomain ( ji + 1 , jj , jk ) - mydomain ( ji , jj , jk ) )
     zwy ( ji , jj , jk ) = vmask ( ji , jj , jk ) * ( mydomain ( ji , jj + 1 , jk ) - mydomain ( ji , jj , jk ) )
    END DO
   END DO
  END DO
!$omp end parallel do
  zslpx ( : , : , jpk ) = 0.e0
  zslpy ( : , : , jpk ) = 0.e0
!$omp parallel do default(shared), private(jk,jj,ji), schedule(static)
  DO jk = 1 , jpk - 1 , 1
   DO jj = 2 , jpj , 1
    DO ji = 2 , jpi , 1
     zslpx ( ji , jj , jk ) = ( zwx ( ji , jj , jk ) + zwx ( ji - 1 , jj , jk ) ) * ( 0.25d0 + sign ( 0.25d0 , zwx ( ji , jj , jk&
      ) * zwx ( ji - 1 , jj , jk ) ) )
     zslpy ( ji , jj , jk ) = ( zwy ( ji , jj , jk ) + zwy ( ji , jj - 1 , jk ) ) * ( 0.25d0 + sign ( 0.25d0 , zwy ( ji , jj , jk&
      ) * zwy ( ji , jj - 1 , jk ) ) )
    END DO
   END DO
  END DO
!$omp end parallel do
!$omp parallel do default(shared), private(jk,jj,ji), schedule(static)
  DO jk = 1 , jpk - 1 , 1
   DO jj = 2 , jpj , 1
    DO ji = 2 , jpi , 1
     zslpx ( ji , jj , jk ) = sign ( 1.d0 , zslpx ( ji , jj , jk ) ) * min ( abs ( zslpx ( ji , jj , jk ) ) , 2.d0 * abs ( zwx (&
      ji - 1 , jj , jk ) ) , 2.d0 * abs ( zwx ( ji , jj , jk ) ) )
     zslpy ( ji , jj , jk ) = sign ( 1.d0 , zslpy ( ji , jj , jk ) ) * min ( abs ( zslpy ( ji , jj , jk ) ) , 2.d0 * abs ( zwy (&
      ji , jj - 1 , jk ) ) , 2.d0 * abs ( zwy ( ji , jj , jk ) ) )
    END DO
   END DO
  END DO
!$omp end parallel do
!$omp parallel do default(shared), private(jk,jj,ji,z0u,z0v,zalpha,zu,zv,zzwy,zzwx), schedule(static)
  DO jk = 1 , jpk - 1 , 1
   zdt = 1
   DO jj = 2 , jpj - 1 , 1
    DO ji = 2 , jpi - 1 , 1
     z0u = sign ( 0.5d0 , pun ( ji , jj , jk ) )
     zalpha = 0.5d0 - z0u
     zu = z0u - 0.5d0 * pun ( ji , jj , jk ) * zdt
     zzwx = mydomain ( ji + 1 , jj , jk ) + zind ( ji , jj , jk ) * ( zu * zslpx ( ji + 1 , jj , jk ) )
     zzwy = mydomain ( ji , jj , jk ) + zind ( ji , jj , jk ) * ( zu * zslpx ( ji , jj , jk ) )
     zwx ( ji , jj , jk ) = pun ( ji , jj , jk ) * ( zalpha * zzwx + ( 1. - zalpha ) * zzwy )
     z0v = sign ( 0.5d0 , pvn ( ji , jj , jk ) )
     zalpha = 0.5d0 - z0v
     zv = z0v - 0.5d0 * pvn ( ji , jj , jk ) * zdt
     zzwx = mydomain ( ji , jj + 1 , jk ) + zind ( ji , jj , jk ) * ( zv * zslpy ( ji , jj + 1 , jk ) )
     zzwy = mydomain ( ji , jj , jk ) + zind ( ji , jj , jk ) * ( zv * zslpy ( ji , jj , jk ) )
     zwy ( ji , jj , jk ) = pvn ( ji , jj , jk ) * ( zalpha * zzwx + ( 1.d0 - zalpha ) * zzwy )
    END DO
   END DO
  END DO
!$omp end parallel do
!$omp parallel do default(shared), private(jk,jj,ji,ztra,zbtr), schedule(static)
  DO jk = 1 , jpk - 1 , 1
   DO jj = 2 , jpj - 1 , 1
    DO ji = 2 , jpi - 1 , 1
     zbtr = 1.
     ztra = ( - zbtr * ( zwx ( ji , jj , jk ) - zwx ( ji - 1 , jj , jk ) + zwy ( ji , jj , jk ) - zwy ( ji , jj - 1 , jk ) ) )
     mydomain ( ji , jj , jk ) = mydomain ( ji , jj , jk ) + ztra
    END DO
   END DO
  END DO
!$omp end parallel do
  zwx ( : , : , 1 ) = 0.e0
  zwx ( : , : , jpk ) = 0.e0
!$omp parallel do default(shared), private(jk), schedule(static)
  DO jk = 2 , jpk - 1 , 1
   zwx ( : , : , jk ) = tmask ( : , : , jk ) * ( mydomain ( : , : , jk - 1 ) - mydomain ( : , : , jk ) )
  END DO
!$omp end parallel do
  zslpx ( : , : , 1 ) = 0.e0
!$omp parallel do default(shared), private(jk,jj,ji), schedule(static)
  DO jk = 2 , jpk - 1 , 1
   DO jj = 1 , jpj , 1
    DO ji = 1 , jpi , 1
     zslpx ( ji , jj , jk ) = ( zwx ( ji , jj , jk ) + zwx ( ji , jj , jk + 1 ) ) * ( 0.25d0 + sign ( 0.25d0 , zwx ( ji , jj , jk&
      ) * zwx ( ji , jj , jk + 1 ) ) )
    END DO
   END DO
  END DO
!$omp end parallel do
!$omp parallel do default(shared), private(jk,jj,ji), schedule(static)
  DO jk = 2 , jpk - 1 , 1
   DO jj = 1 , jpj , 1
    DO ji = 1 , jpi , 1
     zslpx ( ji , jj , jk ) = sign ( 1.d0 , zslpx ( ji , jj , jk ) ) * min ( abs ( zslpx ( ji , jj , jk ) ) , 2.d0 * abs ( zwx (&
      ji , jj , jk + 1 ) ) , 2.d0 * abs ( zwx ( ji , jj , jk ) ) )
    END DO
   END DO
  END DO
!$omp end parallel do
  zwx ( : , : , 1 ) = pwn ( : , : , 1 ) * mydomain ( : , : , 1 )
  zdt = 1
  zbtr = 1.
!$omp parallel do default(shared), private(jk,jj,ji,zzwy,zw,zalpha,zzwx,z0w), schedule(static)
  DO jk = 1 , jpk - 1 , 1
   DO jj = 2 , jpj - 1 , 1
    DO ji = 2 , jpi - 1 , 1
     z0w = sign ( 0.5d0 , pwn ( ji , jj , jk + 1 ) )
     zalpha = 0.5d0 + z0w
     zw = z0w - 0.5d0 * pwn ( ji , jj , jk + 1 ) * zdt * zbtr
     zzwx = mydomain ( ji , jj , jk + 1 ) + zind ( ji , jj , jk ) * ( zw * zslpx ( ji , jj , jk + 1 ) )
     zzwy = mydomain ( ji , jj , jk ) + zind ( ji , jj , jk ) * ( zw * zslpx ( ji , jj , jk ) )
     zwx ( ji , jj , jk + 1 ) = pwn ( ji , jj , jk + 1 ) * ( zalpha * zzwx + ( 1. - zalpha ) * zzwy )
    END DO
   END DO
  END DO
!$omp end parallel do
  zbtr = 1.
!$omp parallel do default(shared), private(jk,jj,ji,ztra), schedule(static)
  DO jk = 1 , jpk - 1 , 1
   DO jj = 2 , jpj - 1 , 1
    DO ji = 2 , jpi - 1 , 1
     ztra = ( - zbtr * ( zwx ( ji , jj , jk ) - zwx ( ji , jj , jk + 1 ) ) )
     mydomain ( ji , jj , jk ) = ztra
    END DO
   END DO
  END DO
!$omp end parallel do
 END DO
 CALL timer_stop ( step_timer )
 OPEN ( unit = 4 , file ="output.dat" , form ="formatted" )
!$omp parallel do default(shared), private(jk,jj,ji), schedule(static)
 DO jk = 1 , jpk - 1 , 1
  DO jj = 2 , jpj - 1 , 1
   DO ji = 2 , jpi - 1 , 1
    WRITE ( unit = 4 , fmt = * ) mydomain ( ji , jj , jk )
   END DO
  END DO
 END DO
!$omp end parallel do
 CLOSE ( unit = 4 )
 DEALLOCATE ( mydomain )
 DEALLOCATE ( zwx )
 DEALLOCATE ( zwy )
 DEALLOCATE ( zslpx )
 DEALLOCATE ( zslpy )
 DEALLOCATE ( pun )
 DEALLOCATE ( pvn )
 DEALLOCATE ( pwn )
 DEALLOCATE ( umask )
 DEALLOCATE ( vmask )
 DEALLOCATE ( tmask )
 DEALLOCATE ( zind )
 DEALLOCATE ( ztfreez )
 DEALLOCATE ( rnfmsk )
 DEALLOCATE ( upsmsk )
 DEALLOCATE ( rnfmsk_z )
 DEALLOCATE ( tsn )
 CALL timer_report ( )
END PROGRAM tra_adv

