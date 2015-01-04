__author__ = 'eddie'


def euler1(num_max):
    temp_list =[]
    for x in range(100):
        if x%5==0:
            temp_list.append(x)
        elif x%3==0:
            temp_list.append(x)
    y = sum(temp_list)
    return y

print euler1(100)


print sum([x for x in range(100) if x%3==0 or x%5==0])
