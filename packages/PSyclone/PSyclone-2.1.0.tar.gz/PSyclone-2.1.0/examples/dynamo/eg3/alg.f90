!BEGINSOURCE 
  !-------------------------------------------------------------------------------
  ! Copyright (c) 2017,  Met Office, on behalf of HMSO and Queen's Printer
  ! For further details please refer to the file LICENCE.original which you
  ! should have received as part of this distribution.
  !-------------------------------------------------------------------------------
  ! LICENCE.original is available from the Met Office Science Repository Service:
  ! https://code.metoffice.gov.uk/trac/lfric/browser/LFRic/trunk/LICENCE.original
  ! -----------------------------------------------------------------------------
  ! BSD 3-Clause License
  !
  ! Modifications copyright (c) 2017-2018, Science and Technology Facilities Council
  ! All rights reserved.
  !
  ! Redistribution and use in source and binary forms, with or without
  ! modification, are permitted provided that the following conditions are met:
  !
  ! * Redistributions of source code must retain the above copyright notice, this
  !   list of conditions and the following disclaimer.
  !
  ! * Redistributions in binary form must reproduce the above copyright notice,
  !   this list of conditions and the following disclaimer in the documentation
  !   and/or other materials provided with the distribution.
  !
  ! * Neither the name of the copyright holder nor the names of its
  !   contributors may be used to endorse or promote products derived from
  !   this software without specific prior written permission.
  !
  ! THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  ! AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  ! IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  ! DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
  ! FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  ! DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  ! SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
  ! CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
  ! OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
  ! OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  ! -----------------------------------------------------------------------------
  ! Modified by I Kavcic, Met Office
  !
  !-------------------------------------------------------------------------------

  !> @brief Contains methods and algorithms for solving a system A.x = b for known
  !! input field b and matrix A and returns field x.
  !!
  !! @details Contains a selction of solvers for inverting the matrix vector
  !! system A.x = b to return x = A^{-1}.b Depending upom the type of system to
  !! solve a number of iterative solver algorithms are possible or for
  !! discontinuous systems an exact solver can be used.

  MODULE solver_mod
    USE constants_mod, ONLY: r_def, str_def, max_iter, solver_tol, cg_solver, bicg_solver, jacobi_solver, gmres_solver, gcr_solver, no_pre_cond
    USE log_mod, ONLY: log_event, log_scratch_space, log_level_error, log_level_info, log_level_debug, log_level_trace
    USE field_mod, ONLY: field_type
    USE function_space_mod, ONLY: function_space_type, w0, w1, w2, w3, wtheta, w2v, w2h
    USE w3_solver_kernel_mod, ONLY: w3_solver_kernel_type
    USE matrix_vector_mm_mod, ONLY: matrix_vector_kernel_mm_type

    USE quadrature_mod, ONLY: quadrature_type
    USE operator_mod, ONLY: operator_type
    USE mesh_mod, ONLY: mesh_type

    IMPLICIT NONE

    PRIVATE

    PUBLIC solver_algorithm

    CONTAINS

    !> @brief Wrapper for specific solver routines for solving system A.x = b
    !! @details solves A.x = b for using a choice of solver where A is a mass
    !! matrix for a given space and x and b are fields belonging to that space.
    !! For a discontinous space the element mass matrix is exactly inverted, for
    !! continuous spaces an iterative solver is used.
    !! The current choices of iteratives solver are:
    !! cg: Conjugate gradient method without preconditioning
    !! bicgstab: bi-conjugate gradient, stabilised without preconditioning
    !! jacobi: a fixed number of jacobi iterations
    !> @param[inout] lhs The field to be solved for (x)
    !> @param[inout] rhs The right hand side field (b)
    !> @param[in]    mesh The mesh object the model for fields
    !> @param[in]    chi The coordinate array fields
    !> @param[in]    solver_type (optional) The type of iterative solver to use for
    !>               continuous systems
    !> @param[in] mm Operator type, optional. This is the mass matrix
    !> @param[in] qr Quadrature type, optional. The quadrature rule.
    !! Either qr or mm are required, but not both.
    SUBROUTINE solver_algorithm(lhs, rhs, mesh, chi, solver_type, qr, mm)
      USE solver_mod_psy, ONLY: invoke_0_w3_solver_kernel_type

      IMPLICIT NONE

      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(inout) :: rhs
      TYPE(mesh_type), intent(in) :: mesh

      ! Chi is really intent(in) but this currently causes
      ! problems because PSyclone makes everything (inout)
      TYPE(field_type), intent(inout) :: chi(3)

      INTEGER, intent(in) :: solver_type
      TYPE(quadrature_type), optional, intent(in) :: qr
      TYPE(operator_type), optional, intent(inout) :: mm

      INTEGER, parameter :: num_jacobi_iters = 5
      INTEGER fs_l, fs_r
      REAL(KIND=r_def) :: ascalar = 3.0

      fs_l = lhs%which_function_space()
      fs_r = rhs%which_function_space()
      ! Check the arguments qr .or. mm not both or neither
      IF (present(qr) .and. .not.present(mm)) THEN
        ! Quadrature present, only for W3
        IF ((fs_l == w3) .and. (fs_r == w3)) THEN
          ! We are on the right space
          CALL invoke_0_w3_solver_kernel_type(lhs, rhs, chi, ascalar, qr)
        ELSE
          WRITE (log_scratch_space, '(A,I3,",",I3)') "Quadrature required for w3 solver, stopping", fs_l, fs_r
          CALL log_event(log_scratch_space, log_level_error)
        END IF 
      ELSE IF (.not.present(qr) .and. present(mm)) THEN
        ! Mass matrix
        IF (fs_l == w3) THEN
          WRITE (log_scratch_space, '(A)') "Solver_algorithm: mass-matrix not implemented for W3,"                " stopping"
          CALL log_event(log_scratch_space, log_level_error)
        ELSE
          SELECT CASE ( solver_type )
            CASE ( cg_solver )
            CALL cg_solver_algorithm(lhs, rhs, mm, mesh)
            CASE ( bicg_solver )
            CALL bicg_solver_algorithm(lhs, rhs, mm, mesh)
            CASE ( jacobi_solver )
            CALL jacobi_solver_algorithm(lhs, rhs, mm, mesh, num_jacobi_iters)
            CASE ( gmres_solver )
            CALL gmres_solver_algorithm(lhs, rhs, mm, mesh)
            CASE ( gcr_solver )
            CALL gcr_solver_algorithm(lhs, rhs, mm, mesh)
            CASE DEFAULT
            WRITE (log_scratch_space, '(A)') "Invalid linear solver choice, stopping"
            CALL log_event(log_scratch_space, log_level_error)
          END SELECT 
        END IF 
      ELSE IF (present(qr) .and. present(mm)) THEN
        ! Both - bork
        WRITE (log_scratch_space, '(A)') "Quadrature OR mass matrix required for solver not both."             " Whats a guy to do?, stopping"
        CALL log_event(log_scratch_space, log_level_error)
      ELSE
        ! Neither - bork
        WRITE (log_scratch_space, '(A)') "Quadrature OR mass matrix required for solver."             " Gimme something to work with, stopping"
      END IF 

    END SUBROUTINE solver_algorithm

    !--------------------------------------------------

    !> @brief BiCGStab solver with no preconditioning.
    !! @details solves A.x = b where the operation A.x is encoded in a kernel using
    !! the stabilised bi-conjugate gradient method. The choice of matrix is
    !! encoded in the matrix vector kernel that is called
    !! @param[in]  rhs_field The input b
    !! @param[inout] lhs_field The answer, x
    !! @param[in] mm operator type, the mass matrix
    !! @param[in] mesh The mesh object the model for fields
    SUBROUTINE bicg_solver_algorithm(lhs, rhs, mm, mesh)
      USE solver_mod_psy, ONLY: invoke_14
      USE solver_mod_psy, ONLY: invoke_bicg_iterloop_group3
      USE solver_mod_psy, ONLY: invoke_bicg_iterloop_group2
      USE solver_mod_psy, ONLY: invoke_11
      USE solver_mod_psy, ONLY: invoke_bicg_iterloop_group1
      USE solver_mod_psy, ONLY: invoke_9
      USE solver_mod_psy, ONLY: invoke_8
      USE solver_mod_psy, ONLY: invoke_7
      USE solver_mod_psy, ONLY: invoke_6
      USE solver_mod_psy, ONLY: invoke_5
      USE solver_mod_psy, ONLY: invoke_bicg_group2
      USE solver_mod_psy, ONLY: invoke_bicg_group1
      USE solver_mod_psy, ONLY: invoke_2
      USE solver_mod_psy, ONLY: invoke_1

      IMPLICIT NONE

      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(in) :: rhs
      TYPE(operator_type), intent(inout) :: mm
      TYPE(mesh_type), intent(in) :: mesh

      ! The temporary fields
      TYPE(field_type) res, cr, p, v, s, t, cs

      ! The scalars
      ! The greeks - standard BiCGStab
      REAL(KIND=r_def) rho, alpha, omega, beta, norm
      REAL(KIND=r_def) ts, tt
      ! Others
      REAL(KIND=r_def) err, sc_err, init_err
      INTEGER iter
      REAL(KIND=r_def) const
      INTEGER rhs_fs
      TYPE(function_space_type) fs

      ! Compute the residual this is a global sum to the PSy ---
      CALL invoke_1(sc_err, rhs)
      sc_err = max(sqrt(sc_err), 0.1_r_def)
      WRITE (log_scratch_space, '(A,E15.8)') "Solver_algorithm: BICGstab starting ... ||b|| = ", sc_err
      CALL log_event(log_scratch_space, log_level_debug)
      CALL invoke_2(lhs)

      rhs_fs = rhs%which_function_space()
      v = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      CALL invoke_bicg_group1(v, lhs, mm)

      res = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      CALL invoke_bicg_group2(res, rhs, v, err)

      err = sqrt(err)/sc_err
      init_err = err
      IF (err < solver_tol) THEN
        WRITE (log_scratch_space, '(A, I2,A,E12.4,A,E15.8)') "BICG solver_algorithm: converged in ", 0, " iters, init=", init_err, " final=", err
        CALL log_event(log_scratch_space, log_level_debug)
        RETURN
      END IF 

      alpha = 1.0_r_def
      omega = 1.0_r_def
      norm = 1.0_r_def

      cr = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      CALL invoke_5(cr, res)

      p = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      CALL invoke_6(p)

      t = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      s = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      cs = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      CALL invoke_7(v)

      DO iter = 1, max_iter

        CALL invoke_8(rho, cr, res)
        beta = (rho/norm) * (alpha/omega)
        const = beta*omega
        CALL invoke_9(t, res, const, v)

        CALL preconditioner(s, t, no_pre_cond)

        CALL invoke_bicg_iterloop_group1(beta, p, s, v, mm, norm, cr)

        alpha = rho/norm
        CALL invoke_11(s, res, alpha, v)

        CALL preconditioner(cs, s, no_pre_cond)

        CALL invoke_bicg_iterloop_group2(t, cs, mm, tt, ts, s)

        omega = ts/tt
        ! lhs = lhs + omega * s + alpha * p
        CALL invoke_bicg_iterloop_group3(lhs, omega, s, alpha, p, res, t)
        norm = rho

        ! Check for convergence
        CALL invoke_14(err, res)
        err = sqrt(err)/sc_err

        WRITE (log_scratch_space, '(A,I2,A, E15.8)') "solver_algorithm[", iter, "]: res = ", err
        CALL log_event(log_scratch_space, log_level_trace)

        IF (err < solver_tol) THEN
          WRITE (log_scratch_space, '(A, I2, A, E12.4, A, E15.8)') "BICG solver_algorithm: converged in ", iter, " iters, init=", init_err, " final=", err
          CALL log_event(log_scratch_space, log_level_debug)
          EXIT
        END IF 
      END DO 

      IF (iter >= max_iter) THEN
        WRITE (log_scratch_space, '(A, I3, A, E15.8)') "BICG solver_algorithm: NOT converged in", iter, " iters, Res=", err
        CALL log_event(log_scratch_space, log_level_error)
      END IF 

    END SUBROUTINE bicg_solver_algorithm

    !--------------------------------------------------

    !> @brief CG solver for the system A.x = b with no preconditioning.
    !! @details solves A.x = b where the operation A.x is encoded in a kernel using
    !! the conjugate gradient method. The choice of matrix is
    !! encoded in the matrix vector kernel that is called.
    !! @param[in] rhs_field The input b
    !! @param[inout] lhs_field The answer, x
    !! @param[in] mm The mass matrix
    !! @param[in] mesh The mesh object the model for fields
    SUBROUTINE cg_solver_algorithm(lhs, rhs, mm, mesh)
      USE solver_mod_psy, ONLY: invoke_19
      USE solver_mod_psy, ONLY: invoke_cg_iterloop_group2
      USE solver_mod_psy, ONLY: invoke_cg_iterloop_group1
      USE solver_mod_psy, ONLY: invoke_cg_first_guess
      USE solver_mod_psy, ONLY: invoke_15

      IMPLICIT NONE

      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(in) :: rhs
      TYPE(operator_type), intent(inout) :: mm
      TYPE(mesh_type), intent(in) :: mesh

      ! The temporary fields
      TYPE(field_type) res, p, ap

      ! The scalars
      REAL(KIND=r_def) alpha, beta
      REAL(KIND=r_def) rs_new, rs_old
      ! Others
      REAL(KIND=r_def) err, sc_err, init_err
      REAL(KIND=r_def) const
      INTEGER iter
      INTEGER rhs_fs
      TYPE(function_space_type) fs

      CALL invoke_15(rs_old, rhs)

      ! Compute the residual this is a global sum to the PSy ---

      rhs_fs = rhs%which_function_space()

      res = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      p = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      ap = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      ! First guess: lhs = 0
      CALL invoke_cg_first_guess(lhs, ap, mm, res, rhs, p, rs_old)

      err = sqrt(rs_old)
      sc_err = max(err, 0.1_r_def)
      init_err = sc_err
      WRITE (log_scratch_space, '(A,E15.8)') "CG solver_algorithm: starting ... ||b|| = ", sc_err
      CALL log_event(log_scratch_space, log_level_debug)
      IF (err < solver_tol) THEN
        WRITE (log_scratch_space, '(A, I2, A, E12.4, A, E15.8)') "CG solver_algorithm: converged in ", 0, " iters, init=", init_err, " final=", err
        CALL log_event(log_scratch_space, log_level_debug)
        RETURN
      END IF 

      DO iter = 1, max_iter
        CALL invoke_cg_iterloop_group1(ap, p, mm, rs_new)

        alpha = rs_old/rs_new

        CALL invoke_cg_iterloop_group2(lhs, alpha, p, res, ap, err)
        ! Check for convergence
        err = sqrt(rs_new)/sc_err

        WRITE (log_scratch_space, '(A, I2, A, E15.8)') "CG solver_algorithm[", iter, "]: res = ", err
        CALL log_event(log_scratch_space, log_level_trace)
        IF (err < solver_tol) THEN
          WRITE (log_scratch_space, '(A, I2, A, E12.4, A, E15.8)') "CG solver_algorithm: converged in ", iter, " iters, init=", init_err, " final=", err
          CALL log_event(log_scratch_space, log_level_debug)
          EXIT
        END IF 

        beta = rs_new/rs_old
        rs_old = rs_new
        CALL invoke_19(beta, p, res)

      END DO 

      IF (iter >= max_iter) THEN
        WRITE (log_scratch_space, '(A, I3, A, E15.8)') "CG solver_algorithm: NOT converged in", iter, " iters, Res=", err
        CALL log_event(log_scratch_space, log_level_error)
      END IF 

    END SUBROUTINE cg_solver_algorithm

    !--------------------------------------------------

    !> @brief Jacobi solver for the system A.x = b.
    !! @details solves A.x = b where the operation A.x is encoded in a kernel using
    !! a fixed (n_iter) number of iterations. The choice of matrix is
    !! encoded in the matrix vector kernel that is called. No measure of convergence
    !! is used instead the algorithm is assumed to have converged sufficiently
    !! after (n_iter) iterations
    !! @param[in] rhs_field The input b
    !! @param[inout] lhs_field The answser, x
    !! @param[in] mm operator type, the mass matrix
    !! @param[in] mesh The mesh object the model for fields
    !! @param[in] n_iter The number of Jacobi iterations to perform
    SUBROUTINE jacobi_solver_algorithm(lhs, rhs, mm, mesh, n_iter)
      USE solver_mod_psy, ONLY: invoke_jacobi_iterloop
      USE solver_mod_psy, ONLY: invoke_21
      USE solver_mod_psy, ONLY: invoke_jacobi_mass_lump

      IMPLICIT NONE

      INTEGER, intent(in) :: n_iter
      TYPE(field_type), intent(inout) :: lhs, rhs
      TYPE(operator_type), intent(inout) :: mm
      TYPE(mesh_type), intent(in) :: mesh
      TYPE(field_type) ax, lumped_weight, res

      REAL(KIND=r_def), parameter :: mu = 0.9_r_def

      INTEGER iter
      INTEGER rhs_fs
      TYPE(function_space_type) fs

      rhs_fs = rhs%which_function_space()

      ax = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      lumped_weight = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      res = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      ! Compute mass lump
      CALL invoke_jacobi_mass_lump(ax, lumped_weight, mm, lhs, rhs)

      ! Initial guess
      CALL invoke_21(lhs)

      DO iter = 1,n_iter

        CALL invoke_jacobi_iterloop(ax, lhs, mm, res, rhs, lumped_weight, mu)
        ! Ready for next iteration
      END DO 

    END SUBROUTINE jacobi_solver_algorithm

    !--------------------------------------------------

    !> @brief GMRes solver for the system A.x = b.
    !! @details solves A.x = b where the operation A.x is encoded in a kernel using
    !! GMRes algorithm. The choice of matrix is
    !! encoded in the matrix vector kernel that is called. No measure of convergence
    !! is used instead the algorithm is assumed to have converged sufficiently
    !! after (n_iter) iterations
    !! @param[in] rhs_field The input b
    !! @param[inout] lhs_field The answser, x
    !! @param[in] mm The mass matrix
    !! @param[in] mesh The mesh object the model for fields
    SUBROUTINE gmres_solver_algorithm(lhs, rhs, mm, mesh)
      USE solver_mod_psy, ONLY: invoke_32
      USE solver_mod_psy, ONLY: invoke_gmres_iterloop_group2
      USE solver_mod_psy, ONLY: invoke_30
      USE solver_mod_psy, ONLY: invoke_29
      USE solver_mod_psy, ONLY: invoke_28
      USE solver_mod_psy, ONLY: invoke_27
      USE solver_mod_psy, ONLY: invoke_gmres_iterloop_group1
      USE solver_mod_psy, ONLY: invoke_25
      USE solver_mod_psy, ONLY: invoke_gmres_group1
      USE solver_mod_psy, ONLY: invoke_23

      USE constants_mod, ONLY: gcrk

      IMPLICIT NONE

      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(in) :: rhs
      TYPE(operator_type), intent(inout) :: mm
      TYPE(mesh_type), intent(in) :: mesh
      ! The temporary fields
      TYPE(field_type) ax, r, s, w, v(gcrk)

      ! The scalars
      REAL(KIND=r_def) h(gcrk+1, gcrk), u(gcrk), g(gcrk+1)
      REAL(KIND=r_def) beta, si, ci, nrm, h1, h2, p, q
      ! Others
      REAL(KIND=r_def) err, sc_err, init_err
      REAL(KIND=r_def) const
      INTEGER iter, i, j, k, m
      INTEGER rhs_fs
      TYPE(function_space_type) fs

      rhs_fs = rhs%which_function_space()
      ax = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      r = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      s = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      w = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      DO iter = 1,gcrk
        v(iter) = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      END DO 

      CALL invoke_23(err, rhs)
      sc_err = max(sqrt(err), 0.01_r_def)
      init_err = sc_err

      IF (err < solver_tol) THEN
        WRITE (log_scratch_space, '(A, I2, A, E12.4, A, E15.8)') "GMRES solver_algorithm: converged in ", 0, " iters, init=", init_err, " final=", err
        CALL log_event(log_scratch_space, log_level_debug)
        RETURN
      END IF 

      CALL invoke_gmres_group1(ax, lhs, mm, r, rhs, s, err)

      beta = sqrt(err)

      const = 1.0_r_def/beta
      CALL invoke_25(v(1), const, s)


      h(:,:) = 0.0_r_def
      g(:) = 0.0_r_def
      g(1) = beta

      DO iter = 1, max_iter

        DO j = 1, gcrk

          ! This is the correct settings => call Precon(w,v(:,:,j),pstit,pstcnd)
          CALL preconditioner(w, v(j), no_pre_cond)
          CALL invoke_gmres_iterloop_group1(s, w, mm)

          ! This is the correct settings => call Precon(w,s,preit,precnd)
          CALL preconditioner(w, s, no_pre_cond)

          DO k = 1, j
            CALL invoke_27(h(k, j), v(k), w)
          END DO 
          CALL invoke_28(err, w)
          h(j+1,j) = sqrt( err )
          IF (j < gcrk) THEN
            const = 1.0_r_def/h(j+1,j)
            CALL invoke_29(v(j + 1), const, w)
          END IF 
        END DO 

        ! Solve (7.23) of Wesseling (see Saad's book)
        DO m = 1, gcrk
          nrm = sqrt(h(m,m)*h(m,m) + h(m+1,m)*h(m+1,m))
          si = h(m+1,m)/nrm
          ci = h(m,m)/nrm
          p = ci*g(m) + si*g(m+1)
          q = -si*g(m) + ci*g(m+1)
          g(m) = p
          g(m+1) = q
          DO j = m, gcrk
            h1 = ci*h(m,j)   + si*h(m+1,j)
            h2 = -si*h(m,j)   + ci*h(m+1,j)
            h(m,j) = h1
            h(m+1,j) = h2
          END DO 
        END DO 

        u(gcrk) = g(gcrk)/h(gcrk,gcrk)
        DO i = gcrk-1, 1, -1
          u(i) = g(i)
          DO j = i+1, gcrk
            u(i) = u(i) - h(i,j)*u(j)
          END DO 
          u(i) = u(i)/h(i,i)
        END DO 

        DO i = 1, gcrk
          ! This is the correct settings => call Precon(s,v(:,:,i),pstit,pstcnd)
          CALL preconditioner(s, v(i), no_pre_cond)
          CALL invoke_30(lhs, u(i), s)
        END DO 

        ! Check for convergence
        CALL invoke_gmres_iterloop_group2(ax, lhs, mm, r, rhs, err)

        beta = sqrt(err)

        err = beta/sc_err
        IF (err <  solver_tol) THEN
          WRITE (log_scratch_space, '(A, I2, A, E12.4, A, E15.8)') "GMRES solver_algorithm: converged in ", iter, " iters, init=", init_err, " final=", err
          CALL log_event(log_scratch_space, log_level_debug)
          EXIT
        END IF 

        ! This is the correct settings => call Precon(s,r,preit,precnd)
        CALL preconditioner(s, r, no_pre_cond)
        const = 1.0_r_def/beta
        CALL invoke_32(v(1), const, s)

        g(:) = 0.0_r_def
        g(1) = beta

      END DO 

      IF (iter >= max_iter .and. err >  solver_tol) THEN
        WRITE (log_scratch_space, '(A, I3, A, E15.8)') "GMRES solver_algorithm: NOT converged in", iter, " iters, Res=", err
        CALL log_event(log_scratch_space, log_level_error)
      END IF 

    END SUBROUTINE gmres_solver_algorithm

    !--------------------------------------------------

    !> @brief GCR solver for the system A.x = b.
    !! @details solves A.x = b where the operation A.x is encoded in a kernel using
    !! the Preconditioned GCR(k) algorithm from Wesseling. The choice of matrix is
    !! encoded in the matrix vector kernel that is called. No measure of convergence
    !! is used instead the algorithm is assumed to have converged sufficiently
    !! after (n_iter) iterations
    !! @param[in] rhs_field The input b
    !! @param[inout] lhs_field The answser, x
    !! @param[in] mm operator type, the mass matrix
    !! @param[in] mesh The mesh object the model for fields
    SUBROUTINE gcr_solver_algorithm(lhs, rhs, mm, mesh)
      USE solver_mod_psy, ONLY: invoke_39
      USE solver_mod_psy, ONLY: invoke_gcr_iterloop_group3
      USE solver_mod_psy, ONLY: invoke_37
      USE solver_mod_psy, ONLY: invoke_gcr_iterloop_group2
      USE solver_mod_psy, ONLY: invoke_gcr_iterloop_group1
      USE solver_mod_psy, ONLY: invoke_gcr_group1
      USE solver_mod_psy, ONLY: invoke_33

      USE constants_mod, ONLY: gcrk

      IMPLICIT NONE

      TYPE(field_type), intent(inout) :: lhs
      TYPE(field_type), intent(in) :: rhs
      TYPE(operator_type), intent(inout) :: mm
      TYPE(mesh_type), intent(in) :: mesh

      ! The temporary fields
      TYPE(field_type) ax, r, s(gcrk), v(gcrk)

      ! The scalars
      REAL(KIND=r_def) alpha
      ! Others
      REAL(KIND=r_def) err, sc_err, init_err
      REAL(KIND=r_def) const
      INTEGER iter, m, n
      INTEGER rhs_fs
      TYPE(function_space_type) fs

      rhs_fs = rhs%which_function_space()

      ax = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      r = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

      DO iter = 1,gcrk
        s(iter) = field_type(vector_space = fs%get_instance(mesh, rhs_fs))

        v(iter) = field_type(vector_space = fs%get_instance(mesh, rhs_fs))
      END DO 
      CALL invoke_33(err, rhs)
      sc_err = max(sqrt(err), 0.01_r_def)
      init_err = sc_err

      IF (err < solver_tol) THEN
        WRITE (log_scratch_space, '(A, I2, A, E12.4, A, E15.8)') "GCR solver_algorithm: converged in ", 0, " iters, init=", init_err, " final=", err
        CALL log_event(log_scratch_space, log_level_debug)
        RETURN
      END IF 

      CALL invoke_gcr_group1(ax, lhs, mm, r, rhs)

      DO iter = 1, max_iter
        DO m = 1, gcrk
          ! This is the correct settings -> call Precon(s(:,:,m),r,prit,prec)
          CALL preconditioner(s(m), r, no_pre_cond)

          CALL invoke_gcr_iterloop_group1(v(m), s(m), mm)

          DO n = 1, m-1
            CALL invoke_gcr_iterloop_group2(alpha, v(m), v(n), s(m), s(n))
          END DO 
          CALL invoke_37(err, v(m))

          alpha = sqrt(err)
          const = 1.0_r_def/alpha
          CALL invoke_gcr_iterloop_group3(const, v(m), s(m), alpha, r, lhs)
        END DO 

        CALL invoke_39(err, r)
        err = sqrt( err )/sc_err
        IF (err <  solver_tol) THEN
          WRITE (log_scratch_space, '(A, I2, A, E12.4, A, E15.8)') "GCR solver_algorithm: converged in ", iter, " iters, init=", init_err, " final=", err
          CALL log_event(log_scratch_space, log_level_debug)
          EXIT
        END IF 
      END DO 

      IF (iter >= max_iter .and. err >  solver_tol) THEN
        WRITE (log_scratch_space, '(A, I3, A, E15.8)') "GCR solver_algorithm: NOT converged in", iter, " iters, Res=", err
        CALL log_event(log_scratch_space, log_level_error)
      END IF 

    END SUBROUTINE gcr_solver_algorithm

    !--------------------------------------------------

    !> @brief Applies a selected prconditioner to a vector x
    !! @details Applies one of s number of preconditioners to a field x
    !! and returns the preconditioned field y. Currently no preconditioner
    !! is applied and y = x.
    !! @param[in]    x The input field
    !! @param[inout] y The output field
    !! @param[in] pre_cond_type The type of preconditioner to be used
    !! routine to use
    SUBROUTINE preconditioner(y, x, pre_cond_type)
      USE solver_mod_psy, ONLY: invoke_40

      USE constants_mod, ONLY: diagonal_pre_cond

      IMPLICIT NONE

      TYPE(field_type), intent(inout) :: y
      TYPE(field_type), intent(in) :: x
      INTEGER, intent(in) :: pre_cond_type

      SELECT CASE ( pre_cond_type )
        CASE ( diagonal_pre_cond )
        ! Diagonal preconditioner
        WRITE (log_scratch_space, '(A)') "Diagonal preconditioner not implemented yet"
        CALL log_event(log_scratch_space, log_level_error)
        CASE DEFAULT
        ! Default - do nothing
        CALL invoke_40(y, x)
      END SELECT 

      RETURN
    END SUBROUTINE preconditioner

  END MODULE solver_mod