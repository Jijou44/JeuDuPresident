
def compareCards(card1, card2):
    if card1.value > card2.value:
        return card1
    elif card1.value < card2.value:
        return card2
    else:
        return card1

