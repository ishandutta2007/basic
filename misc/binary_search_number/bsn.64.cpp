/*
Last updated: 07-Jun-2013
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (64-bit) to binary search a number in a sorted array

ALL YOU NEED TO DO:
Call function bsa_64(a, n1, n2, b) with:
  a = numerical array in which a number to be searched
  n1 = first index from which to begin search (inclusive)
  n2 = last index upto which search is to be made (not inclusive)
  b = number to be searched
NOTE that n2 is not included in the search

OUTPUT:
Output of the functions is the index of number to be searched
If the number does not exist in the array, -1 is returned
*/

#include<iostream>

using namespace std;

template<class tt>
long int bsa_asc_64(tt a[], long int n1, long int n2, tt b);

template<class tt>
long int bsa_dec_64(tt a[], long int n1, long int n2, tt b);

int main()
{
    float aa[1000], ad[1000];
    float b = 101.7;
    for(int i=0;i<1000;i++) {
        aa[i] = 11 + 0.1 * i;
        ad[999-i] = aa[i];
    }

    long int n = sizeof(aa) / sizeof(aa[0]);
    long int nba = bsa_asc_64(aa, 0, n, b);
    cout<<nba<<"  "<<aa[nba]<<endl;
    long int nbd = bsa_dec_64(ad, 0, n, b);
    cout<<nbd<<"  "<<ad[nbd]<<endl;
    return 0;
}

// For ascendingly sorted array
template<class tt>
long int bsa_asc_64(tt a[], long int n1, long int n2, tt b)
{
    if(b > a[n2-1]) {
        return -1; // Not Found
    }
    if(b < a[n1]) {
        return -1; // Not Found
    }
    long int nd = n2 - n1;
    long int nm = n1 + nd / 2;
    while(nd > 1) {
        if(a[nm] > b) {
            n2 = nm;
        }
        else {
            n1 = nm;
        }
        nd = n2 - n1;
        nm = n1 + nd / 2;
    }
    if(a[n1] == b) {
        return n1;
    }
    else if(a[n2] == b) {
        return n2;
    }
    else {
        return -1; // Not Found
    }
}

// For descendingly sorted array
template<class tt>
long int bsa_dec_64(tt a[], long int n1, long int n2, tt b)
{
    if(b < a[n2-1]) {
        return -1; // Not Found
    }
    if(b > a[n1]) {
        return -1; // Not Found
    }
    long int nd = n2 - n1;
    long int nm = n1 + nd / 2;
    while(nd > 1) {
        if(a[nm] < b) {
            n2 = nm;
        }
        else {
            n1 = nm;
        }
        nd = n2 - n1;
        nm = n1 + nd / 2;
    }
    if(a[n1] == b) {
        return n1;
    }
    else if(a[n2] == b) {
        return n2;
    }
    else {
        return -1; // Not Found
    }
}
