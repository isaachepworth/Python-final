"""
file: cards.py
name: Isaac Hepworth

a deck of shuffled cards
"""
import random

class Card(object):
	""" A card object with a PICTURE_NAME."""

	PICTURE_NAMES = ('Spider', 'Pumkin', 'Ghost', 'Cat', 'Candy', 'Headstone')
	
	FACE_DOWN = 'CARDS/back.gif'

	def __init__(self, pictureName):
		"""Creates a card with the PICTURE_NAME."""
		self._pictureName = pictureName
		self._FACE_UP ='CARDS/' + self._pictureName.lower() + '.gif'
		self._faceup = False
		
	def __str__(self):
		"""Returns the string representation of a card."""
		return self._pictureName
		
	def getCard(self):
		"""return wether it is face up or not"""
		return self._faceup
		
	def turn(self):
		"""turns the card up or down depending on its original direction"""
		self._faceup = not self._faceup
		
	def getCardFileName(self):
		if self._faceup:
			return self._FACE_UP
		else:
			return self.FACE_DOWN

import random

class Deck(object):
	""" A deck containing 30 cards."""

	def __init__(self):
		"""Creates a full deck of cards."""
		self._cards = []
		for pictureName in Card.PICTURE_NAMES:
			for i in range(5):
				c = Card(pictureName)
				self._cards.append(c)
		random.shuffle(self._cards)

	def deal(self):
		"""Removes and returns the top card or None 
		if the deck is empty."""
		if len(self) == 0:
		   return None
		else:
		   return self._cards.pop(0)

	def __len__(self):
	   """Returns the number of cards left in the deck."""
	   return len(self._cards)

	def __str__(self): 
		"""Returns the string representation of a deck."""
		result = ''
		for c in self._cards:
			result = self.result + str(c) + '\n'
		return result
		