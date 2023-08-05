__attribute__((reqd_work_group_size(64, 1, 1)))
__kernel void compute_vnew_code(
  __global double * restrict vnew,
  __global double * restrict vold,
  __global double * restrict z,
  __global double * restrict cu,
  __global double * restrict h,
  double tdt,
  double dy,
  int xstart,
  int xstop,
  int ystart,
  int ystop
  ){
  double tdts8;
  double tdtsdy;
  int vnewLEN1 = get_global_size(0);
  int vnewLEN2 = get_global_size(1);
  int voldLEN1 = get_global_size(0);
  int voldLEN2 = get_global_size(1);
  int zLEN1 = get_global_size(0);
  int zLEN2 = get_global_size(1);
  int cuLEN1 = get_global_size(0);
  int cuLEN2 = get_global_size(1);
  int hLEN1 = get_global_size(0);
  int hLEN2 = get_global_size(1);
  int i = get_global_id(0);
  int j = get_global_id(1);
  if ((((i < xstart) || (i > xstop)) || ((j < ystart) || (j > ystop)))) {
    return;
  }
  tdts8 = (tdt / 8.0e0);
  tdtsdy = (tdt / dy);
  vnew[i + j * vnewLEN1] = ((vold[i + j * voldLEN1] - ((tdts8 * (z[(i + 1) + j * zLEN1] + z[i + j * zLEN1])) * (((cu[(i + 1) + j * cuLEN1] + cu[i + j * cuLEN1]) + cu[i + (j - 1) * cuLEN1]) + cu[(i + 1) + (j - 1) * cuLEN1]))) - (tdtsdy * (h[i + j * hLEN1] - h[i + (j - 1) * hLEN1])));
}

