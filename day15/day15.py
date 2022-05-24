# adventOfCode 2020 day 15
# https://adventofcode.com/2020/day/15

def update_with_last_number():
    if last_number in speakingNum_lastTwoIndices_dict:
        speakingNum_lastTwoIndices_dict[last_number].append(turn_number)
        if len(speakingNum_lastTwoIndices_dict[last_number]) > 2:
            speakingNum_lastTwoIndices_dict[last_number].pop(0)
    else:
        speakingNum_lastTwoIndices_dict[last_number] = [turn_number]

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)

    # Parse data from input file
    speaking_numbers = [int(num) for num in in_string.split(',')]

    speakingNum_lastTwoIndices_dict = {}
    for turn_number, last_number in enumerate(speaking_numbers, 1):
        update_with_last_number()
    turn_number += 1

    del in_string
    del speaking_numbers
    del input_filename

    # Loop turn for all calculated speaking numbers through end of program operation
    while turn_number < 2019:

        # "Speak" a number indicating how long ago it was previously spoken

        if len(speakingNum_lastTwoIndices_dict[last_number]) == 1:
            last_number = 0
        else:
            last_number = speakingNum_lastTwoIndices_dict[last_number][1] - speakingNum_lastTwoIndices_dict[last_number][0]
        
        update_with_last_number()
        turn_number += 1

dummy = 123
