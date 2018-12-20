# -*- coding: utf-8 -*-
"""

This module represents a simple blackjack game

Todo:
	* make it work
"""

class Blackjack(object):
	"""
	Create a gameboard for a simple blackjack game
	
	Args:
		
	Methods:
		start : starts the game
	"""
	winning_payout = 1.5
	blackjack_payout = 3
	
	def __init__(self):
		self.game_on = False
		self.game_list = {}
		self.dealer_hand = []

	def __initgame__(self):
		from src.Deck import Deck
		from src.Player import Player
		from src.Gameboard import Gameboard
		print("Welcome to a simple blackjack game!\nAnswer a few simple questions and we'll get started.")
		
		while True:
			result = input('Name of the casino/dealer: ')
			if result != '':
				self.casino = result
				break
			else:
				print('You must provide a casino name...')
		
		while True:
			result = input('Number of players? ')
			try:
			   self.num_players = int(result)
			   break
			except ValueError:
			   print("That's not a proper number!")

		for i in range(1,self.num_players+1):
			while True:
				result1 = input(f"Player {i}'s name? ")
				result2 = input(f"Player {i}'s starting bank balance? ")
				
				try:
					if result1 != '' and int(result2) and int(result2)>0:
						self.game_list.update({i:{'player_name':result1,'player_start_bank':int(result2)}})
						break
					else:
						print("Player name is required...")
				except ValueError:
					print("Player starting bank balance must be greater than 0")

		self.game_deck = Deck()
		self.game_deck.shuffle()
		self.gameboard = Gameboard(self.casino)
		
		for values in self.game_list.values():
			new_player = Player(name=values['player_name'],starting_bank=values['player_start_bank'])
			self.gameboard.addPlayer(new_player)
			values.update({'player':new_player})
		
		self.game_on = True
		
	def __initdeal__(self):
		card1 = self.game_deck.draw_card()
		card1.setFacing('up')
		card2 = self.game_deck.draw_card()
		card2.setFacing('down')
		self.dealer_hand.append(card1)
		self.dealer_hand.append(card2)
		self.gameboard.addDealerHand(self.dealer_hand)
		
		for i in range(1,self.num_players+1):
			card1 = self.game_deck.draw_card()
			card1.setFacing('up')
			card2 = self.game_deck.draw_card()
			card2.setFacing('up')			
			self.game_list[i]['player'].addCard(card1)
			self.game_list[i]['player'].addCard(card2)
	
	def __askPlayerBid__(self,player_id):
		while True:
			player = self.game_list[player_id]['player']
			if player.balance == '$0':
				return False
			result = input(f"--{player.name}--  Please enter bid amount [less than {player.balance()}]: ")
			try:
				player.withdrawal(int(result))
				self.game_list[player_id].update({'current_bid':int(result)})				
				return True

			except ValueError:
				print("Please enter valid number")
			except:
				print("Verify amount is less than or equal to remaining balance")	
	
	def __askPlayerAction__(self,player_id):
		while True:
			player = self.game_list[player_id]['player']
			result = input(f"--{player.name}--  Do you wish to [s]tand or [h]it: ")
			if result.lower()=='s':
				self.cur_state.update({'action':'player_stand'})
				break
			elif result.lower()=='h':
				self.cur_state.update({'action':'player_hit'})
				break
			else:
				print('Incorrect response, please choose s or h (stand or hit)')
			
	def start(self):
		self.__initgame__()
		self.__initdeal__()
		self.cur_state = {'action':'bid','current_player':1}
		
		while self.game_on:
#			while True:
			print(self.gameboard)
			
			if self.cur_state['action']=='bid':		
				if self.__askPlayerBid__(i):
						self.cur_state.update({'action':'player_action'})
						continue
					else:
						self.cur_state.update({'action':'player_stand'})
						continue

			if self.cur_state['action']=='player_action':
				self.askPlayerAction(self.cur_state['current_player'])
				continue

			if self.cur_state['action']=='player_stand':
				if self.cur_state['current_player'] >= self.num_players:
					self.cur_state.update({'action':'dealers_turn'})
					continue
				else:
					self.cur_state.update({'action':'bid','current_player':self.cur_state['current_player']+1})
					continue
			
			if self.cur_state['action']=='player_hit':
				card1 = self.game_deck.draw_card()
				card1.setFacing('up')
				self.game_list[self.cur_state['current_player']]['player'].addCard(card1)
				self.cur_state.update({'action':'check_player_score'})
				continue

			if self.cur_state['action']=='check_player_score':
				#pick up here
				
			break
			
#				for i in range(1,self.num_players+1):
#					self.player_continue = True
#					while True:
#						if not self.__askPlayerBid__(i): break						
#						self.__askPlayerAction__(i)
					#pick back up here


					
			self.game_on = False