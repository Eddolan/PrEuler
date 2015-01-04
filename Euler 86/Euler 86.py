__author__ = 'eddolan'


def get_cubes(m):
    sum = 0
    sum1 = 1
    for x in range(1,m+1):
        for y in range(1,x+1):
            for z in range(1,y+1):
                sum1+=1
                a = max(x,y,z)
                b = x+y+z-a
                if (a**2+b**2)**.5==int((a**2+b**2)**.5):
                    sum+=1
    return sum


print get_cubes(10)
