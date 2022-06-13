# adventOfCode 2020 day 21, Part A
# https://adventofcode.com/2020/day/21

# Thinking through needed data ...
# Each allergen is found in only one ingredient.
# Each ingredient has either 0 or 1 allergens.
# For all foods, all ingredients must be listed.
# Some foods may omit some allergens.
# 
# Compile a list of all listed allergens
#   Each listed allergen will have an associated ingredient (initialized to None ... for not yet known)
#
# Compile a list of all ingredients
#   Count number of times the ingredient appears in the list of foods
#
# Go through allergen list, one at a time
#   For this allergen look at all foods (rows) that that allergen is listed as being in
#   Compile a list of all ingredients in those rows that isn't associated with any allergen.
#   If you find that all only one ingredient appears in all of these rows
#       that allergen should be associated with that ingredient
#       and you don't need to revist that allergen anymore
# Repeat until there are no more allergens with non yet determined ingredients.


# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

