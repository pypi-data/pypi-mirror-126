! ================================================== !
! THIS FILE IS CREATED FROM THE JINJA TEMPLATE FILE  !
! DO NOT MODIFY DIRECTLY                             !
! ================================================== !



! -----------------------------------------------------------------------------
! BSD 3-Clause License
!
! Copyright (c) 2020-2021, Science and Technology Facilities Council.
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
! THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
! "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
! LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
! FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
! COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
! INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
! BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
! LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
! CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
! LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
! ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
! POSSIBILITY OF SUCH DAMAGE.
! -----------------------------------------------------------------------------
! Author: J. Henrichs, Bureau of Meteorology
! Modified: I. Kavcic, Met Office

!> This module implements a simple NetCDF writer using the PSyData
!! interface. A Fortran code instrumented with corresponding calls
!! to the PSyData API and linked in with this library will create
!! a NetCDF file that contains all scalar values, and the dimensions
!! and content for each array.
!! As an extention to the PSyData API it defines additional methods
!! that can be used by a driver/reader:
!! OpenRead:      opens a file for reading
!! ReadScalar...: reads the specified scalar value

module extract_netcdf_base_mod

    use psy_data_base_mod, only : PSyDataBaseType, is_enabled

    use, intrinsic :: iso_fortran_env, only : int64, int32,   &
                                              real32, real64, &
                                              stderr => Error_Unit

    implicit none

    !> This is the data type that manages the information required
    !! to write data to a NetCDF file using the PSyData API. A
    !! static instance of this type is created for each instrumented
    !! region with PSyclone (and each region will write a separate
    !! file).
    type, extends(PSyDataBaseType), public :: ExtractNetcdfBaseType

        !> The NetCDF ID used for this file.
        integer                            :: ncid
        !> Each variable ID. This is required to associate data
        !! with the declared variables: the variables are declared
        !! in the same order in which their value is provided

        integer, dimension(:), allocatable :: var_id

    contains

        ! The various procedures used
        procedure :: PreStart
        procedure :: PreEndDeclaration
        procedure :: PostEnd
        procedure :: OpenRead

        procedure :: DeclareScalarInt
        procedure :: WriteScalarInt
        procedure :: ReadScalarInt
        procedure :: DeclareArray2dInt
        procedure :: WriteArray2dInt
        procedure :: ReadArray2dInt
        procedure :: DeclareScalarReal
        procedure :: WriteScalarReal
        procedure :: ReadScalarReal
        procedure :: DeclareArray2dReal
        procedure :: WriteArray2dReal
        procedure :: ReadArray2dReal
        procedure :: DeclareScalarDouble
        procedure :: WriteScalarDouble
        procedure :: ReadScalarDouble
        procedure :: DeclareArray2dDouble
        procedure :: WriteArray2dDouble
        procedure :: ReadArray2dDouble

        ! Declare generic interface for PreDeclareVariable:
        generic, public :: PreDeclareVariable => &
            DeclareScalarInt, &
            DeclareArray2dInt, &
            DeclareScalarReal, &
            DeclareArray2dReal, &
            DeclareScalarDouble, &
            DeclareArray2dDouble

        !> The generic interface for providing the value of variables:
        generic, public :: ProvideVariable => &
            WriteScalarInt, &
            WriteArray2dInt, &
            WriteScalarReal, &
            WriteArray2dReal, &
            WriteScalarDouble, &
            WriteArray2dDouble

        !> The generic interface for reading the value of variables.
        !! This is not part of the official PSyData API, but is used in
        !! the drivers created by PSyclone.
        generic, public :: ReadVariable => &
            ReadScalarInt, &
            ReadArray2dInt, &
            ReadScalarReal, &
            ReadArray2dReal, &
            ReadScalarDouble, &
            ReadArray2dDouble

    end type ExtractNetcdfBaseType

contains

    ! -------------------------------------------------------------------------
    !> Checks if the return value from a NetCDF call indicates an error.
    !! If so, print the corresponding error message and aborts the program.
    !! It is typically used as a wrapper around NetCDF calls:
    !! retval = CheckError(nf90_close(ncid))
    !! @param[in] retval The return value from a NetCDF operation.
    !! Returns the return value.
    function CheckError(retval)

        use netcdf, only : nf90_noerr, nf90_strerror

        implicit none

        integer, intent(in) :: retval
        integer             :: CheckError

        if (retval /= nf90_noerr) then
            write(stderr, *) "NetCDF Error:"
            write(stderr, *) trim(nf90_strerror(retval))
            stop
        endif
        CheckError = retval

    end function CheckError

    ! -------------------------------------------------------------------------
    !> This is a one-time init function. It is not required for the kernel
    !! extraction and is therefore empty.
    subroutine extract_PSyDataInit()
        implicit none
    end subroutine extract_PSyDataInit

    ! -------------------------------------------------------------------------
    !> This is a one-time shutdown function. It is not required for the kernel
    !! extraction and is therefore empty.
    subroutine extract_PSyDataShutdown()
        implicit none
    end subroutine extract_PSyDataShutdown

    ! -------------------------------------------------------------------------
    !> This subroutine is the first function called when data is written out
    !! before an instrumented region of code.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] module_name The name of the module of the instrumented
    !!            region.
    !! @param[in] region_name The name of the instrumented region.
    !! @param[in] num_pre_vars The number of variables that are declared and
    !!            written before the instrumented region.
    !! @param[in] num_post_vars The number of variables that are also declared
    !!            before an instrumented region of code, but are written after
    !!            this region.
    subroutine PreStart(this, module_name, region_name, num_pre_vars, &
                        num_post_vars)

        use netcdf, only : nf90_create, NF90_CLOBBER

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: module_name, &
                                                               region_name
        integer, intent(in)                                 :: num_pre_vars, &
                                                               num_post_vars

        integer :: retval

        call this%PSyDataBaseType%PreStart(module_name, region_name, &
                                           num_pre_vars, num_post_vars)

        ! Open the NetCDF file
        retval = CheckError(nf90_create(module_name//"-"//region_name//".nc", &
                                        NF90_CLOBBER, this%ncid))
        ! Allocate the array that will store the variable IDs of all
        ! variables that are going to be declared. Note that there might
        ! actually be more variables stored (in LFRic vector fields are
        ! stored as individual NetCDF variables, so a 3d vector field
        ! would actually use 3 individual NetCDF variables). If required,
        ! this array will be re-allocated in the declare functions.
        if (.not. allocated(this%var_id)) then
            allocate(this%var_id(num_pre_vars+num_post_vars))
        endif

    end subroutine PreStart

    ! -------------------------------------------------------------------------
    !> This subroutine is called to open a NetCDF file for reading. The
    !! filename is based on the module and kernel name. This is used by a
    !! driver program that will read a NetCDF file previously created by the
    !! PSyData API.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] module_name The name of the module of the instrumented
    !!            region.
    !! @param[in] region_name The name of the instrumented region.
    subroutine OpenRead(this, module_name, region_name)

        use netcdf, only : nf90_open, NF90_NOWRITE

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: module_name, &
                                                               region_name
        integer :: retval

        retval = CheckError(nf90_open(module_name//"-"//region_name//".nc", &
                                        NF90_NOWRITE, this%ncid))

    end subroutine OpenRead

    ! -------------------------------------------------------------------------
    !> This subroutine is called once all variables are declared (this includes
    !! variables that will be written before as well as variables that are
    !! written after the instrumented region). It is used to switch the NetCDF
    !! file from declaration to writing state, and reset the next_var_index
    !! back to 1.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    subroutine PreEndDeclaration(this)

        use netcdf, only : nf90_enddef

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this

        integer :: retval

        call this%PSyDataBaseType%PreEndDeclaration()
        retval = CheckError(nf90_enddef(this%ncid))

    end subroutine PreEndDeclaration

    ! -------------------------------------------------------------------------
    !> This subroutine is called after the instrumented region has been
    !! executed and all values of variables after the instrumented
    !! region have been provided. This will close the NetCDF file.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    subroutine PostEnd(this)

        use netcdf, only : nf90_close

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this

        integer :: retval
        retval = CheckError(nf90_close(this%ncid))
        call this%PSyDataBaseType%PostEnd()

    end subroutine PostEnd

    ! -------------------------------------------------------------------------
    !> This subroutine declares a scalar integer(kind=int32) value.
    !! A corresponding variable definition is added to the NetCDF file, and
    !! the variable id is stored in the var_id field.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine DeclareScalarInt(this, name, value)

        use netcdf, only : nf90_def_var, NF90_INT

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        integer(kind=int32), intent(in)                                :: value

        integer                            :: retval
        integer, dimension(:), allocatable :: tmp_var_id

        if (this%next_var_index > size(this%var_id)) then
            ! This can happen in LFRic when vector fields are used
            ! Each dimension of this vector becomes one NetCDF
            ! variable, so we need to potentially reallocate this field
            allocate(tmp_var_id(2*size(this%var_id)))
            tmp_var_id(1:size(this%var_id)) = this%var_id
            deallocate(this%var_id)
            call move_alloc(tmp_var_id, this%var_id)
            ! tmp_var_id is deallacted as part of move_alloc
        endif
        retval = CheckError(nf90_def_var(this%ncid, name, NF90_INT, &
                                         this%var_id(this%next_var_index)))
        call this%PSyDataBaseType%DeclareScalarInt(name, value)

    end subroutine DeclareScalarInt

    ! -------------------------------------------------------------------------
    !> This subroutine writes the value of a scalar integer(kind=int32)
    !! variable to the NetCDF file. It takes the variable id from the
    !! corresponding declaration.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine WriteScalarInt(this, name, value)

        use netcdf, only : nf90_put_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        integer(kind=int32), intent(in)                                :: value
        integer                                             :: retval

        retval = CheckError(nf90_put_var(this%ncid, this%var_id(this%next_var_index), &
                                         value))
        call this%PSyDataBaseType%ProvideScalarInt(name, value)

    end subroutine WriteScalarInt

    ! -------------------------------------------------------------------------
    !> This subroutine reads the value of a scalar integer(kind=int32)
    !! variable from the NetCDF file and returns it to the user. Note that
    !! this function is not part of the PSyData API, but it is convenient to
    !! have these functions together here. The driver can then be linked with
    !! this  PSyData library and will be able to read the files.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[out] value The read value is stored here.
    subroutine ReadScalarInt(this, name, value)

        use netcdf, only : nf90_inq_varid, nf90_get_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        integer(kind=int32), intent(out)                               :: value

        integer                                             :: retval, varid

        retval = CheckError(nf90_inq_varid(this%ncid, name, varid))
        retval = CheckError(nf90_get_var(this%ncid, varid, value))

    end subroutine ReadScalarInt



    ! -------------------------------------------------------------------------
    !> This subroutine declares a 2d-array of integer(kind=int32).
    !! A corresponding variable and dimension definitions are added
    !! to the NetCDF file, and the variable id is stored in the var_id field.
    !! @param[in,out] this The instance of the extract_PsyDataType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine DeclareArray2dInt(this, name, value)

        use netcdf

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        integer(kind=int32), dimension(:,:), intent(in)      :: value

        integer                            :: dimid1, dimid2
        integer                            :: retval
        integer, dimension(2)        :: dimids
        integer, dimension(:), allocatable :: tmp_var_id

        if (.not. is_enabled) return

        if (this%next_var_index > size(this%var_id)) then
            allocate(tmp_var_id(2*size(this%var_id)))
            tmp_var_id(1:size(this%var_id)) = this%var_id
            deallocate(this%var_id)
            call move_alloc(tmp_var_id, this%var_id)
            ! tmp_var_id is deallacted as part of move_alloc
        endif

        ! A '%' is added to avoid a clash if the user should have say
        ! an array 'a', and 'adim1'.
        retval = CheckError(nf90_def_dim(this%ncid, name//"dim%1", &
                                         size(value,1), dimid1))
        ! A '%' is added to avoid a clash if the user should have say
        ! an array 'a', and 'adim1'.
        retval = CheckError(nf90_def_dim(this%ncid, name//"dim%2", &
                                         size(value,2), dimid2))
        dimids =  (/ dimid1, dimid2 /)
        retval = CheckError(nf90_def_var(this%ncid, name, NF90_INT, &
                                         dimids, this%var_id(this%next_var_index)))

        call this%PSyDataBaseType%DeclareArray2dInt(name, value)

    end subroutine DeclareArray2dInt

    ! -------------------------------------------------------------------------
    !> This subroutine writes a 2d-array of integer(kind=int32)
    !! to the NetCDF file.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine WriteArray2dInt(this, name, value)

        use netcdf, only : nf90_put_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        integer(kind=int32), dimension(:,:), intent(in)      :: value

        integer :: retval

        if (.not. is_enabled) return
        retval = CheckError(nf90_put_var(this%ncid, this%var_id(this%next_var_index), &
                                         value(:,:)))
        call this%PSyDataBaseType%ProvideArray2dInt(name, value)

    end subroutine WriteArray2dInt

    ! -------------------------------------------------------------------------
    !> This subroutine reads the values of a 2d-array of integer(kind=int32)
    !! It allocates memory for the allocatable parameter 'value' to store the
    !! read values which is then returned to the caller. If the memory for the
    !! array cannot be allocated, the application will be stopped.
    !! @param[in,out] this The instance of the extract_PsyDataType.
    !! @param[in] name The name of the variable (string).
    !! @param[out] value An allocatable, unallocated 2d-double precision array
    !!             which is allocated here and stores the values read.
    subroutine ReadArray2dInt(this, name, value)

        use netcdf

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target          :: this
        character(*), intent(in)                                     :: name
        integer(kind=int32), dimension(:,:), allocatable, intent(out) :: value

        integer        :: retval, varid
        integer        :: dim_id
        integer        :: dim_size1,dim_size2
        integer        :: ierr

        ! First query the dimensions of the original array from the
        ! NetCDF file
        retval = CheckError(nf90_inq_dimid(this%ncid, trim(name//"dim%1"), &
                                           dim_id))
        retval = CheckError(nf90_inquire_dimension(this%ncid, dim_id, &
                                                   len=dim_size1))
        retval = CheckError(nf90_inq_dimid(this%ncid, trim(name//"dim%2"), &
                                           dim_id))
        retval = CheckError(nf90_inquire_dimension(this%ncid, dim_id, &
                                                   len=dim_size2))

        ! Allocate enough space to store the values to be read:
        allocate(value(dim_size1,dim_size2), Stat=ierr)
        if (ierr /= 0) then
            write(stderr,*) "Cannot allocate array for ", name, &
                            " of size ", dim_size1,dim_size2, &
                            " in ReadArray2dInt."
            stop
        endif

        ! Initialise it with 0, so that an array comparison will work
        ! even though e.g. boundary areas or so might not be set at all.
        ! The compiler will convert the double precision value to the right
        ! type (e.g. int or single precision).
        value = 0.0d0
        retval = CheckError(nf90_inq_varid(this%ncid, name, varid))
        retval = CheckError(nf90_get_var(this%ncid, varid, value))

    end subroutine ReadArray2dInt

    ! -------------------------------------------------------------------------
    !> This subroutine declares a scalar real(kind=real32) value.
    !! A corresponding variable definition is added to the NetCDF file, and
    !! the variable id is stored in the var_id field.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine DeclareScalarReal(this, name, value)

        use netcdf, only : nf90_def_var, NF90_REAL

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real32), intent(in)                                :: value

        integer                            :: retval
        integer, dimension(:), allocatable :: tmp_var_id

        if (this%next_var_index > size(this%var_id)) then
            ! This can happen in LFRic when vector fields are used
            ! Each dimension of this vector becomes one NetCDF
            ! variable, so we need to potentially reallocate this field
            allocate(tmp_var_id(2*size(this%var_id)))
            tmp_var_id(1:size(this%var_id)) = this%var_id
            deallocate(this%var_id)
            call move_alloc(tmp_var_id, this%var_id)
            ! tmp_var_id is deallacted as part of move_alloc
        endif
        retval = CheckError(nf90_def_var(this%ncid, name, NF90_REAL, &
                                         this%var_id(this%next_var_index)))
        call this%PSyDataBaseType%DeclareScalarReal(name, value)

    end subroutine DeclareScalarReal

    ! -------------------------------------------------------------------------
    !> This subroutine writes the value of a scalar real(kind=real32)
    !! variable to the NetCDF file. It takes the variable id from the
    !! corresponding declaration.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine WriteScalarReal(this, name, value)

        use netcdf, only : nf90_put_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real32), intent(in)                                :: value
        integer                                             :: retval

        retval = CheckError(nf90_put_var(this%ncid, this%var_id(this%next_var_index), &
                                         value))
        call this%PSyDataBaseType%ProvideScalarReal(name, value)

    end subroutine WriteScalarReal

    ! -------------------------------------------------------------------------
    !> This subroutine reads the value of a scalar real(kind=real32)
    !! variable from the NetCDF file and returns it to the user. Note that
    !! this function is not part of the PSyData API, but it is convenient to
    !! have these functions together here. The driver can then be linked with
    !! this  PSyData library and will be able to read the files.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[out] value The read value is stored here.
    subroutine ReadScalarReal(this, name, value)

        use netcdf, only : nf90_inq_varid, nf90_get_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real32), intent(out)                               :: value

        integer                                             :: retval, varid

        retval = CheckError(nf90_inq_varid(this%ncid, name, varid))
        retval = CheckError(nf90_get_var(this%ncid, varid, value))

    end subroutine ReadScalarReal



    ! -------------------------------------------------------------------------
    !> This subroutine declares a 2d-array of real(kind=real32).
    !! A corresponding variable and dimension definitions are added
    !! to the NetCDF file, and the variable id is stored in the var_id field.
    !! @param[in,out] this The instance of the extract_PsyDataType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine DeclareArray2dReal(this, name, value)

        use netcdf

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real32), dimension(:,:), intent(in)      :: value

        integer                            :: dimid1, dimid2
        integer                            :: retval
        integer, dimension(2)        :: dimids
        integer, dimension(:), allocatable :: tmp_var_id

        if (.not. is_enabled) return

        if (this%next_var_index > size(this%var_id)) then
            allocate(tmp_var_id(2*size(this%var_id)))
            tmp_var_id(1:size(this%var_id)) = this%var_id
            deallocate(this%var_id)
            call move_alloc(tmp_var_id, this%var_id)
            ! tmp_var_id is deallacted as part of move_alloc
        endif

        ! A '%' is added to avoid a clash if the user should have say
        ! an array 'a', and 'adim1'.
        retval = CheckError(nf90_def_dim(this%ncid, name//"dim%1", &
                                         size(value,1), dimid1))
        ! A '%' is added to avoid a clash if the user should have say
        ! an array 'a', and 'adim1'.
        retval = CheckError(nf90_def_dim(this%ncid, name//"dim%2", &
                                         size(value,2), dimid2))
        dimids =  (/ dimid1, dimid2 /)
        retval = CheckError(nf90_def_var(this%ncid, name, NF90_REAL, &
                                         dimids, this%var_id(this%next_var_index)))

        call this%PSyDataBaseType%DeclareArray2dReal(name, value)

    end subroutine DeclareArray2dReal

    ! -------------------------------------------------------------------------
    !> This subroutine writes a 2d-array of real(kind=real32)
    !! to the NetCDF file.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine WriteArray2dReal(this, name, value)

        use netcdf, only : nf90_put_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real32), dimension(:,:), intent(in)      :: value

        integer :: retval

        if (.not. is_enabled) return
        retval = CheckError(nf90_put_var(this%ncid, this%var_id(this%next_var_index), &
                                         value(:,:)))
        call this%PSyDataBaseType%ProvideArray2dReal(name, value)

    end subroutine WriteArray2dReal

    ! -------------------------------------------------------------------------
    !> This subroutine reads the values of a 2d-array of real(kind=real32)
    !! It allocates memory for the allocatable parameter 'value' to store the
    !! read values which is then returned to the caller. If the memory for the
    !! array cannot be allocated, the application will be stopped.
    !! @param[in,out] this The instance of the extract_PsyDataType.
    !! @param[in] name The name of the variable (string).
    !! @param[out] value An allocatable, unallocated 2d-double precision array
    !!             which is allocated here and stores the values read.
    subroutine ReadArray2dReal(this, name, value)

        use netcdf

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target          :: this
        character(*), intent(in)                                     :: name
        real(kind=real32), dimension(:,:), allocatable, intent(out) :: value

        integer        :: retval, varid
        integer        :: dim_id
        integer        :: dim_size1,dim_size2
        integer        :: ierr

        ! First query the dimensions of the original array from the
        ! NetCDF file
        retval = CheckError(nf90_inq_dimid(this%ncid, trim(name//"dim%1"), &
                                           dim_id))
        retval = CheckError(nf90_inquire_dimension(this%ncid, dim_id, &
                                                   len=dim_size1))
        retval = CheckError(nf90_inq_dimid(this%ncid, trim(name//"dim%2"), &
                                           dim_id))
        retval = CheckError(nf90_inquire_dimension(this%ncid, dim_id, &
                                                   len=dim_size2))

        ! Allocate enough space to store the values to be read:
        allocate(value(dim_size1,dim_size2), Stat=ierr)
        if (ierr /= 0) then
            write(stderr,*) "Cannot allocate array for ", name, &
                            " of size ", dim_size1,dim_size2, &
                            " in ReadArray2dReal."
            stop
        endif

        ! Initialise it with 0, so that an array comparison will work
        ! even though e.g. boundary areas or so might not be set at all.
        ! The compiler will convert the double precision value to the right
        ! type (e.g. int or single precision).
        value = 0.0d0
        retval = CheckError(nf90_inq_varid(this%ncid, name, varid))
        retval = CheckError(nf90_get_var(this%ncid, varid, value))

    end subroutine ReadArray2dReal

    ! -------------------------------------------------------------------------
    !> This subroutine declares a scalar real(kind=real64) value.
    !! A corresponding variable definition is added to the NetCDF file, and
    !! the variable id is stored in the var_id field.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine DeclareScalarDouble(this, name, value)

        use netcdf, only : nf90_def_var, NF90_DOUBLE

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real64), intent(in)                                :: value

        integer                            :: retval
        integer, dimension(:), allocatable :: tmp_var_id

        if (this%next_var_index > size(this%var_id)) then
            ! This can happen in LFRic when vector fields are used
            ! Each dimension of this vector becomes one NetCDF
            ! variable, so we need to potentially reallocate this field
            allocate(tmp_var_id(2*size(this%var_id)))
            tmp_var_id(1:size(this%var_id)) = this%var_id
            deallocate(this%var_id)
            call move_alloc(tmp_var_id, this%var_id)
            ! tmp_var_id is deallacted as part of move_alloc
        endif
        retval = CheckError(nf90_def_var(this%ncid, name, NF90_DOUBLE, &
                                         this%var_id(this%next_var_index)))
        call this%PSyDataBaseType%DeclareScalarDouble(name, value)

    end subroutine DeclareScalarDouble

    ! -------------------------------------------------------------------------
    !> This subroutine writes the value of a scalar real(kind=real64)
    !! variable to the NetCDF file. It takes the variable id from the
    !! corresponding declaration.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine WriteScalarDouble(this, name, value)

        use netcdf, only : nf90_put_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real64), intent(in)                                :: value
        integer                                             :: retval

        retval = CheckError(nf90_put_var(this%ncid, this%var_id(this%next_var_index), &
                                         value))
        call this%PSyDataBaseType%ProvideScalarDouble(name, value)

    end subroutine WriteScalarDouble

    ! -------------------------------------------------------------------------
    !> This subroutine reads the value of a scalar real(kind=real64)
    !! variable from the NetCDF file and returns it to the user. Note that
    !! this function is not part of the PSyData API, but it is convenient to
    !! have these functions together here. The driver can then be linked with
    !! this  PSyData library and will be able to read the files.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[out] value The read value is stored here.
    subroutine ReadScalarDouble(this, name, value)

        use netcdf, only : nf90_inq_varid, nf90_get_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real64), intent(out)                               :: value

        integer                                             :: retval, varid

        retval = CheckError(nf90_inq_varid(this%ncid, name, varid))
        retval = CheckError(nf90_get_var(this%ncid, varid, value))

    end subroutine ReadScalarDouble



    ! -------------------------------------------------------------------------
    !> This subroutine declares a 2d-array of real(kind=real64).
    !! A corresponding variable and dimension definitions are added
    !! to the NetCDF file, and the variable id is stored in the var_id field.
    !! @param[in,out] this The instance of the extract_PsyDataType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine DeclareArray2dDouble(this, name, value)

        use netcdf

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real64), dimension(:,:), intent(in)      :: value

        integer                            :: dimid1, dimid2
        integer                            :: retval
        integer, dimension(2)        :: dimids
        integer, dimension(:), allocatable :: tmp_var_id

        if (.not. is_enabled) return

        if (this%next_var_index > size(this%var_id)) then
            allocate(tmp_var_id(2*size(this%var_id)))
            tmp_var_id(1:size(this%var_id)) = this%var_id
            deallocate(this%var_id)
            call move_alloc(tmp_var_id, this%var_id)
            ! tmp_var_id is deallacted as part of move_alloc
        endif

        ! A '%' is added to avoid a clash if the user should have say
        ! an array 'a', and 'adim1'.
        retval = CheckError(nf90_def_dim(this%ncid, name//"dim%1", &
                                         size(value,1), dimid1))
        ! A '%' is added to avoid a clash if the user should have say
        ! an array 'a', and 'adim1'.
        retval = CheckError(nf90_def_dim(this%ncid, name//"dim%2", &
                                         size(value,2), dimid2))
        dimids =  (/ dimid1, dimid2 /)
        retval = CheckError(nf90_def_var(this%ncid, name, NF90_DOUBLE, &
                                         dimids, this%var_id(this%next_var_index)))

        call this%PSyDataBaseType%DeclareArray2dDouble(name, value)

    end subroutine DeclareArray2dDouble

    ! -------------------------------------------------------------------------
    !> This subroutine writes a 2d-array of real(kind=real64)
    !! to the NetCDF file.
    !! @param[in,out] this The instance of the ExtractNetcdfBaseType.
    !! @param[in] name The name of the variable (string).
    !! @param[in] value The value of the variable.
    subroutine WriteArray2dDouble(this, name, value)

        use netcdf, only : nf90_put_var

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target :: this
        character(*), intent(in)                            :: name
        real(kind=real64), dimension(:,:), intent(in)      :: value

        integer :: retval

        if (.not. is_enabled) return
        retval = CheckError(nf90_put_var(this%ncid, this%var_id(this%next_var_index), &
                                         value(:,:)))
        call this%PSyDataBaseType%ProvideArray2dDouble(name, value)

    end subroutine WriteArray2dDouble

    ! -------------------------------------------------------------------------
    !> This subroutine reads the values of a 2d-array of real(kind=real64)
    !! It allocates memory for the allocatable parameter 'value' to store the
    !! read values which is then returned to the caller. If the memory for the
    !! array cannot be allocated, the application will be stopped.
    !! @param[in,out] this The instance of the extract_PsyDataType.
    !! @param[in] name The name of the variable (string).
    !! @param[out] value An allocatable, unallocated 2d-double precision array
    !!             which is allocated here and stores the values read.
    subroutine ReadArray2dDouble(this, name, value)

        use netcdf

        implicit none

        class(ExtractNetcdfBaseType), intent(inout), target          :: this
        character(*), intent(in)                                     :: name
        real(kind=real64), dimension(:,:), allocatable, intent(out) :: value

        integer        :: retval, varid
        integer        :: dim_id
        integer        :: dim_size1,dim_size2
        integer        :: ierr

        ! First query the dimensions of the original array from the
        ! NetCDF file
        retval = CheckError(nf90_inq_dimid(this%ncid, trim(name//"dim%1"), &
                                           dim_id))
        retval = CheckError(nf90_inquire_dimension(this%ncid, dim_id, &
                                                   len=dim_size1))
        retval = CheckError(nf90_inq_dimid(this%ncid, trim(name//"dim%2"), &
                                           dim_id))
        retval = CheckError(nf90_inquire_dimension(this%ncid, dim_id, &
                                                   len=dim_size2))

        ! Allocate enough space to store the values to be read:
        allocate(value(dim_size1,dim_size2), Stat=ierr)
        if (ierr /= 0) then
            write(stderr,*) "Cannot allocate array for ", name, &
                            " of size ", dim_size1,dim_size2, &
                            " in ReadArray2dDouble."
            stop
        endif

        ! Initialise it with 0, so that an array comparison will work
        ! even though e.g. boundary areas or so might not be set at all.
        ! The compiler will convert the double precision value to the right
        ! type (e.g. int or single precision).
        value = 0.0d0
        retval = CheckError(nf90_inq_varid(this%ncid, name, varid))
        retval = CheckError(nf90_get_var(this%ncid, varid, value))

    end subroutine ReadArray2dDouble


end module extract_netcdf_base_mod
