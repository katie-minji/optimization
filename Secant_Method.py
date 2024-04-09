
import numpy as np

g = np.poly1d([1, -12.2, 7.45, 42])
g1 = g.deriv()
g2 = g1.deriv()

err = 10**-6


print('\nSecant Method')

x = {'x-1': 13, 'x0': 12}

# function for x(k+1) using x(k-1), x(k)
def x_kplus1(xkneg1, xk):
    return (g(xk)*xkneg1 - g(xkneg1)*xk) / (g(xk) - g(xkneg1))



i = 0

while True:
    
    maxi = len(x)-2

    if abs(x[f'x{maxi}'] - x[f'x{maxi-1}']) < err:
        break
    
    x[f'x{i+1}'] = x_kplus1(x[f'x{maxi-1}'], x[f'x{maxi}']) 
    
    i += 1


print('x:',x[f'x{maxi-1}'])
