import copy

class Game:
    next_gameID = 1

    def __init__(self, decks):
        self._gameID = Game.next_gameID
        Game.next_gameID += 1

        self._round_counter = 0
        self._set__decks_of_cards = set()
        # This assumes that there will always be players 1 and 2
        self._decks = {1: [], 2: []}
        

        if decks is not None:
            # note it's been copied with copy.deepcopy()
            self._decks = decks

            # modify the deep copy
            del self._decks[1][1+self._decks[1][0]:]
            del self._decks[2][1+self._decks[2][0]:]
            self._decks[1].pop(0)
            self._decks[2].pop(0)

            dummy = 123   

    def card_input(self, player_id, card):
        self._decks[player_id].append(card)

    def record_win(self, winning_playerID):
            self._decks[winning_playerID].append(self._player1card)
            self._decks[winning_playerID].append(self._player2card)

    def do_round(self):
        self._round_counter += 1
        print(f'-- Round {self._round_counter} (Game {self._gameID}) --')

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
            self.record_win(1)
            return

        # See if a recursive game should be played
        if len(self._decks[1]) > self._decks[1][0]:
            if len(self._decks[2]) > self._decks[2][0]:
                # Create cursive object
                Game(copy.deepcopy(self._decks))
                
                # return from do_round, so a new round will start using the newest copy
                return
                dummy = 123


        # If not using a recursive game, then play with the rules from part (a)
        if self._player1card > self._player2card:
            self.record_win(1)
        else:
            self.record_win(2)
            # self._decks[1].append(self._player1card)
            # self._decks[1].append(self._player2card)

game_list = [Game(None)]

# Reading input from the input file
input_filename='input_sample0.txt'
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

while len(game_list) > 0:
    game_list[-1].do_round()
    # break



