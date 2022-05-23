# adventOfCode 2020 day 09
# https://adventofcode.com/2020/day/9

import enum
import sys

preamble = 5  # 5 or 25
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

# Part B takes next_number (solution to part A), and then seeks "a contiguous
# set of at least two numbers in your list which sum to" next_number

# This program avoids recalculating the complete sum for all contiguous subsets of the list by following the steps below, and checking after each step whether the sum equals next_number.  The program would run much slower if the sum were calculated by adding each element anew for each and every sublist.
# 
# (1) Start off with a sublist of values at indices 0 and 1.  The sum for this sublist is both elements added together
#
# (2) Add elements, one at a time, and for each added element recalculate the sum (by adding the new element to the value of the sum)
# 
# (3) Remove the element at index 0 from the sublist and recalculate the sum (by removing the 0-th index value from the sum)

# (4) Then remove the value with the largest index from the sublist and recalculate the sum

# (5) Keep removing the value from the end of the sublist and recalculating the sum, until the list is down to two items

# (6) Remove the element at index 0 from the sublist.  Add another value to the end of the sublist to keep the sublist at least two items long or longer.  Then recalculate the sum, based on the removal and added value.

# The removal of the 0-th index element is done via the outer for loop.  The inner for loop considers all possible sublists that start with the starting element determined by the number of times that the outer loop has run.


# Track whether the program is making the index of the end of the sublist larger or smaller
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

# Find indices of contiguous range that adds up to next_number, and store the resulting sum.  (The sum needs to be stored, so it can be recalculated ... to make the program run faster)
contiguous_range = {
    'lower': None,
    'higher': None,
    'sum': sum(number_list[0:1])
}

the_trend = Trend.ASCENDING



# Outer loop:  loop through all possible indices of the start of the sublist to be summed up
prior_c_r_higher = 0
for contiguous_range['lower'] in range(len(number_list)-1):
    if contiguous_range['lower'] >= 1:
        contiguous_range['sum'] -= number_list[contiguous_range['lower']-1]

    # Inner loop:  loop through all possible indices of the end of the sublist to be summed up
    # Note that the_trend has this alternate between increasing and decreasing
    first_index = contiguous_range['lower'] + 1 if the_trend == Trend.ASCENDING else len(number_list) - 1
    last_index = len(number_list) if the_trend == Trend.ASCENDING else contiguous_range['lower']
    for contiguous_range['higher'] in range(first_index, last_index, the_trend.get_increment()):
        # This has the major improvement in efficiency ... instead of calculating a new sum from the start for
        # every possible sublist, this reuses the previously sum but either adds or substracts a single value from it
        # (the value added or substracted is the one additional or fewer value in the sublist)
        while prior_c_r_higher < contiguous_range['higher']:
            prior_c_r_higher += 1
            contiguous_range['sum'] += number_list[prior_c_r_higher]
        while prior_c_r_higher > contiguous_range['higher']:
            contiguous_range['sum'] -= number_list[prior_c_r_higher]
            prior_c_r_higher -= 1

        # Check if the desired result is found.
        if contiguous_range['sum'] == next_number:
            # Since it's been found: do final calculation, display the result, and end the program
            max_value = max(number_list[contiguous_range['lower']:contiguous_range['higher']+1])
            min_value = min(number_list[contiguous_range['lower']:contiguous_range['higher']+1])
            print(f'The solution to Part B is {(max_value + min_value)}\n')
            sys.exit('Program complete\n')
        
        prior_c_r_higher = contiguous_range['higher']

    the_trend = the_trend.switch_trend()

print('No result for B has been found\n')
