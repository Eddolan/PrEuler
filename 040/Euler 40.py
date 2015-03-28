__author__ = 'eddolan'


def champ(num):
    sum = 0
    count = 0
    while sum < num:
        count += 1
        sum += len(str(count))
    diff = len(str(count)) - (sum - num) - 1
    return int(str(count)[diff])


list = [1,10,100,1000,10000,100000,1000000]

ans = 1
for count in list:
    ans = ans * champ(count)

print ans