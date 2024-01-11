/*
Last updated: 15-Aug-2013
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Functions to calculate Greatest Common Divisor
(GCD) or Highest Common Factor (HCF) using
Euclidean's Algorithm

ALL YOU NEED TO DO:
Call appropriate gcd_() function with
  integers (in any order)

Integers passed to functions don't
  change after calculation
*/

#include<iostream>

using namespace std;

// Greatest Common Divisor (GCD) Function (32-bit)
int gcd_32(int m, int n)
{
    int k;
    while(n!=0) {
        k=n;
        n=m%k;
        m=k;
    }
    return m;
}

// Greatest Common Divisor (GCD) Function (64-bit)
long int gcd_64(long int m, long int n)
{
    long int k;
    while(n!=0) {
        k=n;
        n=m%k;
        m=k;
    }
    return m;
}

int main()
{
    cout<<gcd_32(560,880)<<endl;
    return 0;
}
