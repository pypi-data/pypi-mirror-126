PROGRAM shallow
  USE psy_shallow, ONLY: invoke_3
  USE psy_shallow, ONLY: invoke_2
  USE psy_shallow, ONLY: invoke_1
  USE psy_shallow, ONLY: invoke_0
  USE kind_params_mod
  USE shallow_io_mod
  USE timing_mod
  USE gocean_mod, ONLY: model_write_log
  USE model_mod
  USE grid_mod
  USE field_mod
  USE initial_conditions_mod
  USE time_smooth_mod, ONLY: time_smooth
  USE apply_bcs_mod, ONLY: invoke_apply_bcs
  USE compute_cu_mod, ONLY: compute_cu
  USE compute_cv_mod, ONLY: compute_cv
  USE compute_z_mod, ONLY: compute_z
  USE compute_h_mod, ONLY: compute_h
  USE compute_unew_mod, ONLY: compute_unew
  USE compute_vnew_mod, ONLY: compute_vnew
  USE compute_pnew_mod, ONLY: compute_pnew
  USE infrastructure_mod, ONLY: copy
  IMPLICIT NONE
  TYPE(grid_type), TARGET :: model_grid
  TYPE(r2d_field) :: p_fld, pold_fld, pnew_fld
  TYPE(r2d_field) :: u_fld, uold_fld, unew_fld
  TYPE(r2d_field) :: v_fld, vold_fld, vnew_fld
  TYPE(r2d_field) :: cu_fld, cv_fld
  TYPE(r2d_field) :: z_fld
  TYPE(r2d_field) :: h_fld
  TYPE(r2d_field) :: psi_fld
  INTEGER :: ncycle, itmax
  INTEGER :: idxt0, idxt1
  REAL(KIND = go_wp) :: dt, tdt
  model_grid = grid_type(GO_ARAKAWA_C, (/GO_BC_PERIODIC, GO_BC_PERIODIC, GO_BC_NONE/), GO_OFFSET_SW)
  CALL model_init(model_grid)
  p_fld = r2d_field(model_grid, GO_T_POINTS)
  pold_fld = r2d_field(model_grid, GO_T_POINTS)
  pnew_fld = r2d_field(model_grid, GO_T_POINTS)
  u_fld = r2d_field(model_grid, GO_U_POINTS)
  uold_fld = r2d_field(model_grid, GO_U_POINTS)
  unew_fld = r2d_field(model_grid, GO_U_POINTS)
  v_fld = r2d_field(model_grid, GO_V_POINTS)
  vold_fld = r2d_field(model_grid, GO_V_POINTS)
  vnew_fld = r2d_field(model_grid, GO_V_POINTS)
  cu_fld = r2d_field(model_grid, GO_U_POINTS)
  cv_fld = r2d_field(model_grid, GO_V_POINTS)
  z_fld = r2d_field(model_grid, GO_F_POINTS)
  h_fld = r2d_field(model_grid, GO_T_POINTS)
  psi_fld = r2d_field(model_grid, GO_F_POINTS)
  tdt = dt
  CALL init_initial_condition_params(p_fld)
  CALL invoke_init_stream_fn_kernel(psi_fld)
  CALL init_pressure(p_fld)
  CALL init_velocity_u(u_fld, psi_fld)
  CALL init_velocity_v(v_fld, psi_fld)
  CALL invoke_apply_bcs(u_fld)
  CALL invoke_apply_bcs(v_fld)
  CALL model_write_log("('psi initial CHECKSUM = ',E24.16)", field_checksum(psi_fld))
  CALL model_write_log("('P initial CHECKSUM = ',E24.16)", field_checksum(p_fld))
  CALL model_write_log("('U initial CHECKSUM = ',E24.16)", field_checksum(u_fld))
  CALL model_write_log("('V initial CHECKSUM = ',E24.16)", field_checksum(v_fld))
  CALL copy_field(u_fld, uold_fld)
  CALL copy_field(v_fld, vold_fld)
  CALL copy_field(p_fld, pold_fld)
  CALL ascii_write(0, 'psifld.dat', psi_fld % data, psi_fld % internal % nx, psi_fld % internal % ny, psi_fld % internal % xstart, &
&psi_fld % internal % ystart)
  CALL model_write(0, p_fld, u_fld, v_fld)
  CALL timer_start('Time-stepping', idxt0)
  DO ncycle = 1, itmax
    CALL timer_start('Compute c{u,v},z,h', idxt1)
    CALL invoke_0(cu_fld, p_fld, u_fld, cv_fld, v_fld, z_fld, h_fld)
    CALL timer_stop(idxt1)
    CALL timer_start('PBCs-1', idxt1)
    CALL invoke_apply_bcs(CU_fld)
    CALL invoke_apply_bcs(CV_fld)
    CALL invoke_apply_bcs(H_fld)
    CALL invoke_apply_bcs(Z_fld)
    CALL timer_stop(idxt1)
    CALL timer_start('Compute new fields', idxt1)
    CALL invoke_1(unew_fld, uold_fld, z_fld, cv_fld, h_fld, tdt, vnew_fld, vold_fld, cu_fld, pnew_fld, pold_fld)
    CALL timer_stop(idxt1)
    CALL timer_start('PBCs-2', idxt1)
    CALL invoke_apply_bcs(UNEW_fld)
    CALL invoke_apply_bcs(VNEW_fld)
    CALL invoke_apply_bcs(PNEW_fld)
    CALL timer_stop(idxt1)
    CALL model_write(ncycle, p_fld, u_fld, v_fld)
    IF (NCYCLE .GT. 1) THEN
      CALL timer_start('Time smoothing', idxt1)
      CALL invoke_2(u_fld, unew_fld, uold_fld, v_fld, vnew_fld, vold_fld, p_fld, pnew_fld, pold_fld)
      CALL timer_stop(idxt1)
    ELSE
      tdt = tdt + dt
    END IF
    CALL timer_start('Field copy', idxt1)
    CALL invoke_3(u_fld, unew_fld, v_fld, vnew_fld, p_fld, pnew_fld)
    CALL timer_stop(idxt1)
  END DO
  CALL timer_stop(idxt0)
  CALL model_write_log("('P CHECKSUM after ',I6,' steps = ',E24.16)", itmax, field_checksum(pnew_fld))
  CALL model_write_log("('U CHECKSUM after ',I6,' steps = ',E24.16)", itmax, field_checksum(unew_fld))
  CALL model_write_log("('V CHECKSUM after ',I6,' steps = ',E24.16)", itmax, field_checksum(vnew_fld))
  CALL model_finalise
END PROGRAM shallow