% Last updated: 04-Jun-2016
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Function to find a root of a one
% dimensional function using Bisection Method

% ALL YOU NEED TO DO:
% Call function bsctn() with:
%   f = function whose root is to be found
%   a,b = range in which root is to be found (inclusive)
%   er = tolerance below which root will be accepted,
%        i.e., when |f(c)|<er, c is accepted as root
% Define f(x), external function whose root is to be found
% Function bsctn() has two outputs c and istt respectively, where
%   c = found root, if successful
%   istt = status code of function's execution (see below for details)

% STATUS CODE:
% istt=1, success: root found between a and b
% istt=2, success: root found at a
% istt=3, success: root found at b
% istt=-1, error: root could not be found between a and b

% EXAMPLE:
% Define a function like:
%   g=@(x) x*x-1;
% Then call bsctn() as:
%   [r,ist] = bsctn(g,-2,20,5.e-16)
% If ist is positive, r will be the root of g(x).

% NOTE:
% If f(x) does not cross the x-axis but only touches it,
%   like f(x)=x*x at x=0, then that root will most probably not be found
% Below method does not check for opposite signs to continue operating
%   as conventional bisection method does, but it is then likely to find
%   a root if it exists, even if signs at boundaries are same
% Method is optimized for minimum calls to f(x)

function [c, istt] = bsctn(f, a, b, er)
    fa = f(a);
    fb = f(b);
    if abs(fa) < er
        istt = 2;
        c = a;
        return
    end
    if abs(fb) < er
        istt = 3;
        c = b;
        return
    end
    ep = 2.0 * eps();
    ifa = false;
    ifb = false;
    c = 0.5 * (a + b);
    if abs(c - 1) < ep
        c0 = 2.0;
    else
        c0 = 1.0;
    end
    while true
        fc = f(c);
        if abs(fc) < er
            istt = 1;
            return
        elseif c0 == 0.0 && c == 0.0
            istt = -1;
            return
        elseif c0 != 0.0 && abs(1.0 - c / c0) < ep
            istt = -1;
            return
        else
            if ifa
                fa = f(a);
            elseif ifb
                fb = f(b);
            end
            if fa * fc < 0
                b = c;
                ifa = false;
                ifb = true;
            elseif fb * fc < 0
                a = c;
                ifa = true;
                ifb = false;
            elseif abs(fa) < abs(fb)
                b = c;
                ifa = false;
                ifb = true;
            else
                a = c;
                ifa = true;
                ifb = false;
            end
        end
        c0 = c;
        c = 0.5 * (a + b);
    end
end
