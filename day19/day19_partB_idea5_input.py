# adventOfCode 2020 day 19
# https://adventofcode.com/2020/day/19

import sys
import copy

# Variables with roughly raw input
input_rules = dict()
input_messages = []


# Reading input from the input file
input_filename='input.txt'
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
    'aaaaaaba',
    'aaaaaabb',
    'aaaaabab',
    'aaaaabba',
    'aaaabaab',
    'aaaabbab',
    'aaaabbbb',
    'aaabaabb',
    'aaababba',
    'aaabbaba',
    'aaabbbab',
    'aaabbbbb',
    'aabaaaab',
    'aabaaaba',
    'aabaabaa',
    'aabaabbb',
    'aabababa',
    'aababbba',
    'aababbbb',
    'aabbaaaa',
    'aabbaaab',
    'aabbabba',
    'aabbabbb',
    'aabbbaaa',
    'aabbbbba',
    'abaaaaaa',
    'abaaaaba',
    'abaaaabb',
    'abaaabba',
    'abaaabbb',
    'abaabaaa',
    'abaabaab',
    'abaababa',
    'abaabbba',
    'abaabbbb',
    'ababaaba',
    'ababaabb',
    'abababaa',
    'abababab',
    'abababbb',
    'ababbaaa',
    'ababbaab',
    'ababbaba',
    'ababbbaa',
    'ababbbbb',
    'abbaaaaa',
    'abbaaaab',
    'abbaaaba',
    'abbaabab',
    'abbaabbb',
    'abbabaaa',
    'abbababa',
    'abbabbaa',
    'abbabbab',
    'abbabbba',
    'abbbaaab',
    'abbbaaba',
    'abbbbaab',
    'abbbbaba',
    'abbbbabb',
    'abbbbbaa',
    'abbbbbbb',
    'baaaaaab',
    'baaaaaba',
    'baaaabaa',
    'baaaabab',
    'baaaabba',
    'baaaabbb',
    'baaabaaa',
    'baaabaab',
    'baaababb',
    'baaabbaa',
    'baabaaab',
    'baabaaba',
    'baababba',
    'baababbb',
    'baabbaaa',
    'baabbaab',
    'baabbaba',
    'baabbabb',
    'babaaaab',
    'babaabba',
    'babaabbb',
    'babababa',
    'babababb',
    'bababbaa',
    'bababbab',
    'babbaaaa',
    'babbabaa',
    'babbabba',
    'babbbaba',
    'babbbbaa',
    'babbbbba',
    'babbbbbb',
    'bbaaaaaa',
    'bbaaaabb',
    'bbaaabaa',
    'bbaaabab',
    'bbaabaaa',
    'bbaabaab',
    'bbaababa',
    'bbaababb',
    'bbaabbaa',
    'bbaabbab',
    'bbaabbba',
    'bbaabbbb',
    'bbabaaaa',
    'bbabaaab',
    'bbabaaba',
    'bbabaabb',
    'bbababbb',
    'bbabbaaa',
    'bbabbaab',
    'bbabbbbb',
    'bbbaaaba',
    'bbbaabaa',
    'bbbaabba',
    'bbbaabbb',
    'bbbabaaa',
    'bbbababa',
    'bbbababb',
    'bbbabbba',
    'bbbbaaaa',
    'bbbbaabb',
    'bbbbabaa',
    'bbbbbaaa',
    'bbbbbabb',
    'bbbbbbab'
]

rule_31_strings = [    
    'aaaaaaaa',
    'aaaaaaab',
    'aaaaabaa',
    'aaaaabbb',
    'aaaabaaa',
    'aaaababa',
    'aaaababb',
    'aaaabbaa',
    'aaaabbba',
    'aaabaaaa',
    'aaabaaab',
    'aaabaaba',
    'aaababaa',
    'aaababab',
    'aaababbb',
    'aaabbaaa',
    'aaabbaab',
    'aaabbabb',
    'aaabbbaa',
    'aaabbbba',
    'aabaaaaa',
    'aabaaabb',
    'aabaabab',
    'aabaabba',
    'aababaaa',
    'aababaab',
    'aabababb',
    'aababbaa',
    'aababbab',
    'aabbaaba',
    'aabbaabb',
    'aabbabaa',
    'aabbabab',
    'aabbbaab',
    'aabbbaba',
    'aabbbabb',
    'aabbbbaa',
    'aabbbbab',
    'aabbbbbb',
    'abaaaaab',
    'abaaabaa',
    'abaaabab',
    'abaababb',
    'abaabbaa',
    'abaabbab',
    'ababaaaa',
    'ababaaab',
    'abababba',
    'ababbabb',
    'ababbbab',
    'ababbbba',
    'abbaaabb',
    'abbaabaa',
    'abbaabba',
    'abbabaab',
    'abbababb',
    'abbabbbb',
    'abbbaaaa',
    'abbbaabb',
    'abbbabaa',
    'abbbabab',
    'abbbabba',
    'abbbabbb',
    'abbbbaaa',
    'abbbbbab',
    'abbbbbba',
    'baaaaaaa',
    'baaaaabb',
    'baaababa',
    'baaabbab',
    'baaabbba',
    'baaabbbb',
    'baabaaaa',
    'baabaabb',
    'baababaa',
    'baababab',
    'baabbbaa',
    'baabbbab',
    'baabbbba',
    'baabbbbb',
    'babaaaaa',
    'babaaaba',
    'babaaabb',
    'babaabaa',
    'babaabab',
    'bababaaa',
    'bababaab',
    'bababbba',
    'bababbbb',
    'babbaaab',
    'babbaaba',
    'babbaabb',
    'babbabab',
    'babbabbb',
    'babbbaaa',
    'babbbaab',
    'babbbabb',
    'babbbbab',
    'bbaaaaab',
    'bbaaaaba',
    'bbaaabba',
    'bbaaabbb',
    'bbababaa',
    'bbababab',
    'bbababba',
    'bbabbaba',
    'bbabbabb',
    'bbabbbaa',
    'bbabbbab',
    'bbabbbba',
    'bbbaaaaa',
    'bbbaaaab',
    'bbbaaabb',
    'bbbaabab',
    'bbbabaab',
    'bbbabbaa',
    'bbbabbab',
    'bbbabbbb',
    'bbbbaaab',
    'bbbbaaba',
    'bbbbabab',
    'bbbbabba',
    'bbbbabbb',
    'bbbbbaab',
    'bbbbbaba',
    'bbbbbbaa',
    'bbbbbbba',
    'bbbbbbbb'
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
    for i in range(int(len(message)/8)):
        # print(f'{i}:  {message[i*8: (i+1)*8]}', end=', ')
        if message[i*8: (i+1)*8] in rule_42_strings:
            message_result_list.append(42)
            # print(f'is in Rule 42 list of strings')
            # print('42, ', end='')

        elif message[i*8: (i+1)*8] in rule_31_strings:
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

