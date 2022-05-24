# adventOfCode 2020 day 15
# https://adventofcode.com/2020/day/15


# last_number is the newest value of the speaking number
# This function updates speakingNum_indices_dict to reflect the latest value of last_number
def update_with_last_number():
    if last_number in speakingNum_indices_dict:
        speakingNum_indices_dict[last_number].append(turn_number)
        if len(speakingNum_indices_dict[last_number]) > 2:
            speakingNum_indices_dict[last_number].pop(0)
    else:
        speakingNum_indices_dict[last_number] = [turn_number]

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()

print(f'With starting numbers: {in_string}')

# Parse data from input file
starting_numbers = [int(num) for num in in_string.split(',')]

speakingNum_indices_dict = {}
for turn_number, last_number in enumerate(starting_numbers, 1):
    update_with_last_number()
turn_number += 1

del in_string
del starting_numbers
del input_filename

# Loop turn for all calculated speaking numbers through end of program operation
while True:
    # "Speak" a number indicating how long ago it was previously spoken
    if len(speakingNum_indices_dict[last_number]) == 1:
        last_number = 0
    else:
        last_number = speakingNum_indices_dict[last_number][1] - speakingNum_indices_dict[last_number][0]
    update_with_last_number()

    if turn_number == 2020:
        print(f'Part A result:  {turn_number}-th spoken is {last_number}')
    if turn_number == 30000000:
        print(f'Part B result:  {turn_number}-th spoken is {last_number}')
        break

    turn_number += 1

