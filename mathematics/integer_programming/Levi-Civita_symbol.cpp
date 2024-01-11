/*
Last updated: 28-Apr-2013
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function to compute Levi-Civita Symbol
or Permutation Symbol

DEFINITION:
eps(i,j,k,...) =  0, if any of i,j,k,... are same
               = +1, if (i,j,k,...) is a cyclic
                     permutation of (0,1,2,...)
               = -1, if (i,j,k,...) is a anti-cyclic
                     permutation of (0,1,2,...)

ALL YOU NEED TO DO:
Simply call function lvcvt(a, n) with a as an array
of indices, i.e., {i,j,k,...} and n as its length.
Result is the returned value by this function.

NOTE:
Note that indices used are as usually done in C++,
  i.e., they start from 0
Cyclic or anti-cyclic permutation is decided by counting
  number of swaps in Bubble Sort (will be improved later)
*/

#include <iostream>

int lvcvt(int *a, int n)
{
    int ifsm = 0;
    for (int j = 0; j < n; j++) {
        for (int k = j + 1; k < n; k++){
            if (a[j] == a[k]) { ifsm = 1; break; }
            if (ifsm == 1) break;
        }
    }
    if (ifsm == 1) {
    return 0;
    }
    else {
        int m, ns = 0;
        for(int k = n - 1; k > -1; k--) {
            for (int j = 0; j < k; j++) {
                if (a[j] > a[j + 1]) {
                    m = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = m;
                    ns++;
                }
            }
        }
        if (ns % 2 == 0) return 1;
        else return -1;
    }
}

int main()
{   int n = 3;
    int i[] = {2, 1, 0};

    std::cout << "eps(";
    for (int j = 0; j < n; j++) std::cout << i[j] << ",";
    std::cout << "\b) = ";
    std::cout << lvcvt(i, n) << std::endl;

// For Demo Printing Only (include math or cmath before running this):
/*    int it, j, m, l;
    for(int l = 0; l < int(pow(n, n)); l++) {
        m = l;
        std::cout << "eps(";
        for(j = 0; j < n; j++) {
            it = pow(n, n - j - 1);
            i[j] = m / it;
            m = m - i[j] * it;
            std::cout << i[j] << ",";
        }
        std::cout << "\b) = " << lvcvt(i, n) << '\n';
    } */
}
