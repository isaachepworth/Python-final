# Python-final
created by: Isaac Hepworth

this program was inspired by my kids, it is a memory game with a trist.  i used a couple of queues and array grids to make it esyier to work with. there are alot of buttons but i tryed to focus it towards kids with the pictures, i did not make it a i person game. i hope that others would find it fun, and that my kids would enjoy it. the code i have included is dealing with two array grids that i used to keep track of the cards and the images i used on the buttons.

for x in range(5):
			for y in range(5):
				self._gridOfCards[x][y] = self._memory._deck.deal()
				self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
