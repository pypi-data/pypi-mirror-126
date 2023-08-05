  MODULE gw_mixed_schur_preconditioner_alg_mod_psy
    USE constants_mod, ONLY: r_def
    USE operator_mod, ONLY: operator_type, operator_proxy_type, columnwise_operator_type, columnwise_operator_proxy_type
    USE field_mod, ONLY: field_type, field_proxy_type
    IMPLICIT NONE
    CONTAINS
    SUBROUTINE invoke_0(ones, m_lumped, mb, self_mb_lumped_inv)
      USE matrix_vector_kernel_2_mod, ONLY: matrix_vector_kernel_2_code
      USE mesh_mod, ONLY: mesh_type
      TYPE(field_type), intent(inout) :: m_lumped, ones, self_mb_lumped_inv
      TYPE(operator_type), intent(in) :: mb
      INTEGER cell
      INTEGER df
      INTEGER nlayers
      TYPE(operator_proxy_type) mb_proxy
      TYPE(field_proxy_type) ones_proxy, m_lumped_proxy, self_mb_lumped_inv_proxy
      INTEGER, pointer :: map_any_space_1_m_lumped(:,:) => null(), map_any_space_2_ones(:,:) => null()
      INTEGER ndf_any_space_1_ones, undf_any_space_1_ones, ndf_any_space_1_m_lumped, undf_any_space_1_m_lumped, ndf_any_space_2_ones, undf_any_space_2_ones, ndf_any_space_1_self_mb_lumped_inv, undf_any_space_1_self_mb_lumped_inv
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      ones_proxy = ones%get_proxy()
      m_lumped_proxy = m_lumped%get_proxy()
      mb_proxy = mb%get_proxy()
      self_mb_lumped_inv_proxy = self_mb_lumped_inv%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = ones_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => ones_proxy%vspace%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_m_lumped => m_lumped_proxy%vspace%get_whole_dofmap()
      map_any_space_2_ones => ones_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_ones
      !
      ndf_any_space_1_ones = ones_proxy%vspace%get_ndf()
      undf_any_space_1_ones = ones_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_m_lumped
      !
      ndf_any_space_1_m_lumped = m_lumped_proxy%vspace%get_ndf()
      undf_any_space_1_m_lumped = m_lumped_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_2_ones
      !
      ndf_any_space_2_ones = ones_proxy%vspace%get_ndf()
      undf_any_space_2_ones = ones_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_self_mb_lumped_inv
      !
      ndf_any_space_1_self_mb_lumped_inv = self_mb_lumped_inv_proxy%vspace%get_ndf()
      undf_any_space_1_self_mb_lumped_inv = self_mb_lumped_inv_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      DO df=1,ones_proxy%vspace%get_last_dof_owned()
        ones_proxy%data(df) = 1.0_r_def
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL ones_proxy%set_dirty()
      !
      DO df=1,m_lumped_proxy%vspace%get_last_dof_owned()
        m_lumped_proxy%data(df) = 0.0_r_def
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL m_lumped_proxy%set_dirty()
      !
      CALL m_lumped_proxy%halo_exchange(depth=1)
      !
      CALL ones_proxy%halo_exchange(depth=1)
      !
      DO cell=1,mesh%get_last_halo_cell(1)
        !
        CALL matrix_vector_kernel_2_code(cell, nlayers, m_lumped_proxy%data, ones_proxy%data, mb_proxy%ncell_3d, mb_proxy%local_stencil, ndf_any_space_1_m_lumped, undf_any_space_1_m_lumped, map_any_space_1_m_lumped(:,cell), ndf_any_space_2_ones, undf_any_space_2_ones, map_any_space_2_ones(:,cell))
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL m_lumped_proxy%set_dirty()
      !
      DO df=1,self_mb_lumped_inv_proxy%vspace%get_last_dof_owned()
        self_mb_lumped_inv_proxy%data(df) = ones_proxy%data(df) / m_lumped_proxy%data(df)
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_mb_lumped_inv_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_0
    SUBROUTINE invoke_1(self_mb_rb, rhs0_vector, self_mb_lumped_inv, self_rhs_u, self_q, const1, rhs0_vector_1)
      USE matrix_vector_kernel_3_mod, ONLY: matrix_vector_kernel_3_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: const1
      TYPE(field_type), intent(inout) :: self_rhs_u, self_mb_rb
      TYPE(field_type), intent(in) :: rhs0_vector, self_mb_lumped_inv, rhs0_vector_1
      TYPE(operator_type), intent(in) :: self_q
      INTEGER cell
      INTEGER df
      INTEGER nlayers
      TYPE(operator_proxy_type) self_q_proxy
      TYPE(field_proxy_type) self_mb_rb_proxy, rhs0_vector_proxy, self_mb_lumped_inv_proxy, self_rhs_u_proxy, rhs0_vector_1_proxy
      INTEGER, pointer :: map_any_space_1_self_rhs_u(:,:) => null(), map_any_space_2_self_mb_rb(:,:) => null()
      INTEGER ndf_any_space_1_self_mb_rb, undf_any_space_1_self_mb_rb, ndf_any_space_1_self_rhs_u, undf_any_space_1_self_rhs_u, ndf_any_space_2_self_mb_rb, undf_any_space_2_self_mb_rb
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      self_mb_rb_proxy = self_mb_rb%get_proxy()
      rhs0_vector_proxy = rhs0_vector%get_proxy()
      self_mb_lumped_inv_proxy = self_mb_lumped_inv%get_proxy()
      self_rhs_u_proxy = self_rhs_u%get_proxy()
      self_q_proxy = self_q%get_proxy()
      rhs0_vector_1_proxy = rhs0_vector_1%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = self_mb_rb_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => self_mb_rb_proxy%vspace%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_space_1_self_rhs_u => self_rhs_u_proxy%vspace%get_whole_dofmap()
      map_any_space_2_self_mb_rb => self_mb_rb_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_self_mb_rb
      !
      ndf_any_space_1_self_mb_rb = self_mb_rb_proxy%vspace%get_ndf()
      undf_any_space_1_self_mb_rb = self_mb_rb_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_self_rhs_u
      !
      ndf_any_space_1_self_rhs_u = self_rhs_u_proxy%vspace%get_ndf()
      undf_any_space_1_self_rhs_u = self_rhs_u_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_2_self_mb_rb
      !
      ndf_any_space_2_self_mb_rb = self_mb_rb_proxy%vspace%get_ndf()
      undf_any_space_2_self_mb_rb = self_mb_rb_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      DO df=1,self_mb_rb_proxy%vspace%get_last_dof_owned()
        self_mb_rb_proxy%data(df) = rhs0_vector_proxy%data(df) * self_mb_lumped_inv_proxy%data(df)
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_mb_rb_proxy%set_dirty()
      !
      DO df=1,self_rhs_u_proxy%vspace%get_last_dof_owned()
        self_rhs_u_proxy%data(df) = 0.0_r_def
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_rhs_u_proxy%set_dirty()
      !
      CALL self_rhs_u_proxy%halo_exchange(depth=1)
      !
      CALL self_mb_rb_proxy%halo_exchange(depth=1)
      !
      DO cell=1,mesh%get_last_halo_cell(1)
        !
        CALL matrix_vector_kernel_3_code(cell, nlayers, self_rhs_u_proxy%data, self_mb_rb_proxy%data, self_q_proxy%ncell_3d, self_q_proxy%local_stencil, ndf_any_space_1_self_rhs_u, undf_any_space_1_self_rhs_u, map_any_space_1_self_rhs_u(:,cell), ndf_any_space_2_self_mb_rb, undf_any_space_2_self_mb_rb, map_any_space_2_self_mb_rb(:,cell))
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_rhs_u_proxy%set_dirty()
      !
      DO df=1,self_rhs_u_proxy%vspace%get_last_dof_owned()
        self_rhs_u_proxy%data(df) = const1*self_rhs_u_proxy%data(df) + rhs0_vector_1_proxy%data(df)
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_rhs_u_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_1
    SUBROUTINE invoke_2(self_hb_ru, self_rhs_u, self_hb_lumped_inv, self_rhs_p_tmp, div, self_rhs_p, m3_inv, const2, rhs0_vector)
      USE dg_matrix_vector_kernel_3_mod, ONLY: dg_matrix_vector_kernel_3_code
      USE dg_matrix_vector_kernel_2_mod, ONLY: dg_matrix_vector_kernel_2_code
      USE mesh_mod, ONLY: mesh_type
      REAL(KIND=r_def), intent(in) :: const2
      TYPE(field_type), intent(inout) :: self_rhs_p, self_rhs_p_tmp
      TYPE(field_type), intent(inout) :: self_hb_ru
      TYPE(field_type), intent(in) :: self_rhs_u, self_hb_lumped_inv, rhs0_vector
      TYPE(operator_type), intent(in) :: div, m3_inv
      INTEGER cell
      INTEGER df
      INTEGER nlayers
      TYPE(operator_proxy_type) div_proxy, m3_inv_proxy
      TYPE(field_proxy_type) self_hb_ru_proxy, self_rhs_u_proxy, self_hb_lumped_inv_proxy, self_rhs_p_tmp_proxy, self_rhs_p_proxy, rhs0_vector_proxy
      INTEGER, pointer :: map_any_discontinuous_space_1_self_rhs_p(:,:) => null(), map_any_discontinuous_space_1_self_rhs_p_tmp(:,:) => null(), map_any_space_1_self_hb_ru(:,:) => null(), map_any_space_1_self_rhs_p_tmp(:,:) => null()
      INTEGER ndf_any_space_1_self_hb_ru, undf_any_space_1_self_hb_ru, ndf_any_discontinuous_space_1_self_rhs_p_tmp, undf_any_discontinuous_space_1_self_rhs_p_tmp, ndf_any_discontinuous_space_1_self_rhs_p, undf_any_discontinuous_space_1_self_rhs_p, ndf_any_space_1_self_rhs_p_tmp, undf_any_space_1_self_rhs_p_tmp, ndf_any_space_1_self_rhs_p, undf_any_space_1_self_rhs_p
      TYPE(mesh_type), pointer :: mesh => null()
      !
      ! Initialise field and/or operator proxies
      !
      self_hb_ru_proxy = self_hb_ru%get_proxy()
      self_rhs_u_proxy = self_rhs_u%get_proxy()
      self_hb_lumped_inv_proxy = self_hb_lumped_inv%get_proxy()
      self_rhs_p_tmp_proxy = self_rhs_p_tmp%get_proxy()
      div_proxy = div%get_proxy()
      self_rhs_p_proxy = self_rhs_p%get_proxy()
      m3_inv_proxy = m3_inv%get_proxy()
      rhs0_vector_proxy = rhs0_vector%get_proxy()
      !
      ! Initialise number of layers
      !
      nlayers = self_hb_ru_proxy%vspace%get_nlayers()
      !
      ! Create a mesh object
      !
      mesh => self_hb_ru_proxy%vspace%get_mesh()
      !
      ! Look-up dofmaps for each function space
      !
      map_any_discontinuous_space_1_self_rhs_p_tmp => self_rhs_p_tmp_proxy%vspace%get_whole_dofmap()
      map_any_space_1_self_hb_ru => self_hb_ru_proxy%vspace%get_whole_dofmap()
      map_any_discontinuous_space_1_self_rhs_p => self_rhs_p_proxy%vspace%get_whole_dofmap()
      map_any_space_1_self_rhs_p_tmp => self_rhs_p_tmp_proxy%vspace%get_whole_dofmap()
      !
      ! Initialise number of DoFs for any_space_1_self_hb_ru
      !
      ndf_any_space_1_self_hb_ru = self_hb_ru_proxy%vspace%get_ndf()
      undf_any_space_1_self_hb_ru = self_hb_ru_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_discontinuous_space_1_self_rhs_p_tmp
      !
      ndf_any_discontinuous_space_1_self_rhs_p_tmp = self_rhs_p_tmp_proxy%vspace%get_ndf()
      undf_any_discontinuous_space_1_self_rhs_p_tmp = self_rhs_p_tmp_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_discontinuous_space_1_self_rhs_p
      !
      ndf_any_discontinuous_space_1_self_rhs_p = self_rhs_p_proxy%vspace%get_ndf()
      undf_any_discontinuous_space_1_self_rhs_p = self_rhs_p_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_self_rhs_p_tmp
      !
      ndf_any_space_1_self_rhs_p_tmp = self_rhs_p_tmp_proxy%vspace%get_ndf()
      undf_any_space_1_self_rhs_p_tmp = self_rhs_p_tmp_proxy%vspace%get_undf()
      !
      ! Initialise number of DoFs for any_space_1_self_rhs_p
      !
      ndf_any_space_1_self_rhs_p = self_rhs_p_proxy%vspace%get_ndf()
      undf_any_space_1_self_rhs_p = self_rhs_p_proxy%vspace%get_undf()
      !
      ! Call kernels and communication routines
      !
      DO df=1,self_hb_ru_proxy%vspace%get_last_dof_owned()
        self_hb_ru_proxy%data(df) = self_rhs_u_proxy%data(df) * self_hb_lumped_inv_proxy%data(df)
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_hb_ru_proxy%set_dirty()
      !
      CALL self_hb_ru_proxy%halo_exchange(depth=1)
      !
      DO cell=1,mesh%get_last_edge_cell()
        !
        CALL dg_matrix_vector_kernel_2_code(cell, nlayers, self_rhs_p_tmp_proxy%data, self_hb_ru_proxy%data, div_proxy%ncell_3d, div_proxy%local_stencil, ndf_any_discontinuous_space_1_self_rhs_p_tmp, undf_any_discontinuous_space_1_self_rhs_p_tmp, map_any_discontinuous_space_1_self_rhs_p_tmp(:,cell), ndf_any_space_1_self_hb_ru, undf_any_space_1_self_hb_ru, map_any_space_1_self_hb_ru(:,cell))
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_rhs_p_tmp_proxy%set_dirty()
      !
      CALL self_rhs_p_tmp_proxy%halo_exchange(depth=1)
      !
      DO cell=1,mesh%get_last_edge_cell()
        !
        CALL dg_matrix_vector_kernel_3_code(cell, nlayers, self_rhs_p_proxy%data, self_rhs_p_tmp_proxy%data, m3_inv_proxy%ncell_3d, m3_inv_proxy%local_stencil, ndf_any_discontinuous_space_1_self_rhs_p, undf_any_discontinuous_space_1_self_rhs_p, map_any_discontinuous_space_1_self_rhs_p(:,cell), ndf_any_space_1_self_rhs_p_tmp, undf_any_space_1_self_rhs_p_tmp, map_any_space_1_self_rhs_p_tmp(:,cell))
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_rhs_p_proxy%set_dirty()
      !
      DO df=1,self_rhs_p_proxy%vspace%get_last_dof_owned()
        self_rhs_p_proxy%data(df) = const2*self_rhs_p_proxy%data(df) + rhs0_vector_proxy%data(df)
      END DO 
      !
      ! Set halos dirty/clean for fields modified in the above loop
      !
      CALL self_rhs_p_proxy%set_dirty()
      !
      !
    END SUBROUTINE invoke_2
  END MODULE gw_mixed_schur_preconditioner_alg_mod_psy