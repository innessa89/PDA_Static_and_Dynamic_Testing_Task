import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_ace=Card("ace",1)
        self.card_king=Card("king",3)
        self.card_queen=Card("queen",2)
        self.cards=[self.card_king,self.card_ace]

        self.game=CardGame("Pocker")

    def test_check_for_ace(self):
        cardValue=self.game.check_for_ace(self.card_ace)
        self.assertEqual(True,cardValue)

    def test_check_for_king(self):
        cardValue=self.game.check_for_ace(self.card_king)
        self.assertEqual(False,cardValue)

    def test_check_the_highest_card(self):
        cardValue=self.game.highest_card(self.card_ace,self.card_king)
        self.assertEqual(self.card_king,cardValue)

    def test_card_total(self):
        cardValue=self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 4",cardValue)
