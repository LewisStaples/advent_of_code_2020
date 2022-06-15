# adventOfCode 2020 day 21
# https://adventofcode.com/2020/day/21

# Notes related to the data:
# Each allergen is found in only one ingredient.
# Each ingredient has either 0 or 1 allergens.
# For all foods, all ingredients must be listed.
# Some foods may omit some allergens.

# This is a list of Food objects
food_list = []

# This dict has all ingredients as the keys,
# and the value is how many foods has that ingredient
ingredients_and_freq = dict()

# This dict has allergen as keys, list of 'rownums' as the values
# (rownum is row number in the original text file, and more importantly
# it is the index of the subsequent Food object in food_list )
allergens_and_rownums = dict()

# This dict has allergen as key, ingredient as the value
# (Note: any ingredients without a listed allergen will never be listed here)
allergen_ingredient_map = dict()

# Each line of input lists the ingredients and listed allergens for a particular food
# The data for a given food is represented in class Food
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

        # Update allergens_and_rownums, initialize allergen_ingredient_map to None
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
    # (each line will be represented as a Food object in food_list)
    for i, in_string in enumerate(f):
        in_string = in_string.rstrip()
        food_list.append(Food(in_string, i))
# At this point, all input has been read in from input_filename

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
        # Exclude ingredients that have already been associated with an allergen
        ingredient_set -= set(allergen_ingredient_map.values())

        # Look at all foods associated with that 
        # (not yet assocated with an ingredient) allergen
        for rownum in allergens_and_rownums[allergen]:
            # Narrow set: (old) ingredients not yet associated with an allergen
            # and (new) ingredients associated with this Food
            ingredient_set &= set(food_list[rownum]._ingredients)

            # If there is only a single ingredient that is (2) not associated
            # with any allergens yet, and (2) associated with this Food
            if len(ingredient_set) == 1:
                # We now know that this ingredient and allergen are related
                allergen_ingredient_map[allergen] = ingredient_set.pop()
# At this point, all allergens have been matched to their ingredient

# Create a set all all ingredients that don't have any listed allergens
set_ingredients_without_listed_allergens = set(ingredients_and_freq.keys()) - set(allergen_ingredient_map.values())

# Calculate and display the answer to part A
count_appearances_nonallergenic_ingredients = 0
for ing in set_ingredients_without_listed_allergens:
    count_appearances_nonallergenic_ingredients += ingredients_and_freq[ing]
print(f'The answer to part A is: {count_appearances_nonallergenic_ingredients}')

# Calculate and display the answer to part B
# ("canonical dangerous ingredient list" is a list of ingredients
# known to be associated with an allergen, sorted by the list of
# all associated allergens)
canonical_dangerous_ingredient_list__str = ''
allergen_list = list(allergen_ingredient_map.keys())
allergen_list.sort()
for i, allergen in enumerate(allergen_list):
    if i > 0:
        canonical_dangerous_ingredient_list__str += ','
    canonical_dangerous_ingredient_list__str += allergen_ingredient_map[allergen]
print(f'The answer to part B is: {canonical_dangerous_ingredient_list__str}')

