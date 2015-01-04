__author__ = 'eddolan'

import math

def isPrime(input , primelist):
    for x in primelist:
        if input % x==0:
            return False
    return True

def primes(input):
    ## Returns a list of primes up to input
    if input==1 or input==2:
        return [2,3]
    else:
        primelist = primes(int(input**.5)+1)
        for x in range(primelist[-1]+2,input,2):
            primelist.append(x)
            for y in primelist[:-1]:
                if x%y==0:
                    primelist.remove(x)
                    break

        return primelist

def perm(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    if num1[0] in num2:
        if num1[1] in num2:
            if num1[2] in num2:
                if num1[3] in num2:
                    return True
    return False

prime_numbers = primes(10000)
while prime_numbers[0]<1000:
    prime_numbers.remove(prime_numbers[0])

print len(prime_numbers)
diffs = []
for x in range(0,9000):
    diffs.append(0)

for prime1 in prime_numbers:
    for prime2 in prime_numbers:
        if prime2==prime1:
            break
        lower = min(prime1 , prime2)
        upper = max(prime1 , prime2)
        diff = upper - lower
        if perm(upper, lower):
            if ((diff+upper) in prime_numbers):
                if perm(diff+upper , upper):
                    print lower, upper , upper + diff