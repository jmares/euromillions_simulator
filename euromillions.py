import random
from time import localtime, strftime
import datetime

print('\n******************************')
print('**  Euromillions Simulator  **')
print('******************************\n')

print(strftime("%H:%M:%S", localtime()) + '\tStart')

begin_time = datetime.datetime.now()
draws = dict()
SIMULATIONS = 1_000_000        # number of simulations
DISPLAY_RESULTS = 25           # display the top x results 
DISPLAY_STATUS_DRAWS = 50_000  # display a status message every x draws

print(strftime("%H:%M:%S", localtime()) + '\tDraws')

#while amount < SIMULATIONS:
for simulation in range(SIMULATIONS):
    numbers = []
    while len(numbers) < 5:
        number = random.randint(1,50)
        if number not in numbers: numbers.append(number)

    stars = []
    while len(stars) < 2:
        star = random.randint(1,12)
        if star not in stars: stars.append(star)

    numbers.sort()
    stars.sort()
    #amount += 1
    #draw = ''.join(str(numbers)) + ''.join(str(stars))
    #draw = str(numbers) + str(stars)
    #draw = ', '.join(numbers) + ' | ' + ', '.join(stars)
    draw = f"{numbers}{stars}"

    draws[draw] = draws.get(draw, 0) + 1
    if simulation % DISPLAY_STATUS_DRAWS == 0 : print('{:10d}'.format(simulation))

print('{:10d}'.format(SIMULATIONS))

draws_list = list()

print(strftime("%H:%M:%S", localtime()) + '\tTransfer draws from dictionary to list of tuples.')

for key, val in draws.items():
    draws_list.append((val, key))

draws.clear()
del draws

print(strftime("%H:%M:%S", localtime()) + '\tSorting ...\n')

draws_list.sort(reverse=True)

print(strftime("%H:%M:%S", localtime()) + f"\tDisplay top {DISPLAY_RESULTS} results:\n")
for draw in draws_list[:DISPLAY_RESULTS]:
    print(draw[0], ':', draw[1])

print(strftime("\n" + "%H:%M:%S", localtime()) + '\tEnd')
end_time = datetime.datetime.now()
print("\nExecution time (h:m:s):", str(end_time - begin_time).split('.')[0])
