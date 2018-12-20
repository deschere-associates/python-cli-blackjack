# -*- coding: utf-8 -*-
"""

This module represents a players bankroll in a simple blackjack game

Todo:
	* make it work
"""

class Bankroll(object):
	"""
	Create a bankroll for a simple blackjack game
	
	Args:
		starting_amount (float) [default: 100]
		
	Methods:
		deposit (float) 	- amount to add to account, must be positive number
		withdrawal (float)	- amount to remove from account, must be positive number
		balance (float)		- amount in bankroll
	"""
	from decimal import getcontext
	from decimal import Decimal
	currency_indicator = "$"
	precision = 2
	
	def __init__(self,starting_amount=100):
		Bankroll.getcontext().prec = 2

		self.balance = starting_amount

	def __str__(self):
		return "$"+str(Bankroll.Decimal(self.balance))
		
	def withdrawal(self,amount):
		if amount > self.balance:
			raise ArithmeticError('Insufficient funds for withdrawal')
		
		self.balance -= amount
	
	def deposit(self,amount):
		if amount < 0:
			raise ArithmeticError('Can not deposit negative values')
			
		self.balance += amount
