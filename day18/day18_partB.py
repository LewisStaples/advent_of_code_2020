# adventOfCode 2020 day 18, part B
# https://adventofcode.com/202-/day/18

import sys
def resolve_value(in_string):
    ret_val = None
    line_list = []

    # Convert in_string into a list of int values and operators
    while len(in_string) > 0:
        # Append operator to line_list as a string of length 1
        if in_string[0] in ['+', '*']:
            line_list.append(in_string[0])
            in_string = in_string[1:]
            continue
        # Anything that isn't an operator is a digit in an int,
        # therefore gather digits together, convert to int, append to line_list
        next_num_str = ''
        while len(in_string) > 0 and in_string[0].isdigit():
            next_num_str += in_string[0]
            in_string = in_string[1:]
        line_list.append(int(next_num_str))

    # For all addition symbols, add the adjacent numbers
    while '+' in line_list:
        the_index = line_list.index('+')
        line_list[the_index-1] += line_list[the_index+1]
        line_list.pop(the_index+1)
        line_list.pop(the_index)

    # For all multiplication symbols, multiply the adjacent numbers
    while '*' in line_list:
        the_index = line_list.index('*')
        line_list[the_index-1] *= line_list[the_index+1]
        line_list.pop(the_index+1)
        line_list.pop(the_index)

    ret_val = int(line_list[0])
    return ret_val

def get_value(in_string):
    # Remove space characters
    in_string = in_string.replace(' ', '')

    # Eliminate parentheses, one at a time
    while ('(' in in_string):
        i_start = i_end = None
        for i, ch in enumerate(in_string):
            if ch == '(':
                i_start = i
            if ch == ')':
                i_end = i
                break
        in_string = in_string[:i_start] + str(resolve_value(in_string[i_start+1:i_end])) + in_string[i_end+1:]

    # Resolve value (note that all parentheses have already been removed)
    return resolve_value(in_string)

sum_B = 0

# Reading input from the input file
input_filename='input_scenario1.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # Debugging code ....
        # print(in_string)
        # print( get_value(in_string) )
        # print()
        sum_B += get_value(in_string)

print(f'\nThe answer to part B is {sum_B}\n')
