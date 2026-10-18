from random import choice

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
QUIT_OPTIONS = ('q', 'quit')

PLAYER_MOVES = {
    'r': ROCK,
    'rock': ROCK,
    'p': PAPER,
    'paper': PAPER,
    's': SCISSORS,
    'scissors': SCISSORS
}

COMPUTER_MOVES = (ROCK, PAPER, SCISSORS)

WINNING_MOVES = {
    (ROCK, SCISSORS),
    (PAPER, ROCK),
    (SCISSORS, PAPER)
}


def get_player_move():
    while True:
        player_move = input('Choose [r]ock, [p]aper or [s]cissors or choose q for quit: ').strip().lower()

        if player_move in QUIT_OPTIONS:
            return None
        elif player_move in PLAYER_MOVES:
            return PLAYER_MOVES[player_move]

        print('Invalid input! Please try again.')


def get_result(player_m, computer_m):
    if player_m == computer_m:
        return 'Draw'
    elif (player_m, computer_m) in WINNING_MOVES:
        return 'You win'
    else:
        return 'You lose'


def main():
    while True:
        player_move = get_player_move()

        if player_move is None:
            print('Thank you for playing!')
            break

        computer_move = choice(COMPUTER_MOVES)
        print(f'The computer chose {computer_move}')

        print(get_result(player_move, computer_move))


if __name__ == '__main__':
    main()
