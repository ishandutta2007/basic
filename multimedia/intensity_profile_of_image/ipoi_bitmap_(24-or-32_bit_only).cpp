/*
Last updated: 10-Aug-2012
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Program to get intensity profile of a
24/32-bit Bitmap Image

The program asks user to input the Bitmap image filename
(should be with .bmp or .dib extension) and also to enter
output filename. Output file will be overwritten if already
exists.

Intensity of a pixel is simply the sum of RGB values
in case of 24-bit. In case of 32-bit, the alpha value
is multiplied to the sum to take care of transparency (which
is equivalent to looking the image in black background).
So intensity can vary between 0-765.

Arrangement of intensities in output file is same
as you look at the image. That is, most upper-left pixel
will have first entry in the output file. Note that
this order is not true in actual Bitmap file, hence
appropriate conversions have been applied.

Support for Bitmaps below 24-bit will be added later
Plane error can also be added, but not necessary
*/

#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int main()
{ // Reading filenames and defining input stream
  char fln[100],ofln[100];
  cout<<"Enter the input image filename with extension: ";
  cin.get(fln,101);
  cout<<"Enter the output text filename with extension: ";
  cin>>ofln;
  ifstream fl(fln);
  while(fl.good()==0)
  { fl.close();
    cout<<"Input file not readable, re-enter: ";
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
  ofstream ofl(ofln,ios::out);
  char pc;
  int ipc[ht][wd][cb];
// For 32-bit per pixel Bitmap
  if(cb==4)
  { cout<<"WARNING: This is a 32-bit Bitmap, intensity values are...\n";
    cout<<"...multiplied by alpha values to take care of transparency.\n";
    float s;
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
    for(int i=0;i<ht;i++)
    { for(int j=0;j<wd;j++)
      { s=(ipc[i][j][0]+ipc[i][j][1]+ipc[i][j][2])*ipc[i][j][3]/255.0;
        ofl<<s<<" ";
      }
      ofl<<endl;
    }
  }
// For 24-bit per pixel Bitmap
  if(cb==3)
  { int s;
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
    for(int i=0;i<ht;i++)
    { for(int j=0;j<wd;j++)
      { s=ipc[i][j][0]+ipc[i][j][1]+ipc[i][j][2];
        ofl<<s<<" ";
      }
      ofl<<endl;
    }
  }
// Else error is shown
  if(cb!=3 && cb!=4)
  { cout<<"ERROR: Bitmap not one of 24/32-bit.\n"; }
}
