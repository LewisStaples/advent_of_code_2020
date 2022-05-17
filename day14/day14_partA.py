# adventOfCode 2020 day 14
# https://adventofcode.com/2020/day/14

mask_current = None
memory = {}

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()

        if 'mask' in in_string:
            mask_current = in_string[7:]        
        else:
            in_string = in_string[4:]
            address, value = (int(x) for x in in_string.split('] = '))

            # convert value to list of characters, where each char is a bit
            value_bits = list(format(value, "b").zfill(36))

            # # use bitmask to transform value_bits
            for i in range(len(mask_current)):
                if mask_current[i] != 'X':
                    value_bits[i] = mask_current[i]

            # convert transformed value_bits back to an int
            value = int(''.join(value_bits), 2)

            # write value to memory address
            memory[address] = value

print(f'The answer to part A is {sum(memory.values())}')

