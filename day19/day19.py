# adventOfCode 2020 day 19
# https://adventofcode.com/2020/day/19

import sys
import copy

input_rules = dict()
messages = []

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
# print('Using rules:')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)

        # Skip over blanks
        if len(in_string) == 0:
            continue

        # Inputting a rule
        if in_string[0].isdigit():
            key, val = in_string.split(': ')
            input_rules[key] = val
        
        # Inputting a message
        elif in_string.isalpha():
            messages.append(in_string)

# Rules is a list of lists.
# As the program goes along, each outer list element is created in response to a pipe char in the input.
# At the end, each of outer list's elements will describe one of the valid strings.
# As the program goes along, the inner list has content to describe what is known about the choices that have been made in reponse to pipe characters.
# At the end, the inner list will be a list of letters allowed.
rules = [['0']]

def time_to_stop():
    for rule in rules:
        if [x for x in rule if x.isdigit()] != []:
            return False
    return True

while True:
    for i1 in range(len(rules)):
        for i2, old_ele in enumerate(rules[i1]):
            if old_ele.isdigit():
                # remove int element
                rules[i1].pop(i2)

                # look up the rule associated with the removed int
                new_ele_group = input_rules[old_ele]

                dummy = 123
                # If rule has a pipe character
                new_ele_group_list_pipe = new_ele_group.split(' | ')

                if len(new_ele_group_list_pipe) == 2:
                    rules.append(copy.deepcopy(rules[i1]))

                    for i3, new_ele in enumerate(new_ele_group_list_pipe[1].split(' ')):
                        if new_ele == ' ':
                            continue

                        new_ele = new_ele.replace('"', '')
                        rules[-1].insert(i2+i3, new_ele)
                        dummy = 123


                # for i3, new_ele in enumerate(new_ele_group):
                for i3, new_ele in enumerate(new_ele_group_list_pipe[0].split(' ')):
                    if new_ele == ' ':
                        continue

                    new_ele = new_ele.replace('"', '')
                    rules[i1].insert(i2+i3, new_ele)
                    dummy = 123

                break

        dummy = 123
        # if '|' in rules[i1]:
        #     # Make a deep copy
        #     rules.append(copy.deepcopy(rules[i1]))

        #     # Remove everything after the pipe in i1-th element
        #     split_index =  rules[i1].index('|')
        #     rules[i1] = rules[i1][:split_index]

        #     # Remove everything b the pipe in (new) deep copy
        #     rules[-1] = rules[-1][split_index+1:]


            


    dummy = 123
    # Stop condition ... if there are no digits left in rules
    # for rule in rules:
    #     if [x for x in rule if x.isdigit()] == []:
    #         break
    # break

    # if [x for x in rules if x.isdigit()] == []:
    #     break

    # Detect whether all rules' numbers have been replaced with the actual rule
    if time_to_stop():
        break
dummy = 123
# pattern_str = ''.join(rules).replace('"', '')

# print(f'Pattern string: {pattern_str}')
