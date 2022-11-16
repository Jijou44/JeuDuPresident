import random
import Cartes
class Deck:
        def __init__(self,size):
            self.size = size
            self.cards = []
            for i in range(0,size):
                self.cards.append(Cartes.Carte(Cartes.RANKS()[i%13], Cartes.COLORS()[i%4]))
            random.shuffle(self.cards)
        
        def __str__(self):
            return str(self.cards)
        