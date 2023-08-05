__attribute__((reqd_work_group_size(64, 1, 1)))
__kernel void compute_unew_code(
  __global double * restrict unew,
  __global double * restrict uold,
  __global double * restrict z,
  __global double * restrict cv,
  __global double * restrict h,
  double tdt,
  double dx,
  int xstart,
  int xstop,
  int ystart,
  int ystop
  ){
  double tdts8;
  double tdtsdx;
  int unewLEN1 = get_global_size(0);
  int unewLEN2 = get_global_size(1);
  int uoldLEN1 = get_global_size(0);
  int uoldLEN2 = get_global_size(1);
  int zLEN1 = get_global_size(0);
  int zLEN2 = get_global_size(1);
  int cvLEN1 = get_global_size(0);
  int cvLEN2 = get_global_size(1);
  int hLEN1 = get_global_size(0);
  int hLEN2 = get_global_size(1);
  int i = get_global_id(0);
  int j = get_global_id(1);
  if ((((i < xstart) || (i > xstop)) || ((j < ystart) || (j > ystop)))) {
    return;
  }
  tdts8 = (tdt / 8.0e0);
  tdtsdx = (tdt / dx);
  unew[i + j * unewLEN1] = ((uold[i + j * uoldLEN1] + ((tdts8 * (z[i + (j + 1) * zLEN1] + z[i + j * zLEN1])) * (((cv[i + (j + 1) * cvLEN1] + cv[(i - 1) + (j + 1) * cvLEN1]) + cv[(i - 1) + j * cvLEN1]) + cv[i + j * cvLEN1]))) - (tdtsdx * (h[i + j * hLEN1] - h[(i - 1) + j * hLEN1])));
}

