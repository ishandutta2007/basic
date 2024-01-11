/*
Last updated: 13-Apr-2015
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (64-bit) to generate prime numbers upto
n using the sieve of Eratosthenes

ALL YOU NEED TO DO:
Call the function primes_soe_64(n, np)
where n is the limit up to
which primes are needed (inclusive)
and np is the pre-allocated output int array
that will contain the primes
The function returns number of primes generated
*/

#include <iostream>
#include <cmath>

using namespace std;

long long int primes_soe_64(long long int n, long long int np[]);

int main()
{
    long long int m, n;
    long long int* np = new long long int[2000];
    n = 289;
    m = primes_soe_64(n, np);
    cout << "Prime numbers generated: " << m << endl;

    delete[] np;
    return 0;
}

long long int primes_soe_64(long long int n, long long int np[])
{
    if (n < 2) return 0;
    long long int i, k, m, nsq;
    long long int n2 = (n - 1) / 2;
    bool* ip = new bool[n2];
    for (i = 0; i < n2; i++) {
        ip[i] = true;
    }
    k = 3;
    nsq = floor(sqrt(n) + 0.5);
    while (k <= nsq) {
        for (i = k * k / 2 - 1; i < n2; i += k) {
            ip[i] = false;
        }
        while (k <= nsq) {
            k += 2;
            if(ip[k / 2 - 1]) break;
        }
    }
    m = 1;
    np[0] = 2;
    for (i = 0; i < n2; i++) {
        if (ip[i]) {
            np[m] = 2 * i + 3;
            m++;
        }
    }
    delete[] ip;
    return m;
}
