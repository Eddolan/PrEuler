__author__ = 'Eddie'


mabel = 0

doubles = [ x*2 for x in range(1,21)]
doubles.append(50)
print doubles

scores = [25,50]
for x in range(1,21):
    scores.append(x)
    scores.append(x*2)
    scores.append(x*3)


scores.sort()

for num in doubles:
    if num < 100:
        mabel = mabel + 1
    for num1 in scores:
        score = num + num1
        if score < 100:
            mabel = mabel + 1
            if num + num1 + num1 < 100:
                mabel = mabel +.5
            for num2 in scores:
                score = num + num1 + num2
                if score < 100:
                    mabel = mabel + .5




print mabel