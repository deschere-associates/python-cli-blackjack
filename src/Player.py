# -*- coding: utf-8 -*-
"""

This module represents a players in a simple blackjack game

Todo:
	* make it work
"""

class Player(object):
	"""
	Create a player for a simple blackjack game
	
	Args:
		name (str) - players name
		starting_bank (float) [default: 100] - starting bank balance
		
	Methods:
		deposit (float) 	- amount to add to account, must be positive number
		withdrawal (float)	- amount to remove from account, must be positive number
		balance (float)		- amount in bankroll
	"""
	
	def __init__(self,name,starting_bank=100):
		from src.Bankroll import Bankroll
		self.bank = Bankroll(starting_bank)
		self.name = name
		self.hand = []

	def __str__(self):
		return self.name
		
	def deposit(self,amount):
		try:
			self.bank.deposit(amount)
		except:
			raise
	
	def withdrawal(self,amount):
		try:
			self.bank.withdrawal(amount)
		except:
			raise

	def balance(self):
		return str(self.bank)

	def addCard(self,card):
		self.hand.append(card)
	
	def clearHand(self):
		self.hand = []
	
	def getHand(self):
		return self.hand