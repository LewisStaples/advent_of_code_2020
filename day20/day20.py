# adventOfCode 2020 day 20
# https://adventofcode.com/2020/day/20

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

# Approach that I intend to take:

# When inputting data, associate each tile with its four edges.  (All points away from the edges don't matter ... not at least for part A.  Similarly the orientation of the edges won't matter for part A, either)

# Verify that all edges either match one other edge or no other edges.  And verify that the number of matching edges is exactly what is needed to assemble the tiles into a square.

# If all above conditions apply, the corner tiles are those tiles with two only edges that match edges from other tiles, and getting the answer to part A only requires knowledge of which four tiles are corner tiles.


