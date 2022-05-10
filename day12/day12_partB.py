# adventOfCode 2020 day 12
# https://adventofcode.com/2020/day/12

import sys
import copy

# This is the ship's absolute location
ship_location = {
    'x': 0,
    'y': 0,
}

# This is the waypoint location, relative to the ship
waypoint_offset = {
    'x': 10,
    'y': 1,
}

# Flip waypoint by 180 degrees
def waypoint_flip():
    waypoint_offset['x'] = waypoint_offset['x'] * -1
    waypoint_offset['y'] = waypoint_offset['y'] * -1

# Rotate waypoint by 90 degrees counterclockwise
def waypoint_rotate_ccw():
    old_waypoint_offset = copy.deepcopy(waypoint_offset)
    waypoint_offset['x'] = old_waypoint_offset['y'] * -1
    waypoint_offset['y'] = old_waypoint_offset['x']

# Rotate waypoint by 90 degrees clockwise
def waypoint_rotate_cw():
    old_waypoint_offset = copy.deepcopy(waypoint_offset)
    waypoint_offset['x'] = old_waypoint_offset['y']
    waypoint_offset['y'] = old_waypoint_offset['x'] * -1

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
            waypoint_offset['y'] = waypoint_offset['y'] + value
        if action == 'S':
            waypoint_offset['y'] = waypoint_offset['y'] - value
        if action == 'E':
            waypoint_offset['x'] = waypoint_offset['x'] + value
        if action == 'W':
            waypoint_offset['x'] = waypoint_offset['x'] - value
        if action == 'L':
            if value == 90:
                waypoint_rotate_ccw()
            if value == 180:
                waypoint_flip()
            if value == 270:
                waypoint_rotate_cw()
        if action == 'R':
            if value == 90:
                waypoint_rotate_cw()
            if value == 180:
                waypoint_flip()
            if value == 270:
                waypoint_rotate_ccw()
        if action == 'F':
            ship_location['x'] += value * waypoint_offset['x']
            ship_location['y'] += value * waypoint_offset['y']

manhattan_distance = abs(ship_location['x']) + abs(ship_location['y'])
print(f'The Manh. Dist. (answer to Part B) is {manhattan_distance}')

