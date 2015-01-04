__author__ = 'eddolan'

def main():
    for b in range(10,100):
        for a in range(10,b):
            test_nums( a , b)

def test_nums( a , b):
    ans = float(a) / b
    sa = str(a)
    sb = str(b)
    for letter in sa:
        if letter != "0":
            if letter in sb:
                if sa[0] == sa[1]:
                    a1 = int(sa[1])
                else:
                    a1 = int(sa.replace(letter , ""))
                if sb[0] == sb[1]:
                    b1 = int(sb[1])
                else:
                    b1 = int(sb.replace(letter , ""))
                if a1 == 0 or b1 == 0:
                    ans1 = 1000
                else:
                    ans1 = float(a1)/b1
                if ans - ans1 < .0001:
                    if ans1 - ans <.0001:
                        print a , "+" ,  b , "=", ans , "----" , a1 , "+" ,  b1 , "=", ans1 , "----"



# main()



import time
t=time.time()

for y in range(1,10):
    for z in range(y,10):
        x=float(9)*y*z/(10*y-z)
        if int(x) == x and y/z < 1 and x<10:
            print x, y, z, str(10*y+x)+'/'+str(z+10*x), str(y)+'/'+str(z)
print time.time()-t