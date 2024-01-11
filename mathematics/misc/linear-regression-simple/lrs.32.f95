! Last updated: 07-Jul-2012
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (32-bit) to Linear Fit one-dimensional data points
! using Least Squares Method
! Also known as Simple Linear Regression

! data points x() lie on x-axis and y() on y-axis
! n is the number of data points (or the size of x or y array)
! m is slope and c is intercept, so the equation is  y=m*x+c
! pcc is Pearson Product-Moment Correlation Coefficient

    real x(10),y(10),m
    n=10
    open(1,file='data.txt')
    do i=1,n
        read(1,*) x(i),y(i)
    enddo
    call lnr_ft32(x,y,n,m,c,pcc)
    print *,'Slope:',m
    print *,'Intercept:',c
    print *,"Pearson's r:",pcc
    end

! Subroutine (32-bit) to Linear Fit one-dimensional data points
! m is slope and c is intercept, so the equation is  y=m*x+c
! pcc is Pearson Product-Moment Correlation Coefficient
    subroutine lnr_ft32(x,y,n,m,c,pcc)
    real,intent(in) :: x(n),y(n)
    integer,intent(in) :: n
    real,intent(out) :: m,c,pcc
    sx=0; sy=0
    sx2=0; sxy=0; sy2=0
    do i=1,n
        sx=sx+x(i)
        sy=sy+y(i)
        sx2=sx2+x(i)*x(i)
        sxy=sxy+x(i)*y(i)
        sy2=sy2+y(i)*y(i)
    enddo
    m=(sxy-sx*sy/n)/(sx2-sx*sx/n)
    c=sy/n-m*sx/n
    pcc=(n*sxy-sx*sy)/sqrt((n*sx2-sx*sx)*(n*sy2-sy*sy))
    endsubroutine