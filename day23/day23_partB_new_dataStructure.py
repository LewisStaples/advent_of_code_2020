# adventOfCode 2020 day 23 (Part B)
# https://adventofcode.com/2020/day/23

class CupCircle:
    def __init__(self, in_string):

        # self.LAST_VALUE IS WHATEVER THE HIGHEST NUMBERED CUP WILL BE
        # self.LAST_VALUE = 15
        self.LAST_VALUE = 1000000
        self._cups = dict()
        self._pickedup = []

        # Create cups from in_string:
        previous = self.LAST_VALUE
        for ch in in_string:
            self._cups[previous] = int(ch)
            previous = self._cups[previous]

        # Fill in the remaining cups
        first_auto_cup = max(self._cups.values()) + 1
        last_auto_cup = min(self._cups) + self.LAST_VALUE - 1

        self._cups[previous] = len(in_string) + 1
        previous = self._cups[previous]

        for i in range(first_auto_cup + 1, last_auto_cup + 1):
            self._cups[previous] = previous + 1
            previous += 1
            dummy = 123

        self._current_cup_value = int(in_string[0])
        self._cups['MAX'] = self.LAST_VALUE

    # Revising to accomodate display at end for testing part B
    # Display the two cups "clockwise" of cup 1 at the end
    def display_cups(self):

        print('Cups that are clockwise of cup 1:')
        FirstCup = self._cups[1]
        SecondCup = self._cups[FirstCup]
        print(f'FirstCup: {FirstCup}')
        print(f'SecondCup: {SecondCup}')
        print(f'Product of both above (answer to part B) is {FirstCup*SecondCup}')

    # Revising for only 1 or 2 digit cup labels
    def display_cups_max_two_digits(self):
        prev = self._current_cup_value
        # cup_str = f'cups: ({prev}) '
        cup_str = 'cups: ('
        if prev < 10:
            cup_str += ' '
        cup_str += f'{prev}) '
        
        # for i in range(8):
        # while prev != self.LAST_VALUE:
        # while prev != self._current_cup_value:
        # while True:
        # while self._cups[prev] != self._current_cup_value:
        
        for i in range(16):
            if self._cups[prev] == self._current_cup_value:
                break
            if self._cups[prev] < 10:
                cup_str += ' '
            cup_str += str(self._cups[prev]) + ' '
            prev = self._cups[prev]
        print(cup_str)
        dummy = 123

    def pickup_three_cups(self):
        while len(self._pickedup) < 3:
            self._pickedup.append(self._cups[self._current_cup_value])
            self._cups[self._current_cup_value] = self._cups[self._pickedup[-1]]
            self._cups.pop(self._pickedup[-1])
            dummy = 123
        while self._cups['MAX'] in self._pickedup:
            self._cups['MAX'] -= 1
            
    def putdown_three_cups(self, destination_value):
        while len(self._pickedup) > 0:
            cup_to_put_down = self._pickedup.pop()
            self._cups[cup_to_put_down] = self._cups[destination_value]
            self._cups[destination_value] = cup_to_put_down
        self._cups['MAX'] = self.LAST_VALUE

    def display_pickedup(self):
        print('pick up: ', end='')
        for i in range(len(self._pickedup)):
            print(self._pickedup[i], end= ', ')
        print()
        dummy = 123

    def select_destination(self):
        # Initialize destination_value to the current value
        destination_value = self._current_cup_value
        while True:
            destination_value -= 1
            if destination_value in self._pickedup:
                continue
            # below command is an implicit else clause
            if destination_value not in self._cups:
                # destination_value = max(self._cups)
                destination_value = self._cups['MAX']
            return destination_value

    def select_new_current_cup(self):
        self._current_cup_value = self._cups[self._current_cup_value]

    def do_move(self, i):
        # print(f'-- move {i} --') # for debugging only
        # self.display_cups() # for debugging only
        self.pickup_three_cups()
        # self.display_pickedup() # for debugging only

        # self.display_cups() # for debugging only

        destination_value = self.select_destination()
        # print(f'destination: {destination_value}') # for debugging only

        self.putdown_three_cups(destination_value)
        # print() # for debugging only
        self.select_new_current_cup()

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
print('Input string: ' + in_string + '\n')

# # Parsing input file   
cup_circle = CupCircle(in_string)

dummy = 123

for i in range(1,10000000):
    cup_circle.do_move(i)

print('-- final --')
cup_circle.display_cups()
print()

# # Construct part A output
# partA_output = ''
# prev = 1
# while True:
#     new_cup = cup_circle._cups[prev]
#     if new_cup == 1:
#         break
#     # implicit else:
#     prev = new_cup
#     partA_output += str(new_cup)
    
# print(f'The output for part A is {partA_output}')
# print(f'when using input file: {input_filename}\n')
