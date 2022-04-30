# adventOfCode 202- day ??
# https://adventofcode.com/202-/day/??

this_group = ''
count_sum = 0

# Reading input from the input file
input_filename='input.txt'
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        dummy = 123
        if len(in_string) > 0:
            this_group += in_string
        else:
            count_sum += len(set(this_group))
            this_group = ''
    count_sum += len(set(this_group))
    dummy = 123

print(f'\nThe answer to part A is {count_sum}\n')
