#remake of Disney's toontown online, but single player based and text based

#the class to start the game

class start_game(object):
    
    def __init__(self):
        #start the classes of the game
        self.start_pick_a_toon()
        self.PickAToon = None
        MakeAToon()
        Tutorial()
    def start_pick_a_toon(self):
        self.PickAToon = PickAToon()
        self.PickAToon.start()

    def start_make_a_toon(self):
        self.MakeAToon = MakeAToon()
        if self.PickAToon.state == 'newtoon':
            self.MakeAToon.start()
        else:
            