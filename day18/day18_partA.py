# adventOfCode 2020 day 18, part A
# https://adventofcode.com/202-/day/18

import sys
def resolve_value(in_string):
    ret_val = None
    operator = None
    while len(in_string)>0:
        # Remove any operator
        if in_string[0] in ['+', '*']:
            operator = in_string[0]
            in_string = in_string[1:]
        
        # Get next integer from in_string
        list_digits = []
        while len(in_string) > 0 and in_string[0].isdigit():
            list_digits.append(in_string[0])
            in_string = in_string[1:]
        next_number = int(''.join(list_digits))

        if operator is None:
            ret_val = next_number
        elif operator == '+':
            ret_val += next_number
        elif operator == '*':
            ret_val *= next_number
        else:
            sys.exit(f'Bad operator: {operator}')
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

sum_A = 0

# Reading input from the input file
input_filename='input_scenario1.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # Debugging code ....
        # print(in_string)
        # print( get_value(in_string) )
        # print()
        sum_A += get_value(in_string)

print(f'The answer to part A is {sum_A}')
