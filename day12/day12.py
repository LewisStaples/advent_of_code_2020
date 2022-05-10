# adventOfCode 2020 day 12
# https://adventofcode.com/2020/day/12

import sys

ship_status = {
    'x': 0,
    'y': 0,
    'dir': 90
}
# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        action = in_string[0]
        value = int(in_string[1:])
        if action == 'N':
            ship_status['y'] = ship_status['y'] + value
        if action == 'S':
            ship_status['y'] = ship_status['y'] - value
        if action == 'E':
            ship_status['x'] = ship_status['x'] + value
        if action == 'W':
            ship_status['x'] = ship_status['x'] - value
        if action == 'L':
            ship_status['dir'] = ship_status['dir'] - value
        if action == 'R':
            ship_status['dir'] = ship_status['dir'] + value
        if action == 'F':
            if ship_status['dir'] == 0:
                ship_status['y'] = ship_status['y'] + value
            if ship_status['dir'] == 90:
                ship_status['x'] = ship_status['x'] + value
            if ship_status['dir'] == 180:
                ship_status['y'] = ship_status['y'] - value
            if ship_status['dir'] == 270:
                ship_status['x'] = ship_status['x'] - value

manhattan_distance = abs(ship_status['x']) + abs(ship_status['y'])
print(f'The Manh. Dist. (answer to Part A is {manhattan_distance}')

