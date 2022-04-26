# adventOfCode 2020 day 2
# https://adventofcode.com/2020/day/2

class PasswordPolicy:
    num_lower = num_higher = letter_string = password_string = None
    def __init__(self, in_string):
        [nums_string, letter_string, password_string] = in_string.split(' ')
        [self.num_lower, self.num_higher] = [int(x) for x in nums_string.split('-')]
        self.letter_string = letter_string[0]
        self.password_string = password_string
        dummy = 123

    def valid_partA(self):
        return self.password_string.count(self.letter_string) in range(self.num_lower, self.num_higher+1)

    def valid_partB(self):
        return ((self.password_string[self.num_lower-1] != self.letter_string) == (self.password_string[self.num_higher-1] == self.letter_string))

password_policies = []

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input from {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        password_policies.append(PasswordPolicy(in_string))

valid_password_count = 0 # This is the answer
for password in password_policies:
    if password.valid_partA():
        valid_password_count += 1
print(f'The number of valid passwords for Part A is {valid_password_count}')

valid_password_count = 0 # Resetting to zero, to calculate for part B
for password in password_policies:
    if password.valid_partB():
        valid_password_count += 1
print(f'The number of valid passwords for Part B is {valid_password_count}\n')
