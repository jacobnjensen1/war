#!/usr/bin/python3

from random import shuffle

def war(first, second, one_war, two_war):
	if len(first) <= 1:
		second.extend(one_war)
		second.extend(two_war)
		return
	elif len(second) <= 1:
		first.extend(two_war)
		first.extend(one_war)
		return
	elif one_war[1] > two_war[1]:
		first.extend(two_war)
		first.extend(one_war)
	elif two_war[1] > one_war[1]:
		second.extend(one_war)
		second.extend(two_war)
	else:
		one_war = first[0:2] + one_war
		del first[0:2]
		two_war = second[0:2] + two_war
		del second[0:2]
		war(first, second, one_war, two_war)


def play(first, second):
	while len(first) > 0 and len(second) > 0:
		first_card = first.pop(0)
		second_card = second.pop(0)

		if first_card > second_card:
			first.append(first_card)
			first.append(second_card)
		elif second_card > first_card:
			second.append(second_card)
			second.append(first_card)
		else:
			one_war = first[0:2]
			one_war.append(first_card)
			del first[0:2]
			two_war = second[0:2]
			two_war.append(second_card)
			del second[0:2]

			war(first, second, one_war, two_war)

full_deck = []
for i in range(0,4):
	for j in range(1,14):
		full_deck.append(j)

deck_one = []
deck_two = []

shuffle(full_deck)

for i,c in enumerate(full_deck):
	if i % 2:
		deck_one.append(c)
	else:
		deck_two.append(c)

play(deck_one, deck_two)
if len(deck_one)  == 52:
	print("One")
elif len(deck_two) == 52:
	print("Two")
else:
	print("oops")
