# adventOfCode 202- day 07
# https://adventofcode.com/2020/day/07

from calendar import c


class BagContents:
    def __init__(self, bag_str_list):
        self.contents = []
        for item in bag_str_list:
            number_str, color = item.split(' ', 1)
            number_int = int(number_str)
            self.contents.append( (number_int, color) )

bag_dict = dict()

def gold_in(color_in):
    if bag_dict[color_in] is None:
        return False # no gold bag found here

    # implicit else ...
    for (number_int, color) in bag_dict[color_in].contents:
        if color == 'shiny gold':
            return True
        else:
            if gold_in(color):
                return True
    
    # If no gold is found (if True hasn't been returned before now)
    return False

# Reading input from the input file
input_filename='input.txt'
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        outer_color, inner_string = in_string.split(' bags contain ')
        # print(inner_string)
        # Remove all periods and all instances of 'bag(s)' from inner_string
        inner_string = inner_string.replace('.', '')
        inner_string = inner_string.replace(' bags', '')
        inner_string = inner_string.replace(' bag', '')
        inner_color_list = inner_string.split(', ')
        # print(inner_color_list)
        # print()
        if inner_color_list == ['no other']:
            bag_dict[outer_color] = None
        else:
            bag_dict[outer_color] = BagContents(inner_color_list)

# Solve part A
color_count_with_a_gold_bag = 0
for color in bag_dict.keys():
    # print(color)
    if gold_in(color):
        color_count_with_a_gold_bag += 1

print(f'Using input filename {input_filename}')
print(f'\nThe answer to part A is {color_count_with_a_gold_bag}')

