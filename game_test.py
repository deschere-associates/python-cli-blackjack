from src.Card import Card
from src.Deck import Deck
from src.Bankroll import Bankroll
from src.Player import Player
from src.Gameboard import Gameboard
import unittest

class Testgame(unittest.TestCase):
	def test_random_card(self):
		rnd_card1 = Card()
		rnd_card2 = Card()

		self.assertNotEqual(rnd_card1,rnd_card2)

	def test_specific_card(self):
		face_value = 'A'
		facing = 'up'
		suit = 'clubs'
		ace_card = Card(face_value = face_value, facing = facing, suit = suit)
		
		self.assertEqual(face_value, ace_card.face_value)
		self.assertEqual(facing, ace_card.facing)
		self.assertEqual(suit, ace_card.suit)

	def test_card_kwargs(self):
		three_dia = Card(**{'suit':'diamonds','face_value':'3','facing':'up'})
		self.assertEqual('3', three_dia.face_value)
		self.assertEqual('up', three_dia.facing)
		self.assertEqual('diamonds', three_dia.suit)
		
	def test_deck(self):
		new_deck = Deck()

		self.assertEqual(52, new_deck.count())

	def test_deck_draw(self):
		new_deck = Deck()
		card_type = Card()
		
		self.assertIsInstance(new_deck.draw_card(),Card)
		self.assertEqual(51, new_deck.count())

	def test_deck_shuffle(self):
		new_deck = Deck()
		new_deck.shuffle()
		
		self.assertIsInstance(new_deck,Deck)
		
	def test_bankroll_def(self):
		bank = Bankroll()
		
		self.assertEqual(bank.balance,100)
		self.assertEqual(str(bank),'$100')

	def test_bankroll_withdrawal(self):
		bank = Bankroll()
		bank.withdrawal(50)
		
		self.assertEqual(bank.balance,50)
		self.assertRaises(ArithmeticError,bank.withdrawal,75)	
		
	def test_bankroll_deposit(self):
		bank = Bankroll()
		bank.deposit(75)
		
		self.assertEqual(bank.balance,175)
		self.assertRaises(ArithmeticError,bank.deposit,-1)
	
	def test_player(self):
		new_player = Player("Fred")
		
		self.assertIsInstance(new_player,Player)

	def test_player_withdrawal(self):
		new_player = Player("Bono")
		new_player.withdrawal(75)
		
		self.assertEqual('$25',new_player.balance())
		self.assertRaises(ArithmeticError,new_player.withdrawal,75)

	def test_gameboard(self):
		p1 = Player("Petey!")
		new_player = [p1]
		casino_name = 'Battle boat'
		dealer_hand = [Card(facing='up'),Card(facing='down')]
		p1.addCard(Card(facing='up'))
		p1.addCard(Card(facing='up'))
		
		new_gameboard = Gameboard(name=casino_name, players=new_player)
		new_gameboard.addDealerHand(dealer_hand)
		print(new_gameboard)
		
		self.assertEqual(True,True)

if __name__=='__main__':
	unittest.main()
