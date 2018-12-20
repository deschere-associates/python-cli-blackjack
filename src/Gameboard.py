# -*- coding: utf-8 -*-
"""

This module represents a gameboard in a simple blackjack game

Todo:
	* make it work
"""

class Gameboard(object):
	"""
	Create a gameboard for a simple blackjack game
	
	Args:
		name (str) - Casino name
		players (list of Player) - list of Player objects
		
	Methods:
		addPlayer (new_player Player) - add a new player to the board
		removePlayer (player Player) - remove a player from the game
		addDealerHand (cards Card[]) - list of dealers cards
		clearDealerHand () - clear the dealers hand
		
	"""
	def __init__(self,name,players=[]):
		self.casino_name = name
		self.player_list = players
		self.dealer_hand = []
		
	def __str__(self):
		card_len = 11
		multiplier = min((1,len(self.player_list)))
		border = '=0=0=0=0=0==0=0=0=0=0='*multiplier
		filler = '           '*multiplier
		cnlen = len(self.casino_name)
		if cnlen>(card_len*2)-1:
			cnlen = card_len*2
			
		dealer_head = (' ')*int(((card_len*2)-cnlen)/2) + self.casino_name + (' ')*int(((card_len*2)-cnlen)/2)
		o_dealer_hand = ''
		
		for i in self.dealer_hand:
				o_dealer_hand += str(i)
		
		player_head = ''
		player_balance = ''
		o_player_hand = ''

		for i in self.player_list:
			pnlen = len(i.name)
			if pnlen>(card_len*2)-1:
				pnlen = card_len*2
				
			player_head += (' ')*int(((card_len*2)-pnlen)/2) + i.name + (' ')*int(((card_len*2)-pnlen)/2)
			
			pblen = len(i.balance())
			if pblen>(card_len*2)-1:
				pblen = card_len*2
			
			player_balance += (' ')*int(((card_len*2)-pblen)/2) + i.balance() + (' ')*int(((card_len*2)-pblen)/2)

			for h in i.getHand():
				o_player_hand += str(h) 
		
		return '\n' + border + '\n' + filler + '\n' + dealer_head + '\n' + o_dealer_hand + '\n\n\n' + player_head + '\n' + player_balance + '\n' + o_player_hand + '\n' + filler + '\n' + border
		
	def addPlayer(self,new_player):
		self.player_list.append(new_player)
		
	def removePlayer(self,player):
		self.player_list.remove(player)

	def addDealerHand(self, cards):
		self.dealer_hand = cards

	def clearDealerHand(self):
		self.dealer_hand = []
