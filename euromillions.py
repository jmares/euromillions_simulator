import random
from time import localtime, strftime

print('\nEuromillions\n')
print(strftime("%H:%M:%S", localtime()) + '\tStart')
numbers = list()
stars = list()
draws = dict()
amount = 0
simulations = 10_000_000

print(strftime("%H:%M:%S", localtime()) + '\tDraws')

while amount < simulations:
    numbers = []
    stars = []
    while len(numbers) < 5:
        number = random.randint(1,50)
        if number not in numbers: numbers.append(number)

    while len(stars) < 2:
        star = random.randint(1,12)
        if star not in stars: stars.append(star)
    numbers.sort()
    stars.sort()
    amount += 1
    draw = ''.join(str(numbers)) + ''.join(str(stars))
    draws[draw] = draws.get(draw, 0) + 1
    if amount % 250000 == 0 : print('{:10d}'.format(amount))

draws_list = list()

print(strftime("%H:%M:%S", localtime()) + '\tTransfer draws from dictionary to list of tuples.')

for key, val in draws.items():
    draws_list.append((val, key))

draws.clear()
del draws

print(strftime("%H:%M:%S", localtime()) + '\tSorting ...')

draws_list.sort(reverse=True)

for draw in draws_list[:25]:
    print(draw[0], ':', draw[1])

print(strftime("%H:%M:%S", localtime()) + '\tEnd')

