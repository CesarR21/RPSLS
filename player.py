class Player:
    def __init__(self,name):
        self.point= ""
        self.score= ""
        self.name = name
        self.geastures= ["rock","papr","scissors","lizrd","spock"] 
        self.outcomes = {
            "rock":{"rock":"draw","paper":"loss","scissors":"win","lizard":"win","spock":"loss"},
            "paper":{"rock":"loss","paper":"draw","scissors":"loss","lizard":"loss","spock":"win"},
            "scissors":{"rock":"loss","paper":"win","scissors":"draw","lizard":"win","spock":"loss"},
            "lizard": {"rock":"loss","paper":"win","scissors":"loss","lizard":"draw","spock":"win"},
            "spock":{"rock":"win","paper":"loss","scissors":"win","lizard":"loss","spock":"draw"}
         
    }

    

    

