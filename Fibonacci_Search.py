
def f(x):
    return x**4-14*x**3+60*x**2-70*x

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
            
            