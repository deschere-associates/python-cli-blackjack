# -*- coding: utf-8 -*-
"""

This module represents a card in a simple blackjack game

Todo:
	* make it work
"""

class Card(object):
	"""
	Create a card for a simple blackjack game
	
	Args:
		face_value(str) [defaults to a random value]: The number / face of the card. Example: A,[2-9],10,J,Q,K
		facing (str) [default- 'down']: whether a card is ['up','down']. Used for printing
		suit (str) [defaults to a random value]: The card suit. Example: clubs, diamonds, hearts, spades
	"""
	down_mask = {'value':'##','suit':'#'}
	face_map = {1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
	face_dict = {
		'A':{'name':'Ace','value':(1,11),'print_value':'A'},
		'2':{'name':'Two','value':(2),'print_value':'2'},
		'3':{'name':'Three','value':(3),'print_value':'3'},
		'4':{'name':'Four','value':(4),'print_value':'4'},
		'5':{'name':'Five','value':(5),'print_value':'5'},
		'6':{'name':'Six','value':(6),'print_value':'6'},
		'7':{'name':'Seven','value':(7),'print_value':'7'},
		'8':{'name':'Eight','value':(8),'print_value':'8'},
		'9':{'name':'Nine','value':(9),'print_value':'9'},
		'10':{'name':'Ten','value':(10),'print_value':'10'},
		'J':{'name':'Jack','value':(10),'print_value':'J'},
		'Q':{'name':'Queen','value':(10),'print_value':'Q'},
		'K':{'name':'King','value':(10),'print_value':'K'}
	}
	suit_map = {1:'clubs',2:'diamonds',3:'hearts',4:'spades'}
	suit_dict = {'spades':{'print_value':'\u2660'},'hearts':{'print_value':'\u2665'},'diamonds':{'print_value':'\u2666'},'clubs':{'print_value':'\u2663'}} 
	
	def __init__(self,**kwargs):
		import random
		self.face_value = ''
		self.facing = 'down'
		self.suit = ''
		
		if 'face_value' in kwargs.keys() and kwargs['face_value'] in Card.face_dict.keys():
			self.face_value = kwargs['face_value']
		else:
			self.face_value = Card.face_map[random.randint(1,13)]
			
		if 'facing' in kwargs.keys() and kwargs['facing'] in ('up','down'):
			self.facing = kwargs['facing']
		else:
			self.facing = 'down'

		if 'suit' in kwargs.keys() and kwargs['suit'] in Card.suit_dict.keys():
			self.suit = kwargs['suit']
		else:
			self.suit = Card.suit_map[random.randint(1,4)]
				
	def __str__(self):
		if self.facing == 'down':
			value_print = Card.down_mask['value']
			suit_print = Card.down_mask['suit']
		else:
			value_print = Card.face_dict[self.face_value]['print_value']
			suit_print = Card.suit_dict[self.suit]['print_value']	
			
		return f"||{suit_print} {value_print} {suit_print}||"
	
	def setFacing(self,facing):
		if facing in ('up','down'):
			self.facing = facing
		else:
			raise TypeError("Acceptable values for facing are 'up' or 'down'")
