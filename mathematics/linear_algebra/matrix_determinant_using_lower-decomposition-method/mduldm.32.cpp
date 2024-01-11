/*
Last updated: 11-Mar-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (32-bit) to calculate the determinant
of a matrix using Lower Decomposition Method

The arguments of function detmat_32() are:
  n = number of rows/columns of the square matrix a
  a = the square matrix, whose determinant to calculate
The function returns the determinant

ALL YOU NEED TO DO:
Call function detmat_32(n,a)

NOTE:
All matrices are stored as 1D array, where a[i][j] --> a[i*n+j]
If the matrix is not invertible, function will return 0
Row exchanges are performed if diagonal entry becomes 0
  during operations. Instead, if you want it to be < eps (some
  small number like 1e-10, then change four conditions marked by
  "zero-checking" and "non-zero-checking" in the function,
  change it to check for appropriate relation;
  you would need cmath library for abs
Example given is from a sample file "mduldm.in.txt"; main()
  reads this file. Read instructions in file on how to input data.
  But the function is independent of all this file reading
*/

#include<iostream>
#include<fstream>

using namespace std;

float detmat_32(int n,float* aa);

int main()
{
    cout.precision(8);
    int i,j,n;
    ifstream ifln;
    ifln.open("mduldm.in.txt");
    ifln>>n;
    float* a = new float[n*n];
    for(i=0;i<n*n;i++) ifln>>a[i];
    ifln.close();

    float det = detmat_32(n,a);

    cout<<"Determinant: "<<det<<endl;
    delete[] a;
    return 0;
}

// Function (32-bit) to calculate the determinant
// of a square matrix using Lower Decomposition Method
float detmat_32(int n,float* aa)
{
    int i,j,k,n1=n+1,n2=n*n;
    float af,det=1;
    float* a = new float[n2];
    float* t1 = new float[n];
    bool exc=true;

// Copying aa to a
    for(i=0;i<n2;i++) {
        a[i]=aa[i];
    }

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
                }
                break;
            }
        }
        if(exc) return 0;
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
                    }
                    break;
                }
            }
            if(exc) return 0;
        }
        for(j=k+1;j<n;j++) {
            af=-a[j*n+k]/a[k*n1];
            for(i=k+1;i<n;i++) {
                a[j*n+i]=a[j*n+i]+a[k*n+i]*af;
            }
        }
    }

// Calculating the determinant
    for(i=0;i<n;i++) {
        det*=a[i*n1];
    }
    delete[] a,t1;
    return det;
}
