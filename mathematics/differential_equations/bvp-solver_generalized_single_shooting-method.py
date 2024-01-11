# Last Updated: 10-Jun-2019
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Generalied Shooting Method to solve coupled ODEs with boundary values

# ALL YOU NEED TO DO:
# Call gbvpsolver() with appropriate inputs
# Check function for details on inputs
# Check examples at the bottom

# Similar to D02AGF from NAG Library
# Tested with Python 3.6.4, Numpy 1.16.3, Scipy 1.2.1, Matplotlib 3.1.0

import numpy as np
import scipy.integrate
import scipy.optimize

def odesolver(fy, t, y0, method = 'RK45'):
    ''' (function, array, array, [str]) --> array, array

        Solves Initial Value Problem (IVP): y'(t) == f(t,y)
        with initial values of y at t[0]
        using various methods described below

        fy = function describing RHS of set of equations y'(t) == f(t,y) (function, input)
        t = array on which output of solution is desired (array, input)
        y0 = values of y at first point of t (array, input)
        method = string mentioning method to be used by solver (str, optional input)
        y = final output (array, output)

        Acceptable methods: 'RK45', 'RK23', 'Radau', 'BDF', 'LSODA' for solve_ivp
                            'vode', 'zvode', 'lsoda', 'dopri5', 'dop853' for ode
                            'RK4fs' for fixed-step RK4 on input array t

        Use 'RK45' or 'RK23' method for non-stiff problems and 'Radau' or 'BDF' for stiff problems
        'LSODA' will be same method as used in odeint and can be a good universal choice
        For more details on methods, check:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html
    '''
    # using scipy.integrate.solve_ivp
    if method in ('RK45', 'RK23', 'Radau', 'BDF', 'LSODA'):
        slv = scipy.integrate.solve_ivp(fy, np.array([t[0], t[-1]]), y0, t_eval = t, method = method)
        if not slv.success:
            print(slv.message)
        return t, slv.y
    # using scipy.integrate.ode
    elif method in ('vode', 'zvode', 'lsoda', 'dopri5', 'dop853'):
        t0 = t[0]
        t1 = t[-1]
        dt = t[1] - t[0]
        nt = len(t)
        s = scipy.integrate.ode(fy).set_integrator(method)
        s.set_initial_value(y0, t0)
        r = np.empty((nt, len(y0)))
        r[0,:] = y0
        k = 1
        while s.successful() and k < nt:
            r[k] = s.integrate(s.t+dt)
            k += 1
        return t, np.transpose(r)
    # using fixed-step RK4
    elif method == 'RK4fs':
        ny = len(y0)
        nt = len(t)
        y = np.zeros((ny, nt))
        y[:, 0] = y0
        for i in range(1, nt):
            h = t[i] - t[i-1]
            f = fy(t[i-1], y[:, i-1])
            k1 = h * f
            f = fy(t[i-1] + 0.5 * h, y[:, i-1] + 0.5 * k1)
            k2 = h * f
            f = fy(t[i-1] + 0.5 * h, y[:, i-1] + 0.5 * k2)
            k3 = h * f
            f = fy(t[i-1] + h, y[:, i-1] + k3)
            k4 = h * f
            y[:, i] = y[:, i-1] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0
        return t, y
    else:
        print('ode-solving method', method, 'is not recognized...')
        return None

def rootfinder(fx, x0, method = 'hybr', tol = 1.0e-10, options = {}):
    ''' (function, array, [str, float, dict]) --> array

        fx = function whose root needs to be found, should only
             accept one input (function, input)
        x0 = guess values of the root (array, input)
        method = str mentioning method to be used (str, optional input)
        tol = tolerance upto which root is acceptable (float, optional input)
        options = method specific options (dict, optional input)
        x = found root of equation fx(x)==0 (float, output)

        Acceptable methods: 'hybr', 'lm', 'broyden1', 'broyden2', 'anderson', 'linearmixing', 'diagbroyden', 'excitingmixing', 'krylov', 'df-sane'
        Please check https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html for details

        Also added 'newt0' and 'newt1' for Newton-Raphson method, currently under development
        Variable dxj is used to compute Jacobian
    '''
    if method in ('hybr', 'lm', 'broyden1', 'broyden2', 'anderson', 'linearmixing', 'diagbroyden', 'excitingmixing', 'krylov', 'df-sane'):
        slv = scipy.optimize.root(fx, x0, method = method, tol = tol, options = options)
        if not slv.success:
            print(slv.message)
        return slv.x
    # Newton-Raphson, lower function calls but forward difference formula for derivative
    elif method == 'newt0':
        itrmax = 1000
        dxj = 1.0e-6
        x = np.array(x0, dtype = 'float64')
        f = fx(x)
        n = len(x)
        jc = np.empty((n, n))
        k = 0
        while any(np.abs(f) > tol) and k < itrmax:
            k += 1
            for ix in range(n):
                dx = dxj if x[ix] == 0 else x[ix] * dxj
                xt = np.array(x)
                xt[ix] += dx
                jc[:,ix] = (fx(xt) - f) / dx
            x -= np.linalg.lstsq(jc, f)[0]
            f = fx(x)
        if k >= itrmax:
            print('Warning: Maximum iterations =', itrmax, 'reached...')
        return x
    # Newton-Raphson, central difference formula for derivative but higher function calls
    elif method == 'newt1':
        itrmax = 1000
        dxj = 0.5e-6
        x = np.array(x0, dtype = 'float64')
        n = len(x)
        jc = np.empty((n, n))
        f = fx(x)
        k = 0
        while any(np.abs(f) > tol) and k < itrmax:
            k += 1
            for ix in range(n):
                dx = dxj if x[ix] == 0 else x[ix] * dxj
                xt0 = np.array(x)
                xt1 = np.array(x)
                xt0[ix] -= dx
                xt1[ix] += dx
                jc[:,ix] = (fx(xt1) - fx(xt0)) * 0.5 / dx
            x -= np.linalg.lstsq(jc, f)[0]
            f = fx(x)
        if k >= itrmax:
            print('Warning: Maximum iterations =', itrmax, 'reached...')
        return x
    else:
        print('root-finding method', method, 'is not recognized...')
        return None

def gbvpsolver(ft, fyp, fy0, frt, pg0, ivp_method = 'RK45', rt_method = 'lm', rt_tol = 1.0e-10, rt_options = {}):
    ''' (function, function, function, function, array, [str, str, float, dict]) --> array, array

        ft =  function describing grid t (function, input)
        fyp = function describing RHS of y'(t) == f(t,y,p) (function, input)
        fy0 = function describing initial values of y (i.e., at t[0]) (function, input)
        frt = function whose root needs to be found (function, input)
        pg0 = guess values for parameters (array, input)
        ivp_method = str mentioning method to be used by ODE solver (str, optional input)
        rt_method = str mentioning method to be used by root finder (str, optional input)
        rt_tol = tolerance to be used by root finder (float, optional input)
        rt_options = options specific to methods used by root finder (dict, optional input)
        t = final grid on which solution is obtained (array, output)
        y = final solution of shooting method (array, output)

        Solves boundary value problems (BVP) for coupled ordinary differential equations
        y'(t) == f(t, y, p)
        Finds free parameters p that can appear in ft, fyp and fy0 such that frt = 0

        Description of functions:
        ft(p) should take parameters p as input and should output whole t grid on
            which system needs to be solved
        fyp(t, yt, p) should take a value of t (float), values of y at that t and
            values of parameters p and should output RHS of equations y' = f(t,y,p)
        fy0(t0, p) should take intial value of t as t0 (float) and parameters p
            and should output initial values of y (i.e. their values at t0)
        frt(t, y) should take whole t array and y arrays as input and should output
            the quantity whose root needs to be found, i.e., that quantity needs to
            be 0
    '''
    def fxr(p):
        t = ft(p)
        y0 = fy0(t[0], p)
        t, y = odesolver(lambda t, f: fyp(t, f, p), t, y0, method = ivp_method)
        return frt(t, y)
    rt = rootfinder(fxr, pg0, method = rt_method, tol = rt_tol, options = rt_options)
    t = ft(rt)
    t, y = odesolver(lambda t, f: fyp(t, f, rt), t, fy0(t[0], rt), method = ivp_method)
    return t, y

if __name__ == '__main__':

    def fyp(t, yt, p):
        return np.array([yt[1], (yt[0]**3 - yt[1]) * 0.5 / t])
    def fy0(t0, p):
        return np.array([0.1 + p[0] * np.sqrt(t0) * 0.1 + t0 * 0.01, p[1]])
    def frt(t, y):
        return np.array([y[0,-1] - 1.0/6.0, 0.0])
    def ft(p):
        return np.linspace(0.1, 16.0, 101)
    pg0 = np.array([0.2, 0])

##    # Use ivp_method = 'Radau'
##    def fyp(t, yt, p):
##        return np.array([np.tan(yt[2]), -(p[0] * np.sin(yt[2]) + 0.00002 * yt[1]**2) / (yt[1] * np.cos(yt[2])), -p[0] / yt[1] / yt[1]])
##    def fy0(t0, p):
##        return np.array([0.0, 500.0, 0.5])
##    def frt(t, y):
##        return np.array([y[0,-1], y[1,-1] - 450.0])
##    def ft(p):
##        return np.linspace(0.0, p[1], 10001)
##    pg0 = np.array([32.0, 6000.0])

##    def fyp(t, yt, p):
##        return np.array([yt[1], 1.5 * yt[0]**2])
##    def fy0(t0, p):
##        return np.array([4, p[0]])
##    def frt(t, y):
##        return np.array([y[0, -1] - 1])
##    def ft(p):
##        return np.linspace(0.0, 1.0, 101)
##    pg0 = np.array([-21.0])
    
    t, y = gbvpsolver(ft, fyp, fy0, frt, pg0, rt_method = 'lm', ivp_method = 'RK45')

    import matplotlib.pyplot as plt
    for k in range(len(y)):
        plt.plot(t, y[k, :], label = 'y' + str(k))
    plt.xlabel('t')
    plt.legend()
    plt.show()
