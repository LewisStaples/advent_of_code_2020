# adventOfCode 2020 day 15
# https://adventofcode.com/2020/day/15

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)

    # Convert string to a list of integers
    speaking_numbers = [int(ch) for ch in in_string if ch != ',']


