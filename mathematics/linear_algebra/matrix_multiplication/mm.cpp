/*
Last updated: 24-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function to multiply two matrices

ALL YOU NEED TO DO:
Call matmul(a,b,c,na1,na2,nb2), where
  where a,b,c are matrices and
  na1,na2,nb2 are dimensions such that
  a is of size (na1,na2)
  b is of size (na2,nb2)
  c is of size (na1,nb2)

NOTE:
Matrices can be of any class as long as
  * multiplies its elements
Matrices are stored as one-dimensional arrays
  such that (i,j) element of matrix A(n1,n2) can
  be accessed via i*n2+j element
If matrix A is of size (n1,n2), B is of size (n2,n3),
  then C is of size (n1,n3)
*/

#include<iostream>

using namespace std;

template <class tt>
int matmul(tt *a,tt *b,tt *c,int na1,int na2,int nb2)
{
    for(int i=0;i<na1;i++) {
        for(int j=0;j<nb2;j++) {
            c[i*nb2+j]=0;
            for(int k=0;k<na2;k++) {
                c[i*nb2+j]+=a[i*na2+k]*b[k*nb2+j];
            }
        }
    }
    return 0;
}

int main()
{
    int n1=3,n2=2,n3=4,i,j;
    double *a = new double[n1*n2];
    double *b = new double[n2*n3];
    double *c = new double[n1*n3];

// Define Matrix A:
    for(i=0;i<n1;i++) {
        for(j=0;j<n2;j++) {
            a[i*n2+j]=i+j;
        }
    }

// Define Matrix B:
    for(i=0;i<n2;i++) {
        for(j=0;j<n3;j++) {
            b[i*n3+j]=i-j;
        }
    }

// Call real matrix multiplication function
    matmul(a,b,c,n1,n2,n3);

// Rest is just to print the results:

    cout.precision(15);

    cout<<"Matrix A:"<<endl;
    for(i=0;i<n1;i++) {
        for(j=0;j<n2;j++) {
            cout<<a[i*n2+j]<<"  ";
        }
        cout<<endl;
    }
    cout<<endl;

    cout<<"Matrix B:"<<endl;
    for(i=0;i<n2;i++) {
        for(j=0;j<n3;j++) {
            cout<<b[i*n3+j]<<"  ";
        }
        cout<<endl;
    }
    cout<<endl;

    cout<<"Matrix C = A * B:"<<endl;
    for(i=0;i<n1;i++) {
        for(j=0;j<n3;j++) {
            cout<<c[i*n3+j]<<"  ";
        }
        cout<<endl;
    }

    delete[] a,b,c;
    return 0;
}

