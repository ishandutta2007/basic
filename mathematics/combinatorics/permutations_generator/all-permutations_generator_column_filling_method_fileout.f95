! Last updated: 17-Sept-2011
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Program to get all permutations of digits (maximum 9)

! Permutations of numbers (max 9)
! Technique is to go column wise and filling
!   by appropriately choosing (pl-array) what to fill
! Method self-discovered (hence many improvements will follow soon)

! In case some input are same, they will still be treated as distinct
! and their repeatation will be reflected in the output

! ALL YOU NEED TO DO:
! Simply run the program, all inputs are on screen
! Please enter two-digit integers only and total integers less than 10

! Output is ascendingly sorted (with respect to indices)
! Output by default goes to the file 'permutations.txt'

	integer nm(9),pm(9,362880),fc,fct,pl(9),t1,t2,t3,pi,pj
	write(6,*) 'Enter the # digits to enter'
	read *,n
	write(6,*) 'Enter the digits'
	do i=1,n
		read *,nm(i)
	end do
	fc=fct(n)
	t2=fc/n
	t3=t2/(n-1)

	do k=1,n
		do l=t2*(k-1)+1,t2*k
			pm(1,l)=nm(k)
		end do
	end do

	pi=2; pj=1
1	m=0
	do k=1,n
		t1=0
		do l=1,pi-1
			if(nm(k)==pm(l,pj)) then
				t1=1; exit
			end if
		end do
		if(t1==0) then
			m=m+1
			pl(m)=nm(k)
		end if
	end do

	do k=1,m
		do l=pj+(k-1)*t3,pj+k*t3-1
			pm(pi,l)=pl(k)
		end do
	end do
	if(pj+t2<fc) then
		pj=pj+t2
	else
		t2=t2/(n-pi+1)
		if(n/=pi) t3=t3/(n-pi)
		pi=pi+1
		pj=1
	end if
	if(pi<=n) goto 1
	pm(n,fc)=nm(1)

3   format(9I3)
	open(2,file='permutations.txt')
	do j=1,fc
		write(2,3) (pm(i,j),i=1,n)
	end do
	end

	integer function fct(i)
	fct=1
	do j=2,i
		fct=fct*j
	end do
	end function
    