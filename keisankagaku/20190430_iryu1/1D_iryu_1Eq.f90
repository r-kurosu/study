module constants
  implicit none
  integer::i,nt
  integer, parameter :: imax = 200,ntmax = 250
  real(8):: T(0:imax),xmax,x,u,dx,dt,cfl
  integer,parameter :: SP = kind(1.0)
  integer,parameter :: DP = selected_real_kind(2*precision(1.0_SP))
end module constants

module print
  use constants
  implicit none
 
 contains
  subroutine print__profile(f)
    real(DP), dimension(0:imax), intent(in) :: f
    integer :: counter = 0
    character(len=*), parameter :: base = "./data/temp.j=middle."
    character(len=4) :: serial_num
    character(len=40) filename
  
    write(serial_num,'(i4.4)') counter

    write(filename,"(a,i5.5,a)") base//serial_num
    open(10,file=filename)
    do i = 0 , imax
       write(10,*) i*dx, f(i)
    end do
    close(10)
    counter = counter + 1
    
  end subroutine print__profile
end module print

program thermal_explicit
  use constants
  use print

  implicit none
  
  u=1
  dt   = 0.1
  xmax = 200
  dx   = xmax/imax
  cfl=u*dt/dx
  
  open(10,file="initial.txt")
  open(11,file="final.txt")

   !initial state
   do i = 0, imax
      x = dx*i
      if (i>=20 .and. i<=50) then
         T(i) = 1
       else
         T(i) =0
      endif
      write(10,*) i,x,T(i)
   enddo
   call print__profile(T(:))

   
   !Time step
   do nt = 1, ntmax
      do i = 1, imax-1
         T(i) = T(i) -cfl*(T(i+1)-T(i))
      end do
      if (mod(nt,10)==0) call print__profile(T(:))
      write(*,*)nt
   end do
   
   !Final state
   do i = 0, imax
      x = dx*i
      write(11,*) i,x,T(i)
   end do
end program thermal_explicit
