The programs solve the following coupled ordinary differential equation:

y'(1)=f(x,y(1),y(2))(1)
y'(2)=f(x,y(1),y(2))(2)

Different types of boundary conditions are:

Type-1: y(1)=y11 at x=x1 and y(1)=y12 at x=x2
Type-2: y(2)=y21 at x=x1 and y(1)=y12 at x=x2
Type-3: y(1)=y11 at x=x1 and y(2)=y22 at x=x2
Type-4: y(2)=y21 at x=x1 and y(2)=y22 at x=x2

Or if you are solving a 2nd order ODE by breaking it into 2 coupled ODEs, i.e.,
solving y1''(x)=g(y1(x),y1'(x),x) by breaking it into
y'(1)=y(2)
y'(2)=g(y(1),y(2),x)
Then the types mean the following (function means y1(x)):

Type-1: Function values are known at both boundaries x1 and x2
Type-2: Function's derivative is known at x1 and Function value is known at x2
Type-3: Function value is known at x1 and Function's derivative is known at x2
Type-4: Function's derivatives are known at both boundaries x1 and x2
