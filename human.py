from player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__(name)
        



        
    def choose_gesture(self):       
        gesture1 = self.geastures[0]
        gesture2 = self.geastures[1]
        gesture3 = self.geastures[2]
        gesture4 = self.geastures[3]
        gesture5 = self.geastures[4]
        player_input = input('please choose a gesture')
        f"{player_input}"
        if player_input == 1:
            print(gesture1)
        elif player_input == 2:
            print(gesture2)
        elif player_input == 3:
            print(gesture3) 
        elif player_input == 4:
            print(gesture4)
        elif player_input == 5:
            print(gesture5)



            
        

