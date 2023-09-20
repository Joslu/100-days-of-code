# The fibonacci sequences is defined as follows: the first number
# of the sequence is 0, the second number is 1 and the nth
# number is the sum of the (n-1) and (n-2). Write a fucntion tat takes an integer n
# and returns the nth fibonacci number

# 0,1,1,2,3,5,8,13


def getNthFib(n):
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


def getNthFib2(n, calculated={1: 0, 2: 1, 3: 1}):
    if n in calculated:
        return calculated[n]

    calculated[n] = getNthFib2(n - 1, calculated) + getNthFib2(n - 2, calculated)

    return calculated[n]


## Print fibonacci series
items = []

for item in range(10):
    items.append(getNthFib2(item + 1))

print(items)
