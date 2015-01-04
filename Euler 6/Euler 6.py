__author__ = 'DT'

def euler6():
    sum_of_squares = sum([x**2 for x in range(101)])
    square_of_sum = sum([y for y in range(101)])**2
    return (square_of_sum - sum_of_squares)

print euler6()

print ((sum([y for y in range(101)])**2) - (sum([x**2 for x in range(101)])))
