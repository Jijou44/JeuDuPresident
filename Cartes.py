class Carte:
        def __init__(self, rank, color):
          self.rank = rank
          self.color = color
          self.value = VALUES()[RANKS().index(rank)]
        
        def __str__(self):
            return self.rank + " " + self.color

def COLORS(): return ['coeur', 'carreau', 'trefle', 'pique']
def RANKS(): return [ "As", "2", "3", "4", "5", "6", "7","8", "9", "10", "Valet", "Reine", "Roi" ]
def VALUES(): return [1,13,2,3,4,5,6,7,8,9,10,11,12]


    
