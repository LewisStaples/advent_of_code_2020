# adventOfCode 2020 day 1, part a
# https://adventofcode.com/2020/day/1

print()

expense_list = []
# Reading input from the input file
input_filename='input.txt'
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        expense_list.append(int(in_string))

for i in range(len(expense_list)-1):
    for j in range(i+1, len(expense_list)):
        if expense_list[i] + expense_list[j] == 2020:
            print(f'The answer to part A is {expense_list[i] * expense_list[j]}\n')

