# adventOfCode 2020 day 14
# https://adventofcode.com/2020/day/14

import copy

mask_current = None
memory = {}

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()

        if 'mask' in in_string:
            mask_current = in_string[7:]        
            floating_bits = set()
        else:
            in_string = in_string[4:]
            address, value = (int(x) for x in in_string.split('] = '))

            # # convert value to list of characters, where each char is a bit
            # value_bits = list(format(value, "b").zfill(36))

            # convert address to list of characters, where each char is a bit
            address_bits = list(format(address, "b").zfill(36))

            # # # use bitmask to transform value_bits
            # for i in range(len(mask_current)):
            #     if mask_current[i] != 'X':
            #         value_bits[i] = mask_current[i]

            # traverse bitmask
            for i in range(len(mask_current)):
                if mask_current[i] == '1':
                    address_bits[i] = mask_current[i]
                elif mask_current[i] == 'X':
                    floating_bits.add(i)

            address_list = [address_bits]
            for bit in floating_bits:
                new_address_list = []
                for address_bits in address_list:
                    new_address_bits = copy.deepcopy(address_bits)
                    new_address_bits[bit] = '1' if new_address_bits[bit] == '0' else '0'
                    new_address_list.append(new_address_bits)
                    dummy = 123

                for new_address_bits in new_address_list:
                    address_list.append(new_address_bits)
                    dummy = 123

            # # write value to memory address
            # memory[address] = value

            # write value to all memory addresses
            for address in address_list:
                address = int(''.join(address), 2)
                memory[address] = value
                dummy = 123

print(f'The answer to part B is {sum(memory.values())}')

