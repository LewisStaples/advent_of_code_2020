# adventOfCode 202- day 06
# https://adventofcode.com/202-/day/06

def initialize_this_group():
    return {
        'any_yeses': None,
        'all_yeses': None,
        'restarted': True
    }

def update_sums(count_sum_a, count_sum_b):
    count_sum_a += len(this_group['any_yeses'])
    count_sum_b += len(this_group['all_yeses'])
    return (count_sum_a, count_sum_b)

def create_set_from_string(in_string):
    return {ch for ch in in_string}

this_group = initialize_this_group()
count_sum_a = count_sum_b = 0

# Reading input from the input file
input_filename='input_sample1.txt'
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            (count_sum_a, count_sum_b) = update_sums(count_sum_a, count_sum_b)
            this_group = initialize_this_group()
        
        elif this_group['restarted'] == True:
            this_group['restarted'] = False
            this_group['any_yeses'] = create_set_from_string(in_string)
            this_group['all_yeses'] = create_set_from_string(in_string)
        else:
            pass
            this_group['any_yeses'] |= create_set_from_string(in_string)
            this_group['all_yeses'] &= create_set_from_string(in_string)

(count_sum_a, count_sum_b) = update_sums(count_sum_a, count_sum_b)

print(f'\nUsing input file {input_filename}')
print(f'\nThe answer to part A is {count_sum_a}')
print(f'\nThe answer to part B is {count_sum_b}\n')

