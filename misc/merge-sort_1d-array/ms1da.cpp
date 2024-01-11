/*
Last updated: 13-Sept-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function to sort one-dimensional array using Merge Sort

ALL YOU NEED TO DO:
Call function merge_sort_asc (for ascending) or
  merge_sort_dsc (for descending) with:
  n  = number of elements in array a to be sorted
  a = array to be sorted (will be overwritten)

a can be of any class as long as its elements can be compared
  with logical operators < and >

Time Complexity  = O(n.log(n))
Space Complexity = O(n)
Not In-Place
*/

#include<iostream>

using namespace std;

template <class nmb>
int merge_sort_asc(int n, nmb* a);
template <class nmb>
int merge_sort_dsc(int n, nmb* a);

int main()
{
    int n=11;
    long int* a = new long int[n];
    for(int k=0;k<n;k++) {
        a[k]=rand()%1000-400;
    }

    merge_sort_dsc(n,a);

    for(int k=0;k<n;k++) {
        cout<<a[k]<<endl;
    }

    return 0;
}

// Function to sort array in ascending order using Merge Sort
template <class nmb>
int merge_sort_asc(int n, nmb* a)
{
    if(n<2) return 0;
    int m,i1,i2,i10,j,j0,k;
    bool sw;
    nmb* b = new nmb[n];
    j=0;
    b[n-1]=a[n-1];
    while(j<n-1) {
        if(a[j]>a[j+1]) {
            b[j]=a[j+1];
            b[j+1]=a[j];
        }
        else {
            b[j]=a[j];
            b[j+1]=a[j+1];
        }
        j+=2;
    }
    sw=false;
    m=2;
    while(m<n) {
        if(sw) {
            i1=0;
            while(i1<n) {
                i2=i1+m;
                if(i2>=n) {
                    for(k=i1;k<n;k++) { b[k]=a[k]; }
                    break;
                }
                if(i2+m>n) { j0=n; }
                else { j0=i1+2*m; }
                j=i1;
                i10=i1+m;
                while(j<j0) {
                    if(a[i1]<a[i2]) {
                        b[j]=a[i1];
                        i1++;
                    }
                    else {
                        b[j]=a[i2];
                        i2++;
                    }
                    j++;
                    if(i1>=i10) {
                        for(k=0;k<j0-j;k++) { b[j+k]=a[i2+k]; }
                        break;
                    }
                    if(i2>=j0) {
                        for(k=0;k<j0-j;k++) { b[j+k]=a[i1+k]; }
                        break;
                    }
                }
                i1=j0;
            }
            sw=false;
            m*=2;
        }
        else {
            i1=0;
            while(i1<n) {
                i2=i1+m;
                if(i2>=n) {
                    for(k=i1;k<n;k++) { a[k]=b[k]; }
                    break;
                }
                if(i2+m>n) { j0=n; }
                else { j0=i1+2*m; }
                j=i1;
                i10=i1+m;
                while(j<j0) {
                    if(b[i1]<b[i2]) {
                        a[j]=b[i1];
                        i1++;
                    }
                    else {
                        a[j]=b[i2];
                        i2++;
                    }
                    j++;
                    if(i1>=i10) {
                        for(k=0;k<j0-j;k++) { a[j+k]=b[i2+k]; }
                        break;
                    }
                    if(i2>=j0) {
                        for(k=0;k<j0-j;k++) { a[j+k]=b[i1+k]; }
                        break;
                    }
                }
                i1=j0;
            }
            sw=true;
            m*=2;
        }
    }
    if(!sw) {
        for(k=0;k<n;k++) { a[k]=b[k]; }
    }
    return 0;
}

// Function to sort array in descending order using Merge Sort
template <class nmb>
int merge_sort_dsc(int n, nmb* a)
{
    if(n<2) return 0;
    int m,i1,i2,i10,j,j0,k;
    bool sw;
    nmb* b = new nmb[n];
    j=0;
    b[n-1]=a[n-1];
    while(j<n-1) {
        if(a[j]<a[j+1]) {
            b[j]=a[j+1];
            b[j+1]=a[j];
        }
        else {
            b[j]=a[j];
            b[j+1]=a[j+1];
        }
        j+=2;
    }
    sw=false;
    m=2;
    while(m<n) {
        if(sw) {
            i1=0;
            while(i1<n) {
                i2=i1+m;
                if(i2>=n) {
                    for(k=i1;k<n;k++) { b[k]=a[k]; }
                    break;
                }
                if(i2+m>n) { j0=n; }
                else { j0=i1+2*m; }
                j=i1;
                i10=i1+m;
                while(j<j0) {
                    if(a[i1]>a[i2]) {
                        b[j]=a[i1];
                        i1++;
                    }
                    else {
                        b[j]=a[i2];
                        i2++;
                    }
                    j++;
                    if(i1>=i10) {
                        for(k=0;k<j0-j;k++) { b[j+k]=a[i2+k]; }
                        break;
                    }
                    if(i2>=j0) {
                        for(k=0;k<j0-j;k++) { b[j+k]=a[i1+k]; }
                        break;
                    }
                }
                i1=j0;
            }
            sw=false;
            m*=2;
        }
        else {
            i1=0;
            while(i1<n) {
                i2=i1+m;
                if(i2>=n) {
                    for(k=i1;k<n;k++) { a[k]=b[k]; }
                    break;
                }
                if(i2+m>n) { j0=n; }
                else { j0=i1+2*m; }
                j=i1;
                i10=i1+m;
                while(j<j0) {
                    if(b[i1]>b[i2]) {
                        a[j]=b[i1];
                        i1++;
                    }
                    else {
                        a[j]=b[i2];
                        i2++;
                    }
                    j++;
                    if(i1>=i10) {
                        for(k=0;k<j0-j;k++) { a[j+k]=b[i2+k]; }
                        break;
                    }
                    if(i2>=j0) {
                        for(k=0;k<j0-j;k++) { a[j+k]=b[i1+k]; }
                        break;
                    }
                }
                i1=j0;
            }
            sw=true;
            m*=2;
        }
    }
    if(!sw) {
        for(k=0;k<n;k++) { a[k]=b[k]; }
    }
    return 0;
}
