#!/usr/bin/python3

from random import shuffle

def war(first, second, one_war, two_war):
	if len(first) <= 1 and len(second) <= 1:
		return
		#base case: both players ran out of cards = stalemate
		#because *_war is not returned to the decks, num cards in play < 52
		#this will keep the program from declaring a winner
		#this is probably very unlikely

	if len(first) <= 1:
		#base case: only player one ran out of cards = automatic loss
		second.extend(one_war)
		second.extend(two_war)
		return

	elif len(second) <= 1:
		#base case: only player two ran out of cards = automatic loss
		first.extend(two_war)
		first.extend(one_war)
		return

	if one_war[1] > two_war[1]:
		#base case: player one sets down higher card
		first.extend(two_war)
		first.extend(one_war)
		return

	elif two_war[1] > one_war[1]:
		#base case: player two sets down higher card
		second.extend(one_war)
		second.extend(two_war)
		return

	else:
		#recursive case: there is a tie in war
		one_war = first[0:2] + one_war
		del first[0:2]
		two_war = second[0:2] + two_war
		del second[0:2]
		war(first, second, one_war, two_war)


def play(first, second):
	while len(first) > 0 and len(second) > 0:
		first_card = first.pop(0)
		second_card = second.pop(0)

		#first 2 statements cover the basic game mechanics
		if first_card > second_card:
			first.append(first_card)
			first.append(second_card)
		elif second_card > first_card:
			second.append(second_card)
			second.append(first_card)
		else:
			#if there is a tie, go into a war
			one_war = first[0:2]
			one_war.append(first_card)
			del first[0:2]
			two_war = second[0:2]
			two_war.append(second_card)
			del second[0:2]
			# *_war is now 3 long

			war(first, second, one_war, two_war)
			#war() is recursive

full_deck = []
for i in range(0,4):
	for j in range(1,14):
		full_deck.append(j)
#full_deck populated with 52 cards
deck_one = []
deck_two = []

shuffle(full_deck)

for i,c in enumerate(full_deck):
	if i % 2:
		deck_one.append(c)
	else:
		deck_two.append(c)

play(deck_one, deck_two)
#play() contains the game itself

if len(deck_one)  == 52:
	print("One")
elif len(deck_two) == 52:
	print("Two")
else:
	#this is used when play() makes a mistake
	#and lists end up with not 0 and 52 cards
	print("oops")
