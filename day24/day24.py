
# adventOfCode 2020 day 24
# https://adventofcode.com/2020/day/24

tile_coords_and_count = dict()
compass_directions = {'e':[1,0], 'w':[-1,0], 'n':[0,1], 's':[0,-1]}
# Reading input from the input file
input_filename='input_sample2.txt'
print(f'Using input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        in_string_list = list(in_string)
        tile_coords = [0,0]
        while len(in_string_list) > 0:
            steps = []
            steps.append(in_string_list.pop(0))
            if steps[0] in ['n', 's']:
                steps.append(in_string_list.pop(0))
            for component in steps:
                for index in range(len(tile_coords)):
                    tile_coords[index] += compass_directions[component][index] * 2 / len(steps)
                dummy = 123
                # tile_coords += compass_directions[component] * 2 / len(steps)
                # tile_coords = [tile_coords + compass_directions[x] * 2 / len(steps) for x in component]
            dummy = 123
        tile_coords_tuple = tuple(tile_coords)
        if tile_coords_tuple in tile_coords_and_count:
            tile_coords_and_count[tile_coords_tuple] += 1
        else:
            tile_coords_and_count[tile_coords_tuple] = 1

dummy = 123

