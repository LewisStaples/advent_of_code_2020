# adventOfCode 2020 day 09
# https://adventofcode.com/2020/day/9

preamble = 5
number_list = []
print(f'\nUsing preamble: {preamble}')

# Reading input from the input file
input_filename='input_sample1_preamble5.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        number_list.append(int(in_string))

def first_nonsum(i_next, next_number):
    for i in range(i_next - preamble, i_next - 1):
        for j in range(i + 1, i_next):
            if next_number == number_list[i] + number_list[j]:
                return False
    return True

# Part A
for i_next, next_number in enumerate(number_list):
    if i_next >= preamble:
        if first_nonsum(i_next, next_number):
            print(f'\nThe solution is ... {next_number}\n')
            break
