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

    def valid(self):
        if self.password_string.count(self.letter_string) in range(self.num_lower, self.num_higher+1):
            return True
        else:
            return False

password_policies = []
valid_password_count = 0 # This is the answer

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input from {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        password_policies.append(PasswordPolicy(in_string))

for password in password_policies:
    if password.valid():
        valid_password_count += 1

print(f'The number of valid passwords is {valid_password_count}\n')

