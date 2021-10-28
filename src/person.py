class Person:
    """
    Constructor for every object in the game.
    Anything that will be placed on the map
    is a instance of this class.
    """
    def __init__(self, x=2, y=2, icon="icon"):
        self.x = x
        self.y = y
        self.icon = icon
        self.last = []

    def __getitem__(self, x):
        return self.x
    def __getitem__(self, y):
        return self.y
    def __getitem__(self,icon):
        return str(self.icon)

class Player(Person):
    pass

class Box(Person):
    def update_position(self):
        pass

class Goal(Person): 
    
    def update_position(self):
        pass

