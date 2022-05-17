# adventOfCode 2020 day 14
# https://adventofcode.com/2020/day/14

mask_current = None

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        if 'mask' in in_string:
            mask_current = in_string[7:]        
        else:
            in_string = in_string[4:]
            address, value = (int(x) for x in in_string.split('] = '))
