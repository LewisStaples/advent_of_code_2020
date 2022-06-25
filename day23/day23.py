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
        for i in range(3,0,-1):
            pickup_index = self._index_current_cup + i
            if pickup_index >= len(self._cups):
                pickup_index -= len(self._cups)
            self._pickedup.append(self._cups.pop(pickup_index))

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'Using input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
   
# Parsing input file   
# print(in_string)
cup_circle = CupCircle(in_string)

for i in range(1,2):
    print(f'-- move {i} --')
    cup_circle.display_cups()
    cup_circle.pickup_three_cups()
    cup_circle.display_cups()
    dummy = 123