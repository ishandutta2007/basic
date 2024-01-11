% Last updated: 16-Dec-2014
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Function to solve Poisson's Equation in Three Dimensional Uniform
% Grid with Dirichlet Boundary Conditions using Seven-Point
% Stencil and Fourier Transform Method
% THIS CODE IS STILL UNDER DEVELOPMENT

% ALL YOU NEED TO DO:
% Define Boundary Conditions in function bcs() as per its description below
% Define the known function f(x,y,z) in fxyz() as per its description below
% Call the poisson solver function tspei3dugwdbcu7psaftm(nx,x0,x1,ny,y0,y1,nz,z0,z1), where
%   nx, ny and nz are number of points in x, y and z axes (includes boundaries)
%   x0, x1, y0, y1, z0 and z1 are values at boundaries
% This function returns unknown u in Poisson's Equation (read its description below)
% Please follow General Example given below for practical usage

% POISSON'S EQUATION:
% The Poisson's Equation: u_xx + u_yy + u_zz = f(x,y,z)
% where u_xx is double derivative of unknown u with respect to x,
% similarly for u_yy and u_zz; and f(x,y,z) is a user-input function

% UNKNOWN QUANTITY u in LHS of POISSON'S EQUATION:
% It is of size nz * ny * nx
% It includes values at boundaries
% Arrangement is such that for nx=5 and ny=4, the indices look like:
%   41 42 43 44 45
%   31 32 33 34 35
%   21 22 23 24 25
%   11 12 13 14 15
% where y on vertical increases from down to up and x on horizontal
% increases from left to right
% u is initialized by boundary conditions function bcs(), the boundaries
% in above configuration are:
%   up:    41 42 43 44 45
%   down:  11 12 13 14 15
%   left:  21 31
%   right: 25 35

% INPUT FUNCTION f in RHS of POISSON'S EQUATION:
% It is of size ny * nx
% It includes values at boundaries (however boundary values of f are actually not used)
% Arrangement is such that for nx=5 and ny=4, the indices look same as u:
%   41 42 43 44 45
%   31 32 33 34 35
%   21 22 23 24 25
%   11 12 13 14 15
% where y on vertical increases from down to up and x on horizontal
% increases from left to right
% Function f must be specified in the function fxy()

% DIRICHLET BOUNDARY CONDITIONS:
% Define boundary conditions in function bcs(). Whatever you do in this
% function, it should return the boundaries of u.
% Up and down boundaries have length nx, whereas left and right have
% length ny-2. The arrangement for nx=5,ny=4 looks like:
%   41 42 43 44 45
%   31          35
%   21          25
%   11 12 13 14 15
% where y on vertical increases from down to up and x on horizontal
% increases from left to right
% So, the boundaries in above configuration are:
%   up:    41 42 43 44 45
%   down:  11 12 13 14 15
%   left:  21 31
%   right: 25 35
% Note that bcs() function initializes u. You can use any values
% for the inside of u, but boundaries should be properly defined as required.

% 5-POINT STENCIL:
% It refers to the approximation of double derivatives:
% u_xx(i,j) = (u(i-1,j) - 2u(i,j) + u(i+1,j)) / hx^2
% u_yy(i,j) = (u(i,j-1) - 2u(i,j) + u(i,j+1)) / hy^2

% ALGORITHM:
% Refer to: http://www.cs.berkeley.edu/~demmel/cs267/lecture24/lecture24.html

% COMPLEXITY:
% Time Complexity = O(nx*ny*log(nx*ny))
% Space Complexity = O(nx*ny)

% QUICK TESTING:
% A quick test to verify the program's working is to calculate
% u_xx + u_yy at every point from output and match against f,
% where u_xx and u_yy should be calculated using 5-point stencil

% GENERAL EXAMPLE:
% Suppose you want to solve u_xx+u_yy=f(y,x)
% in the rectangular grid [x0,x1] x [y0,y1] with boundary conditions
% u(y,x0)=left(y,x0); u(y,x1)=right(y,x1); u(y0,x)=down(y0,x); u(y1,x)=up(y1,x);
% Choose some values of nx and ny
% Define boundaries in bcs() as:
%   u(j,1)=left(y,x0);
%   u(j,nx)=right(y,x1);
%   u(1,i)=down(y0,x);
%   u(ny,i)=up(y1,x);
%   where x -> x0+hx*(i-1) and y -> y0+hy*(j-1)
%   and hx, hy are grid spacings defined below in the example as
%   hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1);
%   and loops go as i: 1 -> nx and j: 2 -> ny-1
% Define function in fxy() as:
%   f(j,i)=f(y,x);
%   where x -> x0+hx*(i-1) and y -> y0+hy*(j-1)
%   and loops go as i: 1 -> nx and j: 1 -> ny
% Now return to your main program or matlab command window
% Say values of nx, x0, x1, ny, y0, y1 are:
%   >> nx=1500; x0=0; x1=1; ny=2000; y0=0; y1=1;
% Calculate the solution of Poisson's Equation:
%   >> u=tspei2dugwdbcu5psaftm(nx,x0,x1,ny,y0,y1);
% Set values of grid spacing, which will be helpful in plotting:
%   >> hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1);
% Plot the solution as:
%   >> imagesc(x0+hx*(0:nx-1),y0+hy*(0:ny-1),u); colorbar
% To plot with flipped y-axis:
%   >> imagesc(x0+hx*(0:nx-1),y0+hy*(0:ny-1),u); set(gca,'YDir','normal'); colorbar

% GIVEN EXAMPLE:
% The example given below has f(y,x)=2*exp(x+y)
% in the square grid [0,1]x[0,1] with boundary conditions:
% u(0,y)=exp(y); u(1,y)=exp(1+y); u(x,0)=exp(x); u(x,1)=exp(1+x);
% Its exact solution is u=exp(x+y)

function u=tspei2dugwdbcu5psaftm(nx,x0,x1,ny,y0,y1,nz,z0,z1)
    hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1); hz=(z1-z0)/(nz-1);
    rhx2=1/hx/hx; rhy2=1/hy/hy; rhz2=1/hz/hz;
    u=bcs(nx,x0,x1,ny,y0,y1,nz,z0,z1);
    f=fxy(nx,x0,x1,ny,y0,y1,nz,z0,z1);
    for j=2:ny-1
        f(j,2)=f(j,2)-u(j,1)*rhx2;
        f(j,nx-1)=f(j,nx-1)-u(j,nx)*rhx2;
    end
    for i=2:nx-1
        f(2,i)=f(2,i)-u(1,i)*rhy2;
        f(ny-1,i)=f(ny-1,i)-u(ny,i)*rhy2;
    end
    f=imag(fft([zeros(1,ny-2);f(2:ny-1,2:nx-1)';zeros(nx-1,ny-2)]));
    f=imag(fft([zeros(1,nx-2);f(2:nx-1,:)';zeros(ny-1,nx-2)]));
    for j=1:ny-2
        for i=1:nx-2
            f(j+1,i)=f(j+1,i)*0.5/((1-cos(i*pi/(nx-1)))*rhx2+(1-cos(j*pi/(ny-1)))*rhy2);
        end
    end
    f=imag(fft([zeros(1,ny-2);f(2:ny-1,:)';zeros(nx-1,ny-2)]));
    f=imag(fft([zeros(1,nx-2);f(2:nx-1,:)';zeros(ny-1,nx-2)]));
    u(2:ny-1,2:nx-1)=-f(2:ny-1,:)*4/((nx-1)*(ny-1));

% Right Hand Side Function in Poisson's Equation
% Includes values at boundaries
function f=fxy(nx,x0,x1,ny,y0,y1)
    hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1);
    f=zeros(ny,nx);
    for j=1:ny
        y=y0+(j-1)*hy;
        for i=1:nx
            x=x0+(i-1)*hx;
            f(j,i)=2*exp(x+y);
        end
    end

% Dirichlet Boudary Conditions
% Initializes unknown u with user-input boundaries
function u=bcs(nx,x0,x1,ny,y0,y1)
    u=zeros(ny,nx);
    hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1);
    for j=2:ny-1
        y=y0+(j-1)*hy;
        u(j,1)=exp(y);       % Left Boundary
        u(j,nx)=exp(1+y);    % Right Boundary
    end
    for i=1:nx
        x=x0+(i-1)*hx;
        u(1,i)=exp(x);       % Down Boundary
        u(ny,i)=exp(1+x);    % Up Boundary
    end

