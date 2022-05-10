# adventOfCode 2020 day 11, Part B
# https://adventofcode.com/2020/day/11

import enum

class SeatType(enum.Enum):
    FLOOR = 0
    EMPTY = 1
    OCCUPIED = 2
    OUT_OF_BOUNDS = 3

seat_type = {'.': SeatType.FLOOR, 'L': SeatType.EMPTY, '#': SeatType.OCCUPIED}

class SeatStatus:
    def __init__(self, seat_status):
        self.seat_status = seat_status
        self.coords_to_change = []

    def get_seat_type(self, i, j):
        if i<0 or j<0 or i >= len(self.seat_status) or j >= len(self.seat_status[i]):
            return SeatType.OUT_OF_BOUNDS
        return seat_type[self.seat_status[i][j]]

    def count_visible_occ(self, i, j):
        ret_val = 0
        for (par1, par2) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            n = 0
            while True:
                n += 1
                this_seat_type = self.get_seat_type(i + n * par1, j + n * par2)
                if this_seat_type != SeatType.FLOOR:
                    break
            if this_seat_type == SeatType.OCCUPIED:
                ret_val += 1
        return ret_val

    def update_seat(self, i, j):
        num_count_visible_occ = self.count_visible_occ(i,j)
        if self.seat_status[i][j] == 'L':
            if num_count_visible_occ == 0:
                self.coords_to_change.append((i,j))
        elif self.seat_status[i][j] == '#':
            if num_count_visible_occ >= 5:
                self.coords_to_change.append((i,j))

    # Return True if at least one change was made, else return False    
    def next_round(self):
        self.coords_to_change.clear()
        for i in range(len(self.seat_status)):
            for j in range(len(self.seat_status[i])):
                self.update_seat(i,j)

        # flip any seats that should be updated
        for (i,j) in self.coords_to_change:
            if self.seat_status[i][j] == '#':
                self.seat_status[i][j] = 'L'
            else:
                self.seat_status[i][j] = '#'
        return (len(self.coords_to_change) > 0)

    def print(self):
        for i in range(len(self.seat_status)):
            for j in range(len(self.seat_status[i])):
                print(self.seat_status[i][j], end='')
            print()
        print()

    def count_all_occupied(self):
        ret_val = 0
        for i in range(len(self.seat_status)):
            for j in range(len(self.seat_status[i])):
                if self.seat_status[i][j] == '#':
                    ret_val += 1
        return ret_val

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    seat_status = []
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        seat_status.append(list(in_string))
    seat_status = SeatStatus(seat_status)
to_continue = True
while to_continue:
    to_continue = seat_status.next_round()

print(f'The answer to Part A is {seat_status.count_all_occupied()}')

