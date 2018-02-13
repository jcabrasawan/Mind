class Item:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __repr__(self):
        return self.name

class Book(Item):
    def __init__(self):
        self.name= "Book"
        self.description= "The title seems familiar, but you can't quite place it."\
                          "It looks a bit dry."
    def __str__(self):
        return self.description

#class Table(Item):
 #   def __init__(self):
 #       self.name= "A reading table."
 #       self.description = "A dusty old table."\
 #                          "It looks worn down."
 #   def __str__(self):
 #      return self.description
    
#class Chair(Item):
 #   def __init__(self):
 #       self.name = "An uncomfortable chair."
 #       self.description = "This chair looks stiff and uncomfortable."\
 #                          "You doubt it can take your weight and decide not to attempt"\
 #                          "sitting on it."
 #   def __str__(self):
 #       return self.description

inventory = ['Nothing']

def play():
    print('test')
    print("INVENTORY: ")
    print (inventory)

play()
