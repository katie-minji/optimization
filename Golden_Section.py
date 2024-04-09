
import numpy as np

def f(x):
    return x**4-14*x**3+60*x**2-70*x


print('\nGolden Section Search')

# save fixed ro value
ro = (3-np.sqrt(5))/2

# choose N
control = (10**(-6)) / 2
n = 0
while True:
    if (1-ro)**n <= control:
        break
    n+=1
        

# initial condition
d = {'a0':0, 'b0':2}
my_range = d['b0'] - d['a0']

for i in range(1,n+1):
    
    if i == 1:
        # take ai/bi through f
        for letr in ['a','b']:
            if letr == 'a':
                d[f'{letr}{i}'] = d[f'a{i-1}'] + ro*my_range
            elif letr == 'b':
                d[f'{letr}{i}'] = d[f'a{i-1}'] + (1-ro)*my_range
            # d[f'f({letr}{i})'] = f(d[f'{letr}{i}'])
    
    # put value into functions, save output in d
    for letr in ['a','b']:
        d[f'f({letr}{i})'] = f(d[f'{letr}{i}'])
        
    # look for smaller value and set range and next
    if d[f'f(a{i})'] < d[f'f(b{i})']:
        my_range = d[f'b{i}'] - d[f'a{i}']
        d[f'a{i+1}'] = d[f'a{i}']
        d[f'b{i+1}'] = d[f'a{i}'] + (1-ro)*my_range
        if i == n:
            print('x:',d[f'a{n}'])
        
    else: #d[f'f(a{i})'] >= d[f'f(b{i})']:
        my_range = d[f'b{i}'] - d[f'a{i}']
        d[f'b{i+1}'] = d[f'b{i}']
        d[f'a{i+1}'] = d[f'a{i}'] + ro*my_range
        if i == n:
            print('x:',d[f'b{n}'])





