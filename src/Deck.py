# -*- coding: utf-8 -*-
"""

This module represents a deck of cards in a simple blackjack game

Todo:
	* make it work
"""

class Deck(object):
	"""
	Create a deck of cards for a simple blackjack game.  The cards do not start shuffled
	
	Args:
		None
		
	Methods:
		shuffle():
			refills the deck and shuffles the order of the cards
			
		pop():
			returns the top card
			RETURN: Card
			
		remaining():
			returns the number of cards remaining in the deck
			RETURN: int
	"""
	num_cards = 52
	base_setup = {'suit':('clubs','diamonds','hearts','spades'),'face_value':('A','2','3','4','5','6','7','8','9','10','J','Q','K')}
	card_meta = (
		{'suit':'clubs','face_value':'A'},
		{'suit':'clubs','face_value':'2'},
		{'suit':'clubs','face_value':'3'},
		{'suit':'clubs','face_value':'4'},
		{'suit':'clubs','face_value':'5'},
		{'suit':'clubs','face_value':'6'},
		{'suit':'clubs','face_value':'7'},
		{'suit':'clubs','face_value':'8'},
		{'suit':'clubs','face_value':'9'},
		{'suit':'clubs','face_value':'10'},
		{'suit':'clubs','face_value':'J'},
		{'suit':'clubs','face_value':'Q'},
		{'suit':'clubs','face_value':'K'},
		{'suit':'diamonds','face_value':'A'},
		{'suit':'diamonds','face_value':'2'},
		{'suit':'diamonds','face_value':'3'},
		{'suit':'diamonds','face_value':'4'},
		{'suit':'diamonds','face_value':'5'},
		{'suit':'diamonds','face_value':'6'},
		{'suit':'diamonds','face_value':'7'},
		{'suit':'diamonds','face_value':'8'},
		{'suit':'diamonds','face_value':'9'},
		{'suit':'diamonds','face_value':'10'},
		{'suit':'diamonds','face_value':'J'},
		{'suit':'diamonds','face_value':'Q'},
		{'suit':'diamonds','face_value':'K'},
		{'suit':'hearts','face_value':'A'},
		{'suit':'hearts','face_value':'2'},
		{'suit':'hearts','face_value':'3'},
		{'suit':'hearts','face_value':'4'},
		{'suit':'hearts','face_value':'5'},
		{'suit':'hearts','face_value':'6'},
		{'suit':'hearts','face_value':'7'},
		{'suit':'hearts','face_value':'8'},
		{'suit':'hearts','face_value':'9'},
		{'suit':'hearts','face_value':'10'},
		{'suit':'hearts','face_value':'J'},
		{'suit':'hearts','face_value':'Q'},
		{'suit':'hearts','face_value':'K'},
		{'suit':'spades','face_value':'A'},
		{'suit':'spades','face_value':'2'},
		{'suit':'spades','face_value':'3'},
		{'suit':'spades','face_value':'4'},
		{'suit':'spades','face_value':'5'},
		{'suit':'spades','face_value':'6'},
		{'suit':'spades','face_value':'7'},
		{'suit':'spades','face_value':'8'},
		{'suit':'spades','face_value':'9'},
		{'suit':'spades','face_value':'10'},
		{'suit':'spades','face_value':'J'},
		{'suit':'spades','face_value':'Q'},
		{'suit':'spades','face_value':'K'},
	)
	
	def __init__(self):
		from src.Card import Card
		self.card_deck = []
		iter = 0
	
		# build the deck
		for x in Deck.card_meta:
			self.card_deck.append({'card_id':iter,'card':Card(facing='up',**x)})
			
	def __str__(self):
		output = ''
		
		for x in self.card_deck:
			x['card'].setFacing('up')
			output += str(x['card']) + '\n'

		return output

	def shuffle(self):
		from random import shuffle
		
		shuffle(self.card_deck)
		
	def draw_card(self):
		try:
			return self.card_deck.pop()['card']
		except IndexError:
			return 'x'
			
	def count(self):
		return len(self.card_deck) 