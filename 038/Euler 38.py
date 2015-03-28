__author__ = 'eddolan'





def conc( num , conc_num , a):
    snum = str(num)
    if len(snum)>9:
        return False
    if snum.count("0") > 0:
        return False
    for letter in snum:
        if snum.count(letter) > 1:
            return False
    if len(snum)==9:
        return True
    snum += str( conc_num * a )
    conc_num += 1
    return conc( snum , conc_num , a)


for x in range(100000):
    if conc( x , 2 , x ):
        print x

print 9327*2
