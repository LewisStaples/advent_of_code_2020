# adventOfCode 2020 day 09
# https://adventofcode.com/2020/day/9

import enum
import sys

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

# Part A logic
for i_next, next_number in enumerate(number_list):
    if i_next >= preamble:
        if first_nonsum(i_next, next_number):
            print(f'\nThe solution to Part A is: {next_number}\n')
            break

# Part B declarations and initializations
class Trend(enum.Enum):
    ASCENDING  = 1
    DESCENDING = 2

    def switch_trend(self):
        if self == Trend.ASCENDING:
            return self.DESCENDING
        else:
            return self.ASCENDING

    def get_increment(self):
        if self == Trend.ASCENDING:
            return 1
        else:
            return -1

# Find indices of contiguous range that adds up to next_number
contiguous_range = {
    'lower': None,
    'higher': None,
    'sum': sum(number_list[0:1])
}

the_trend = Trend.ASCENDING


# Use indices to get a slice of number_list and find min and max values in that slice

# Pseudocode:  keep lower at 0, increment higher up to end of the list
# Then move lower to 1, remove from end one at a time
# Then move lower to 2, add to slice one at a time
# ....
# (This should be much more efficient than calculating the sum all over again for all permutations)



# Outer loop:  loop through all possible indices of the start of the sublist to be summed up
for contiguous_range['lower'] in range(len(number_list)-1):
    # Inner loop:  loop through all possible indices of the end of the sublist to be summed up
    # Note that the_trend has this alternate between increasing and decreasing
    first_index = contiguous_range['lower'] + 1 if the_trend == Trend.ASCENDING else len(number_list) - 1
    last_index = len(number_list) if the_trend == Trend.ASCENDING else contiguous_range['lower']
    for contiguous_range['higher'] in range(first_index, last_index, the_trend.get_increment()):
        # This has the major improvement in efficiency ... instead of calculating a new sum from the start for
        # every possible sublist, this reuses the previously sum but either adds or substracts a single value from it
        # (the value added or substracted is the one additional or fewer value in the sublist)
        contiguous_range['sum'] += number_list[contiguous_range['higher']] * the_trend.get_increment()
        # Check if the desired result is found.
        if contiguous_range['sum'] == next_number:
            max_value = max(number_list[contiguous_range['lower']:contiguous_range['higher']+1])
            min_value = min(number_list[contiguous_range['lower']:contiguous_range['higher']+1])
            print(f'The solution to Part B is {(max_value + min_value)}\n')
            sys.exit('Program complete\n')
    the_trend = the_trend.switch_trend()

