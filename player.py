class Player:
    def __init__(self,name):
        self.point= ""
        self.score= ""
        self.name = name
        self.geastures= ["rock","papr","scissors","lizrd","spock"] 
        
  
    def determine_winner(self):
        choices = self.geastures
    
        
        
        win = {
            choices[0]: [choices[2]], 
            choices[1]: [choices[0]], 
            choices[2]: [choices[1]],
            choices[0]: [choices[4]],
            choices[4]: [choices[5]],
            choices[4]: [choices[2]],
            choices[2]: [choices[3]],
            choices[3]: [choices[1]],
            choices[1]: [choices[4]],
            choices[4]: [choices[0]],
        }
        defeat = win[choices]
        pass

    

    

