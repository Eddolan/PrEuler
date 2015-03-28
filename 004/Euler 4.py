__author__ = 'eddie'

def math1():
    list1 = []
    for x in range(999,100,-1):
        for y in range(999,100,-1):
            if str(x*y)[0:3]==str(x*y)[-1:2:-1]:
                list1.append(x*y)
    return max(list1)
print math1()

print max([x*y for x in range(999,100,-1) for y in range(999,100,-1) if str(x*y)[0:3]==str(x*y)[-1:2:-1]])