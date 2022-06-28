# adventOfCode 2020 day 23 (Part A)
# https://adventofcode.com/2020/day/23

class CupCircle:
    def __init__(self, in_string):
        self._cups = dict()
        self._pickedup = []

        previous = None
        for ch in in_string:
            self._cups[previous] = int(ch)
            previous = self._cups[previous]
        
        self._cups[previous] = self._cups[None]
        self._cups.pop(None)
        self._current_cup_value = int(in_string[0])

    def display_cups(self):
        prev = self._current_cup_value
        cup_str = f'cups: ({prev}) '
        
        for i in range(8):
            if self._cups[prev] == self._current_cup_value:
                break

            cup_str += str(self._cups[prev]) + ' '
            prev = self._cups[prev]
        print(cup_str)

    def pickup_three_cups(self):
        while len(self._pickedup) < 3:
            self._pickedup.append(self._cups[self._current_cup_value])
            self._cups[self._current_cup_value] = self._cups[self._pickedup[-1]]
            self._cups.pop(self._pickedup[-1])
            dummy = 123

    def putdown_three_cups(self, destination_value):
        while len(self._pickedup) > 0:
            cup_to_put_down = self._pickedup.pop()
            self._cups[cup_to_put_down] = self._cups[destination_value]
            self._cups[destination_value] = cup_to_put_down

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

    def select_new_current_cup(self):
        self._current_cup_value = self._cups[self._current_cup_value]

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
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
print('Input string: ' + in_string + '\n')

# # Parsing input file   
cup_circle = CupCircle(in_string)

dummy = 123

for i in range(1,101):
    cup_circle.do_move(i)

print('-- final --')
cup_circle.display_cups()
print()

# Construct part A output
partA_output = ''
prev = 1
while True:
    new_cup = cup_circle._cups[prev]
    if new_cup == 1:
        break
    # implicit else:
    prev = new_cup
    partA_output += str(new_cup)
    
print(f'The output for part A is {partA_output}')
print(f'when using input file: {input_filename}\n')
