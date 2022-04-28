# adventOfCode 2020 day 04
# https://adventofcode.com/2020/day/04

import re

class Passport:
    def __init__(self, first_line):
        self.fields = {}
        self.add_line(first_line)
    
    def add_line(self, line_to_add):
        for kvpair in line_to_add.split():
            (key, value) = kvpair.split(':')
            self.fields[key] = value

    def is_year_valid(self, year_str, lower_lim, higher_lim):
        # Parse string
        if not year_str.isdigit():
            return False
        year_num = int(year_str)

        if year_num in range(lower_lim, higher_lim+1):
            return True
        return False

    def is_hgt_valid(self):
        # Parse string
        height_str = self.fields['hgt']
        if not height_str[:-2].isdigit():
            return False
        height_number = int(height_str[:-2])
        height_unit = height_str[-2:]

        # Check value
        if height_unit == 'in':
            if height_number in range(59, 77):
                return True
        if height_unit == 'cm':
            if height_number in range(150, 194):
                return True
        return False

    def update_validity_count(self, valid_passport_count):
        # Part A validation
        for required_key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if required_key not in self.fields.keys():
                return
        valid_passport_count[0] += 1

        # Part B validation
        for partB_test in [
            self.is_year_valid(self.fields['byr'],1920, 2002),
            self.is_year_valid(self.fields['iyr'],2010, 2020),
            self.is_year_valid(self.fields['eyr'],2020, 2030),
            self.is_hgt_valid(),
            re.match('^#[0-9a-f]{6}$', self.fields['hcl']),
            self.fields['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'],
            re.match('^\d{9}$', self.fields['pid'])
        ]:
            if not partB_test:
                return
        valid_passport_count[1] += 1

# Read input into memory
input_filename='input_sample3_valid.txt'
the_passport = None
valid_passport_count = [0,0]

# Reading input from the input file
with open(input_filename) as f:
    print(f'\nUsing file {input_filename}\n')
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if the_passport == None:
            the_passport = Passport(in_string)
        elif len(in_string) == 0:
            the_passport.update_validity_count(valid_passport_count)
            the_passport = None
        else:
            the_passport.add_line(in_string)

    # Evaluate if the password at the end of the input file is valid
    if the_passport is not None:
        the_passport.update_validity_count(valid_passport_count)

print(f'The answer for part A is: {valid_passport_count[0]}')
print(f'The answer for part B is: {valid_passport_count[1]}\n')

