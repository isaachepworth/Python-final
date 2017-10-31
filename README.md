# Python-final
created by: Isaac Hepworth

This program was inspired by my kids, it is a memory game with a trist.  I used a couple of queues and array grids to make it esyier to work with. There are alot of buttons but I tryed to focus it towards kids with the pictures, I did not make it a I person game. I hope that others would find it fun, and that my kids would enjoy it. The code I have included is dealing with two array grids that I used to keep track of the cards and the images I used on the buttons. The main is part of the memoryGUI file and is the one that will start the program.

for x in range(5):
			for y in range(5):
				self._gridOfCards[x][y] = self._memory._deck.deal()
				self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
