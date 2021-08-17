from player import Player
from ai import AI
from human import Human
import random


human_player_1 = Human('Player 1')
    
# human_player_2 = Human('Player 2')
# human_player_2
computer_player_1 = AI('computer 1')
ai_choice = random.choice(computer_player_1.geastures)
human_choice = int(input(f'please choose a gesture({human_player_1.geastures})'))
gamerounds=0
humanwins=0
aiwins=0




class Game:
    def __init__(self):
        self.game_status = True
    def run_game(self):
        print("welcome to Rock,Paper,Scisors...featuring Lizard and Spock!")

        print('this is a basic game of rock paper scissors,with a twist!')
        print('this version includes two extra choices')
        print('the controls are as follows:')
        print('1 is rock','2 is paper','3 is scissors','4 is lizard','5 is spock')
    def add_player(self):
        print(f"Hello, {human_player_1.name}.")
        print(f'Hello, {computer_player_1.name}.')
       
    def choose_gesture(self,):       
        gesture1 = human_player_1.geastures[0]
        gesture2 = human_player_1.geastures[1]
        gesture3 = human_player_1.geastures[2]
        gesture4 = human_player_1.geastures[3]
        gesture5 = human_player_1.geastures[4]
     #    human_choice = int(input(f'please choose a gesture({human_player_1.geastures})'))
        if human_choice == 1:
            print(f'{human_player_1.name} chose {gesture1}')
        elif human_choice == 2:
            print(f'{human_player_1.name} chose {gesture2}')
        elif human_choice == 3:
            print(f'{human_player_1.name} chose {gesture3}') 
        elif human_choice == 4:
            print(f'{human_player_1.name} chose {gesture4}')
        elif human_choice == 5:
            print(f'{human_player_1.name} chose {gesture5}')
           
       
        
    def ai_choice(self):
          ai_choice
          print(f'{computer_player_1.name} chose {ai_choice} ')
          
        
        
        


        

    #     print(f'Hello, {human_player_2}. ')
    #creating the actual 1 v 1, where we pit one player against the other
    # we will establish which esture beats waht and how that will make the winner gain points
    #

   
              

    def choose_winner(self,):
     gamerounds=0
     ties=0
     humanwins=0
     aiwins=0
     while (aiwins < 3 or humanwins < 3):
     
      print(f'{computer_player_1.name} chose {ai_choice} ')
     if human_choice == 1 and ai_choice == computer_player_1.geastures[2]:
       humanwins += 1
       print(f'{human_player_1.name}' 'wins!')
     elif human_choice == 3 and ai_choice == computer_player_1.geastures[0]:
          aiwins += 1
          print("computer wins")
     elif human_choice == 2 and ai_choice == computer_player_1.geastures[0]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')
     elif human_choice == 1 and ai_choice == computer_player_1.geastures[1]:
          aiwins += 1
          print('computer wins')
     elif human_choice == 2 and ai_choice == computer_player_1.geastures[3]:
          aiwins += 1
          print('computer wins')  
     elif human_choice == 2 and ai_choice == computer_player_1.geastures[2]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')
     elif human_choice == 1 and ai_choice == computer_player_1.geastures[3]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')               
     elif human_choice == 4 and ai_choice == computer_player_1.geastures[1]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')
     elif human_choice == 4 and ai_choice == computer_player_1.geastures[4]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')
     elif human_choice == 3 and ai_choice == computer_player_1.geastures[4]:
          aiwins += 1
          print('computer wins')
     elif human_choice == 4 and ai_choice == computer_player_1.geastures[0]:
          aiwins += 1
          print('computer wins')
     elif human_choice == 4 and ai_choice == computer_player_1.geastures[3]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins!')
     elif human_choice == 5 and ai_choice == computer_player_1.geastures[0]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')    
     elif human_choice == 5 and ai_choice == computer_player_1.geastures[2]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')
     elif human_choice == 5 and ai_choice == computer_player_1.geastures[1]:
          aiwins += 1
          print('computer wins')
     elif human_choice == 4 and ai_choice == computer_player_1.geastures[2]:
          aiwins += 1
          print('computer wins')   
     elif human_choice == 2 and ai_choice == computer_player_1.geastures[4]:
          humanwins += 1
          print(f'{human_player_1.name}' 'wins')
     elif human_choice == 1 and ai_choice == computer_player_1.geastures[4]:
          aiwins += 1
          print('computer wins') 
     elif human_choice == ai_choice: 
          ties += 1 
          print('its a tie')
     print ("Wins: " + str(humanwins) + " " "Ties" +str(ties) + " " "Losses" + str(aiwins))
     gamerounds += 1
     
    def game_status(self):
        status = self.game_status
        while  (humanwins < 3 or aiwins < 3):
         status = True
        else: status = False
        return status      
          
     
      

       
     



     

       
       
       
       

        
            
        
            
       
        
    
        
    

    

    
    

    
    
    
        
        
    
    
    
        





                
        
    
















