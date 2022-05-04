# adventOfCode 2020 day ??
# https://adventofcode.com/2020/day/8

input_list = []

def get_accumulator(line_num_to_swap):
    list_line_numbers_seen = []
    line_number = 0
    accumulator = 0

    while True:
        # Return if either of two stopping conditions are met
        if line_number in list_line_numbers_seen:
            return ('repeat', accumulator)
        if line_number == len(input_list):
            return ('eof', accumulator)

        # Cycle through this iteration
        list_line_numbers_seen.append(line_number)
        command_str, integer_str = input_list[line_number].split(' ')
        integer_val = int(integer_str)
        if command_str == 'jmp' and line_number != line_num_to_swap:
            line_number += integer_val - 1
        if command_str == 'nop' and line_number == line_num_to_swap:
            line_number += integer_val - 1
        if command_str == 'acc':
            accumulator += integer_val
        line_number += 1

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        input_list.append(in_string)

# Part A
print(f'\nThe answer to part A is {get_accumulator(None)[1]}')

# Part B
for line_num in range(len(input_list)):
    end_status, accumulator = get_accumulator(line_num)
    if end_status == 'eof':
        print(f'\nThe answer to part A is {accumulator}\n')

