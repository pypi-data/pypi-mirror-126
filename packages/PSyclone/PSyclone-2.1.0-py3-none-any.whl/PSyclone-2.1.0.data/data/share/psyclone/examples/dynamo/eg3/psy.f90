  MODULE solver_mod_psy
    USE constants_mod, ONLY: r_def
    USE operator_mod, ONLY: operator_type, operator_proxy_type, columnwise_operator_type, columnwise_operator_proxy_type
    USE field_mod, ONLY: field_type, field_proxy_type
    IMPLICIT NONE
    CONTAINS
    SUBROUTINE invoke_0_w3_solver_kernel_type(lhs, rhs, chi, ascalar, qr)
      USE w3_solver_kernel_mod, ONLY: solver_w3_code
      USE quadrature_xyoz_mod, ONLY: quadrature_xyoz_type, quadrature_xyoz_proxy_type
      USE function_space_mod, ONLY: BASIS, DIFF_BASIS
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: ascalar
      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(in) :: rhs, chi(3)
      TYPE(quadrature_xyoz_type), intent(in) :: qr
      INTEGER cell
      REAL(KIND=r_def), allocatable :: basis_w3_qr(:,:,:,:), diff_basis_w0_qr(:,:,:,:)
      INTEGER dim_w3, diff_dim_w0
      REAL(KIND=r_def), pointer :: weights_xy_qr(:) => null(), weights_z_qr(:) => null()
      INTEGER np_xy_qr, np_z_qr
      INTEGER ndf_w3, undf_w3, ndf_w0, undf_w0
      INTEGER nlayers
      TYPE(field_proxy_type) lhs_proxy, rhs_proxy, chi_proxy(3)
      TYPE(quadrature_xyoz_proxy_type) qr_proxy
      INTEGER, pointer :: map_w3(:,:) => null(), map_w0(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      lhs_proxy = lhs%get_proxy()
      rhs_proxy = rhs%get_proxy()
      chi_proxy(1) = chi(1)%get_proxy()
      chi_proxy(2) = chi(2)%get_proxy()
      chi_proxy(3) = chi(3)%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = lhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => lhs%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_w3 => lhs_proxy%vspace%get_whole_dofmap()
      map_w0 => chi_proxy(1)%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for w3
      !
      ndf_w3 = lhs_proxy%vspace%get_ndf()
      undf_w3 = lhs_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for w0
      !
      ndf_w0 = chi_proxy(1)%vspace%get_ndf()
      undf_w0 = chi_proxy(1)%vspace%get_undf()
      !
      ! Look-up quadrature variables
      !
      qr_proxy = qr%get_quadrature_proxy()
      np_xy_qr = qr_proxy%np_xy
      np_z_qr = qr_proxy%np_z
      weights_xy_qr => qr_proxy%weights_xy
      weights_z_qr => qr_proxy%weights_z
      !
      ! Allocate basis arrays
      !
      dim_w3 = lhs_proxy%vspace%get_dim_space()
      ALLOCATE (basis_w3_qr(dim_w3, ndf_w3, np_xy_qr, np_z_qr))
      !
      ! Allocate differential basis arrays
      !
      diff_dim_w0 = chi_proxy(1)%vspace%get_dim_space_diff()
      ALLOCATE (diff_basis_w0_qr(diff_dim_w0, ndf_w0, np_xy_qr, np_z_qr))
      !
      ! Compute basis arrays
      !
      CALL qr%compute_function(BASIS, lhs_proxy%vspace, dim_w3, ndf_w3, basis_w3_qr)
      !
      ! Compute differential basis arrays
      !
      CALL qr%compute_function(DIFF_BASIS, chi_proxy(1)%vspace, diff_dim_w0, ndf_w0, diff_basis_w0_qr)
      !
      ! Call kernels and communication routines
      !
      IF (chi_proxy(1)%is_dirty(depth=1)) THEN
        CALL chi_proxy(1)%halo_exchange(depth=1)
      END IF 
      !
      IF (chi_proxy(2)%is_dirty(depth=1)) THEN
        CALL chi_proxy(2)%halo_exchange(depth=1)
      END IF 
      !
      IF (chi_proxy(3)%is_dirty(depth=1)) THEN
        CALL chi_proxy(3)%halo_exchange(depth=1)
      END IF 
      !
      !$omp parallel do default(shared), private(cell), schedule(static)
      DO cell=1,mesh%get_last_edge_cell()
        !
        CALL solver_w3_code(nlayers, lhs_proxy%data, rhs_proxy%data, chi_proxy(1)%data, chi_proxy(2)%data, chi_proxy(3)%data, ascalar, ndf_w3, undf_w3, map_w3(:,cell), basis_w3_qr, ndf_w0, undf_w0, map_w0(:,cell), diff_basis_w0_qr, np_xy_qr, np_z_qr, weights_xy_qr, weights_z_qr)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !
      ! Deallocate basis arrays
      !
      DEALLOCATE (diff_basis_w0_qr, basis_w3_qr)
      !
    END SUBROUTINE invoke_0_w3_solver_kernel_type
    SUBROUTINE invoke_1(sc_err, rhs)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: sc_err
      TYPE(field_type), intent(in) :: rhs
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_rhs, undf_any_space_1_rhs
      INTEGER nlayers
      TYPE(field_proxy_type) rhs_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      rhs_proxy = rhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = rhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => rhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_rhs
      !
      ndf_any_space_1_rhs = rhs_proxy%vspace%get_ndf()
      undf_any_space_1_rhs = rhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      sc_err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:sc_err)
      DO df=1,rhs_proxy%vspace%get_last_dof_owned()
        sc_err = sc_err+rhs_proxy%data(df)*rhs_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = sc_err
      sc_err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_1
    SUBROUTINE invoke_2(lhs)
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: lhs
      INTEGER df
      INTEGER ndf_any_space_1_lhs, undf_any_space_1_lhs
      INTEGER nlayers
      TYPE(field_proxy_type) lhs_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      lhs_proxy = lhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = lhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => lhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_2
    SUBROUTINE invoke_bicg_group1(v, lhs, mm)
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: v
      TYPE(field_type), intent(in) :: lhs
      TYPE(operator_type), intent(in) :: mm
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_v, undf_any_space_1_v
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) v_proxy, lhs_proxy
      INTEGER, pointer :: map_any_space_1_v(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      lhs_proxy = lhs%get_proxy()
      mm_proxy = mm%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_v => v_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      CALL v_proxy%halo_exchange(depth=1)
      !
      IF (lhs_proxy%is_dirty(depth=1)) THEN
        CALL lhs_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, v_proxy%data, lhs_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_v, undf_any_space_1_v, map_any_space_1_v(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_bicg_group1
    SUBROUTINE invoke_bicg_group2(res, rhs, v, err)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(inout) :: res
      TYPE(field_type), intent(in) :: rhs, v
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_res, undf_any_space_1_res
      INTEGER nlayers
      TYPE(field_proxy_type) res_proxy, rhs_proxy, v_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      res_proxy = res%get_proxy()
      rhs_proxy = rhs%get_proxy()
      v_proxy = v%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = res_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => res%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_res
      !
      ndf_any_space_1_res = res_proxy%vspace%get_ndf()
      undf_any_space_1_res = res_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        res_proxy%data(df) = rhs_proxy%data(df) - v_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL res_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        err = err+res_proxy%data(df)*res_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_bicg_group2
    SUBROUTINE invoke_5(cr, res)
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: cr
      TYPE(field_type), intent(in) :: res
      INTEGER df
      INTEGER ndf_any_space_1_cr, undf_any_space_1_cr
      INTEGER nlayers
      TYPE(field_proxy_type) cr_proxy, res_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      cr_proxy = cr%get_proxy()
      res_proxy = res%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = cr_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => cr%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_cr
      !
      ndf_any_space_1_cr = cr_proxy%vspace%get_ndf()
      undf_any_space_1_cr = cr_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,cr_proxy%vspace%get_last_dof_owned()
        cr_proxy%data(df) = res_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL cr_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_5
    SUBROUTINE invoke_6(p)
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: p
      INTEGER df
      INTEGER ndf_any_space_1_p, undf_any_space_1_p
      INTEGER nlayers
      TYPE(field_proxy_type) p_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      p_proxy = p%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = p_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => p%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_p
      !
      ndf_any_space_1_p = p_proxy%vspace%get_ndf()
      undf_any_space_1_p = p_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,p_proxy%vspace%get_last_dof_owned()
        p_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL p_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_6
    SUBROUTINE invoke_7(v)
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: v
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_7
    SUBROUTINE invoke_8(rho, cr, res)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: rho
      TYPE(field_type), intent(in) :: cr, res
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_cr, undf_any_space_1_cr
      INTEGER nlayers
      TYPE(field_proxy_type) cr_proxy, res_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      cr_proxy = cr%get_proxy()
      res_proxy = res%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = cr_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => cr%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_cr
      !
      ndf_any_space_1_cr = cr_proxy%vspace%get_ndf()
      undf_any_space_1_cr = cr_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      rho = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:rho)
      DO df=1,cr_proxy%vspace%get_last_dof_owned()
        rho = rho+cr_proxy%data(df)*res_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = rho
      rho = global_sum%get_sum()
      !
    END SUBROUTINE invoke_8
    SUBROUTINE invoke_9(t, res, const, v)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: const
      TYPE(field_type), intent(inout) :: t
      TYPE(field_type), intent(in) :: res, v
      INTEGER df
      INTEGER ndf_any_space_1_t, undf_any_space_1_t
      INTEGER nlayers
      TYPE(field_proxy_type) t_proxy, res_proxy, v_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      t_proxy = t%get_proxy()
      res_proxy = res%get_proxy()
      v_proxy = v%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = t_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => t%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_t
      !
      ndf_any_space_1_t = t_proxy%vspace%get_ndf()
      undf_any_space_1_t = t_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,t_proxy%vspace%get_last_dof_owned()
        t_proxy%data(df) = res_proxy%data(df) - const*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL t_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_9
    SUBROUTINE invoke_bicg_iterloop_group1(beta, p, s, v, mm, norm, cr)
      USE scalar_mod, ONLY: scalar_type
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: norm
      REAL(KIND=r_def), intent(in) :: beta
      TYPE(field_type), intent(inout) :: p
      TYPE(field_type), intent(inout) :: v
      TYPE(field_type), intent(in) :: s, cr
      TYPE(operator_type), intent(in) :: mm
      TYPE(scalar_type) global_sum
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_p, undf_any_space_1_p, ndf_any_space_1_v, undf_any_space_1_v, ndf_any_space_1_cr, undf_any_space_1_cr
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) p_proxy, s_proxy, v_proxy, cr_proxy
      INTEGER, pointer :: map_any_space_1_v(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      p_proxy = p%get_proxy()
      s_proxy = s%get_proxy()
      v_proxy = v%get_proxy()
      mm_proxy = mm%get_proxy()
      cr_proxy = cr%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = p_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => p%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_v => v_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_p
      !
      ndf_any_space_1_p = p_proxy%vspace%get_ndf()
      undf_any_space_1_p = p_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_cr
      !
      ndf_any_space_1_cr = cr_proxy%vspace%get_ndf()
      undf_any_space_1_cr = cr_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,p_proxy%vspace%get_last_dof_owned()
        p_proxy%data(df) = beta*p_proxy%data(df) + s_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL p_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      CALL v_proxy%halo_exchange(depth=1)
      !
      CALL p_proxy%halo_exchange(depth=1)
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, v_proxy%data, p_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_v, undf_any_space_1_v, map_any_space_1_v(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      norm = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:norm)
      DO df=1,cr_proxy%vspace%get_last_dof_owned()
        norm = norm+cr_proxy%data(df)*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = norm
      norm = global_sum%get_sum()
      !
    END SUBROUTINE invoke_bicg_iterloop_group1
    SUBROUTINE invoke_11(s, res, alpha, v)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: alpha
      TYPE(field_type), intent(inout) :: s
      TYPE(field_type), intent(in) :: res, v
      INTEGER df
      INTEGER ndf_any_space_1_s, undf_any_space_1_s
      INTEGER nlayers
      TYPE(field_proxy_type) s_proxy, res_proxy, v_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      s_proxy = s%get_proxy()
      res_proxy = res%get_proxy()
      v_proxy = v%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = s_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => s%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_s
      !
      ndf_any_space_1_s = s_proxy%vspace%get_ndf()
      undf_any_space_1_s = s_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,s_proxy%vspace%get_last_dof_owned()
        s_proxy%data(df) = res_proxy%data(df) - alpha*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL s_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_11
    SUBROUTINE invoke_bicg_iterloop_group2(t, cs, mm, tt, ts, s)
      USE scalar_mod, ONLY: scalar_type
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: tt, ts
      TYPE(field_type), intent(inout) :: t
      TYPE(field_type), intent(in) :: cs, s
      TYPE(operator_type), intent(in) :: mm
      TYPE(scalar_type) global_sum
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_t, undf_any_space_1_t
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) t_proxy, cs_proxy, s_proxy
      INTEGER, pointer :: map_any_space_1_t(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      t_proxy = t%get_proxy()
      cs_proxy = cs%get_proxy()
      mm_proxy = mm%get_proxy()
      s_proxy = s%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = t_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => t%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_t => t_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_t
      !
      ndf_any_space_1_t = t_proxy%vspace%get_ndf()
      undf_any_space_1_t = t_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,t_proxy%vspace%get_last_dof_owned()
        t_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL t_proxy%set_dirty()
      !
      CALL t_proxy%halo_exchange(depth=1)
      !
      IF (cs_proxy%is_dirty(depth=1)) THEN
        CALL cs_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, t_proxy%data, cs_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_t, undf_any_space_1_t, map_any_space_1_t(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL t_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      tt = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:tt)
      DO df=1,t_proxy%vspace%get_last_dof_owned()
        tt = tt+t_proxy%data(df)*t_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = tt
      tt = global_sum%get_sum()
      !
      ! Zero summation variables
      !
      ts = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:ts)
      DO df=1,t_proxy%vspace%get_last_dof_owned()
        ts = ts+t_proxy%data(df)*s_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = ts
      ts = global_sum%get_sum()
      !
    END SUBROUTINE invoke_bicg_iterloop_group2
    SUBROUTINE invoke_bicg_iterloop_group3(lhs, omega, s, alpha, p, res, t)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: omega, alpha
      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(inout) :: res
      TYPE(field_type), intent(in) :: s, p, t
      INTEGER df
      INTEGER ndf_any_space_1_lhs, undf_any_space_1_lhs, ndf_any_space_1_res, undf_any_space_1_res
      INTEGER nlayers
      TYPE(field_proxy_type) lhs_proxy, s_proxy, p_proxy, res_proxy, t_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      lhs_proxy = lhs%get_proxy()
      s_proxy = s%get_proxy()
      p_proxy = p%get_proxy()
      res_proxy = res%get_proxy()
      t_proxy = t%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = lhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => lhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_res
      !
      ndf_any_space_1_res = res_proxy%vspace%get_ndf()
      undf_any_space_1_res = res_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = lhs_proxy%data(df) + omega*s_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = lhs_proxy%data(df) + alpha*p_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        res_proxy%data(df) = s_proxy%data(df) - omega*t_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL res_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_bicg_iterloop_group3
    SUBROUTINE invoke_14(err, res)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(in) :: res
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_res, undf_any_space_1_res
      INTEGER nlayers
      TYPE(field_proxy_type) res_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      res_proxy = res%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = res_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => res%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_res
      !
      ndf_any_space_1_res = res_proxy%vspace%get_ndf()
      undf_any_space_1_res = res_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        err = err+res_proxy%data(df)*res_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_14
    SUBROUTINE invoke_15(rs_old, rhs)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: rs_old
      TYPE(field_type), intent(in) :: rhs
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_rhs, undf_any_space_1_rhs
      INTEGER nlayers
      TYPE(field_proxy_type) rhs_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      rhs_proxy = rhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = rhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => rhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_rhs
      !
      ndf_any_space_1_rhs = rhs_proxy%vspace%get_ndf()
      undf_any_space_1_rhs = rhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      rs_old = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:rs_old)
      DO df=1,rhs_proxy%vspace%get_last_dof_owned()
        rs_old = rs_old+rhs_proxy%data(df)*rhs_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = rs_old
      rs_old = global_sum%get_sum()
      !
    END SUBROUTINE invoke_15
    SUBROUTINE invoke_cg_first_guess(lhs, ap, mm, res, rhs, p, rs_old)
      USE scalar_mod, ONLY: scalar_type
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: rs_old
      TYPE(field_type), intent(inout) :: ap
      TYPE(field_type), intent(inout) :: lhs, res, p
      TYPE(field_type), intent(in) :: rhs
      TYPE(operator_type), intent(in) :: mm
      TYPE(scalar_type) global_sum
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_lhs, undf_any_space_1_lhs, ndf_any_space_1_ap, undf_any_space_1_ap, ndf_any_space_1_res, undf_any_space_1_res, ndf_any_space_1_p, undf_any_space_1_p
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) lhs_proxy, ap_proxy, res_proxy, rhs_proxy, p_proxy
      INTEGER, pointer :: map_any_space_1_ap(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      lhs_proxy = lhs%get_proxy()
      ap_proxy = ap%get_proxy()
      mm_proxy = mm%get_proxy()
      res_proxy = res%get_proxy()
      rhs_proxy = rhs%get_proxy()
      p_proxy = p%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = lhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => lhs%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_ap => ap_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_ap
      !
      ndf_any_space_1_ap = ap_proxy%vspace%get_ndf()
      undf_any_space_1_ap = ap_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_res
      !
      ndf_any_space_1_res = res_proxy%vspace%get_ndf()
      undf_any_space_1_res = res_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_p
      !
      ndf_any_space_1_p = p_proxy%vspace%get_ndf()
      undf_any_space_1_p = p_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      IF (ap_proxy%is_dirty(depth=1)) THEN
        CALL ap_proxy%halo_exchange(depth=1)
      END IF 
      !
      CALL lhs_proxy%halo_exchange(depth=1)
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, ap_proxy%data, lhs_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_ap, undf_any_space_1_ap, map_any_space_1_ap(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ap_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        res_proxy%data(df) = rhs_proxy%data(df) - ap_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL res_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,p_proxy%vspace%get_last_dof_owned()
        p_proxy%data(df) = res_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL p_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      rs_old = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:rs_old)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        rs_old = rs_old+res_proxy%data(df)*res_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = rs_old
      rs_old = global_sum%get_sum()
      !
    END SUBROUTINE invoke_cg_first_guess
    SUBROUTINE invoke_cg_iterloop_group1(ap, p, mm, rs_new)
      USE scalar_mod, ONLY: scalar_type
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: rs_new
      TYPE(field_type), intent(inout) :: ap
      TYPE(field_type), intent(in) :: p
      TYPE(operator_type), intent(in) :: mm
      TYPE(scalar_type) global_sum
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_ap, undf_any_space_1_ap, ndf_any_space_1_p, undf_any_space_1_p
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) ap_proxy, p_proxy
      INTEGER, pointer :: map_any_space_1_ap(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      ap_proxy = ap%get_proxy()
      p_proxy = p%get_proxy()
      mm_proxy = mm%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = ap_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => ap%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_ap => ap_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_ap
      !
      ndf_any_space_1_ap = ap_proxy%vspace%get_ndf()
      undf_any_space_1_ap = ap_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_p
      !
      ndf_any_space_1_p = p_proxy%vspace%get_ndf()
      undf_any_space_1_p = p_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,ap_proxy%vspace%get_last_dof_owned()
        ap_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ap_proxy%set_dirty()
      !
      CALL ap_proxy%halo_exchange(depth=1)
      !
      IF (p_proxy%is_dirty(depth=1)) THEN
        CALL p_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, ap_proxy%data, p_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_ap, undf_any_space_1_ap, map_any_space_1_ap(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ap_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      rs_new = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:rs_new)
      DO df=1,p_proxy%vspace%get_last_dof_owned()
        rs_new = rs_new+p_proxy%data(df)*ap_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = rs_new
      rs_new = global_sum%get_sum()
      !
    END SUBROUTINE invoke_cg_iterloop_group1
    SUBROUTINE invoke_cg_iterloop_group2(lhs, alpha, p, res, ap, err)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      REAL(KIND=r_def), intent(in) :: alpha
      TYPE(field_type), intent(inout) :: lhs, res
      TYPE(field_type), intent(in) :: p, ap
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_lhs, undf_any_space_1_lhs, ndf_any_space_1_res, undf_any_space_1_res
      INTEGER nlayers
      TYPE(field_proxy_type) lhs_proxy, p_proxy, res_proxy, ap_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      lhs_proxy = lhs%get_proxy()
      p_proxy = p%get_proxy()
      res_proxy = res%get_proxy()
      ap_proxy = ap%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = lhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => lhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_res
      !
      ndf_any_space_1_res = res_proxy%vspace%get_ndf()
      undf_any_space_1_res = res_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = lhs_proxy%data(df) + alpha*p_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        res_proxy%data(df) = res_proxy%data(df) - alpha*ap_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL res_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        err = err+res_proxy%data(df)*res_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_cg_iterloop_group2
    SUBROUTINE invoke_19(beta, p, res)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: beta
      TYPE(field_type), intent(inout) :: p
      TYPE(field_type), intent(in) :: res
      INTEGER df
      INTEGER ndf_any_space_1_p, undf_any_space_1_p
      INTEGER nlayers
      TYPE(field_proxy_type) p_proxy, res_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      p_proxy = p%get_proxy()
      res_proxy = res%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = p_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => p%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_p
      !
      ndf_any_space_1_p = p_proxy%vspace%get_ndf()
      undf_any_space_1_p = p_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,p_proxy%vspace%get_last_dof_owned()
        p_proxy%data(df) = beta*p_proxy%data(df) + res_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL p_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_19
    SUBROUTINE invoke_jacobi_mass_lump(ax, lumped_weight, mm, lhs, rhs)
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: lumped_weight
      TYPE(field_type), intent(inout) :: ax, lhs
      TYPE(field_type), intent(in) :: rhs
      TYPE(operator_type), intent(in) :: mm
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_ax, undf_any_space_1_ax, ndf_any_space_1_lumped_weight, undf_any_space_1_lumped_weight, ndf_any_space_1_lhs, undf_any_space_1_lhs
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) ax_proxy, lumped_weight_proxy, lhs_proxy, rhs_proxy
      INTEGER, pointer :: map_any_space_1_lumped_weight(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      ax_proxy = ax%get_proxy()
      lumped_weight_proxy = lumped_weight%get_proxy()
      mm_proxy = mm%get_proxy()
      lhs_proxy = lhs%get_proxy()
      rhs_proxy = rhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = ax_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => ax%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_lumped_weight => lumped_weight_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_ax
      !
      ndf_any_space_1_ax = ax_proxy%vspace%get_ndf()
      undf_any_space_1_ax = ax_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_lumped_weight
      !
      ndf_any_space_1_lumped_weight = lumped_weight_proxy%vspace%get_ndf()
      undf_any_space_1_lumped_weight = lumped_weight_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,ax_proxy%vspace%get_last_dof_owned()
        ax_proxy%data(df) = 1.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      IF (lumped_weight_proxy%is_dirty(depth=1)) THEN
        CALL lumped_weight_proxy%halo_exchange(depth=1)
      END IF 
      !
      CALL ax_proxy%halo_exchange(depth=1)
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, lumped_weight_proxy%data, ax_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_lumped_weight, undf_any_space_1_lumped_weight, map_any_space_1_lumped_weight(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lumped_weight_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = rhs_proxy%data(df) / lumped_weight_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_jacobi_mass_lump
    SUBROUTINE invoke_21(lhs)
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: lhs
      INTEGER df
      INTEGER ndf_any_space_1_lhs, undf_any_space_1_lhs
      INTEGER nlayers
      TYPE(field_proxy_type) lhs_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      lhs_proxy = lhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = lhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => lhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_21
    SUBROUTINE invoke_jacobi_iterloop(ax, lhs, mm, res, rhs, lumped_weight, mu)
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: mu
      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(inout) :: ax, res
      TYPE(field_type), intent(in) :: rhs, lumped_weight
      TYPE(operator_type), intent(in) :: mm
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_ax, undf_any_space_1_ax, ndf_any_space_1_res, undf_any_space_1_res, ndf_any_space_1_lhs, undf_any_space_1_lhs
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) ax_proxy, lhs_proxy, res_proxy, rhs_proxy, lumped_weight_proxy
      INTEGER, pointer :: map_any_space_1_ax(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      ax_proxy = ax%get_proxy()
      lhs_proxy = lhs%get_proxy()
      mm_proxy = mm%get_proxy()
      res_proxy = res%get_proxy()
      rhs_proxy = rhs%get_proxy()
      lumped_weight_proxy = lumped_weight%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = ax_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => ax%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_ax => ax_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_ax
      !
      ndf_any_space_1_ax = ax_proxy%vspace%get_ndf()
      undf_any_space_1_ax = ax_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_res
      !
      ndf_any_space_1_res = res_proxy%vspace%get_ndf()
      undf_any_space_1_res = res_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,ax_proxy%vspace%get_last_dof_owned()
        ax_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      CALL ax_proxy%halo_exchange(depth=1)
      !
      IF (lhs_proxy%is_dirty(depth=1)) THEN
        CALL lhs_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, ax_proxy%data, lhs_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_ax, undf_any_space_1_ax, map_any_space_1_ax(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        res_proxy%data(df) = rhs_proxy%data(df) - ax_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL res_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,res_proxy%vspace%get_last_dof_owned()
        res_proxy%data(df) = res_proxy%data(df) / lumped_weight_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL res_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = lhs_proxy%data(df) + mu*res_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_jacobi_iterloop
    SUBROUTINE invoke_23(err, rhs)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(in) :: rhs
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_rhs, undf_any_space_1_rhs
      INTEGER nlayers
      TYPE(field_proxy_type) rhs_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      rhs_proxy = rhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = rhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => rhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_rhs
      !
      ndf_any_space_1_rhs = rhs_proxy%vspace%get_ndf()
      undf_any_space_1_rhs = rhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,rhs_proxy%vspace%get_last_dof_owned()
        err = err+rhs_proxy%data(df)*rhs_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_23
    SUBROUTINE invoke_gmres_group1(ax, lhs, mm, r, rhs, s, err)
      USE scalar_mod, ONLY: scalar_type
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(inout) :: ax, r, s
      TYPE(field_type), intent(in) :: lhs, rhs
      TYPE(operator_type), intent(in) :: mm
      TYPE(scalar_type) global_sum
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_ax, undf_any_space_1_ax, ndf_any_space_1_r, undf_any_space_1_r, ndf_any_space_1_s, undf_any_space_1_s
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) ax_proxy, lhs_proxy, r_proxy, rhs_proxy, s_proxy
      INTEGER, pointer :: map_any_space_1_ax(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      ax_proxy = ax%get_proxy()
      lhs_proxy = lhs%get_proxy()
      mm_proxy = mm%get_proxy()
      r_proxy = r%get_proxy()
      rhs_proxy = rhs%get_proxy()
      s_proxy = s%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = ax_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => ax%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_ax => ax_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_ax
      !
      ndf_any_space_1_ax = ax_proxy%vspace%get_ndf()
      undf_any_space_1_ax = ax_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_r
      !
      ndf_any_space_1_r = r_proxy%vspace%get_ndf()
      undf_any_space_1_r = r_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_s
      !
      ndf_any_space_1_s = s_proxy%vspace%get_ndf()
      undf_any_space_1_s = s_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,ax_proxy%vspace%get_last_dof_owned()
        ax_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      CALL ax_proxy%halo_exchange(depth=1)
      !
      IF (lhs_proxy%is_dirty(depth=1)) THEN
        CALL lhs_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, ax_proxy%data, lhs_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_ax, undf_any_space_1_ax, map_any_space_1_ax(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,r_proxy%vspace%get_last_dof_owned()
        r_proxy%data(df) = rhs_proxy%data(df) - ax_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL r_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,s_proxy%vspace%get_last_dof_owned()
        s_proxy%data(df) = r_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL s_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,s_proxy%vspace%get_last_dof_owned()
        err = err+s_proxy%data(df)*s_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_gmres_group1
    SUBROUTINE invoke_25(v, const, s)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: const
      TYPE(field_type), intent(inout) :: v
      TYPE(field_type), intent(in) :: s
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy, s_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      s_proxy = s%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = const * s_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_25
    SUBROUTINE invoke_gmres_iterloop_group1(s, w, mm)
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: s
      TYPE(field_type), intent(in) :: w
      TYPE(operator_type), intent(in) :: mm
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_s, undf_any_space_1_s
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) s_proxy, w_proxy
      INTEGER, pointer :: map_any_space_1_s(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      s_proxy = s%get_proxy()
      w_proxy = w%get_proxy()
      mm_proxy = mm%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = s_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => s%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_s => s_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_s
      !
      ndf_any_space_1_s = s_proxy%vspace%get_ndf()
      undf_any_space_1_s = s_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,s_proxy%vspace%get_last_dof_owned()
        s_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL s_proxy%set_dirty()
      !
      CALL s_proxy%halo_exchange(depth=1)
      !
      IF (w_proxy%is_dirty(depth=1)) THEN
        CALL w_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, s_proxy%data, w_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_s, undf_any_space_1_s, map_any_space_1_s(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL s_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_gmres_iterloop_group1
    SUBROUTINE invoke_27(h, v, w)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: h
      TYPE(field_type), intent(inout) :: w
      TYPE(field_type), intent(in) :: v
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v, ndf_any_space_1_w, undf_any_space_1_w
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy, w_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      w_proxy = w%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_w
      !
      ndf_any_space_1_w = w_proxy%vspace%get_ndf()
      undf_any_space_1_w = w_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      h = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:h)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        h = h+v_proxy%data(df)*w_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = h
      h = global_sum%get_sum()
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,w_proxy%vspace%get_last_dof_owned()
        w_proxy%data(df) = w_proxy%data(df) - h*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL w_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_27
    SUBROUTINE invoke_28(err, w)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(in) :: w
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_w, undf_any_space_1_w
      INTEGER nlayers
      TYPE(field_proxy_type) w_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      w_proxy = w%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = w_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => w%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_w
      !
      ndf_any_space_1_w = w_proxy%vspace%get_ndf()
      undf_any_space_1_w = w_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,w_proxy%vspace%get_last_dof_owned()
        err = err+w_proxy%data(df)*w_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_28
    SUBROUTINE invoke_29(v, const, w)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: const
      TYPE(field_type), intent(inout) :: v
      TYPE(field_type), intent(in) :: w
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy, w_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      w_proxy = w%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = const * w_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_29
    SUBROUTINE invoke_30(lhs, u, s)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: u
      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(in) :: s
      INTEGER df
      INTEGER ndf_any_space_1_lhs, undf_any_space_1_lhs
      INTEGER nlayers
      TYPE(field_proxy_type) lhs_proxy, s_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      lhs_proxy = lhs%get_proxy()
      s_proxy = s%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = lhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => lhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = lhs_proxy%data(df) + u*s_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_30
    SUBROUTINE invoke_gmres_iterloop_group2(ax, lhs, mm, r, rhs, err)
      USE scalar_mod, ONLY: scalar_type
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(inout) :: ax, r
      TYPE(field_type), intent(in) :: lhs, rhs
      TYPE(operator_type), intent(in) :: mm
      TYPE(scalar_type) global_sum
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_ax, undf_any_space_1_ax, ndf_any_space_1_r, undf_any_space_1_r
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) ax_proxy, lhs_proxy, r_proxy, rhs_proxy
      INTEGER, pointer :: map_any_space_1_ax(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      ax_proxy = ax%get_proxy()
      lhs_proxy = lhs%get_proxy()
      mm_proxy = mm%get_proxy()
      r_proxy = r%get_proxy()
      rhs_proxy = rhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = ax_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => ax%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_ax => ax_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_ax
      !
      ndf_any_space_1_ax = ax_proxy%vspace%get_ndf()
      undf_any_space_1_ax = ax_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_r
      !
      ndf_any_space_1_r = r_proxy%vspace%get_ndf()
      undf_any_space_1_r = r_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,ax_proxy%vspace%get_last_dof_owned()
        ax_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      CALL ax_proxy%halo_exchange(depth=1)
      !
      IF (lhs_proxy%is_dirty(depth=1)) THEN
        CALL lhs_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, ax_proxy%data, lhs_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_ax, undf_any_space_1_ax, map_any_space_1_ax(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,r_proxy%vspace%get_last_dof_owned()
        r_proxy%data(df) = rhs_proxy%data(df) - ax_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL r_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,r_proxy%vspace%get_last_dof_owned()
        err = err+r_proxy%data(df)*r_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_gmres_iterloop_group2
    SUBROUTINE invoke_32(v, const, s)
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: const
      TYPE(field_type), intent(inout) :: v
      TYPE(field_type), intent(in) :: s
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy, s_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      s_proxy = s%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = const * s_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_32
    SUBROUTINE invoke_33(err, rhs)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(in) :: rhs
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_rhs, undf_any_space_1_rhs
      INTEGER nlayers
      TYPE(field_proxy_type) rhs_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      rhs_proxy = rhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = rhs_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => rhs%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_rhs
      !
      ndf_any_space_1_rhs = rhs_proxy%vspace%get_ndf()
      undf_any_space_1_rhs = rhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,rhs_proxy%vspace%get_last_dof_owned()
        err = err+rhs_proxy%data(df)*rhs_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_33
    SUBROUTINE invoke_gcr_group1(ax, lhs, mm, r, rhs)
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: ax, r
      TYPE(field_type), intent(in) :: lhs, rhs
      TYPE(operator_type), intent(in) :: mm
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_ax, undf_any_space_1_ax, ndf_any_space_1_r, undf_any_space_1_r
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) ax_proxy, lhs_proxy, r_proxy, rhs_proxy
      INTEGER, pointer :: map_any_space_1_ax(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      ax_proxy = ax%get_proxy()
      lhs_proxy = lhs%get_proxy()
      mm_proxy = mm%get_proxy()
      r_proxy = r%get_proxy()
      rhs_proxy = rhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = ax_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => ax%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_ax => ax_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_ax
      !
      ndf_any_space_1_ax = ax_proxy%vspace%get_ndf()
      undf_any_space_1_ax = ax_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_r
      !
      ndf_any_space_1_r = r_proxy%vspace%get_ndf()
      undf_any_space_1_r = r_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,ax_proxy%vspace%get_last_dof_owned()
        ax_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      CALL ax_proxy%halo_exchange(depth=1)
      !
      IF (lhs_proxy%is_dirty(depth=1)) THEN
        CALL lhs_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, ax_proxy%data, lhs_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_ax, undf_any_space_1_ax, map_any_space_1_ax(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ax_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,r_proxy%vspace%get_last_dof_owned()
        r_proxy%data(df) = rhs_proxy%data(df) - ax_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL r_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_gcr_group1
    SUBROUTINE invoke_gcr_iterloop_group1(v, s, mm)
      USE matrix_vector_mm_mod, ONLY: matrix_vector_mm_code
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: v
      TYPE(field_type), intent(in) :: s
      TYPE(operator_type), intent(in) :: mm
      INTEGER colour
      INTEGER cell
      INTEGER df
      INTEGER, pointer :: cmap(:,:)
      INTEGER ndf_any_space_1_v, undf_any_space_1_v
      INTEGER nlayers
      TYPE(operator_proxy_type) mm_proxy
      TYPE(field_proxy_type) v_proxy, s_proxy
      INTEGER, pointer :: map_any_space_1_v(:,:) => null()
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      s_proxy = s%get_proxy()
      mm_proxy = mm%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_v => v_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = 0.0_r_def
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      CALL v_proxy%halo_exchange(depth=1)
      !
      IF (s_proxy%is_dirty(depth=1)) THEN
        CALL s_proxy%halo_exchange(depth=1)
      END IF 
      !
      !
      ! Look-up colour map
      !
      cmap => mesh%get_colour_map()
      !
      DO colour=1,mesh%get_ncolours()
        !$omp parallel do default(shared), private(cell), schedule(static)
        DO cell=1,mesh%get_last_halo_cell_per_colour(colour,1)
          !
          CALL matrix_vector_mm_code(cmap(colour, cell), nlayers, v_proxy%data, s_proxy%data, mm_proxy%ncell_3d, mm_proxy%local_stencil, ndf_any_space_1_v, undf_any_space_1_v, map_any_space_1_v(:,cmap(colour, cell)))
        END DO 
        !$omp end parallel do
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_gcr_iterloop_group1
    SUBROUTINE invoke_gcr_iterloop_group2(alpha, v, v_1, s, s_1)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: alpha
      TYPE(field_type), intent(inout) :: v, s
      TYPE(field_type), intent(in) :: v_1, s_1
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v, ndf_any_space_1_s, undf_any_space_1_s
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy, v_1_proxy, s_proxy, s_1_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      v_1_proxy = v_1%get_proxy()
      s_proxy = s%get_proxy()
      s_1_proxy = s_1%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_s
      !
      ndf_any_space_1_s = s_proxy%vspace%get_ndf()
      undf_any_space_1_s = s_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      alpha = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:alpha)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        alpha = alpha+v_proxy%data(df)*v_1_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = alpha
      alpha = global_sum%get_sum()
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = v_proxy%data(df) - alpha*v_1_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,s_proxy%vspace%get_last_dof_owned()
        s_proxy%data(df) = s_proxy%data(df) - alpha*s_1_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL s_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_gcr_iterloop_group2
    SUBROUTINE invoke_37(err, v)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(in) :: v
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        err = err+v_proxy%data(df)*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_37
    SUBROUTINE invoke_gcr_iterloop_group3(const, v, s, alpha, r, lhs)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: alpha
      REAL(KIND=r_def), intent(in) :: const
      TYPE(field_type), intent(inout) :: v, s, lhs, r
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_v, undf_any_space_1_v, ndf_any_space_1_s, undf_any_space_1_s, ndf_any_space_1_r, undf_any_space_1_r, ndf_any_space_1_lhs, undf_any_space_1_lhs
      INTEGER nlayers
      TYPE(field_proxy_type) v_proxy, s_proxy, r_proxy, lhs_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      v_proxy = v%get_proxy()
      s_proxy = s%get_proxy()
      r_proxy = r%get_proxy()
      lhs_proxy = lhs%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = v_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => v%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_v
      !
      ndf_any_space_1_v = v_proxy%vspace%get_ndf()
      undf_any_space_1_v = v_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_s
      !
      ndf_any_space_1_s = s_proxy%vspace%get_ndf()
      undf_any_space_1_s = s_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_r
      !
      ndf_any_space_1_r = r_proxy%vspace%get_ndf()
      undf_any_space_1_r = r_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_lhs
      !
      ndf_any_space_1_lhs = lhs_proxy%vspace%get_ndf()
      undf_any_space_1_lhs = lhs_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,v_proxy%vspace%get_last_dof_owned()
        v_proxy%data(df) = const*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL v_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,s_proxy%vspace%get_last_dof_owned()
        s_proxy%data(df) = const*s_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL s_proxy%set_dirty()
      !
      !
      ! Zero summation variables
      !
      alpha = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:alpha)
      DO df=1,r_proxy%vspace%get_last_dof_owned()
        alpha = alpha+r_proxy%data(df)*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = alpha
      alpha = global_sum%get_sum()
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,lhs_proxy%vspace%get_last_dof_owned()
        lhs_proxy%data(df) = lhs_proxy%data(df) + alpha*s_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL lhs_proxy%set_dirty()
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,r_proxy%vspace%get_last_dof_owned()
        r_proxy%data(df) = r_proxy%data(df) - alpha*v_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL r_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_gcr_iterloop_group3
    SUBROUTINE invoke_39(err, r)
      USE scalar_mod, ONLY: scalar_type
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(out) :: err
      TYPE(field_type), intent(in) :: r
      TYPE(scalar_type) global_sum
      INTEGER df
      INTEGER ndf_any_space_1_r, undf_any_space_1_r
      INTEGER nlayers
      TYPE(field_proxy_type) r_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      r_proxy = r%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = r_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => r%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_r
      !
      ndf_any_space_1_r = r_proxy%vspace%get_ndf()
      undf_any_space_1_r = r_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !
      ! Zero summation variables
      !
      err = 0.0_r_def
      !
      !$omp parallel do default(shared), private(df), schedule(static), reduction(+:err)
      DO df=1,r_proxy%vspace%get_last_dof_owned()
        err = err+r_proxy%data(df)*r_proxy%data(df)
      END DO 
      !$omp end parallel do
      global_sum%value = err
      err = global_sum%get_sum()
      !
    END SUBROUTINE invoke_39
    SUBROUTINE invoke_40(y, x)
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: y
      TYPE(field_type), intent(in) :: x
      INTEGER df
      INTEGER ndf_any_space_1_y, undf_any_space_1_y
      INTEGER nlayers
      TYPE(field_proxy_type) y_proxy, x_proxy
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      y_proxy = y%get_proxy()
      x_proxy = x%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = y_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => y%get_mesh()
      !
      ! Initialise number of DoFs for any_space_1_y
      !
      ndf_any_space_1_y = y_proxy%vspace%get_ndf()
      undf_any_space_1_y = y_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      !$omp parallel do default(shared), private(df), schedule(static)
      DO df=1,y_proxy%vspace%get_last_dof_owned()
        y_proxy%data(df) = x_proxy%data(df)
      END DO 
      !$omp end parallel do
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL y_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_40
  END MODULE solver_mod_psy