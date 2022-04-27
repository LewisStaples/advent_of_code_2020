# adventOfCode 202- day ??
# https://adventofcode.com/202-/day/??

from fileinput import filename

forest = set()
product = 1

# Reading input from the input file
input_filename='input_sample0.txt'
with open(input_filename) as f:
    # Pull in each line from the input file
    for row_num, in_string in enumerate(f):
        in_string = in_string.rstrip()
        for col_num in [i for i,ch in enumerate(in_string) if ch=='#']:
            forest.add( (row_num, col_num) )

for slope in ((1,1),(1,3),(1,5),(1,7), (2,1)):    
    current_location = [0,0]
    tree_tally = 0
    while current_location[0] <= row_num:
        if tuple(current_location) in forest:
            tree_tally += 1
        current_location[0] += slope[0]
        current_location[1] = (current_location[1] + slope[1]) % (len(in_string))
    print(f'Reading data in from input file: {input_filename}')
    print(f'The number of trees for slope ({slope[1]},{slope[0]}) is: {tree_tally}')
    product *= tree_tally

print()
print(f'The final product is {product}')

