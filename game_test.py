
from unittest import result
from game import Game
import unittest

class GameTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

     # def tearDown(self) -> None:
    #     pass

    def test_P1_win(self):
        game = Game()
        p1_gesture="Rock"
        p2_gesture="Lizard" 

        result = game.choose_round_winner(p1_gesture,p2_gesture)
        self.assertEqual(result,"P1Wins!")

    def test_P2_win(self):
        game = Game()
        p1_gesture="Rock"
        p2_gesture="Paper" or "Spock"

        result = game.choose_round_winner(p1_gesture,p2_gesture)
        self.assertEqual(result,"P2Wins!")

    def test_Tie(self):
        game = Game()
        p1_gesture="Paper"
        p2_gesture="Paper" 

        result = game.choose_round_winner(p1_gesture,p2_gesture)
        self.assertEqual(result,"Tie!")
   

if __name__ == '__main__':
        unittest.main()