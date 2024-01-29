

import numpy as np
print('\n------------------------------------')
print('<Question 1>')

def f(x):
    return x**4-14*x**3+60*x**2-70*x


#%%


# Golden Section Search

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


# for i in range(1,n+1):
    
#     if i == 1:
#         # take ai/bi through f
#         for letr in ['a','b']:
#             if letr == 'a':
#                 d[f'{letr}{i}'] = d[f'a{i-1}'] + ro*my_range
#             elif letr == 'b':
#                 d[f'{letr}{i}'] = d[f'a{i-1}'] + (1-ro)*my_range
#             # d[f'f({letr}{i})'] = f(d[f'{letr}{i}'])
    
#     # put value into functions, save output in d
#     for letr in ['a','b']:
#         d[f'f({letr}{i})'] = f(d[f'{letr}{i}'])
        
#     # look for smaller value and set range and next
#     if d[f'f(a{i})'] < d[f'f(b{i})']:
#         my_range = d[f'b{i}'] - d[f'a{i-1}']
#         d[f'b{i+1}'] = d[f'a{i}']
#         d[f'a{i+1}'] = d[f'a{i-1}'] + ro*my_range
#         if i == n:
#             print('x:',d[f'a{n}'])
        
#     else: #d[f'f(a{i})'] >= d[f'f(b{i})']:
#         my_range = d[f'b{i-1}'] - d[f'a{i}']
#         d[f'a{i+1}'] = d[f'b{i}']
#         d[f'b{i+1}'] = d[f'a{i}'] + (1-ro)*my_range
#         if i == n:
#             print('x:',d[f'b{n}'])




#%%


# fibonacci search

print('\nFibonacci Search Method')

# find N value
epsilon = 0.1
choose_n = ((1 + 2*epsilon) / 10**-6 * 2)
fib = {'F-1': 0, 'F0': 1}

while True:
    maxi = len(fib) - 2
    if choose_n <= fib[f'F{maxi}']:
        n = maxi - 1 
        break
    # create list of fibonacci numbers, until within error range
    fib[f'F{maxi+1}'] = fib[f'F{maxi}'] + fib[f'F{maxi-1}'] 
        

# make list of changing ro values
ro = {}
for k in range(1,n+2):
    ro[f'p{k}'] = 1 - (fib[f'F{n-k+1}'] / fib[f'F{n-k+2}']) 


# initial condition
d = {'a0':0, 'b0':2}
my_range = d['b0'] - d['a0']

for i in range(1,n+1):
    
    if i == 1:
        # take ai/bi through f
        for letr in ['a','b']:
            if letr == 'a':
                d[f'{letr}{i}'] = d[f'a{i-1}'] + ro[f'p{i}']*my_range
            elif letr == 'b':
                d[f'{letr}{i}'] = d[f'a{i-1}'] + (1-ro[f'p{i}'])*my_range
            # d[f'f({letr}{i})'] = f(d[f'{letr}{i}'])


    # put value into functions, save output in d
    for letr in ['a','b']:
        d[f'f({letr}{i})'] = f(d[f'{letr}{i}'])
        
    # look for smaller value and set range and next
    if d[f'f(a{i})'] < d[f'f(b{i})']:
        my_range = d[f'b{i}'] - d[f'a{i}']
        d[f'a{i+1}'] = d[f'a{i}']
        d[f'b{i+1}'] = d[f'a{i}'] + (1-ro[f'p{i+1}'])*my_range
        if i == n:
            print('x:',d[f'a{n}'])
        
    elif d[f'f(a{i})'] >= d[f'f(b{i})']:
        my_range = d[f'b{i}'] - d[f'a{i}']
        d[f'b{i+1}'] = d[f'b{i}']
        d[f'a{i+1}'] = d[f'a{i}'] + ro[f'p{i+1}']*my_range
        if i == n:
            print('x:',d[f'b{n}'])
            
    
    
#%%

print('\n------------------------------------')
print('<Question 2>')


# functions, original, first, second derivatives
g = np.poly1d([1, -12.2, 7.45, 42])
g1 = g.deriv()
g2 = g1.deriv()

err = 10**-6


#%%


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
# print(g1(x[f'x{maxi-1}']))



#%%


# Secant method

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
# print(g1(x[f'x{maxi-1}']))


#%% 

print('\n------------------------------------')

