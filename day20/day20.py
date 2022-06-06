# adventOfCode 2020 day 20
# https://adventofcode.com/2020/day/20

import numpy as np
import pandas as pd

import re

tile_number = None
tile_line_number = None
tile_edges = pd.DataFrame(columns = ['TileNumber', 'EdgeString'])
left_edge = ''
right_edge = ''

def add_edge(tile_number, in_string):
    # Reverse the string to ensure that matching rows are identified
    i1 = 0
    i2 = -1
    while i1 < len(in_string)/2:
        if in_string[i1] == in_string[i2]:
            i1 += 1
            i2 -= 1
        else:
            if in_string[i1] == '#':
                in_string = in_string[::-1]
            break
    
    # Add the edge
    tile_edges.loc[len(tile_edges.index)] = [tile_number, in_string]

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        if len(in_string) == 0:
            # Skip blank line
            pass
        elif in_string[0] == 'T':
            # Read in new tile number
            dummy, tile_number = in_string.split()
            tile_number = tile_number.replace(':', '')
            tile_number = int(tile_number)

            tile_line_number = 0
            dummy = 123
        
        else:
            # Read in one line of a given tile
            tile_line_number += 1

            left_edge += in_string[0]
            right_edge += in_string[-1]

            if tile_line_number in [1, len(in_string)]:
                # This line is an edge
                add_edge(tile_number, in_string)

            if tile_line_number == len(in_string):
                add_edge(tile_number, left_edge)
                add_edge(tile_number, right_edge)

dummy = 123


# Approach that I intend to take:

# When inputting data, associate each tile with its four edges.  (All points away from the edges don't matter ... not at least for part A.  Similarly the orientation of the edges won't matter for part A, either)

# Verify that all edges either match one other edge or no other edges.  And verify that the number of matching edges is exactly what is needed to assemble the tiles into a square.

# If all above conditions apply, the corner tiles are those tiles with two only edges that match edges from other tiles, and getting the answer to part A only requires knowledge of which four tiles are corner tiles.


