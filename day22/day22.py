# adventOfCode 2020 day 22
# https://adventofcode.com/202-/day/22

player_id = None
decks_of_cards = dict() # ID: player_id, value: list of cards (int values)

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'Using input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            continue
        if in_string[0] == 'P':
            dummy, player_id_string = in_string.split()
            player_id = int(player_id_string[:-1])
            print(f'This is player # {player_id_string}')
            decks_of_cards[player_id] = []
        else:
            card_value = int(in_string)
            print(f'Card for player # {player_id} ...... {card_value}')
            decks_of_cards[player_id].append(card_value)


