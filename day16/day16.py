# adventOfCode 2020 day 16
# https://adventofcode.com/2020/day/16

from enum import Enum
class TicketType(Enum):
    NON_TICKET = 1
    YOUR_TICKET = 2
    NEARBY_TICKETS = 3

valid_values = set()

def range_append(lower, higher):
    values_to_add = [x for x in range(lower, higher+1)]
    valid_values.update(values_to_add)

ticket_type = TicketType.NON_TICKET
sum_invalid_values = 0

# Reading input from the input file
input_filename='input.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        if in_string == 'your ticket:':
            ticket_type = TicketType.YOUR_TICKET
        elif in_string == 'nearby tickets:':
            ticket_type = TicketType.NEARBY_TICKETS
        elif len(in_string) == 0:
            ticket_type = TicketType.NON_TICKET
        elif in_string[0].isalpha():
            param_name, param_range = in_string.split(': ')
            param_intervals = param_range.split(' or ')
            for param_interval in param_intervals:
                lower, higher = [int(x) for x in param_interval.split('-')]
                range_append(lower, higher)
        else:
            if ticket_type == TicketType.NEARBY_TICKETS:
                for value in [int(x) for x in in_string.split(',')]:
                    if value not in valid_values:
                        # An invalid ticket has been found
                        sum_invalid_values += value

print(f'\nThe answer to part A (the "ticket scanning error rate") is {sum_invalid_values}\n')

