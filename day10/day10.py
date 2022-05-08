# adventOfCode 2020 day 10
# https://adventofcode.com/2020/day/10

from sortedcontainers import SortedDict

# Note the list of "adapters" will also include the 0 Jolt output as if it were an adapter output
adapter_ratings = []
joltage_differences = []

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        adapter_ratings.append(int(in_string))

# Compute part A
adapter_ratings.append(0)
adapter_ratings.sort()
adapter_ratings.append(adapter_ratings[-1] + 3)
for i in range(1, len(adapter_ratings)):
    joltage_differences.append(adapter_ratings[i] - adapter_ratings[i-1])
print(f'The answer to Part A is {joltage_differences.count(1) * joltage_differences.count(3)}\n')

# Compute part B
# For each adapter (by index), list the indices of all other adapters that could be after them
next_adapters = []
for i in range(len(adapter_ratings) - 1):
    next_for_i = []
    j = i
    while j < len(adapter_ratings) - 1:
        j += 1
        if adapter_ratings[j] > 3 + adapter_ratings[i]:
            break
        next_for_i.append(j)
    next_adapters.append(next_for_i)

# Start with the 
branches = SortedDict({0:1})
while branches.keys() != {len(adapter_ratings)-1}:
    (index, count) = branches.popitem(0)
    for new_index in next_adapters[index]:
        if new_index in branches:
            branches[new_index] += count
        else:
            branches[new_index] = count

(index, count) = branches.popitem(0)
print(f'The answer to Part B is {count}\n')
