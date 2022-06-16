# adventOfCode 2020 day 22
# https://adventofcode.com/202-/day/22

round_number = 0 # Testing only
player_id = None
decks_of_cards = dict() # ID: player_id, value: list of cards (int values)

set__decks_of_cards = set() # Note that the deck_of_cards in this set are a different datatype than the above dict

def continue_playing():
    for deck in decks_of_cards.values():
        if len(deck) == 0:
            return False
    return True

# Reading input from the input file
input_filename='input_scenario0_repeat_round.txt'
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

    round_number += 1 # Testing only
    print(f'-- Round {round_number} --') # Testing only

    # Store the current deck states
    set__decks_of_cards.add(
        (
            tuple(decks_of_cards[1]),
            tuple(decks_of_cards[2])
        )
    )

    # Verify if the newest deck state was seen before ("repeat")
    # (If there are not repeats the set's length will equal the round_number,
    # whereas the first repeat will cause the length to be less than the round_number)
    if len(set__decks_of_cards) < round_number:
        # Player 1 wins
        decks_of_cards[1].append(cards_this_round.pop(1))
        decks_of_cards[1].append(cards_this_round.pop(2))
        break
    # Draw cards
    cards_this_round = {}
    for player_id in decks_of_cards:
        print(f"Player {player_id}'s deck: {decks_of_cards[player_id]}") # Testing only
        cards_this_round[player_id] = decks_of_cards[player_id].pop(0)

    for player_id in decks_of_cards: # Testing only
        print(f'Player {player_id} plays: {cards_this_round[player_id]}') # Testing only
    # Determine the winning card
    winning_card = max(cards_this_round.values())

    # Determine the player_id of the winner
    winner_player_id = None
    for player_id in cards_this_round:
        if winning_card == cards_this_round[player_id]:
            # The winner has been found
            print(f'Player {player_id} wins the round!') # Testing only
            break

    decks_of_cards[player_id].append(cards_this_round.pop(player_id))
    decks_of_cards[player_id].append(cards_this_round.popitem()[1])

ans_A = 0
while len(decks_of_cards[player_id]) > 0:
    ans_A += len(decks_of_cards[player_id]) * decks_of_cards[player_id].pop(0)
dummy = 123

print(f'The answer to part A is: {ans_A}\n')
