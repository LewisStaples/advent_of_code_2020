# adventOfCode 2020 day 04
# https://adventofcode.com/2020/day/04

class Passport:
    def __init__(self, first_line):
        self.fields = {}
        self.add_line(first_line)
        
    def add_line(self, line_to_add):
        for kvpair in line_to_add.split():
            (key, value) = kvpair.split(':')
            self.fields[key] = value

    def is_valid(self):
        # Returns 1 or 0 instead of True or False, so the count of valid passports may be incremented with the returned value
        for required_key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if required_key not in self.fields.keys():
                return 0 # It's not valid
        return 1 # It's valid

# Read input into memory
input_filename='input_sample0.txt'
the_passport = None
valid_passport_count = 0

# Reading input from the input file
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        if the_passport == None:
            the_passport = Passport(in_string)
        elif len(in_string) == 0:
            valid_passport_count += the_passport.is_valid()
            the_passport = None
        else:
            the_passport.add_line(in_string)

    # Evaluate if the password at the end of the input file is valid
    if the_passport is not None:
        valid_passport_count += the_passport.is_valid()
        the_passport = None

print(f'\nThe answer is: {valid_passport_count}\n')

