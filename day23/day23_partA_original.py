# adventOfCode 2020 day 23 (Part A)
# https://adventofcode.com/2020/day/23

class CupCircle:
    def __init__(self, in_string):
        self._cups = []
        self._pickedup = []
        for ch in in_string:
            self._cups.append(int(ch))
        self._current_cup_value = self._cups[0]

    def display_cups(self):
        cup_str = 'cups: '
        for cup in self._cups:
            if cup == self._current_cup_value:
                cup_str += '(' + str(cup) + ') '
            else:
                cup_str += str(cup) + ' '
        print(cup_str)

    def pickup_three_cups(self):
        while len(self._pickedup) < 3:
            pickup_index = self._cups.index(self._current_cup_value) + 1
            if pickup_index >= len(self._cups):
                pickup_index -= len(self._cups)
            self._pickedup.append(self._cups.pop(pickup_index))

    def putdown_three_cups(self, destination_value):
        # determine destination_index from destination_value
        destination_index = self._cups.index(destination_value) + 1
        if destination_index >= len(self._cups):
            destination_index -= len(self._cups)
        while len(self._pickedup) > 0:
            self._cups.insert(destination_index, self._pickedup.pop())
            dummy = 123
        dummy = 123

        if destination_index < self._cups.index(self._current_cup_value):
            # need to shuffle three digits
            for i in range(3):
                self._cups.append(self._cups.pop(0))

    def display_pickedup(self):
        print('pick up: ', end='')
        for i in range(len(self._pickedup)):
            print(self._pickedup[i], end= ', ')
        print()

    def select_destination(self):
        # Initialize destination_value to the current value
        destination_value = self._current_cup_value
        while True:
            destination_value -= 1
            if destination_value in self._pickedup:
                continue
            # below command is an implicit else clause
            if destination_value not in self._cups:
                destination_value = max(self._cups)
            return destination_value

        dummy = 123

    def select_new_current_cup(self):
        index_current_cup = self._cups.index(self._current_cup_value)
        index_current_cup += 1
        if index_current_cup == len(self._cups):
            index_current_cup += 0
        
        self._current_cup_value = self._cups[index_current_cup]

    def do_move(self, i):
        print(f'-- move {i} --') # for debugging only
        self.display_cups() # for debugging only
        self.pickup_three_cups()
        self.display_pickedup()

        destination_value = self.select_destination()
        print(f'destination: {destination_value}') # for debugging only

        self.putdown_three_cups(destination_value)
        print() # for debugging only
        self.select_new_current_cup()

# Reading input from the input file
input_filename='input_sample1.txt'
# input_filename='input.txt'
print(f'Using input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
   
# Parsing input file   
cup_circle = CupCircle(in_string)

for i in range(1,101):
    cup_circle.do_move(i)

print('-- final --')
cup_circle.display_cups()
print()

# Construct part A output
partA_output = ''
index_partA_output = cup_circle._cups.index(1)
while len(partA_output) < len(cup_circle._cups) - 1:
    index_partA_output += 1
    if index_partA_output == len(cup_circle._cups):
        index_partA_output = 0
    partA_output += str(cup_circle._cups[index_partA_output])
    dummy = 123

print(f'The output for part A is {partA_output}\n')

