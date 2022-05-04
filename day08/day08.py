# adventOfCode 2020 day ??
# https://adventofcode.com/2020/day/8

input_list = []
# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        input_list.append(in_string)

# Part A
list_line_numbers_seen = []
line_number = 0
accumulator = 0
while line_number not in list_line_numbers_seen:
    list_line_numbers_seen.append(line_number)
    command_str, integer_str = input_list[line_number].split(' ')
    integer_val = int(integer_str)
    if command_str == 'jmp':
        line_number += integer_val - 1
    if command_str == 'acc':
        accumulator += integer_val
    line_number += 1

print(f'\nThe answer to part A is {accumulator}\n')

