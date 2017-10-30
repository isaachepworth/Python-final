"""
file: memory
name: Isaac Hepworth

sets up a memory game
"""
from player import Player
from cards import Card, Deck
from linkedqueue import LinkedQueue

class Memory(object):
	
	def __init__(self, numOfPlayers = 2):
		self._numOfPlayers = numOfPlayers
		self._totalScore = 0
		self._deck = Deck()
		self._queue = LinkedQueue()
		for player in range(self._numOfPlayers):
			self._queue.add(Player('Player ' + str(player + 1)))
		self._currentPlayer = self._queue.pop()
		
	def getPlayerName(self):
		return self._currentPlayer.getName()
		
	def setPlayerName(self, name):
		"""sets current player name"""
		self._currentPlayer.setName(name)
		
	def addPlayerScore(self, points):
		"""adds points to current player"""
		if self._totalScore + points > 30:
			while self._totalScore < 30:
				self._currentPlayer.addToScore(1)
				self._totalScore += 1
		elif self._currentPlayer.getScore() + points >= 0:
			self._currentPlayer.addToScore(points)
			self._totalScore += points
			
	def nextPlayer(self):
		"""moves to next player and puts previous player to back of queue"""
		self._queue.add(self._currentPlayer)
		self._currentPlayer = self._queue.pop()
		
	def checkGameOver(self):
		"""checks if point add to 30"""
		if self._totalScore >= 30:
			return True
		return False
				
	def playerHigh(self):
		"""finds player with high score"""
		for player in range(self._numOfPlayers):
			temp = self._queue.pop()
			if temp.getScore() > self._currentPlayer.getScore():
				self._queue.add(self._currentPlayer)
				self._currentPlayer = temp
			else:
				self._queue.add(temp)
		return self._currentPlayer.getName()