# adventOfCode 2020 day 19
# https://adventofcode.com/2020/day/19

import sys
import copy

# Variables with roughly raw input
input_rules = dict()
input_messages = []

# This is a list of lists.
# As the program goes along, each outer list element is created in response to a pipe char in the input.
# At the end, each of outer list's elements will describe one of the valid strings.
# As the program goes along, the inner list has content to describe what is known about the choices that have been made in reponse to pipe characters.
# At the end, the inner list will be a list of letters allowed.
rules = [['0']]

# This is a list of all rules shown as strings
final_rule_strings = []

# Reading input from the input file
input_filename='input_sample2.txt'
print(f'\nUsing input file: {input_filename}\n')
# print('Using rules:')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()

        # Skip over blanks
        if len(in_string) == 0:
            continue

        # Inputting a rule
        if in_string[0].isdigit():
            key, val = in_string.split(': ')
            input_rules[key] = val
        
        # Inputting a message
        elif in_string.isalpha():
            input_messages.append(in_string)

# This determines whether rules has any elements that are integers that should be looked up from the raw rules input.
def time_to_stop():
    for rule in rules:
        if [x for x in rule if x.isdigit()] != []:
            return False
    return True

while True:
    # Loop through all lists inside rules (which is a list of lists)
    for i1 in range(len(rules)):
        # Loop through rules' inner list
        for i2, old_ele in enumerate(rules[i1]):
            if old_ele.isdigit():
                # remove int element
                rules[i1].pop(i2)

                # look up the rule associated with the removed int
                new_ele_group = input_rules[old_ele]

                # If rule has a pipe character
                new_ele_group_list_pipe = new_ele_group.split(' | ')

                if len(new_ele_group_list_pipe) == 2:
                    rules.append(copy.deepcopy(rules[i1]))

                    for i3, new_ele in enumerate(new_ele_group_list_pipe[1].split(' ')):
                        if new_ele == ' ':
                            continue

                        new_ele = new_ele.replace('"', '')
                        rules[-1].insert(i2+i3, new_ele)

                # for i3, new_ele in enumerate(new_ele_group):
                for i3, new_ele in enumerate(new_ele_group_list_pipe[0].split(' ')):
                    if new_ele == ' ':
                        continue

                    new_ele = new_ele.replace('"', '')
                    rules[i1].insert(i2+i3, new_ele)

                break
    
    # Detect whether all rules' numbers have been replaced with the actual rule
    if time_to_stop():
        break

for rule in rules:
    final_rule_strings.append(''.join(rule))
final_rule_strings.sort()

input_messages.sort()

i_rule = i_message = num_matching_messages = 0

while True:
    if final_rule_strings[i_rule] == input_messages[i_message]:
        num_matching_messages += 1
        i_rule += 1
        print(input_messages[i_message])
    elif final_rule_strings[i_rule] < input_messages[i_message]:
        i_rule += 1
    else:
        i_message += 1
    if i_rule == len(final_rule_strings):
        break
    if i_message == len(input_messages):
        break

print(f'The answer to part A is {num_matching_messages}\n')

