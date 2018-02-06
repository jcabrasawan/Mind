import items

class Player:
    def __init__(self):
        self.x = 2
        self.y = 3

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def move_north(self):
        self.move(dx = 0, dy = -1)
    def move_south(self):
        self.move(dx = 0, dy = 1)
    def move_west(self):
        self.move(dx = -1, dy = 0)
    def move_east(self):
        self.move(dx = 1, dy = 0)

    def print_inventory(self):
        print("Inventory:")
        for item in self.invventory:
            print("*"+ str(item))      
        
