__author__ = 'eddolan'

import time
from math import *

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
        print primelist
        print primelist[:-1]
        for x in range(primelist[-1]+2,input,2):
            primelist.append(x)
            for y in primelist[:-1]:
                if x%y==0:
                    primelist.remove(x)
                    break
        return primelist
def eddie( number ):
    primelist = primes( number )
    return primelist
def eratosthenes( number ):
    prime_list = range(2 , number  + 1)
    x = prime_list[0]
    y = x
    while y < number ** .5:
        while y < number:
            y += x
            try:
                prime_list.remove( y )
            except:
                pass
    return  prime_list

def FourxOney( n ):
    for x in xrange(1,int(sqrt(n))):
        if isinstance((sqrt((n-sqrt(x))/4)),int):
            print 1
            return True
    return False

def atkin_generator( number ):
    num = 1
    while num <= number:
        maybel = num % 60
        if maybel in [ 1,13,17,29,37,41,49,53]:
            FourxOney(num)
        yield maybel
        num += 1

def atkin( number ):
    inf = 0
    maybel = atkin_generator( number )
    primelist = [2,3,5]

    while inf == 0:
        try:
            kitty  = maybel.next()
        except StopIteration:
            return primelist

def test( number ):
    start_time = time.time()
    eddie( number )
    print time.time() - start_time , "    ",
    start_time = time.time()
    eratosthenes( number )
    print time.time() - start_time


#list = [10,100,1000,10000,100000,200000,1000000]
#for num in list:
#    print num ,
#    test( num )

atkin( 10000 )