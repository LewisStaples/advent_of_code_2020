# adventOfCode 2020 day 22
# https://adventofcode.com/202-/day/22

player_id = None
decks_of_cards = dict() # ID: player_id, value: list of cards (int values)

def continue_playing():
    for deck in decks_of_cards.values():
        if len(deck) == 0:
            return False
    return True

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            continue
        if in_string[0] == 'P':
            dummy, player_id_string = in_string.split()
            player_id = int(player_id_string[:-1])
            decks_of_cards[player_id] = []
        else:
            card_value = int(in_string)
            decks_of_cards[player_id].append(card_value)

while continue_playing():
    # Draw cards
    cards_this_round = {}
    for player_id in decks_of_cards:
        cards_this_round[player_id] = decks_of_cards[player_id].pop(0)

    # Determine the winning card
    winning_card = max(cards_this_round.values())

    # Determine the player_id of the winner
    winner_player_id = None
    for player_id in cards_this_round:
        if winning_card == cards_this_round[player_id]:
            # The winner has been found
            break

    decks_of_cards[player_id].append(cards_this_round.pop(player_id))
    decks_of_cards[player_id].append(cards_this_round.popitem()[1])

ans_A = 0
while len(decks_of_cards[player_id]) > 0:
    ans_A += len(decks_of_cards[player_id]) * decks_of_cards[player_id].pop(0)
dummy = 123

print(f'The answer to part A is: {ans_A}\n')
