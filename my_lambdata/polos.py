# my_lambbdata/polos.py

# Polo Class!
# attributes / properties (NOUNS): size, style, color, texture, price
# methods (VERBS): wash, fold, pop collar

class Polo():
    def __init__(self, size, color):
        self.size = size
        self.color = color

    @property
    def full_name(self):
        return f"{self.size} {self.color}"

    def wash(self):
        print(f"WASHING THE {self.size} {self.color} POLO!")
        
    @staticmethod    
    def fold():
        print(f"FOLDING THE POLO!")

if __name__ == "__main__":

    # initialize a small blue polo and a large yellow polo

    #df = DataFrame(_____)
    #df.columns
    #df.head()

    p1 = Polo(size="Small", color="Blue")
    print(p1.size, p1.color)
    print(p1.full_name)
    p1.wash()

    p2 = Polo(size="Large", color="Yellow")
    print(p2.size, p2.color)
    print(p2.full_name)
    p2.fold()