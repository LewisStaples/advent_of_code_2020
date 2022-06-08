# adventOfCode 2020 day 20
# https://adventofcode.com/2020/day/20

# Outline of part A approach (written before I started to write any code)

# When inputting data, associate each tile with its four edges.  (All points away from the edges don't matter ... not at least for part A.  Similarly the orientation of the edges won't matter for part A, either)

# Verify that all edges either match one other edge or no other edges.  And verify that the number of matching edges is exactly what is needed to assemble the tiles into a square.

# If all above conditions apply, the corner tiles are those tiles with two only edges that match edges from other tiles, and getting the answer to part A only requires knowledge of which four tiles are corner tiles.

#
#
#

# Outline of part B approach (written before I started to write any code on part B)

# Additional code to add to part A:

# Extend dataframe tile_edges with two additional fields:  
# 	'InitCompassPoint' is an enum (0,1,2,3) indicating whether this edge was top, right, bottom, or left in the original input.  (The name is borrowed from maps, where directions could be North, East, South, or West)
	
# 	'Reversed' is a bool indicating whether the edge was or wasn't reversed when solving part A.  I anticipate that top/bottom edges as well as left/right edges will be reversed together (as this is a flip of the tile)

# When inputting a tile's data, fill in 'InitCompassPoint,' and initialize 'Reversed' to False.

# When inputting a tile's data, capture the interior points.  This will be stored separately from the edges, as the data will be processed differently.  [FILL IN DETAILS !!!!!!]
# 	??? points will be in an 2-dim array as inputted ???
# 	two boolean values if reversed/flipped horizontally and/or vertically
# 	enum indicating rotation (90, 180, 270) after any reversing/flipping .. not used until Part B is coded.
	
	
# When adding an edge, if that edge gets reversed modify 'Reversed' to True.

# Part B coding:

# Write code to visualize a given tile (without edges, and then with edges).  Since tile 1951 in sample input is at the top left of the test code against that.  As displayed in the example, Tile 1951 has no rotation and its flipped around the horizontal axis (both left and right edges are reversed).

# Write code to match edges to the known tile(s), and determine how all other tiles should be oriented to match what is already known.

# Then create a new data structure that combines of all tiles' interior points.

# Then match the sea monster by looking for three points in a row, and then the two adjacent, and then everything else in the sea monster.

import numpy as np
import pandas as pd
import math
import enum

class CompassStatus(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class RotationStatus(enum.Enum):
    NONE = 0
    NINETY_DEGREES = 1
    ONE_EIGHTY_DEGREES = 2
    TWO_SEVENTY_DEGREES = 3

class InteriorPoints:
    def __init__(self, tile_id):
        self._tile_id = tile_id
        self._interior_points = []
        self._rotation = RotationStatus.NONE
        self._flipped = {'horizontally': False, 'vertically': False}
    def append(self, next_row):
        self._interior_points.append(next_row)
        dummy = 123


tile_number = None
tile_line_number = None
tile_edges = pd.DataFrame(columns = ['TileNumber', 'EdgeString', 'InitCompassPoint', 'Reversed'])
interior_points = dict()
left_edge = ''
right_edge = ''

# This function adds an edge to the pandas dataframe while reading from the input text file.
# About half of the time it will reverse the edge before adding it.
def add_edge(tile_number, in_string, init_compass_point):
    reverse_status = False
    # First determine if the string should be reversed
    # (This prevents, for example, "#.." and "..#" from being incorrectly considered to be unique edges)

    # Start at the endpoints of the string
    i1 = 0
    i2 = -1
    
    # Look if the characters at i1 and i2 are different.  If not, go farther inward
    while i1 < len(in_string)/2:
        if in_string[i1] == in_string[i2]:
            i1 += 1
            i2 -= 1
        # If i1, i2 characters are different ensure that the '.' is the leftmost of this pair
        else:
            if in_string[i1] == '#':
                # Reverse the string
                in_string = in_string[::-1]
                reverse_status = True
            break
    
    # Add the edge to tile_edges
    tile_edges.loc[len(tile_edges.index)] = [tile_number, in_string, init_compass_point, reverse_status]

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            # Skip blank line
            pass
        elif in_string[0] == 'T':
            # Read in new tile number
            dummy, tile_number = in_string.split()
            tile_number = tile_number.replace(':', '')
            tile_number = int(tile_number)
            tile_line_number = 0
            interior_points[tile_number] = InteriorPoints(tile_number)
        else:
            # Deal with one line of a given tile
            tile_line_number += 1

            # Each read line will contribute a new character to the left and right edges
            left_edge += in_string[0]
            right_edge += in_string[-1]

            # Add a tile's top or bottom edge
            if tile_line_number == 1:
                # This line is an edge
                add_edge(tile_number, in_string, CompassStatus.NORTH)

            # After reading the tile's bottom edge, add the left and right edges
            elif tile_line_number == len(in_string):
                add_edge(tile_number, left_edge, CompassStatus.EAST)
                add_edge(tile_number, right_edge, CompassStatus.WEST)
                add_edge(tile_number, in_string, CompassStatus.SOUTH)
                left_edge = ''
                right_edge = ''

            else:
                interior_points[tile_number].append(list(in_string[1:-1]))
                dummy = 123

# Diagnostics:
# Is the number of tiles a perfect square?
number_of_tiles = int(len(tile_edges)/4)
square_length = int(math.sqrt(number_of_tiles))
is_perfect_square = math.sqrt(len(tile_edges)/4).is_integer()
print(f'Q: Is the number of tiles ({number_of_tiles}) a perfect square?')
print(f'A: {is_perfect_square}.  Each side of each square is {square_length}\n')

# Verify that all edges either match one other edge or no other edges
print('Below are the min. and max counts of appearances of any particular edge:')
print(tile_edges.groupby(['EdgeString']).count().values.min())
print(tile_edges.groupby(['EdgeString']).count().values.max())
print()

# Filter out all edges that appear only once: leaving edges that appear twice
edges_appear_twice = tile_edges.groupby(['EdgeString'])['EdgeString'].filter(lambda x: x.count() == 2)

# For every time an edge that appears twice, list the tile_number
tilenumbers_dual_appearances = tile_edges[tile_edges.EdgeString.isin(edges_appear_twice.values)]['TileNumber']

# Multiply together the tile numbers that have two edges that appear twice (these are corner edges).  This is the answer to part A.
product_corner_tiles = 1
for tilenumber in tilenumbers_dual_appearances.unique():
    if np.count_nonzero(tilenumbers_dual_appearances == tilenumber) == 2:
        print(tilenumber)
        product_corner_tiles *= tilenumber

print(f'The answer to part A is {product_corner_tiles}')
