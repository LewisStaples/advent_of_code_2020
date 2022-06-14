# adventOfCode 2020 day 21, Part A
# https://adventofcode.com/2020/day/21

# Thinking through data and algorithm ...
# Each allergen is found in only one ingredient.
# Each ingredient has either 0 or 1 allergens.
# For all foods, all ingredients must be listed.
# Some foods may omit some allergens.
# 
# Create a dict with all listed allergens as the keys
#   Each listed allergen will have exactly one associated ingredient as its value (initialized to None ... for not yet known)
#
# Compile a dict with all ingredients as the keys
#   The key will be the number of times the ingredient appears in the list of foods
#
# Go through allergen list, one at a time
#   For this allergen look at all foods (rows) that that allergen is listed as being in
#   Compile a list of all ingredients in those rows that isn't associated with any allergen.
#   If you find that all only one ingredient appears in all of these rows
#       that allergen should be associated with that ingredient
#       and you don't need to revisit that allergen anymore

# Repeat until there are no more allergens with non yet determined ingredients.

food_list = []
ingredients_and_freq = dict()
allergens_and_rownums = dict()
allergen_ingredient_map = dict()

class Food:
    def __init__(self, str_input, line_num):
        # Parse input, create the Food object
        ingredients_str, allergens_str = str_input.split(' (contains ')
        self._ingredients= ingredients_str.split()

        allergens_str = allergens_str[:-1]
        self._allergens_labelled = allergens_str.split(', ')
        
        # Update ingredients_and_freq
        for ingredient in self._ingredients:
            if ingredient in ingredients_and_freq:
                ingredients_and_freq[ingredient] += 1
            else:
                ingredients_and_freq[ingredient] = 1

        # Update allergens_and_rownums
        for allergen_labelled in self._allergens_labelled:
            if allergen_labelled in allergens_and_rownums:
                allergens_and_rownums[allergen_labelled].append(line_num)
            else:
                allergens_and_rownums[allergen_labelled] = [line_num]
                allergen_ingredient_map[allergen_labelled] = None

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for i, in_string in enumerate(f):
        in_string = in_string.rstrip()
        food_list.append(Food(in_string, i))

# Loop until all allergens have been matched to their ingredient
while None in allergen_ingredient_map.values():
    # Loop through all allergens
    for allergen in allergen_ingredient_map:
        # Skip any allergens whose ingredient has already been identified
        # (Only not-yet-identified allergens will get past this if statement)
        if allergen_ingredient_map[allergen] is not None:
            continue

        # Consider all ingredients
        ingredient_set = set(ingredients_and_freq.keys())
        # Exclude ingredients that have already been discovered
        ingredient_set -= set(allergen_ingredient_map.values())

        # Look at all foods associated with that allergen
        for rownum in allergens_and_rownums[allergen]:
            ingredient_set &= set(food_list[rownum]._ingredients)
            if len(ingredient_set) == 1:
                # It has been found !!!!!
                allergen_ingredient_map[allergen] = ingredient_set.pop()

set_ingredients_without_listed_allergens = set(ingredients_and_freq.keys()) - set(allergen_ingredient_map.values())

total_appearances = 0
for ing in set_ingredients_without_listed_allergens:
    total_appearances += ingredients_and_freq[ing]

print(f'The answer to part A is : {total_appearances}')

canonical_dangerous_ingredient_list__str = ''
allergen_list = list(allergen_ingredient_map.keys())
allergen_list.sort()

for i, allergen in enumerate(allergen_list):
    if i > 0:
        canonical_dangerous_ingredient_list__str += ','
    canonical_dangerous_ingredient_list__str += allergen_ingredient_map[allergen]

print(f'The answer to part B is : {canonical_dangerous_ingredient_list__str}')

