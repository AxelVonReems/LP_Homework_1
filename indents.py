import random

x = random.randint(0, 10)


def more_or_less(num):
    if x >= 5:
        print('More')
    else:
        print('Less')


more_or_less(x)

while x < 10:
    print(x)
    x = x + 1
