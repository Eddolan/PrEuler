__author__ = 'eddie'

def fibo(n):
    sum = 0
    a, b= 0 , 1
    c = a + b
    while c < n:
        if c % 2 == 0:
            sum = sum + c
        a, b = b , c
        c = a + b

    return sum

print fibo(4000000)

