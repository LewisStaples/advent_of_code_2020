# adventOfCode 2020 day 13
# https://adventofcode.com/2020/day/13

import copy

bus_pair = []

input_filename='input_sample1.txt'
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

# Get the start time and period for the earliest bus
# Treat those as the earliest bus that needs all requirements of all buses seen up until now
# (That is labelled as "combined")
start_time_combined, period_combined = bus_pair.pop(0)
print(f'{start_time_combined} , {period_combined}')

while len(bus_pair) > 0:
    # Get the start time and period for the next bus
    start_time_new, period_new = bus_pair.pop(0)
    print(f'{start_time_new} , {period_new}')

    # Combine the prior combined with this newest bus
    # Start by trying the next scheduled bus on the combined route
    new_start_time_combined = start_time_combined + period_combined
    while (new_start_time_combined + start_time_new) % period_new != 0:
        # Now try the bus on the combined route that is scheduled after the prior one
        new_start_time_combined += period_combined

    # The above while loop ends only when the above is complete
    start_time_combined = new_start_time_combined
    period_combined *= period_new

# soln_B = None
print(f'\nThe solution to Part B is {start_time_combined}\n')
