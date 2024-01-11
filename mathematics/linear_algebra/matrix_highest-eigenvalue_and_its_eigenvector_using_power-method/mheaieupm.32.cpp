/*
Last updated: 14-Aug-2013
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Power Method Function (32-bit) to calculate greatest
Eigenvalue of a Real Matrix and corresponding Eigenvector

ALL YOU NEED TO DO:
Call pwr_ev_32() with n, a, ef and ev
  a is the matrix whose eigens to calculate
  n is the size of ev (or nxn is size of a)
  ef is precision parameter for eigenvalue
    such that when difference in successive calculations
    of eigenvalues is < ef, the iteration stops
  ev is the initial guess for eigenvector
    and will later contain (normalized) eigenvector
  Function returns the eigenvalue
If iteration never stops, you can limit the while
  loop where it is indicated in the function
*/

#include<iostream>
#include<cmath>

using namespace std;

// To multiply two matrices a and b
template <class tt>
int matmul(tt *a,tt *b,tt *c,int na,int nab,int nb)
{
    tt s;
    int i,j,k;
    for(i=0;i<na;i++) {
        for(j=0;j<nb;j++) {
            s=0;
            for(k=0;k<nab;k++) {
                s=s+a[i*nab+k]*b[k*nb+j];
            }
            c[i*nb+j]=s;
        }
    }
    return 0;
}

// To calculate magnitude of vector v
template <class tt>
float vmg(tt v[],int n)
{
    tt vm=v[0]*v[0];
    for(int i=1;i<n;i++) {
        vm=vm+v[i]*v[i];
    }
    return sqrt(vm);
}

// To calculate dot product of vectors v and w
template <class tt>
tt dot(tt v[],tt w[],int n)
{
    tt vw=v[0]*w[0];
    for(int i=1;i<n;i++) {
        vw=vw+v[i]*w[i];
    }
    return vw;
}

// Power Method Function (32-bit)
float pwr_ev_32(int n,float *a,float ef,float ev[])
{
    float v[n],vm,eg,eg1,df;
    int j;
    df=1.e+15;
// If iteration does not stop, limit this
//   while loop to some finite iterations
    while(df>ef) {
        vm=vmg(ev,n);
        for(j=0;j<n;j++) {
            v[j]=ev[j]/vm;
        }
        matmul(a,v,ev,n,n,(int)1);
        eg=dot(v,ev,n);
        for(j=0;j<n;j++) {
            v[j]=ev[j]-eg*v[j];
        }
        df=fabs(eg-eg1);
        eg1=eg;
    }
// Normalizing the eigenvector
    vm=vmg(ev,n);
    for(j=0;j<n;j++) {
        ev[j]=ev[j]/vm;
    }
    return eg;
}

int main()
{
    int n=3;
    float a[n][n],ev[n],eg,ef;

// Precision parameter for eigenvalue
    ef=1.e-6;

// Matrix A whose eigens to be calculated
    a[0][0]=1; a[0][1]=0; a[0][2]=0;
    a[1][0]=0; a[1][1]=1; a[1][2]=2;
    a[2][0]=0; a[2][1]=1; a[2][2]=0;

// Initial guess for eigenvector
    ev[0]=1; ev[1]=1; ev[2]=1;

// Calling Power Method Function
    eg=pwr_ev_32(n,*a,ef,ev);

// Printing Output
    cout.precision(7);
    cout<<"Greatest Eigenvalue: "<<eg<<endl<<endl;
    cout<<"Eigenvector (normalized): "<<endl;
    for(int i=0;i<n;i++) {
        cout<<ev[i]<<"  ";
    }
    cout<<endl;

    return 0;
}
