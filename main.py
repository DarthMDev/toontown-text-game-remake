#remake of Disney's toontown online, but single player based and text based

#the class to start the game

class StartGame(object):
    
    def __init__(self):
        #start the classes of the game
        self.start_pick_a_toon()

    def start_pick_a_toon(self):
        #start the pick a toon class 
        self.PickAToon = PickAToon() #define pickatoon class
        self.PickAToon.__init__()
        self.Toon = Toon() # define the toon class
        if self.PickAToon.get_state() == 'toon selected': #if you select a toon that has been already created you load the previouszone you were in
            Toon.load_previous_zone()
        else:
            self.start_make_a_toon() #otherwise if there is no toon in that slot make a new one
    def start_make_a_toon(self):

        #starts the make a toon class which creates a new toon object
        self.MakeAToon = MakeAToon() #define makeatoon class
        self.Toon = Toon() #define the toon class
        self.Tutorial = Tutorial() # define tutorial class
        self.Toon.new_toon() # make a new toon in the database
        self.start_tutorial() # starts the tutorial level

    def start_tutorial(self):
        #starts the tutorial for new toons
        self.tutorial = Tutorial()
        self.tutorial


class PickAToon(object):
    #class to load up the toons and select one
    def __init__(self):
        #initalizes the variables
        self.toons = []
        self.state = ''
        self.name = ''
        self.selected_toon = None
        self.chosen_toon = None
        #starts the select which toon function asking the user what toon they want to use
        self.chosen_toon = self.select_a_toon(self.get_toons)
        #starts the function for selecting the actual toon and starting the game
        self.choose_a_toon(self.toons, self.chosen_toon)
        
    def get_toons(self):
        return self.toons #gets the self.toons list and returns it
    def which_toon(self, toonslist):
        self.toons = self.get_toons() #runs the get toons function to know what the current list of toons is
        if len(self.toons) != 0: #if list isnt empty
            self.selected_toon = raw_input("Select a toon from the list, types its name: {0}".format(toonslist)) #asks the user to select a toon from the list
        else:
            self.selected_toon = None #set it to None so we create a new toon
        return self.selected_toon #return the selectedtoon
    def choose_a_toon(self, toonslist, toon):
        self.toonslist = toonslist #sets self.toonslist to the argument
        self.toon = toon #self to argument
        if len(self.toonslist) == 0: #if list is None make a new toon
            self.set_state('make new toon')
            print('creating new toon')
        elif self.toon in toonslist: # if toon is in the list of toons then select it and load previous zone
            self.set_state('toon selected') #set the state
        elif self.toon is None: #if no toon is selected or the list is empty make a new toon
            self.set_state('make new toon') #sets the state
            print('creating new toon')
        else:
            self.set_state('make new toon') #if all else fails make a new toon
            print('creating new toon')

    def set_state(self, state):
        self.state = state #sets the state to the argument given

    def get_state(self):
        return self.state #gets the current state and return it

class MakeAToon(object):
    #makes a new toon and creates new data for it
    
    def __init__(self):
        #initalizes the variables
        self.arms = None
        self.legs = None
        self.color = None
        self.species = None
        self.species_to_choose_from = ['dog', 'cat', 'penguin', 'bear', 'pig', 'rabbit', 'duck', 'horse', 'chicken', 'beaver', 'bat', 'deer', 'crocodile', 'monkey']
        self.select_species(self.species_to_choose_from)
    def select_species(self, species_to_choose_from):
        self.species_to_choose_from = species_to_choose_from
        self.species = raw_input('Please select a species from the list of species: {0}'.format(self.species_to_choose_from))
        if self.species in self.species_to_choose_from:
            self.set_species(species)
            print('Your toon is a {0}'.format(species))
        else:
            print('invalid species please select one from the list')

    def set_species(self, species):
        self.species = species
    
    def get_species(self):
        return self.species

    def set_appearance(self, sizeoptions):
        self.size_options = sizeoptions
        self.body = raw_input('Select the size of your toon: {0}'.format(self.size_options))
        self.legs = raw_input('Select the size of your legs: {0}'.format(self.size_options))
        
    def set_color(self):
        self.color = raw_input('Choose a color for your toon: ')
        try:
            int(self.color)
            print('Color has to be a string not an integer!')
        except:
            self.color = self.color
        