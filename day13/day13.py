# adventOfCode 2020 day 13
# https://adventofcode.com/2020/day/13

input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    in_string1 = f.readline().rstrip()
    earliest_timestamp = int(in_string1)
    in_string2 = f.readline().rstrip()
    string_list = in_string2.split(',')
    bus_IDs = [int(n) for n in string_list if n != 'x']

    # get rid of variables that won't be needed anymore
    del in_string1, in_string2, string_list, f, input_filename

    dummy = 123
    
