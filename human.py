from player import Player
from random import randint

class Human(Player):
    def __init__(self,name):
        super().__init__(name)
        
        
    def choose_gesture(self):       
        gesture1 = self.geastures[0]
        gesture2 = self.geastures[1]
        gesture3 = self.geastures[2]
        gesture4 = self.geastures[3]
        gesture5 = self.geastures[4]
        player_input = int(input(f'please choose a gesture({self.geastures})'))
        if player_input == 1:
            print(f'{self.name} chose {gesture1}')
        elif player_input == 2:
            print(f'{self.name} chose {gesture2}')
        elif player_input == 3:
            print(f'{self.name} chose {gesture3}') 
        elif player_input == 4:
            print(f'{self.name} chose {gesture4}')
        elif player_input == 5:
            print(f'{self.name} chose {gesture5}')

    

       






        


            
        

