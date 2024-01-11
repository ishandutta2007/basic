/*
Last updated: 16-Dec-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (64-bit) to solve Poisson's Equation in Two Dimensional Uniform
Grid with Dirichlet Boundary Conditions using Finite Difference Method
(Five-Point Stencil and Fourier Transform)
(uses FFTW Libraries, http://www.fftw.org/)

ALL YOU NEED TO DO:
Define Boundary Conditions in function bcs() as per its description below
Define the known function f(x,y) in fxy() as per its description below
Call the poisson solver function poisson_solver_fft_2d_64(nx, x0, x1, ny, y0, y1, u), where
  u is unknown in Poisson's Equation (read its description below)
  nx and ny are number of points in x and y axes (includes boundaries), ny is number of rows
  x0, x1, y0 and y1 are values at boundaries
Compile with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tspei2dugwdbcufdm(5psaft).64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tspei2dugwdbcufdm(5psaft).64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm
Please follow General Example given below for practical usage

POISSON'S EQUATION:
The Poisson's Equation: u_xx + u_yy = f(x,y)
where u_xx is double derivative of unknown u with respect to x,
similarly for u_yy; and f(x,y) is a known function

UNKNOWN QUANTITY u in LHS of POISSON'S EQUATION:
It is of size ny * nx
It includes values at boundaries
Arrangement is such that for nx=5 and ny=4, the indices look like:
  30 31 32 33 34
  20 21 22 23 24
  10 11 12 13 14
  00 01 02 03 04
where y on vertical increases from down to up and x on horizontal
increases from left to right
its boundaries are defined by boundary conditions function bcs(), the boundaries
in above configuration are:
  up:    30 31 32 33 34
  down:  00 01 02 03 04
  left:  10 20
  right: 14 24

INPUT FUNCTION f in RHS of POISSON'S EQUATION:
It is of size ny * nx
It includes values at boundaries (however boundary values of f are actually not used)
Arrangement is such that for nx=5 and ny=4, the indices look same as u:
  30 31 32 33 34
  20 21 22 23 24
  10 11 12 13 14
  00 01 02 03 04
where y on vertical increases from down to up and x on horizontal
increases from left to right
Function f must be specified in the function fxy()

DIRICHLET BOUNDARY CONDITIONS:
Define boundary conditions in function bcs(). Whatever you do in the
function, it should give u with required boundary values.
Up and down boundaries have length nx, whereas left and right have
length ny-2. The arrangement for nx=5,ny=4 looks like:
  30 31 32 33 34
  20          24
  10          14
  00 01 02 03 04
where y on vertical increases from down to up and x on horizontal
increases from left to right
  up:    30 31 32 33 34
  down:  00 01 02 03 04
  left:  10 20
  right: 14 24
Note that you are free to change any value of u in bcs() function, but
boundaries should be properly defined as required.

5-POINT STENCIL:
It refers to the approximation of double derivatives:
u_xx[i,j] = (u[i-1,j] - 2u[i,j] + u[i+1,j]) / hx^2
u_yy[i,j] = (u[i,j-1] - 2u[i,j] + u[i,j+1]) / hy^2

ALGORITHM:
Refer to: http://www.cs.berkeley.edu/~demmel/cs267/lecture24/lecture24.html

COMPLEXITY:
Time Complexity = O(nx*ny*log(nx*ny))
Space Complexity = O(nx*ny)

QUICK TESTING:
A quick test to verify the program's working is to calculate
u_xx + u_yy at every point from output and match against f,
where u_xx and u_yy should be calculated using 5-point stencil

GENERAL EXAMPLE:
Suppose you want to solve u_xx+u_yy=f(y,x)
in the rectangular grid [x0,x1] x [y0,y1] with boundary conditions
u(y,x0)=left(y,x0); u(y,x1)=right(y,x1); u(y0,x)=down(y0,x); u(y1,x)=up(y1,x);
Choose some values of nx and ny
Define boundaries in bcs() as:
  u[j*nx]=left(y,x0);
  u[j*nx+nx-1]=right(y,x1);
  u[i]=down(y0,x);
  u[ny*nx-nx+i]=up(y1,x);
  where x -> x0+hx*i and y -> y0+hy*j
  and hx, hy are grid spacings defined below in the example as
  hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1);
  and loops go as i: 0 -> nx-1 and j: 1 -> ny-2 (inclusive)
Define function in fxy() as:
  f[j*nx+i]=f(y,x);
  where x -> x0+hx*(i-1) and y -> y0+hy*(j-1)
  and loops go as i: 0 -> nx-1 and j: 0 -> ny-1 (inclusive)
Now return to your main() program
Say values of nx, x0, x1, ny, y0, y1 are:
  nx=1500; x0=0; x1=1; ny=2000; y0=0; y1=1;
and calculate the solution of Poisson's Equation:
  poisson_solver_fft_2d_64(nx,x0,x1,ny,y0,y1,u);
Write the values of u, see commented lines in main() for different ways

GIVEN EXAMPLE:
The example given below has f(y,x)=2*exp(x+y)
in the square grid [0,1]x[0,1] with boundary conditions:
u(0,y)=exp(y); u(1,y)=exp(1+y); u(x,0)=exp(x); u(x,1)=exp(1+x);
Its exact solution is u=exp(x+y)
*/

#include <iostream>
#include <cmath>
#include <fftw3.h>

using namespace std;

int fxy(int nx, double x0, double x1, int ny, double y0, double y1, double* f);
int bcs(int nx, double x0, double x1, int ny, double y0, double y1, double* u);
int poisson_solver_fft_2d_64(int nx, double x0, double x1, int ny, double y0, double y1, double* u);

int main()
{
    cout.precision(15);
    int nx=5,ny=9;
    double x0=0.0, x1=1.0, y0=0.0, y1=1.0;
    double *u = new double[nx*ny];

    poisson_solver_fft_2d_64(nx, x0, x1, ny, y0, y1, u);

// To directly print on screen:
/*    for(int j=0;j<ny;j++) {
        for(int i=0;i<nx;i++) {
            cout<<u[j*nx+i]<<" ";
        }
        cout<<endl;
    } */

// To write to a file: (please include fstream at the top)
/*    ofstream ofl;
    ofl.open("poisson64_u.txt");
    for(int j=0;j<ny;j++) {
        for(int i=0;i<nx;i++) {
            ofl<<u[j*nx+i]<<" ";
        }
        ofl<<endl;
    }
    ofl.close(); */

    delete[] u;
    return 0;
}

// Right Hand Side Function in Poisson's Equation
// Includes values at boundaries
int fxy(int nx, double x0, double x1, int ny, double y0, double y1, double* f)
{
    double hx = (x1 - x0) / (nx - 1);
    double hy = (y1 - y0) / (ny - 1);
    double x, y;
    for(int j=0;j<ny;j++) {
        y = y0 + j * hy;
        for(int i=0;i<nx;i++) {
            x = x0 + i * hx;
            f[j*nx+i] = 2 * exp(x + y);
        }
    }
    return 0;
}

// Dirichlet Boudary Conditions
int bcs(int nx, double x0, double x1, int ny, double y0, double y1, double* u)
{
    double hx = (x1 - x0) / (nx - 1);
    double hy = (y1 - y0) / (ny - 1);
    double x, y;
    for(int j=1;j<ny-1;j++) {
        y = y0 + j * hy;
        u[j*nx] = exp(y);              // Left Boundary
        u[j*nx+nx-1] = exp(y + 1);     // Right Boundary
    }
    for(int i=0;i<nx;i++) {
        x = x0 + i * hx;
        u[i] = exp(x);                // Down Boundary
        u[ny*nx-nx+i] = exp(x + 1);   // Up Boundary
    }
    return 0;
}

int poisson_solver_fft_2d_64(int nx, double x0, double x1, int ny, double y0, double y1, double* u)
{
    int nn = nx * ny;
    const double pi = 3.14159265358979324;
    double hx = (x1 - x0) / (nx - 1); double rhx2 = 1/hx/hx;
    double hy = (y1 - y0) / (ny - 1); double rhy2 = 1/hy/hy;
    double *f = new double[nn];

// Obtaining Boudaries and Function values
    bcs(nx, x0, x1, ny, y0, y1, u);
    fxy(nx, x0, x1, ny, y0, y1, f);

// Redefining Function values to include effects of boundaries
    for(int i=1;i<nx-1;i++) {
        f[nx+i] -= u[i] * rhy2;
        f[nn-2*nx+i] -= u[nn-nx+i] * rhy2;
    }
    for(int j=1;j<ny-1;j++) {
        f[j*nx+1] -= u[j*nx] * rhx2;
        f[j*nx+nx-2] -= u[j*nx+nx-1] * rhx2;
    }

// Preparations for FFTs
    int nx2 = 2 * nx - 2;
    int ny2 = 2 * ny - 2;
    double *bx, *by;
    fftw_complex *cx, *cy;
    bx = (double*) fftw_malloc(sizeof(double) * nx2);
    by = (double*) fftw_malloc(sizeof(double) * ny2);
    cx = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * nx2);
    cy = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * ny2);
    fftw_plan px, py;
    px = fftw_plan_dft_r2c_1d(nx2, bx, cx, FFTW_ESTIMATE);
    py = fftw_plan_dft_r2c_1d(ny2, by, cy, FFTW_ESTIMATE);

// Matrix Multiplications using FFT
    for(int j=1;j<ny-1;j++) {
        bx[0] = 0;
        for(int i=1;i<nx-1;i++) {
            bx[i]=f[j*nx+i];
        }
        for(int i=nx-1;i<nx2;i++) {
            bx[i]=0;
        }
        fftw_execute(px);
        for(int i=1;i<nx-1;i++) {
            u[j*nx+i]=cx[i][1];
        }
    }
    delete[] f;
    for(int i=1;i<nx-1;i++) {
        by[0] = 0;
        for(int j=1;j<ny-1;j++) {
            by[j]=u[j*nx+i];
        }
        for(int j=ny-1;j<ny2;j++) {
            by[j]=0;
        }
        fftw_execute(py);
        for(int j=1;j<ny-1;j++) {
            u[j*nx+i]=cy[j][1];
        }
    }
    for(int j=1;j<ny-1;j++) {
        for(int i=1;i<nx-1;i++) {
            u[j*nx+i]=u[j*nx+i]*0.5/((1-cos(i*pi/(nx-1)))*rhx2+(1-cos(j*pi/(ny-1)))*rhy2);
        }
    }
    for(int j=1;j<ny-1;j++) {
        bx[0] = 0;
        for(int i=1;i<nx-1;i++) {
            bx[i]=u[j*nx+i];
        }
        for(int i=nx-1;i<nx2;i++) {
            bx[i]=0;
        }
        fftw_execute(px);
        for(int i=1;i<nx-1;i++) {
            u[j*nx+i]=cx[i][1];
        }
    }
    double tt = -4.0 / ((nx - 1) * (ny - 1));
    for(int i=1;i<nx-1;i++) {
        by[0] = 0;
        for(int j=1;j<ny-1;j++) {
            by[j]=u[j*nx+i];
        }
        for(int j=ny-1;j<ny2;j++) {
            by[j]=0;
        }
        fftw_execute(py);
        for(int j=1;j<ny-1;j++) {
            u[j*nx+i]=cy[j][1]*tt;
        }
    }

    fftw_destroy_plan(px); fftw_destroy_plan(py);
    fftw_free(bx); fftw_free(by); fftw_free(cx); fftw_free(cy);
    return 0;
}

