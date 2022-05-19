# adventOfCode 2020 day 14
# https://adventofcode.com/2020/day/14

import copy

mask_current = None
memory = {}

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()

        # Parse input line for a mask
        if 'mask' in in_string:
            mask_current = in_string[7:]        
            floating_bits = set()
        
        # Parse input line for a pair consisting of memory address and value
        else:
            in_string = in_string[4:]
            address, value = (int(x) for x in in_string.split('] = '))

            # Convert address to list of characters, where each char is a bit
            address_bits = list(format(address, "b").zfill(36))

            # Traverse bitmask
            for i in range(len(mask_current)):
                # Any '1' bits in the mask become a one in the address
                if mask_current[i] == '1':
                    address_bits[i] = mask_current[i]
                # Any 'X' bits in the mask are added to a list of indices of what I have labelled "floating bits"
                elif mask_current[i] == 'X':
                    floating_bits.add(i)

            # Create a list with one of the resulting masks (where the 'X' bits will be whichever bit started wtih)
            address_list = [address_bits]

            # Loop through the list of indices of where 'X' is in the mask
            for bit in floating_bits:
                # Make duplicates of everything in address_list, and then flip the i-th bit in each duplicate
                new_address_list = []
                for address_bits in address_list:
                    new_address_bits = copy.deepcopy(address_bits)
                    new_address_bits[bit] = '1' if new_address_bits[bit] == '0' else '0'
                    new_address_list.append(new_address_bits)

                # Add the addresses with i-th bit flipped to address_list
                # (In the next iteration of the bit for loop these addresses will have 
                # duplicates created and have another bit flipped)
                for new_address_bits in new_address_list:
                    address_list.append(new_address_bits)

            # write value to all memory addresses
            for address in address_list:
                address = int(''.join(address), 2)
                memory[address] = value

print(f'The answer to part B is {sum(memory.values())}')

