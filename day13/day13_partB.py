# adventOfCode 2020 day 13
# https://adventofcode.com/2020/day/13

import copy

bus_pair = []

input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    f.readline().rstrip()
    in_string2 = f.readline().rstrip()
    print(f'line2: {in_string2}\n')
    string_list = in_string2.split(',')

    for time_dep_init, busID in enumerate(string_list):
        if busID != 'x':
            bus_pair.append((time_dep_init, int(busID)))
    # get rid of variables that won't be needed anymore
    del in_string2, string_list, f, input_filename, busID

# sort bus_pair by element 1 in tuple (therefore period_new < period_combination)
bus_pair.sort(key=lambda tup: tup[1])

start_time_combination, period_combination = bus_pair.pop()
print(f'{start_time_combination} , {period_combination}')

while len(bus_pair) > 0:
    start_time_new, period_new = bus_pair.pop()
    print(f'{start_time_new} , {period_new}')
    combination_list = [start_time_combination]
    new_entry_list = [start_time_new]

    while True:
        if len(combination_list) > 2 and len(new_entry_list) > 2:
            break
        if combination_list[-1] < new_entry_list[-1]:
            combination_list.append(combination_list[-1] + period_combination)
        elif combination_list[-1] > new_entry_list[-1]:
            new_entry_list.append(new_entry_list[-1] + period_new)
        else:
            break

    # combine combination and new_entry in new values of start_time_combination, period_combination
    # start_time_combination = copy.deepcopy(combination_list[-1])
    combo0 = combination_list.pop(0)
    if new_entry_list[0] > combo0:
        combo0 = combination_list.pop(0)
    combo1 = combination_list.pop(0)

    # find how many slots is the new_entry_list entry before combo0
    # find how many slots is the new_entry_list entry before combo1
    # use both slot counts above to calculate the new value of start_time_combination

    period_combination = period_new * period_combination

    # delete lists, as they won't be needed again
    del combination_list, new_entry_list

soln_B = period_combination - start_time_combination
print(f'\nThe solution to Part B is {soln_B}\n')
