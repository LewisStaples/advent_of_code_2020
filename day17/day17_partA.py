# adventOfCode 2020 day 17, part Alatest_state
# https://adventofcode.com/2020/day/17

number_of_cycles = 6
state_cycleNum = []
cubes_to_evaluate = set()

# Determine next cube state by counting active neighbors and then using rules from spec.
def determine_next_cube_state(x,y,z):
    # Count number of active neighbors (stop counting if four is reached)
    number_active_neighbors = 0
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            for c in range(z-1, z+2):
                if (a,b,c) == (x,y,z):
                    # Not a neighbor ... it's itself
                    continue
                if (a,b,c) in state_cycleNum[i1]:
                    number_active_neighbors += 1
                if number_active_neighbors > 3:
                    # Since count has reached four, this cube can't be active in the next state
                    return
    
    # Use active neighbor count and current cube state to determine next cube state
    if (x,y,z) in state_cycleNum[i1]:  # If cube active
        if number_active_neighbors in [2,3]: # If 2 or 3 neighbors
            state_cycleNum[i1+1].add((x,y,z))

    else: # If cube inactive
        if number_active_neighbors == 3: # If 3 neighbors
            state_cycleNum[i1+1].add((x,y,z))

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    initial_state = []
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        in_string = in_string.rstrip()
        initial_state.extend([ (a + number_of_cycles , number_of_cycles + len(in_string) - line_num - 1, number_of_cycles) for a in range(len(in_string)) if in_string[a] == '#' ])
    state_cycleNum.append(set(initial_state))
    del initial_state

 # Loop through the number_of_cycles
for i1 in range(number_of_cycles):
    # Create a blank (i1+1)-th element
    state_cycleNum.append(set())

    # Loop through all active cubes in the prior state to create a list of cubes to try out in this new state
    # (It is anticipated that this is faster than visiting all cubes)
    for (x,y,z) in state_cycleNum[i1]:
        cubes_to_evaluate.update([(a,b,c) for a in range(x-1, x+2) for b in range(y-1, y+2) for c in range(z-1, z+2)])

    for (x,y,z) in cubes_to_evaluate:
        determine_next_cube_state(x,y,z)

    print(f'Cycle #{i1+1}: {len(state_cycleNum[i1+1])}')

print(f'\nThe solution to part A is {len(state_cycleNum[i1+1])}\n')

