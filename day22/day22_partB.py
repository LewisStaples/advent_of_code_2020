import copy
import sys

# This class tracks information about a given "game."
class Game:
    def __init__(self, decks):
        self._round_counter = 0
        self._set__decks_of_cards = set()
        if decks is None:
            # This assumes that there will always be players 1 and 2
            self._decks = {1: [], 2: []}
        else:
            # Note that decks has been copied from a prior Game object with copy.deepcopy()
            self._decks = decks

    # This handles inputting a card (from text in the input file)
    def card_input(self, player_id, card):
        self._decks[player_id].append(card)

    # This handles logic when either player has been determined to have won this round
    def record_win_for_round(self, winning_playerID, repeated_deck):
            # The winner gets both drawn cards (the winning card is added before the other one)
            self._decks[winning_playerID].append(max(self._player1card, self._player2card))
            self._decks[winning_playerID].append(min(self._player1card, self._player2card))
            # Use this to "label" this Game's round as completed
            self._player1card = self._player2card = None
            # Check whether to continue with another round in this game (two questions)
            # Q.1 Does the losing player have cards remaining?
            losing_playerID = 1 if winning_playerID == 2 else 2
            if len(self._decks[losing_playerID]) != 0:
                # Q.2 Is this a new deck? (is it not a repeat?)
                if not repeated_deck:
                    # Continue with another round in this game
                    return 0
            # If above return doesn't happen, then there's a winner for this game
            if len(game_list) == 1:
                ans_B = 0
                while len(game_list[-1]._decks[winning_playerID]) > 0:
                    ans_B += len(game_list[-1]._decks[winning_playerID]) * game_list[-1]._decks[winning_playerID].pop(0)
                print(f'The answer to part B is: {ans_B}\n')
                sys.exit('The end')
            game_list.pop()
            return winning_playerID

    def do_round_forward(self):
        self._round_counter += 1
        # Store the current deck states
        self._set__decks_of_cards.add(
            (
                tuple(self._decks[1]),
                tuple(self._decks[2])
            )
        )
        # Each player draws a card
        self._player1card = self._decks[1].pop(0)
        self._player2card = self._decks[2].pop(0)

        # Verify if the newest deck state was seen before ("repeat")
        # (If there are not repeats the set's length will equal the round_number,
        # whereas the first repeat will cause the length to be less than the round_number)
        if len(self._set__decks_of_cards) < self._round_counter:
            # Player 1 wins
            return self.record_win_for_round(1, True)

        # See if a recursive game should be played
        if len(self._decks[1]) >= self._player1card:
            if len(self._decks[2]) >= self._player2card:
                # Create new game
                game_list.append(Game(copy.deepcopy(self._decks)))
                # reduce number of cards .....
                del game_list[-1]._decks[1][self._player1card:]
                del game_list[-1]._decks[2][self._player2card:]
                # return, so the next round will start using the newest Game in game_list
                return 0

        # Play this round with the rules from part (a)
        if self._player1card > self._player2card:
            return self.record_win_for_round(1, False)
        else:
            return self.record_win_for_round(2, False)

    # This handles if a round is returned to from a "recursive" game
    def do_round_backward(self, last_round_result):
        # Add cards to deck based on winner of recursive game
        player_card = {
            1: self._player1card,
            2: self._player2card
        }
        losing_card = 1 if last_round_result == 2 else 2
        self._decks[last_round_result].append(player_card[last_round_result])
        self._decks[last_round_result].append(player_card[losing_card])

        # Then proceed to the next round

input_filename='input.txt'
game_list = [Game(None)]

# Reading input from the input file
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
        else:
            game_list[0].card_input(player_id, int(in_string))

last_round_result = 0
while len(game_list) > 0:
    if last_round_result == 0:
        last_round_result = game_list[-1].do_round_forward()
    else:
        game_list[-1].do_round_backward(last_round_result)
        last_round_result = 0
