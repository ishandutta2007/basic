/*
Last updated: 02-Mar-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (32-bit) to calculate the inverse and
determinant of a matrix using Augmented Matrix Method

The arguments of function invmat_32() are:
  n = number of rows/columns of the square matrix a
  a = the square matrix, whose inverse and determinant to calculate
  ai = the output inverse matrix
The function returns the determinant

ALL YOU NEED TO DO:
Call function invmat_32(n,a,ai)

NOTE:
All matrices are stored as 1D array, where a[i][j] --> a[i*n+j]
If the matrix is not invertible, ai will contain nan entries
  and the function will return 0
Row exchanges are performed if diagonal entry becomes 0
  during operations. Instead, if you want it to be < eps (some
  small number like 1e-10, then change four conditions marked by
  "zero-checking" and "non-zero-checking" in the function,
  change it to check for appropriate relation;
  you would need cmath library for abs
Example given is from a sample file "miaduamm.in.txt"; main()
  reads this file. Read instructions in file on how to input data.
  But the function is independent of all this file reading
*/

#include<iostream>
#include<fstream>

using namespace std;

float invmat_32(int n,float* aa,float* ai);

int main()
{
    cout.precision(8);
    int i,j,n;
    ifstream ifln;
    ifln.open("miaduamm.in.txt");
    ifln>>n;
    float* a = new float[n*n];
    float* ai = new float[n*n];
    for(i=0;i<n*n;i++) ifln>>a[i];
    ifln.close();

    float det = invmat_32(n,a,ai);

    cout<<"Determinant:"<<endl;
    cout<<det<<endl<<endl;
    cout<<"Inverse:"<<endl;
    for(i=0;i<n;i++) {
        for(j=0;j<n;j++) cout<<ai[i*n+j]<<"   ";
        cout<<endl;
    }
    delete[] a,ai;
    return 0;
}

// Function (32-bit) to calculate the inverse and determinant
// of a square matrix using Augmented Matrix Method
float invmat_32(int n,float* aa,float* ai)
{
    int i,j,k,n1=n+1,n2=n*n;
    float af,det=1;
    float* a = new float[n2];
    float* t1 = new float[n];
    bool exc=true;
    float nanf (const char* c);

// Copying aa to a and initializing ai to identity matrix
    for(i=0;i<n2;i++) {
        a[i]=aa[i];
        ai[i]=0;
    }
    for(i=0;i<n2;i=i+n1) ai[i]=1;

// Exchanging first row with anouther such that a[0]!=0
    if(!a[0]) {                      // zero-checking; abs(a[0])<eps
        for(i=1;i<n;i++) {
            if(a[i*n]) {             // non-zero-checking; abs(a[i*n])>eps
                exc=false;
                det*=-1;
                for(k=0;k<n;k++) {
                    t1[k]=a[i*n+k];
                    a[i*n+k]=a[k];
                    a[k]=t1[k];
                    t1[k]=ai[i*n+k];
                    ai[i*n+k]=ai[k];
                    ai[k]=t1[k];
                }
                break;
            }
        }
        if(exc) {
            for(i=0;i<n2;i++) ai[i]=nanf("");
            return 0;
        }
    }

// Applying operations that convert a to upper-triangular
//   and applying row exchanges as necessary
    for(k=0;k<n-1;k++) {
        if(!a[k*n1]) {              // zero-checking; abs(a[k*n+k])<eps
            exc=true;
            for(i=k+1;i<n;i++) {
                if(a[i*n+k]) {       // non-zero-checking; abs(a[i*n+k])>eps
                    exc=false;
                    det*=-1;
                    for(j=0;j<n;j++) {
                        t1[j]=a[i*n+j];
                        a[i*n+j]=a[k*n+j];
                        a[k*n+j]=t1[j];
                        t1[j]=ai[i*n+j];
                        ai[i*n+j]=ai[k*n+j];
                        ai[k*n+j]=t1[j];
                    }
                    break;
                }
            }
            if(exc) {
                for(i=0;i<n2;i++) ai[i]=nanf("");
                return 0;
            }
        }
        for(j=k+1;j<n;j++) {
            af=-a[j*n+k]/a[k*n1];
            for(i=k+1;i<n;i++) {
                a[j*n+i]=a[j*n+i]+a[k*n+i]*af;
            }
            for(i=0;i<j;i++) {
                ai[j*n+i]=ai[j*n+i]+ai[k*n+i]*af;
            }
        }
    }

// Exiting if last element is 0
    if(!a[n2-1]) {
        for(i=0;i<n2;i++) ai[i]=nanf("");
        return 0;
    }

// Calculating the determinant
    for(i=0;i<n;i++) {
        det*=a[i*n1];
    }

// Applying operations that convert a to diagonal matrix
    for(k=n-1;k>0;k--) {
        for(j=k-1;j>-1;j--) {
            af=-a[j*n+k]/a[k*n1];
            a[j*n+k]=0;
            for(i=0;i<n;i++) {
                ai[j*n+i]=ai[j*n+i]+ai[k*n+i]*af;
            }
        }
    }

// Applying operations that normalize diagonals of a
    for(j=0;j<n;j++) {
        for(i=0;i<n;i++) {
            ai[j*n+i]=ai[j*n+i]/a[j*n1];
        }
    }

    delete[] a,t1;
    return det;
}
