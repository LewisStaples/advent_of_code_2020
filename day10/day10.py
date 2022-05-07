# adventOfCode 2020 day 10
# https://adventofcode.com/2020/day/10

adapter_ratings = []
joltage_differences = []

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        adapter_ratings.append(int(in_string))

adapter_ratings.sort()
joltage_differences.append(adapter_ratings[0])
for i in range(1, len(adapter_ratings)):
    joltage_differences.append(adapter_ratings[i] - adapter_ratings[i-1])
joltage_differences.append(3)

print(f'The answer to Part A is {joltage_differences.count(1) * joltage_differences.count(3)}\n')
