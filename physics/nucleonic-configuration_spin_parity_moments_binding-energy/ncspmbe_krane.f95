! Last updated: 31-Dec-2011
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Program to get Nucleonic Configuration, Spin, Parity,
! Magnetic Dipole Moment, Binding Energy of nucleus in ground state

! Idea is to feed l and compute the rest based on it.
! In while-loop, l goes from 1 onwards.
! ln is like principal quantum number.
! lc is the sign of spin quantum number
! lm is to decide the last l of p & n, lmc the corresponding spin sign
! s,j denote usual quantities, ol denotes actual l (i.e. l-1 in program)
! Shell filling based on krane_fig-5.6

	character oam*28,ll(7),sh*17,sh1*10,sh2*14,oo1*2,oo2*2,ch2*2
	integer lc(7),ln(7),n(2),m(2),lm(2),lmc(2),cc,A
	real j
	real*8 u,un,be,mevtj,bemv
	oam='01120231314422055331164264026'
	ll(1)='s';ll(2)='p';ll(3)='d'
	do i=4,7
		ll(i)=char(i+98)
	end do
	gs1=5.5858; gs0=-3.8263; un=5.05078324; cc=0; mevtj=1.602176565e-19
	print *,'Nuclear magneton, mu_n=',un,'*10^(-27) J/T'
1	lc=1;ln=1;lm=1;lmc=1
	print *,'Enter # of n & p respectively (each <169):'
	read *,n
	A=n(1)+n(2)
	print *,'Neutron Number:    ',n(1)
	print *,'Atomic Number:     ',n(2)
	print *,'Atomic Mass Number:',A
	bemv=be(A,n(2))
	print *,'Binding Energy:',bemv,'MeV'
	print *,'            Or:',bemv*mevtj,'J'
	print *,'Nucleonic Configuration:'
	m=n; i=1
	do while(max(m(1),m(2))>0)
		l=ichar(oam(i:i))-47
		nc=2*l+lc(l)-1
		if(nc>10) then
			sh1=char(ln(l)+48)//ll(l)//'('//char(nc/10+48)//char(mod(nc,10)+47)//'/2)  '
		else
			sh1=char(ln(l)+48)//ll(l)//'('//char(nc+47)//'/2)   '
		end if
		if(l/=1) then
			ln(l)=ln(l)-(lc(l)-1)/2
			s=lc(l)*0.5
			lc(l)=lc(l)*(-1)
		else
			ln(l)=ln(l)+1
			s=0.5
		end if
		i=i+1
		do k=1,2
			if(m(1)>0) then
				lm(1)=l; lmc(1)=-1*lc(l)
				sh2=sh1//ch2(min(nc,m(1)))//'n'
				if(m(2)>0) sh2(14:14)=','
			else
				sh2=sh1//'   '
			end if
			if(m(2)>0) then
				lm(2)=l; lmc(2)=-1*lc(l)
				sh=sh2//ch2(min(nc,m(2)))//'p'
			else
				sh=sh2
			end if
		end do
		print *,sh
		m(1)=m(1)-nc; m(2)=m(2)-nc
	end do
	print *,''
	if(mod(n(1)-n(2),2)==0) then
		if(mod(n(1),2)==0) then
			print *,'Parity: +'
			print *,'Spin: 0'
			print *,'Magnetic Dipole Moment: 0 J/T'
		else
			print *,'Parity: ',char(44+(-1)**(lm(1)+lm(2)+1))
			oo1=ch2(abs(lm(1)-lm(2)+(lmc(1)-lmc(2))/2))
			oo2=ch2((lm(1)+lm(2))+(lmc(1)+lmc(2))/2-2)
			print *,'Spin: varies in step of one from ',oo1,' to ',oo2
			print *,'Magnetic Dipole Moment: (complicated odd-odd case)'
		end if
		goto 2
	end if
	if(mod(n(1),2)==0) then
		l=lm(2)
		is=2
	else
		l=lm(1)
		is=1
	end if
	print *,'Parity: ',char(44+(-1)**(l))
	print *,'Spin: ',sh(4:6)
	ol=1.0*(l-1); j=ol+s
	if(is==1) then
		u=0.5*((j*(j+1)+ol*(ol+1)-s*(s+1))+gs1*(j*(j+1)-ol*(ol+1)+s*(s+1)))/(j+1)
	else
		u=0.5*gs0*(j*(j+1)-ol*(ol+1)+s*(s+1))/(j+1)
	end if
	print *,'Magnetic Dipole Moment:',u*un,'x 10^(-27) J/T'
	print *,'                    Or:',u,'* mu_n'

2	cc=cc+1
	print *,'-------------------------- ',ch2(cc),' --------------------------'
	goto 1
	end

	character*2 function ch2(n)
	if(n<10) then
		ch2=' '//char(n+48)
	else
		ch2=char(n/10+48)//char(mod(n,10)+48)
	end if
	end function

	real*8 function be(A,Z)
	integer A,Z
	real*8 crA,tfA
	crA=exp(log(A*1.0)/3)
	tfA=exp(-3*log(A*1.0)/4)
	if(mod(A,2)==0) then
		if(mod(Z,2)==0) then
			dA=33.6*tfA
		else
			dA=-33.6*tfA
		end if
	else
		dA=0
	end if
	be=15.753*A-17.804*crA*crA-0.7103*Z*Z/crA-23.69*(A-2*Z)*(A-2*Z)/A+dA
	end function
