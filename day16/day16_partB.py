# adventOfCode 2020 day 16
# https://adventofcode.com/2020/day/16

from enum import Enum

class TicketType(Enum):
    NON_TICKET = 1
    YOUR_TICKET = 2
    NEARBY_TICKETS = 3

# valid_values is a dict of sets
# index: param_name, value: set of valid numeric values (for that parameter)
# It is initialized with an empty string as the first index and an empty set
# The empty string index will be for all values that could be valid for at 
# least one of the parameters
valid_values = {'': set()}

# This stores the numbers on "your ticket"
your_ticket = None

# Either create of extend the ranges associated with param_name
def append_ranges(lower, higher, param_name):    
    # This handles a scenario where param_name hasn't been seen before
    if param_name not in valid_values:
        valid_values[param_name] = set([])
    
    # Find all int values in the given range
    values_to_add = [x for x in range(lower, higher+1)]
    # Indicate that these values are valid for param_name
    valid_values[param_name].update(values_to_add)
    # Indicate that these values are valid for at least one parameter
    valid_values[''].update(values_to_add)
    
ticket_type = TicketType.NON_TICKET

# Reading input from the input file
input_filename='input_scenario1.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
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
                your_ticket = [int(x) for x in in_string.split(',')]
                # Initialize fieldNum_to_name: all field numbers could have all field names
                fieldNum_to_name = dict()
                for i1 in range(len(valid_values)-1):
                    fieldNum_to_name[i1] = [fieldName for fieldName in valid_values.keys() if fieldName != '']
            if ticket_type == TicketType.NEARBY_TICKETS:
                bad_ticket = False
                ticket_int_value_list = [int(x) for x in in_string.split(',')]
                # Ignore any ticket with any fields that aren't valid for any field
                for value1 in ticket_int_value_list:
                    if value1 not in valid_values['']:
                        bad_ticket = True
                        break
                
                if bad_ticket:
                    # Go to the next line in the input file (probably the next nearby ticket)
                    continue

                # Remove any field_name that can't match its field number in this ticket
                # (Note from that value1 for loop, that field_number must match some other field)
                for i2, value in enumerate(ticket_int_value_list):
                    for field_name in valid_values:
                        if value not in valid_values[field_name]:
                            if field_name in fieldNum_to_name[i2]:
                                fieldNum_to_name[i2].remove(field_name)
                                break

# Input file has been read, so manipulate data in memory
# Variable i3 is really a dummy variable that's not used elsewhere,
# but it's a fast way to ensure that each field gets converted
for i3 in range(len(valid_values)-1):
    # Traverse fieldNum_to_name and search for a numbered field with only one possible field_name.  Convert the data type from a list with a single int to a plain int, so the data type can be used to distinguish between fields that have already been found to have a single field_name (and had extra logic performed ... see i5 loop) vs. those that haven't been found.
    for i4 in fieldNum_to_name:
        if type(fieldNum_to_name[i4]) is list and len(fieldNum_to_name[i4]) == 1:
            fieldNum_to_name[i4] = fieldNum_to_name[i4][0]
            break

    # Since loop i4 has discovered a numbered field with only one possible field_name, exclude that field name as possible field names from all other numbered fields.
    for i5 in fieldNum_to_name:
        if type(fieldNum_to_name[i5]) is list:
            if fieldNum_to_name[i4] in fieldNum_to_name[i5]:
                fieldNum_to_name[i5].remove(fieldNum_to_name[i4])

product_partB_ans = 1
for i6 in range(len(fieldNum_to_name)):
    if fieldNum_to_name[i6][0:9] == 'departure':
        product_partB_ans *= your_ticket[i6]

print(f'\nThe answer to part B is {product_partB_ans}\n')

