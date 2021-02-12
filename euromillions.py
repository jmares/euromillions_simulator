import random
from time import localtime, strftime
import datetime

print('\n******************************')
print('**  Euromillions Simulator  **')
print('******************************\n')

print(strftime("%H:%M:%S", localtime()) + '\tStart')

begin_time = datetime.datetime.now()
numbers = list()
stars = list()
draws = dict()
amount = 0
simulations = 1_000_000
display_results = 25
display_status_draws = 100_000

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
    if amount % display_status_draws == 0 : print('{:10d}'.format(amount))

draws_list = list()

print(strftime("%H:%M:%S", localtime()) + '\tTransfer draws from dictionary to list of tuples.')

for key, val in draws.items():
    draws_list.append((val, key))

draws.clear()
del draws

print(strftime("%H:%M:%S", localtime()) + '\tSorting ...\n')

draws_list.sort(reverse=True)

print(strftime("%H:%M:%S", localtime()) + f"\tDisplay top {display_results} results:\n")
for draw in draws_list[:display_results]:
    print(draw[0], ':', draw[1])

print(strftime("%H:%M:%S", localtime()) + '\tEnd')
end_time = datetime.datetime.now()
print("Execution time (h:m:s):", str(end_time - begin_time).split('.')[0])
