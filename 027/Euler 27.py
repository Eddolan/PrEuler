__author__ = 'eddolan'



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




def isPrime(input):
    for x in primelist:
        if input % x==0:
            if input != x:
                return False
    return True

def main():
    max1 = []
    max2 = []
    # consider the number 1
    for a in alist:
        bs = get_Bs(a)
        x , y = get_best_bs( a , bs)
        max1.append(x)
        max2.append(y)




def get_Bs( a ):
    b = []
    n = 0
    while (primelist[n] - a - 1) < 1000:
        b.append (primelist[n] - a - 1)
        n += 1
    return b
def refine_bs( a , bs  , n):
    returnlist =[]
    for b in bs:
        if isPrime( n**2 + b*n + a):
            returnlist.append( b )
    return returnlist
def get_best_bs( a , bs):
    bs1 = refine_bs( a , bs , 2)
    n = 3
    while len(bs)>0:
        bs1 = bs
        bs = refine_bs( a , bs , n)
        n += 1
    if len(bs) == 0:
        bs = bs1
    return bs , n

primelist = primes( 2200 )
alist = [ prime for prime in primelist if prime<1000]

main()