# adventOfCode 2020 day 13
# https://adventofcode.com/2020/day/13

earliest_timestamp = None
bus_IDs = None

input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string1 = f.readline().rstrip()
    earliest_timestamp = int(in_string1)
    in_string2 = f.readline().rstrip()
    string_list = in_string2.split(',')
    bus_IDs = [int(n) for n in string_list if n != 'x']

    # get rid of variables that won't be needed anymore
    del in_string1, in_string2, string_list, f, input_filename

earliest_known_bus = {
    'bus_ID': -1,
    'earliest_departure': float('inf')
}
for this_bus_ID in bus_IDs:
    earliest_departure_for_this_bus = this_bus_ID - earliest_timestamp % this_bus_ID
    if earliest_departure_for_this_bus < earliest_known_bus['earliest_departure']:
        earliest_known_bus['bus_ID'] = this_bus_ID
        earliest_known_bus['earliest_departure'] = earliest_departure_for_this_bus

soln_A = earliest_known_bus['bus_ID'] * earliest_known_bus['earliest_departure']
print(f'The solution to Part A is {soln_A}\n')
