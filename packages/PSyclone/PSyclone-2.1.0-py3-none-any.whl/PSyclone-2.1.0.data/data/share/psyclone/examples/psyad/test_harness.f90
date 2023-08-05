program adj_test
  use testkern_mod, only : testkern_code
  use testkern_mod_adj, only : testkern_code_adj
  integer, parameter :: array_extent = 20
  integer, parameter :: npts = array_extent
  double precision :: inner1
  double precision :: inner2
  double precision :: abs_diff
  real :: ascalar
  real :: ascalar_input
  real, dimension(npts) :: field1
  real, dimension(npts) :: field1_input
  real, dimension(npts) :: field2
  real, dimension(npts) :: field2_input

  CALL random_number(ascalar)
  ascalar_input = ascalar
  CALL random_number(field1)
  field1_input = field1
  CALL random_number(field2)
  field2_input = field2
  call testkern_code(ascalar, field1, field2, npts)
  inner1 = 0.0
  inner1 = inner1 + ascalar * ascalar
  inner1 = inner1 + DOT_PRODUCT(field1, field1)
  inner1 = inner1 + DOT_PRODUCT(field2, field2)
  call testkern_code_adj(ascalar, field1, field2, npts)
  inner2 = 0.0
  inner2 = inner2 + ascalar * ascalar_input
  inner2 = inner2 + DOT_PRODUCT(field1, field1_input)
  inner2 = inner2 + DOT_PRODUCT(field2, field2_input)
  abs_diff = ABS(inner1 - inner2)
  if (abs_diff > 1.0d-10) then
    WRITE(*, *) 'Test of adjoint of ''testkern_code'' failed: diff = ', abs_diff
    return
  end if
  WRITE(*, *) 'Test of adjoint of ''testkern_code'' passed: diff = ', abs_diff

end program adj_test
