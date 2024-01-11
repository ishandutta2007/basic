/*
Last updated: 10-Aug-2012
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Program to get pixel array of a 24/32-bit Bitmap Image

The program asks user to input the Bitmap image filename
(should be with .bmp or .dib extension)
Output is the array ipc of dimensions Height x Width x p
where p=3 for 24-bit and p=4 for 32-bit.

24-bit Bitmap will have order RGB for each pixel.
32-bit Bitmap will have order RGBA for each pixel,
where A is the alpha value for transparency.
All values vary between 0-255.

Array size is automatically set as per height and
width of the image. Array is arranged same as you look
at the image, that means upper-left most pixel
will have first entry in the array. Note that
this order is not true in actual Bitmap file, hence
appropriate conversions have been applied.

Support for Bitmaps below 24-bit will be added later.
Plane error can also be added, but not necessary.
Program will probably be better using pointers,
structs, classes and functions. Will be updated later.
Try to add support for very large Bitmaps.
*/

#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int main()
{ // Reading filenames and defining input stream
  char fln[100];
  cout<<"Enter the input image filename with extension: ";
  cin.get(fln,101);
  ifstream fl(fln);
  while(fl.good()==0)
  { fl.close();
    cout<<"File not readable, re-enter: ";
    cin.get(fln,101);
    fl.open(fln);
  }

// Reading BMP Header
  char bh[14];
  int ibh[14];
  for(int i=0;i<14;i++)
  { fl.get(bh[i]); ibh[i]=int(bh[i]); }
  if((ibh[0]!=66 || ibh[1]!=77) && // BM: most common
     (ibh[0]!=66 || ibh[1]!=65) && // BA: OS/2 struct Bitmap Array
     (ibh[0]!=67 || ibh[1]!=73) && // CI: OS/2 struct Color Icon
     (ibh[0]!=67 || ibh[1]!=80) && // CP: OS/2 struct Color Pointer
     (ibh[0]!=73 || ibh[1]!=67) && // IC: OS/2 struct Icon
     (ibh[0]!=80 || ibh[1]!=84))   // PT: OS/2 Pointer
  { cout<<"WARNING: Input file is either damaged or not a Bitmap image.\n"; }

// Reading DIB Header
  char dh[ibh[10]-14];
  int idh[ibh[10]-14];
  for(int i=0;i<ibh[10]-14;i++)
  { fl.get(dh[i]); idh[i]=int(dh[i]); }

// Width, Height and Bytes/Pixel
  int wd,ht,cb;
  wd=0; ht=0;
  for(int j=0;j<4;j++)
  { wd=wd+idh[j+4]*int(pow(256,j));
    ht=ht+idh[j+8]*int(pow(256,j));
  }
  cb=idh[14]/8;

// Reading Pixel data
  char pc;
  int ipc[ht][wd][cb];
// For 32-bit per pixel Bitmap
  if(cb==4)
  { cout<<"INFO: 32-bit Bitmap encountered.\n";
    for(int i=ht-1;i>-1;i--)
    { for(int j=0;j<wd;j++)
      { for(int k=3;k>-1;k--)
        { fl.get(pc);
          ipc[i][j][k]=int(pc);
          if(ipc[i][j][k]<0)
          { ipc[i][j][k]=ipc[i][j][k]+256; }
        }
      }
    }
  }
// For 24-bit per pixel Bitmap
  if(cb==3)
  { cout<<"INFO: 24-bit Bitmap encountered.\n";
    int pd=fmod(wd,4);
    for(int i=ht-1;i>-1;i--)
    { for(int j=0;j<wd;j++)
      { for(int k=2;k>-1;k--)
        { fl.get(pc);
          ipc[i][j][k]=int(pc);
          if(ipc[i][j][k]<0)
          { ipc[i][j][k]=ipc[i][j][k]+256; }
        }
      }
      for(int pi=0;pi<pd;pi++)
      { fl.get(); }
    }
  }
// Else error is shown
  if(cb!=3 && cb!=4)
  { cout<<"ERROR: Bitmap not one of 24/32-bit.\n"; }
}
