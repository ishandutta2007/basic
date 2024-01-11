/*
Last updated: 20-Sept-2012
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
To encrypt/decrypt Vigenere Cipher using known key

Program encrypts/decrypts a Vigenere Cipher from a known key
User is asked whether to shift the input code forward or
backward using the input key
Forward may be used to encrypt, backward to decrypt
Key should be in small caps only
Program treats small and large caps as same in the code
Program disregards all other characters apart form alphabets
like space and prints them as it is on the screen
After printing result on screen,
a new key is immediately asked for new trial
It works according to attached image from Wikipedia
Program can also be used for Caesar Cipher using key as 'c'

A sample is provided with program, its key is mec
Use backward shifting for this sample

TO DO: Add +/- in key for shifting.
*/

#include<iostream>
#include<fstream>
#include<string>
#include<unistd.h>
#include<fcntl.h>
#include<sys/stat.h>

using namespace std;

// To get the file size
// Not used now, but may be useful later
int fl_sz(char fln[100])
{ struct stat st;
  int fd=open(fln,O_RDONLY);
  while(fd==-1)
  { cout<<"File not readable, re-enter: ";
    cin.get(fln,100);
    fd=open(fln,O_RDONLY);
  }
  fstat(fd,&st);
  close(fd);
  return st.st_size;
}

int main()
{ char ch,fln[100];
  string ky;
  int i,nt,kl,sh;
  cout<<"Enter the input filename with extension: ";
  cin>>fln;
  ifstream fl(fln);
  while(fl.good()==0)
  { fl.close();
    cout<<"File not readable, re-enter: ";
    cin>>fln;
    fl.open(fln);
  }
  cout<<"Enter 1 to add the key to the code, 0 to subtract: ";
  cin>>sh;
  while(1)
  { i=0;
    cout<<"Enter the key in small caps: ";
    cin>>ky;
    kl=ky.length();
    fl.clear();
    fl.seekg(0,ios::beg);
    while(1)
    { fl.get(ch);
      if(fl.eof()) break;
      if(ch>96 && ch<123)
      { if(sh==1) nt=(ch+ky[i%kl]-193)%26;
        else nt=(26+(ch-ky[i%kl]+1)%26)%26;
        if(nt==0) { nt=26; }
        cout<<char(96+nt);
        i++; }
      else
      { if(ch>64 && ch<91)
        { if(sh==1) nt=(ch+ky[i%kl]-161)%26;
          else nt=(26+(ch-ky[i%kl]+33)%26)%26;
          if(nt==0) { nt=26; }
          cout<<char(64+nt);
          i++; }
        else
        { cout<<ch; }
      }
    }
    cout<<"\n-----------x-----------\n";
  }
  return 0;
}
