# adventOfCode 2020 day 19
# https://adventofcode.com/2020/day/19

from numpy import isin


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

rules = ['0']
close_paren_needed = False
# while [x for x in rules if isinstance(x, int)] != []:
while True:
    for i, old_ele in enumerate(rules):
        # if isinstance(old_ele, int):
        if old_ele.isdigit():
            # remove int element
            rules.pop(i)

            # look up the rule associated with the int
            new_ele_group = input_rules[old_ele].split(' ')

            # if the rule has a pipe character, split it up
            pipeChar_indices = []
            for k, ch in enumerate(new_ele_group):
                if ch == '|':
                    pipeChar_indices.append(k)
            if len(pipeChar_indices) > 0:
                dummy = 123
                while len(pipeChar_indices) > 0:
                    l = pipeChar_indices.pop()

                    new_ele_group.insert(l+1, '(')
                    new_ele_group.insert(l, ')')

                new_ele_group.insert(0, '(')
                new_ele_group.append(')')
                dummy = 123
            dummy = 123

            # for j, new_ele in enumerate(new_ele_group):
                # if new_ele[0].isdigit():
                #     new_ele_group[j] = int(new_ele)
                # rules.insert(i + j, new_ele)

            dummy = 123



            # for j, new_ele in enumerate(input_rules[old_ele].split(' ')):
            #     if new_ele[0].isdigit():
            #         new_ele = int(new_ele)
            #     rules.insert(i + j, new_ele)
            #     # if new_ele == '|':
            #     #     close_paren_needed = True
            #     dummy = 123

            # # Insert parentheses here
            # if close_paren_needed:
            #     close_paren_needed = False

                # # First opening parenthesis
                # rules.insert(i, '(')

                # # Insert internal parentheses
                # pipeChar_indices = []
                # for k, ch in enumerate(rules):
                #     if ch == '|':
                #         pipeChar_indices.append(k)
                # while len(pipeChar_indices) > 0:
                #     l = pipeChar_indices.pop()
                #     rules.insert(l+1, '(')
                #     rules.insert(l, ')')

                # # Last closing parenthesis
                # rules.append(')')

                # dummy = 123

            dummy = 123
        
            # Only replace one rule at a time
            for q, ele in enumerate(new_ele_group):
                rules.insert(i+q, ele)
            break

        # elif old_ele[0] == '"':
        #     # remove the quotes (from starting and ending characters)
        #     rules.pop(i)
        #     old_ele = old_ele[1:-1]
        #     rules.insert(i, old_ele)
        #     dummy = 123
        #     break

    dummy = 123
    # if new_ele_group
    if [x for x in rules if x.isdigit()] == []:
        break
dummy = 123
pattern_str = ''.join(rules).replace('"', '')

print(f'Pattern string: {pattern_str}')
