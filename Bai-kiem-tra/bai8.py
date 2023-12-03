n = int(input('Input a positive number:'))

if n == 1:
    print('First 1 Fibonacci number(s): 1')
elif n == 2:
    print('First 2 Fibonacci number(s): 1 1')
else:
    print('First {n} Fibonacci number(s): 1 1',end = ' ')
    f1 = 1
    f2 = 1
    fn = 0
    for i in range(3,n+1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
        print(fn,end = ' ')