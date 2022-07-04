# adventOfCode 2020 day 24 part A
# https://adventofcode.com/2020/day/24


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
for value in tile_coords_and_count.values():
    if value % 2:
        count_partA += 1
print(f'The answer to part A is: {count_partA}\n')

