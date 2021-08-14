from player import Player
import random

class AI(Player):
    def __init__(self,name):
        super().__init__(name)

    def ai_gesture(self):
        print(f'{self.name} chose {random.choice(self.geastures)}')