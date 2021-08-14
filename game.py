from ai import AI
from human import Human


human_player_1 = Human('Player 1')
human_player_1    
human_player_2 = Human('Player 2')
human_player_2
computer_player_1 = AI('computer 1')
computer_player_1

class Game:

    def __init__(self):
        pass


    def run_game(self):
        print("welcome to Rock,Paper,Scisors...featuring Lizard and Spock!")

        print('this is a basic game of rock paper scissors,with a twist!')
        print('this version includes two extra choices')
        print('the controls are as follows:')
        print('1 is rock','2 is paper','3 is scissors','4 is lizard','5 is spock')


    def add_player(self):
        human_player_1 = Human('Player 1')
        print(f"Hello, {human_player_1.name}.")
        human_choice = human_player_1.choose_gesture()
        human_choice
        human_player_2 = Human('Player 2')
        human2_choice = human_player_2.choose_gesture()
        human2_choice
        computer_player_1 = AI('computer 1')
        print(f'Hello, {computer_player_1.name}. ')
        computer_player_1.ai_gesture()
        
    #     print(f'Hello, {human_player_2}. ')
    #creating the actual 1 v 1, where we pit one player against the other
    # we will establish which esture beats waht and how that will make the winner gain points
    #


    
    

    
        
        
    # print(f'Hello, {computer_player_1}. ')

        
        
    
        
    

    

    
    

    
    
    
        
        
    
    
    
        





                
        
    
















