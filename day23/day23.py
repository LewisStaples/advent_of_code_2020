# adventOfCode 2020 day 23 (Part A)
# https://adventofcode.com/2020/day/23

class CupCircle:
    def __init__(self, in_string):
        self._index_current_cup = 0
        self._cups = []
        self._pickedup = []
        for ch in in_string:
            self._cups.append(int(ch))

    def display_cups(self):
        cup_str = 'cups: '
        for i, cup in enumerate(self._cups):
            if i == self._index_current_cup:
                cup_str += '(' + str(cup) + ') '
            else:
                cup_str += str(cup) + ' '
        print(cup_str)

    def pickup_three_cups(self):
        indices_to_pickup = []
        for i in range(3,0,-1):
            pickup_index = self._index_current_cup + i
            if pickup_index >= len(self._cups):
                pickup_index -= len(self._cups)
            # self._pickedup.append(self._cups.pop(pickup_index))
            indices_to_pickup.append(pickup_index)
        
        indices_to_pickup.sort(reverse=True)

        for pickup_index in indices_to_pickup:
            self._pickedup.append(self._cups.pop(pickup_index))
        dummy = 123

    def putdown_three_cups(self, destination_value):
        # determine destination_index from destination_value
        destination_index = self._cups.index(destination_value) + 1
        if destination_index > len(self._cups):
            destination_index -= len(self._cups)
        while len(self._pickedup) > 0:
            # self._pickedup.pop()
            self._cups.insert(destination_index, self._pickedup.pop(0))
            dummy = 123
        dummy = 123

        if destination_index < self._index_current_cup:
            # need to shuffle three digits
            for i in range(3):
                self._cups.append(self._cups.pop(0))

    def display_pickedup(self):
        # print(f'pick up: {self._pickedup}')
        print('pick up: ', end='')
        for i in range(len(self._pickedup)-1, -1, -1):
            print(self._pickedup[i], end= ', ')
        print()

    def select_destination(self):
        # Initialize destination_value to the current value
        destination_value = self._cups[self._index_current_cup]
        while True:
            destination_value -= 1
            if destination_value in self._pickedup:
                continue
            # below command is an implicit else clause
            if destination_value not in self._cups:
                destination_value = max(self._cups)
            # break
            return destination_value

        dummy = 123

    def select_new_current_cup(self):
        self._index_current_cup += 1
        if self._index_current_cup == len(self._cups):
            self._index_current_cup = 0

    def do_move(self, i):
        print(f'-- move {i} --') # for debugging only
        self.display_cups() # for debugging only
        self.pickup_three_cups()
        # self.display_cups() # for debugging only
        # print(f'pick up: {self._pickedup}') # for debugging only
        self.display_pickedup()

        destination_value = self.select_destination()
        print(f'destination: {destination_value}') # for debugging only

        self.putdown_three_cups(destination_value)
        print() # for debugging only
        self.select_new_current_cup()

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'Using input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
   
# Parsing input file   
# print(in_string)
cup_circle = CupCircle(in_string)

for i in range(1,11):
    cup_circle.do_move(i)
