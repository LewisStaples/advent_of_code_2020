# adventOfCode 2020 day 20
# https://adventofcode.com/2020/day/20

# Outline of approach (written before I started to write any code)

# When inputting data, associate each tile with its four edges.  (All points away from the edges don't matter ... not at least for part A.  Similarly the orientation of the edges won't matter for part A, either)

# Verify that all edges either match one other edge or no other edges.  And verify that the number of matching edges is exactly what is needed to assemble the tiles into a square.

# If all above conditions apply, the corner tiles are those tiles with two only edges that match edges from other tiles, and getting the answer to part A only requires knowledge of which four tiles are corner tiles.


import numpy as np
import pandas as pd
import math


tile_number = None
tile_line_number = None
tile_edges = pd.DataFrame(columns = ['TileNumber', 'EdgeString'])
left_edge = ''
right_edge = ''

# This function adds an edge to the pandas dataframe while reading from the input text file.
# About half of the time it will reverse the edge before adding it.
def add_edge(tile_number, in_string):
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
            break
    
    # Add the edge to tile_edges
    tile_edges.loc[len(tile_edges.index)] = [tile_number, in_string]

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
        
        else:
            # Deal with one line of a given tile
            tile_line_number += 1

            # Each read line will contribute a new character to the left and right edges
            left_edge += in_string[0]
            right_edge += in_string[-1]

            # Add a tile's top or bottom edge
            if tile_line_number in [1, len(in_string)]:
                # This line is an edge
                add_edge(tile_number, in_string)

            # After reading the tile's bottom edge, add the left and right edges
            if tile_line_number == len(in_string):
                add_edge(tile_number, left_edge)
                add_edge(tile_number, right_edge)
                left_edge = ''
                right_edge = ''

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
