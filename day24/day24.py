# adventOfCode 2020 day 24 part A
# https://adventofcode.com/2020/day/24

import copy
from itertools import count

# This program has defined a coordinate system to identify all tiles.
# The below notes define how the input characters are represented in the coordinates.
#   e alone will be treated as +2 in the horizontal
#   e after n or s will be treated as +1 in the horizontal
#   w alone will be treated as -2 in the horizontal
#   w after n or s will be treated as -1 in the horizontal
#   n before e or w will be treated as +1 in the vertical
#   s before e or w will be treated as -1 in the vertical

# The key is the pair of coordinates of a unique tile
#     Note that it is stored as a tuple when used as the key in the dict
#     (In tile_coords it is stored as a list)
# The value is the count of many input lines give directions to that tile
#     (Tiles without any input lines pointing to them do not appear in this data structure)
tile_coords_and_count = dict()

# This defines the compass directions used in the coordinates.
# (Note that these coordinates are not cartesian coordinates)
compass_directions = {'e':[1,0], 'w':[-1,0], 'n':[0,1], 's':[0,-1]}

# This function returns True if this black tile should remain black
def dont_flip_black(black_tile, black_tile_set__old):
    adj_matrix = [[0,-2],[0,2],[1,1],[1,-1],[-1,1],[-1,-1]]
    count_black = 0

    for adj in adj_matrix:
        adjacent_tile = []
        for dim in range(len(black_tile)):
            dummy = 123
            adjacent_tile.append(black_tile[dim] + adj[dim])
        if tuple(adjacent_tile) in black_tile_set__old:
            count_black += 1
    
    return count_black == 1

def get_adjacent_white_tiles(black_tile, black_tile_set__old):
    adj_matrix = [[0,-2],[0,2],[1,1],[1,-1],[-1,1],[-1,-1]]
    adj_white_tiles = []

    for adj in adj_matrix:
        adjacent_tile = []
        for dim in range(len(black_tile)):
            dummy = 123
            adjacent_tile.append(black_tile[dim] + adj[dim])
        if tuple(adjacent_tile) not in black_tile_set__old:
            adj_white_tiles.append(tuple(adjacent_tile))
    return adj_white_tiles

# Reading input from the input file
input_filename='input_sample2.txt'
print(f'Using input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # Convert input line to list of characters, so pop command may be used
        in_string_list = list(in_string)
        # Initialize the tile coordinates to the origin for this tile
        tile_coords = [0,0]
        # While there are characters that haven't been analyzed
        while len(in_string_list) > 0:
            # Get next direction (e, se, sw, w, nw, or ne)
            steps = []
            steps.append(in_string_list.pop(0))
            if steps[0] in ['n', 's']:
                steps.append(in_string_list.pop(0))
            # Update tile coordinates with coordinates for the direction
            for component in steps:
                for index in range(len(tile_coords)):
                    tile_coords[index] += compass_directions[component][index] * 2 / len(steps)
        # Update tile_coords_and_count
        tile_coords_tuple = tuple(tile_coords)
        if tile_coords_tuple in tile_coords_and_count:
            tile_coords_and_count[tile_coords_tuple] += 1
        else:
            tile_coords_and_count[tile_coords_tuple] = 1

# Count all tiles with an odd number of counts.
# Display count as the answer to part A.
count_partA = 0
black_tile_set__old = set()
for key, value in tile_coords_and_count.items():
    if value % 2:
        count_partA += 1
        black_tile_set__old.add(key)
print(f'The answer to part A is: {count_partA}\n')

# Starting on part B
for day_step in range(1, 6):
    print(f'Day {day_step}', end=': ')
    black_tile_set__new = set()
    white_tile_count_black_adjacent = dict()

    # Traverse all black tiles in the old set
    for black_tile in black_tile_set__old:
        if dont_flip_black(black_tile, black_tile_set__old):
            black_tile_set__new.add(black_tile)
        for white_tile in get_adjacent_white_tiles(black_tile, black_tile_set__old):
            if white_tile in white_tile_count_black_adjacent:
                white_tile_count_black_adjacent[white_tile] += 1
            else:
                white_tile_count_black_adjacent[white_tile] = 1

    # Traverse white_tile_count_black_adjacent
    for white_tile, tile_count in white_tile_count_black_adjacent.items():
        if tile_count == 2:
            black_tile_set__new.add(white_tile)
    print(len(black_tile_set__new))

    black_tile_set__old = copy.deepcopy(black_tile_set__new)
