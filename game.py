from ai import AI
from human import Human





class Game:
    def __init__(self):
        self.player_one="player_one"
        self.player_two="player_two"
        pass

    def run_game(self):
        print("welcome to the game")
        pass

    def add_player(self):
        human_player_1 = Human('Player 1')
        print(f"Hello, {human_player_1.name}.")
        human_player_2 = Human('Player 2')
        print(f'Hello, {human_player_2.name}. ')
        computer_player_1 = AI('computer 1')
        print(f'Hello, {computer_player_1.name}. ')
        # computer_player_2 = AI('computer 2')













   

