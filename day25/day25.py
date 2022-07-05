# adventOfCode 2020 day 25
# https://adventofcode.com/202-/day/25

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}\n')
public_keys = []
with open(input_filename) as f:
    for i in range(2):
        public_keys.append(int(f.readline().rstrip()))

value = 1
loop_size_seeker = 0
while True:
    loop_size_seeker += 1
    value *= 7 # mult. by "subject number"
    value %= 20201227
    
    # Test if loop size is discovered
    if value in public_keys:
        break

# print(f'loop_size found: {loop_size_seeker}:  {value}')

public_keys.remove(value)
encryption_key = 1
for i in range(loop_size_seeker):
    encryption_key *= public_keys[0] # mult. by "subject number"
    encryption_key %= 20201227

print(f'Encryption key (answer to Day25, part A): {encryption_key}\n')


