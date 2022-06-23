import copy
import sys

class Game:
    next_gameID = 1

    def __init__(self, decks):
        self._gameID = Game.next_gameID

        print(f"=== Game {self._gameID} ===\n")
        Game.next_gameID += 1

        self._round_counter = 0
        self._set__decks_of_cards = set()

        if decks is None:
            # This assumes that there will always be players 1 and 2
            self._decks = {1: [], 2: []}
        
        if decks is not None:
        #     # note it's been copied with copy.deepcopy()
            self._decks = decks

        #     # modify the deep copy: consider only the number of cards needed
        #     del self._decks[1][1+self._decks[1][0]:]
        #     del self._decks[2][1+self._decks[2][0]:]
        #     # self._decks[1].pop(0)
        #     # self._decks[2].pop(0)

            dummy = 123   

    def card_input(self, player_id, card):
        self._decks[player_id].append(card)

    def record_win_for_round(self, winning_playerID):
            self._decks[winning_playerID].append(max(self._player1card, self._player2card))
            self._decks[winning_playerID].append(min(self._player1card, self._player2card))
            # Use this to "label" this Game's round as completed
            self._player1card = self._player2card = None

            # Output to match sample output
            print(f"Player {winning_playerID} wins the round!\n") # {self._round_counter} of game {self._gameID}!")

            # Check if this round's loser has lost this game
            losing_playerID = 1 if winning_playerID == 2 else 2
            if len(self._decks[losing_playerID]) != 0:
                return 0
            
            # There is a winner for this game
            print(f"The winner of game {self._gameID} is player {winning_playerID}!\n")
            game_list.pop()

            print(f"...anyway, back to game {game_list[-1]._gameID}")
            print(f"Player {winning_playerID} wins round {game_list[-1]._round_counter} of game {game_list[-1]._gameID}!")
            return winning_playerID

    def do_round_forward(self):
        # # Do these steps if it is a new round
        # if self._player1card is not None:

        self._round_counter += 1

        # if self._round_counter > 10:
        #     sys.exit('Counter value is too high: stopping to prevent infinite loop')
        # if self._gameID > 10:
        #     sys.exit('game_id value is too high: stopping to prevent infinite loop')
        # Output to match sample output
        print(f'-- Round {self._round_counter} (Game {self._gameID}) --')
        print(f"Player 1's deck: {self._decks[1]}")
        print(f"Player 2's deck: {self._decks[2]}")
        print(f"Player 1 plays: {self._decks[1][0]}")
        print(f"Player 2 plays: {self._decks[2][0]}")

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
            # self._decks[1].append(self._player1card)
            # self._decks[1].append(self._player2card)
            return self.record_win_for_round(1)
            # return

        # See if a recursive game should be played
        if len(self._decks[1]) >= self._player1card:
            if len(self._decks[2]) >= self._player2card:
                # Create new game (recursive)
                print('Playing a sub-game to determine the winner...\n')
                game_list.append(Game(copy.deepcopy(self._decks)))
                
                # Modify new game (make it look the same as a non-recursive game)
                # game_list[-1]._decks[1].insert(0, self._player1card)
                # game_list[-1]._decks[2].insert(0, self._player2card)
                # game_list[-1]._player1card = game_list[-1]._player2card = None

                # reduce number of cards .....
                del game_list[-1]._decks[1][self._player1card:]
                del game_list[-1]._decks[2][self._player2card:]

        #     del self._decks[1][1+self._decks[1][0]:]
        #     del self._decks[2][1+self._decks[2][0]:]

                # return from do_round, so a new round will start using the newest copy
                return 0

        # If not using a recursive game, then play with the rules from part (a)
        if self._player1card > self._player2card:
            return self.record_win_for_round(1)
        else:
            return self.record_win_for_round(2)

    def do_round_backward(self, last_round_result):
        dummy = 123

        player_card = {
            1: self._player1card,
            2: self._player2card
        }

        losing_card = 1 if last_round_result == 2 else 2

        self._decks[last_round_result].append(player_card[last_round_result])
        self._decks[last_round_result].append(player_card[losing_card])

input_filename='input_sample0.txt'

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
    # if game_list[-1]._player1card is None:
    if last_round_result == 0:
        last_round_result = game_list[-1].do_round_forward()
        dummy = 123
    else:
        game_list[-1].do_round_backward(last_round_result)
        last_round_result = 0



