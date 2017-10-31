"""
file: memoryGUI
name: Isaac Hepworth

creates the GUI for the memory game and runs it
"""
from arrayGrid import ArrayGrid
from linkedqueue import LinkedQueue
from memory import Memory
from tkinter import *
from tkinter import messagebox

class MemoryGUI(Frame):
	
	def __init__(self):
		Frame.__init__(self)
		self.master.title("Memory")
		self.grid()
		
		self._gridOfPictures = ArrayGrid(5, 5)
		self._gridOfCards = ArrayGrid(5, 5)
		self._gridOfButtons = ArrayGrid(5, 5)
		
		"""pane that will contain the buttons thourghout the program"""
		self._mainPane = Frame(self)
		self._mainPane.grid(row = 0, column = 0)
		
		"""info pane will hold scores and a button to start new game"""
		self._infoPane = Frame(self)
		self._infoPane.grid(row = 0, column = 1) 
		
		"""create buttons for opening screen"""
		self._buttonImage2 = PhotoImage(file = 'CARDS/2player.gif')
		self._2PlayerButton = Button(self._mainPane, image = self._buttonImage2, command = self._button2)
		self._2PlayerButton.grid(row = 0, column = 0)
		self._buttonImage3 = PhotoImage(file = 'CARDS/3player.gif')
		self._3PlayerButton = Button(self._mainPane, image = self._buttonImage3, command = self._button3)
		self._3PlayerButton.grid(row = 0, column = 1)
		self._buttonImage4 = PhotoImage(file = 'CARDS/4player.gif')
		self._4PlayerButton = Button(self._mainPane, image = self._buttonImage4, command = self._button4)
		self._4PlayerButton.grid(row = 1, column = 0)
		self._buttonImage5 = PhotoImage(file = 'CARDS/5player.gif')
		self._5PlayerButton = Button(self._mainPane, image = self._buttonImage5, command = self._button5)
		self._5PlayerButton.grid(row = 1, column = 1)
		
	def _button2(self):
		self._mainButtons(2)
		
	def _button3(self):
		self._mainButtons(3)
			
	def _button4(self):
		self._mainButtons(4)
				
	def _button5(self):
		self._mainButtons(5)
		
	def _mainButtons(self, numOfPlayers):
		"""create all the buttons"""
		self._numberOfPlayers = numOfPlayers
		self._2PlayerButton.grid_forget()
		self._3PlayerButton.grid_forget()
		self._4PlayerButton.grid_forget()
		self._5PlayerButton.grid_forget()
		self._memory = Memory(numOfPlayers)
		self._listOfPressed = []
		for x in range(5):
			for y in range(5):
				self._gridOfCards[x][y] = self._memory._deck.deal()
				self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
		
		x = 0
		y = 0
		self._cardButton1 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress1)
		self._cardButton1.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton1
		y += 1
		self._cardButton2 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress2)
		self._cardButton2.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton2
		y += 1
		self._cardButton3 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress3)
		self._cardButton3.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton3
		y += 1
		self._cardButton4 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress4)
		self._cardButton4.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton4
		y += 1
		self._cardButton5 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress5)
		self._cardButton5.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton5
		
		y = 0
		x += 1
		self._cardButton6 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress6)
		self._cardButton6.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton6
		y += 1
		self._cardButton7 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress7)
		self._cardButton7.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton7
		y += 1
		self._cardButton8 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress8)
		self._cardButton8.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton8
		y += 1
		self._cardButton9 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress9)
		self._cardButton9.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton9
		y += 1
		self._cardButton10 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress10)
		self._cardButton10.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton10
		
		y = 0
		x += 1
		self._cardButton11 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress11)
		self._cardButton11.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton11
		y += 1
		self._cardButton12 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress12)
		self._cardButton12.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton12
		y += 1
		self._cardButton13 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress13)
		self._cardButton13.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton13
		y += 1
		self._cardButton14 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress14)
		self._cardButton14.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton14
		y += 1
		self._cardButton15 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress15)
		self._cardButton15.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton15
		
		y = 0
		x += 1
		self._cardButton16 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress16)
		self._cardButton16.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton16
		y += 1
		self._cardButton17 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress17)
		self._cardButton17.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton17
		y += 1
		self._cardButton18 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress18)
		self._cardButton18.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton18
		y += 1
		self._cardButton19 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress19)
		self._cardButton19.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton19
		y += 1
		self._cardButton20 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress20)
		self._cardButton20.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton20
		
		y = 0
		x += 1
		self._cardButton21 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress21)
		self._cardButton21.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton21
		y += 1
		self._cardButton22 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress22)
		self._cardButton22.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton22
		y += 1
		self._cardButton23 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress23)
		self._cardButton23.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton23
		y += 1
		self._cardButton24 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress24)
		self._cardButton24.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton24
		y += 1
		self._cardButton25 = Button(self._mainPane, image = self._gridOfPictures[x][y], command = self._cardButtonPress25)
		self._cardButton25.grid(row = x, column = y)
		self._gridOfButtons[x][y] = self._cardButton25
		
		"""adding labels and buttons to info pane"""
		self._playerLabelQueue = LinkedQueue()
		for label in range(numOfPlayers):
			self._playerScore = Label(self._infoPane, text = 'Player ' + str(label + 1) + ': 0')
			self._playerScore.grid(row = label + 2, column = 0)
			self._playerLabelQueue.add(self._playerScore)
		self._currentLabel = self._playerLabelQueue.pop()
			
		self._rulesButton = Button(self._infoPane, text = 'Rules', command = self._rules)
		self._rulesButton.grid(row = 0, column = 0)	
		
		self._resetButton = Button(self._infoPane, text = 'New Game', command = self._reset)
		self._resetButton.grid(row = 1, column = 0)
		
		self._popupMsg('Player 1 turn')
		
	def _reset(self):
		self._mainButtons(self._numberOfPlayers)
		
	def _rules(self):
		messagebox.showinfo("Rules", '1. The first player turns over 2 cards, looking for matching cards. If the two Treasures match, turn over another card to try to find an additional match, Keep going until you do not find a matching card. \n2. For each matching card uncovered, he or she is rewarded with 1 point! \n3. If a player turns up a headstone that he or she wasnt looking for, he or she looses his or her turn and must give 1 point back unless player has none. \n4. When a player finds a non-matching card, or a headstone, the cards are turned face down except for the last card that was found, which is kept face up. \n5. Play continues with the next player trying to find a match for the card that is face up. \n6. Continue until the total of all players points add up to 30.')
	
	def _cardButtonPress1(self):
		x = 0
		y = 0
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))	
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress2(self):
		x = 0
		y = 1
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress3(self):
		x = 0
		y = 2
		if tuple([x, y]) not in self._listOfPressed: 
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress4(self):
		x = 0
		y = 3
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress5(self):
		x = 0
		y = 4
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress6(self):
		x = 1
		y = 0
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress7(self):
		x = 1
		y = 1
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress8(self):
		x = 1
		y = 2
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress9(self):
		x = 1
		y = 3
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress10(self):
		x = 1
		y = 4
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress11(self):
		x = 2
		y = 0
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress12(self):
		x = 2
		y = 1
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress13(self):
		x = 2
		y = 2
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress14(self):
		x = 2
		y = 3
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress15(self):
		x = 2
		y = 4
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress16(self):
		x = 3
		y = 0
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress17(self):
		x = 3
		y = 1
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress18(self):
		x = 3
		y = 2
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress19(self):
		x = 3
		y = 3
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress20(self):
		x = 3
		y = 4
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress21(self):
		x = 4
		y = 0
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress22(self):
		x = 4
		y = 1
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress23(self):
		x = 4
		y = 2
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress24(self):
		x = 4
		y = 3
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonPress25(self):
		x = 4
		y = 4
		if tuple([x, y]) not in self._listOfPressed:
			self._listOfPressed.append(tuple([x, y]))
			self._gridOfCards[x][y].turn()
			self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
			self._gridOfButtons[x][y].config(image = self._gridOfPictures[x][y])
			self._cardButtonMain()
		
	def _cardButtonMain(self):
		"""checks if card is the same as last"""
		print(self._listOfPressed, 'begain')
		if len(self._listOfPressed) > 1:
			x, y = self._listOfPressed[-1]
			x1, y1 = self._listOfPressed[-2]
			if str(self._gridOfCards[x][y]) != str(self._gridOfCards[x1][y1]):
				if str(self._gridOfCards[x][y]) == 'Headstone':
					"""-1 point if you turned over a headstone"""
					self._memory.addPlayerScore(-1)
				elif len(self._listOfPressed) > 2:
					self._memory.addPlayerScore(len(self._listOfPressed)-1)
					if self._memory.checkGameOver():
						self._resetButtons()
						self._popupMsg(str(self._memory.playerHigh() + ' Won', True))
				if not self._memory.checkGameOver():
					self._resetButtons(tuple([x, y]))
					self._currentLabel['text'] = self._memory._currentPlayer.getName()  + ': ' + str(self._memory._currentPlayer.getScore())
					self._playerLabelQueue.add(self._currentLabel)
					self._currentLabel = self._playerLabelQueue.pop()
					self._memory.nextPlayer()
					print(str(self._memory._currentPlayer.getName()))
					self._popupMsg(str(self._memory._currentPlayer.getName() + ' Turn'))
		if self._memory.checkGameOver():
			self._mainButtons(self._numberOfPlayers)
			
	def _resetButtons(self, xy = tuple([5, 5])):
		"""resets buttons but leaves last one pressed untuched"""
		for xandy in self._listOfPressed[::-1]:
			x1, y1 = xandy
			if xy != xandy:
				self._gridOfCards[x1][y1].turn()
				self._gridOfButtons[x1][y1].state = 'Normal'
				self._gridOfPictures[x1][y1] = PhotoImage(file = self._gridOfCards[x1][y1].getCardFileName())
				self._gridOfButtons[x1][y1].config(image = self._gridOfPictures[x1][y1])
				self._listOfPressed.remove(xandy)
		
	def _popupMsg(self, msg, done = False):
		messagebox.showinfo("Information", msg)
								
def main():
	"""Instantiate game."""
	MemoryGUI().mainloop()

main()
