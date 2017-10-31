# Python-final
created by: Isaac Hepworth

This program was inspired by my kids, it is a memory game with a twist. They love it because it is simple enough for them to understand it but it has enough strategy to keep the adults interested, it deals a lot with memorization. I used a couple of queues and array grids to make it easier to work with. There are a lot of buttons but I tried to focus it towards kids with the pictures, I did not make it a one-person game namely for the need of a computer player which I was not up to right now. I hope that others would find it fun, as my kids enjoy it. The code I have included is dealing with two array grids that I used to keep track of the cards and the images I used on the buttons. The main is part of the memoryGUI file and is the one that will start the program. All files are needed for the program to work.

for x in range(5):
			for y in range(5):
				self._gridOfCards[x][y] = self._memory._deck.deal()
				self._gridOfPictures[x][y] = PhotoImage(file = self._gridOfCards[x][y].getCardFileName())
