# adventOfCode 2020 day 05
# https://adventofcode.com/2020/day/05

def parse_boarding_pass(code):
    row_number = 0
    row_addend = 64
    for ch in code[:7]:
        if ch == 'B':
            row_number += row_addend
        row_addend = int(row_addend / 2)
    
    col_number = 0
    col_addend = 4
    for ch in code[7:]:
        if ch == 'R':
            col_number += col_addend
        col_addend = int(col_addend / 2)
    return (row_number, col_number, (8 * row_number + col_number))

# Compile a list of all seat numbers (by reading and parsing input)
seat_number_list = []
input_filename='input_sample1.txt'
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        seat_number_list.append(parse_boarding_pass(in_string)[2])

# Sort the list of seat numbers for part A
seat_number_list.sort()
print(f'\nThe answer to part A is {seat_number_list[-1]}')

# Find a missing seat number for part B
for i in range(0, len(seat_number_list)-1):
    # Compare i-th vs i+1-th seat numbers
    if seat_number_list[i+1] - seat_number_list[i] == 2:
        print(f'\nThe answer to part B is {seat_number_list[i]+1}\n')
