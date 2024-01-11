! Last updated: 03-Feb-2012
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
! BE and moment calculations are done to 64-bit precesion
! Shell filling as per: particles_and_nuclei-povh_et_al-fig_17.6

	character oamn*27,oamp*27,ll(7),sh*29,oo1*2,oo2*2,ch2*2,spn*4
	integer lc(7,2),ln(7,2),n(2),m(2),lm(2),lmc(2),cc,A
	real j
	real*8 u,un,be,mevtj,bemv
	oamn='011202313142452035316146242'
	oamp='011202313144252053361169999'
	ll(1)='s';ll(2)='p';ll(3)='d'
	do i=4,7
		ll(i)=char(i+98)
	end do
	gs1=5.5858d0; gs0=-3.8263d0; un=5.05078324d0; mevtj=1.602176565d-19; cc=0
	print *,'Nuclear magneton, mu_n=',un,'*10^(-27) J/T'
1	lc=1;ln=1;lm=1;lmc=1
	print *,'Enter # of n & p respectively (n<167,p<139):'
	read *,n
	if(n(1)>166 .or. n(2)>138) then
		write(*,*) 'ERROR: n or p out of range!'
		goto 1
	end if
	A=n(1)+n(2)
	print *,'Neutron Number:    ',n(1)
	print *,'Atomic Number:     ',n(2)
	print *,'Atomic Mass Number:',A
	bemv=be(A,n(2))
	print *,'Binding Energy:',bemv,'MeV'
	print *,'            Or:',bemv*mevtj,'J'
	print *,'Nucleonic Configuration:'
	print *
	print *,'Neutron       | Proton      '
	print *,'-------------------------------'
	m=n; i=1
	sh(9:11)='   ';	sh(14:16)=' | '; sh(25:27)='   '
	do while(max(m(1),m(2))>0)
		l1=ichar(oamn(i:i))-47
		l2=ichar(oamp(i:i))-47
		nc1=2*l1+lc(l1,1)-1
		sh(1:8)=char(ln(l1,1)+48)//ll(l1)//'('//ch2(nc1-1)//'/2)'
		if(l2<10) then
			nc2=2*l2+lc(l2,2)-1
			sh(17:24)=char(ln(l2,2)+48)//ll(l2)//'('//ch2(nc2-1)//'/2)'
		else
			sh(17:24)='        '
		end if
		if(l1/=1) then
			ln(l1,1)=ln(l1,1)-(lc(l1,1)-1)/2
			s1=lc(l1,1)*0.5
			lc(l1,1)=lc(l1,1)*(-1)
		else
			ln(l1,1)=ln(l1,1)+1
			s1=0.5
		end if
		if(l2/=1 .and. l2<10) then
			ln(l2,2)=ln(l2,2)-(lc(l2,2)-1)/2
			s2=lc(l2,2)*0.5
			lc(l2,2)=lc(l2,2)*(-1)
		else if(l2<10) then
			ln(l2,2)=ln(l2,2)+1
			s2=0.5
		end if
		i=i+1
		do k=1,2
			if(m(1)>0) then
				lm(1)=l1; lmc(1)=-1*lc(l1,1)
				sh(12:13)=ch2(min(nc1,m(1)))
				if(mod(n(1),2)/=0 .and. mod(n(2),2)==0) then
					spn=sh(4:7)
					s=s1
				end if
			else
				sh(12:13)='  '
			end if
			if(m(2)>0) then
				lm(2)=l2; lmc(2)=-1*lc(l2,2)
				sh(28:29)=ch2(min(nc2,m(2)))
				if(mod(n(1),2)==0 .and. mod(n(2),2)/=0) then
					spn=sh(20:23)
					s=s2
				end if
			else
				sh(28:29)='  '
			end if
		end do
		print *,sh
		m(1)=m(1)-nc1; m(2)=m(2)-nc2
	end do
	print *,'-------------------------------'
	print *,''
	if(mod(n(1)-n(2),2)==0) then
		if(mod(n(1),2)==0) then
			print *,'Parity: +'
			print *,'Spin: 0'
			print *,'Magnetic Dipole Moment: 0 J/T'
		else
			print *,'Parity: ',char(44+(-1)**(lm(1)+lm(2)+1))
			oo1=ch2(abs(lm(1)-lm(2)+(lmc(1)-lmc(2))/2))
			oo2=ch2(abs((lm(1)+lm(2))+(lmc(1)+lmc(2))/2-2))
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
	print *,'Spin: ',spn
	print *,'ssss:',l,is,s
	ol=1.0*(l-1); j=ol+s
	if(is==1) then
		u=0.5d0*((j*(j+1)+ol*(ol+1)-s*(s+1))+gs1*(j*(j+1)-ol*(ol+1)+s*(s+1)))/((j+1)*1.0d0)
	else
		u=0.5d0*gs0*(j*(j+1)-ol*(ol+1)+s*(s+1))/((j+1)*1.0d0)
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
	crA=dexp(dlog(A*1.0d0)/3.0d0)
	tfA=dexp(-3.0d0*dlog(A*1.0d0)/4.0d0)
	if(mod(A,2)==0) then
		if(mod(Z,2)==0) then
			dA=33.6d0*tfA
		else
			dA=-33.6d0*tfA
		end if
	else
		dA=0.0d0
	end if
	be=15.753d0*A-17.804d0*crA*crA-0.7103d0*Z*Z/crA-23.69d0*(A-2*Z)*(A-2*Z)/A+dA
	end function
