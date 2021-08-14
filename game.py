from ai import AI
from human import Human

human_player_1 = Human('Player 1')
human_player_2 = Human('Player 2')
computer_player_1 = AI('computer 1')

class Game:

    def __init__(self):
        self.add_player

        
    

    def run_game(self):
        print("welcome to the game")
        

    def add_player(self):
        # human_player_1 = Human('Player 1')
        print(f"Hello, {human_player_1.name}.")
        # human_player_1.choose_gesture
        # human_player_2 = Human('Player 2')
        print(f'Hello, {human_player_2.name}. ')
        # human_player_2.choose_gesture
        # computer_player_1 = AI('computer 1')
        print(f'Hello, {computer_player_1.name}. ')

     
    def choose_gesture(self):       
        gesture1 = human_player_1.geastures[0]
        gesture2 = human_player_1.geastures[1]
        gesture3 = human_player_1.geastures[2]
        gesture4 = human_player_1.geastures[3]
        gesture5 = human_player_1.geastures[4]
        player_input = int(input('please choose a gesture'))
        if player_input == 1:
            print(f'{gesture1}')
        elif player_input == 2:
            print(gesture2)
        elif player_input == 3:
            print(gesture3) 
        elif player_input == 4:
            print(gesture4)
        elif player_input == 5:
            print(gesture5)


        

    
        

    

    
    
    
        
        
    
    
    
        





                
        
    
 













   

