__author__ = 'eddolan'


triangles = []


def get_cubes(num):
    sum = 0
    a , b = 0 , 0
    m = 2
    while (a <= num and b <= 2 * num) or (a <= 2 * num and b <= num):
        for n in range(1,m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            for count in range(1, (min(a,b,num)+1)/2):
                sum += 1
                triangles.append([ count, min(a,b) - count , max(a,b) , "     " , a , b])
            for count in range(1, min((max(a,b)+1)/2,min(a,b))+1):
                sum += 1
            triangles.append([ count, max(a,b) - count , min(a,b) , "     " , a , b])
        m += 1
    return sum

print get_cubes(6)
print triangles