# adventOfCode 2020 day 25
# https://adventofcode.com/202-/day/25

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}\n')
with open(input_filename) as f:
    public_key_1 = int(f.readline().rstrip())
    public_key_2 = int(f.readline().rstrip())

for loop_size_seeker in range(1,16):
    value = 1
    for i in range(loop_size_seeker):
        value *= 7 # mult. by "subject number"
        value = value % 20201227
    
    # Test if loop size is discovered
    if value in [public_key_1, public_key_2]:
        print(f'{loop_size_seeker}:  {value}')

dummy = 123


