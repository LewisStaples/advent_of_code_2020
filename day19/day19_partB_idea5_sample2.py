# adventOfCode 2020 day 19
# https://adventofcode.com/2020/day/19

import sys
import copy

# Variables with roughly raw input
input_rules = dict()
input_messages = []


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

# input_messages.sort()

rule_42_strings = [
    'aaaaa',
    'aaaab',
    'aaaba',
    'aaabb',
    'aabbb',
    'ababa',
    'abbbb',
    'baaaa',
    'baabb',
    'babbb',
    'bbaaa',
    'bbaab',
    'bbabb',
    'bbbab',
    'bbbba',
    'bbbbb',
]




rule_31_strings = [
    'aabaa' ,
    'aabab' ,
    'aabba' ,
    'abaaa' ,
    'abaab' ,
    'ababb' ,
    'abbaa' ,
    'abbab' ,
    'abbba' ,
    'baaab' ,
    'baaba' ,
    'babaa' ,
    'babab' ,
    'babba' ,
    'bbaba' ,
    'bbbaa' ,
]

# To verify no overlap between rule_42_strings and rule_31_strings
# Add both lists to a set.  If len(set) equals the sum of list lengths, then there is no overlapping between them.

set_of_two_lists = set()
set_of_two_lists.update(rule_31_strings, rule_42_strings)

if len(set_of_two_lists) == len(rule_31_strings) + len(rule_42_strings):
    print('There are no overlaps')
else:
    print('There are overlaps')
print()

# Loop through messages, and count messages that follow rule#0
count_messages_follow_rule_zero = 0
for message in input_messages:
    message_result_list = []
    # print(message)
    # print(len(message))
    
    for i in range(int(len(message)/5)):
        # print(f'{i}:  {message[i*5: (i+1)*5]}', end=', ')
        if message[i*5: (i+1)*5] in rule_42_strings:
            message_result_list.append(42)
            # print(f'is in Rule 42 list of strings')
            # print('42, ', end='')

        elif message[i*5: (i+1)*5] in rule_31_strings:
            message_result_list.append(31)
            # print(f'is in Rule 31 list of strings')
            # print('31, ', end='')
        # print('\n')
        else:
            print('neither, ', end='')
            print('FAILED')
            continue

    # print(message_result_list, end='  ')
    if message_result_list[0] == 31:
        # print('FAILED', end='  ')
        pass
    elif message_result_list[-1] == 42:
        # print('FAILED', end='  ')
        pass
    elif message_result_list.count(42) <= message_result_list.count(31):
        # print('FAILED', end='  ')
        pass
    else:
        index_first_31 =  message_result_list.index(31)
        if 42 in message_result_list[index_first_31:]:
            # print('FAILED')
            pass
        else:
            # print('SUCCEEDED', end='  ')
            print(message)
            count_messages_follow_rule_zero += 1



print(f'\nThe answer to part B is: {count_messages_follow_rule_zero}\n')


