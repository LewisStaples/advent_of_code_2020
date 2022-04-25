# adventOfCode 2020 day 1, part b
# https://adventofcode.com/2020/day/1

import sys
print()

expense_list = []
# Reading input from the input file
input_filename='input.txt'
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        expense_list.append(int(in_string))

for i in range(len(expense_list)-2):
    for j in range(i+1, len(expense_list)-1):
        for k in range(j+1, len(expense_list)):
            if expense_list[i] + expense_list[j] + expense_list[k] == 2020:
                print(f'The answer to part B is {expense_list[i] * expense_list[j] * expense_list[k]}\n')
