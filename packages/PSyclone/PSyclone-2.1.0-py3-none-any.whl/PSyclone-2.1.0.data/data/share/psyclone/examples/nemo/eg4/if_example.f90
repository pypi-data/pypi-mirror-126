! -----------------------------------------------------------------------------
!
! Original code Governed by the CeCILL licence (http://www.cecill.info)
!
! -----------------------------------------------------------------------------
! BSD 3-Clause License
!
! Code modifications Copyright (c) 2019-2020, Science and Technology Facilities
! Council
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
! Author R. W. Ford, STFC Daresbury Lab

! Code extracted from the tra_adv benchmark, with a SIGN intrinsic
! replaced with equivalent code and the resultant expression
! simplified. Literals have also had the Fortran double precision
! specification (e.g. 0.d0) removed.
program test_ifs

  integer, parameter :: jpi=10, jpj=10, jpk=10
  real, dimension(jpi,jpj,jpk) :: zwx, zslpx
  real :: tmpx
  integer :: ji, jj, jk
  
  DO jk = 1, jpk-1
     DO jj = 2, jpj
        DO ji = 2, jpi
           tmpx = zwx(ji,jj,jk) * zwx(ji-1,jj,jk)
           if (tmpx .ge. 0.0d0) then
              zslpx(ji,jj,jk) = 0.5 * ( zwx(ji,jj,jk) + zwx(ji-1,jj,jk) )
           else
              zslpx(ji,jj,jk) = 0.0
           end if
        END DO
     END DO
  END DO

end program
