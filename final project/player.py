"""
file: player.py
by: Isaac Hepworth

player object will keep track of the player score and name
"""
class Player(object):
	
	def __init__(self, name = "name"):
		"""recive a name and set name and score"""
		self._name = name
		self._score = 0
			
	def __str__(self):
		"""return string Representation of player"""
		string = "Name: " + self._name + "\nScore: " + self._score
		return string	
	
	def getName(self):
		"""returns name as string"""
		return self._name
		 
	def getScore(self):
		"""returns score as int"""
		return self._score
		
	def addToScore(self, points):
		"""adds points to score"""
		self._score += points
		
	def resetScore(self):
		"""resets score to 0"""
		self._score = 0