/*
Last updated: 20-Aug-2019
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function to compute GCD using Binary GCD/Stein's Algorithm
*/

#include <iostream>

long long int bgcd(long long int a, long long int b)
{
    long long int k, t;
    if (a == 0) return b;
    if (b == 0) return a;
    k = 0;
    while ((a | b) & 1 == 0) {
        a >>= 1;
        b >>= 1;
        k += 1;
    }
    while (a & 1 == 0) {
        a >>= 1;
    }
    while (b != 0) {
        while (b & 1 == 0) {
            b >>= 1;
        }
        if (a > b) {
            t = b;
            b = a;
            a = t;
        }
        b -= a;
    }
    return a << k;
}
