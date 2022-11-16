
# Version sans la class deck a mettre direct dans le main
import Cartes

def compare_cards(card1, card2):
    if card1.value > card2.value:
        return card1
    elif card1.value < card2.value:
        return card2
    else:
        return card1

# generate 52 cards
cards = []
for color in Cartes.COLORS():
    for rank in Cartes.RANKS():
        cards.append(Cartes.Carte(rank, color))

# print cards
print(compare_cards(cards[3], cards[4]))
