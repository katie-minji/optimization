
import numpy as np

g = np.poly1d([1, -12.2, 7.45, 42])
g1 = g.deriv()
g2 = g1.deriv()

err = 10**-6


# Newtons method

print('\nNewtons Method')

x = {'x0': 12}


i = 0

while True:
    
    maxi = len(x)-1
    
    if maxi != 0:
        if abs(x[f'x{maxi}'] - x[f'x{maxi-1}']) < err:
            break
    
    x[f'x{i+1}'] = x[f'x{i}'] - (g(x[f'x{i}'])/g1(x[f'x{i}'])) 
    
    i += 1

print('x:',x[f'x{maxi-1}'])

