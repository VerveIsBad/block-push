class Tile:
    """
    everything on the grid but
    the player, box, and goal.
    """
    def __init__(self, icon = "▦"):
        self.icon = icon
    
    def __getitem__(self, icon):
        return self.icon