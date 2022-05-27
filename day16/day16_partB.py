# adventOfCode 2020 day 16
# https://adventofcode.com/2020/day/16

from enum import Enum

from attr import field
class TicketType(Enum):
    NON_TICKET = 1
    YOUR_TICKET = 2
    NEARBY_TICKETS = 3

# valid_values is a dict of sets
# index: param_name, value: set of valid numeric values (for that parameter)
valid_values = dict()

def append_ranges(lower, higher, param_name):
    values_to_add = [x for x in range(lower, higher+1)]
    if param_name not in valid_values:
        valid_values[param_name] = set([])
    valid_values[param_name].update([x for x in range(lower, higher+1)])
    
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
                append_ranges(lower, higher, param_name)
        else:
            # This assumes that all fields appear before any tickets in the input file
            # and that the "your ticket" appears before any "nearby tickets" in the input
            if ticket_type == TicketType.YOUR_TICKET:
                # Initialize fieldNum_to_name: all field numbers could have all field names
                fieldNum_to_name = dict()
                for i1 in range(len(valid_values)):
                    fieldNum_to_name[i1] = [fieldName for fieldName in valid_values.keys()]
            if ticket_type == TicketType.NEARBY_TICKETS:
                for i2, value in enumerate([int(x) for x in in_string.split(',')]):
                    for field_name in valid_values:
                        if value not in valid_values[field_name]:
                            if field_name in fieldNum_to_name[i2]:
                                fieldNum_to_name[i2].remove(field_name)

# Input file has been read, so manipulate data in memory
for i3 in range(len(valid_values)):
    for i4 in fieldNum_to_name:
        if type(fieldNum_to_name[i4]) is list and len(fieldNum_to_name[i4]) == 1:
            fieldNum_to_name[i4] = fieldNum_to_name[i4][0]
            break
    for i5 in fieldNum_to_name:
        if type(fieldNum_to_name[i5]) is list:
            if fieldNum_to_name[i4] in fieldNum_to_name[i5]:
                fieldNum_to_name[i5].remove(fieldNum_to_name[i4])

    dummy = 123

print(f'\nThe answer to part B (not yet written up) is {None}\n')

