#remake of Disney's toontown online, but single player based and text based

import time
import random
#checks if provided string is an integer
def check_if_int(string):
    try:
        int(string) #if its a string it will produce an error and go to except
        print("{0} is a integer".format(string))
        return True #if it is an integer it will run this 
    except:
        return False 

#the class to start the game
class StartGame(object):
    
    def __init__(self):
        #start the classes of the game
        time.sleep(1)
        print('Starting game...')
        time.sleep(5)
        self.start_pick_a_toon()

    def start_pick_a_toon(self):
        #start the pick a toon class 
        print('Starting pick a toon...')
        time.sleep(5)
        self.PickAToon = PickAToon() #define pickatoon class
        self.PickAToon.start()
        self.Toon = Toon() # define the toon class
        if self.PickAToon.get_state() == 'toon selected': #if you select a toon that has been already created you load the previouszone you were in
            Toon.load_previous_zone()
        else:
            self.start_make_a_toon() #otherwise if there is no toon in that slot make a new one
            print('Starting make a toon....')
    def start_make_a_toon(self):
        #starts the make a toon class which creates a new toon object
        self.MakeAToon = MakeAToon() #define makeatoon class
        self.MakeAToon.start()
        self.Toon = Toon() #define the toon class
        self.Tutorial = Tutorial() # define tutorial class

class PickAToon(object):
    #class to load up the toons and select one
    def __init__(self):
        #initalizes the variables
        self.toons = []
        self.state = ''
        self.name = ''
        self.selected_toon = None
        self.chosen_toon = None
        
    def start(self):
        #starts the select which toon function asking the user what toon they want to use
        self.chosen_toon = self.which_toon(self.get_toons)
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
        self.item = None
        self.list = []
        self.legs = None
        self.color = None
        self.species = None
        self.body = None
        self.legs = None
        self.name = ''
        self.sizes = []
        self.species_to_choose_from = []
        self.start() # starts the makeatoon process
        
    def start(self):
        #start the makeatoon process
        print ('Starting make a toon....')
        self.species_to_choose_from = ['dog', 'cat', 'penguin', 'bear', 'pig', 'rabbit', 'duck', 'horse', 'chicken', 'beaver', 'bat', 'deer', 'crocodile', 'monkey'] #define the list of animals to choose from
        self.select_species(self.species_to_choose_from) #asks the user for the species they want
        self.sizes = ['small', 'medium', 'large'] #define the list of sizes to choose from
        self.set_appearance(self.sizes) #set the appearance options of your toon
        self.set_color() # set the color of your toon
        self.set_name() # set the name of your toon
        self.Toon = Toon() # class of toon initalizing
        print('Creating toon in database')
        self.Toon.new_toon(self.get_species(), self.get_body_size(), self.get_leg_size(), self.get_color(), self.get_name()) #makes a new toon from the makeatoon

    def select_species(self, species_to_choose_from):
        self.species_to_choose_from = species_to_choose_from 
        while self.species is None or check_if_int(self.species) or self.species not in self.species_to_choose_from:  #as long as species is none , species is an integer, or species is not in species to choose from
            self.species = raw_input('Please select a species from the list of species: {0}'.format(self.species_to_choose_from))
            if self.species in self.species_to_choose_from: #if its in the list set the species
                self.set_species(self.species)
                print('Your toon is a {0}'.format(self.species))
                break
            else:
                print('invalid species please select one from the list')

    def set_species(self, species):
        self.species = species
    
    def get_species(self):
        return self.species

    def appearance_loop(self, item, list):
        self.item = item
        self.list = list
        while self.item not in self.list:
            self.item = raw_input('Select the size of your {0}: {1}'.format(item, self.list)) 
            if self.item in self.list:
                print('{0} size is: {1}'.format(item, self.list[self.list.index(self.item)]))
                break
            else:
                print('The size must be an option in the list')
                continue
        return self.item
    def set_appearance(self, sizeoptions):
        self.size_options = sizeoptions
        self.body = 'body'
        self.legs = 'legs'
        #do the loop for selecting a proper size for body and legs and set it to the variables
        self.body = self.appearance_loop(self.body, self.size_options) 
        self.legs = self.appearance_loop(self.legs, self.size_options)
    def get_body_size(self):
        return self.body
    def get_leg_size(self):
        return self.legs
    def set_color(self):
        while check_if_int(self.color) or self.color is None or self.color == '': #as long as color is an integer, Nonetype, or blank ask the user for the color they want
            self.color = raw_input('Choose a color for your toon: ')
            if self.color == '':
                print('Color cannot be nothing')
                continue
            elif check_if_int(self.color):
                print('Color cannot be an integer')
                continue
            elif self.color is None:
                print('Color is none type')
                continue
            else:
                print("Toon's color is {0}".format(self.color))
                break
         
            
    def get_color(self):
        return self.color
        
    def set_name(self):
        while check_if_int(self.name) or self.name is None or self.name == '': #as long as name is an integer, nonetype, or blank ask the user for the name they want
            self.name = raw_input("Please enter your toon's name")
            if self.name == '':
                print("Name cannot be blank")
                continue
            elif check_if_int(self.name):
                print('Name cannot be an integer')
            else:
                print("Toon's name is {0}".format(self.name))
                break
    def get_name(self):
        return self.name 

class Toon(object):
    def __init__(self):
        self.dna = []
        self.inventory = ['Throw', 'Squirt']
        self.throw_gags = ['Cupcake']
        self.squirt_gags = ['Squirting Flower']
        self.toon_up_gags = []
        self.trap_gags = []
        self.lure_gags = []
        self.sound_gags = []
        self.drop_gags = []
        self.inventory_experience = []
        self.gag = ''
        self.maxhp = 15
        self.hp = 15
        self.exp = 0
        self.maxexp = 10500
        self.quest_id = 0
        self.quests = []
        self.current_quests = []
        self.carry_limit_quests = 1
        self.gag_carry_limit = 20

    def start(self):
        pass
    def new_toon(self, species, body, legs, color, name):
        self.species = species
        self.body = body
        self.legs = legs
        self.color = color
        self.name = name
        self.dna.append((self.species, self.body, self.legs, self.color, self.name))
        self.set_dna(self.dna)
        tutorial = Tutorial()
        tutorial.start()

    def set_dna(self, dna):
        self.dna = dna

    def get_dna(self):
        return self.dna

    def set_gag_pouch(self, gag_carry_limit):
        self.previous_gag_pouch = self.gag_carry_limit
        self.gag_carry_limit = gag_carry_limit
        if self.previous_gag_pouch in self.dna:
            self.dna.insert(self.dna.index(self.dna[self.previous_gag_pouch]), self.gag_carry_limit) 

        else:
            self.dna.append(self.gag_carry_limit)


    def set_experience(self, track, experience):
        self.track = track
        self.experience = experience
        if self.track in self.inventory and index(self.inventory_experience[self.inventory[self.inventory.index(self.track)]]) < len(self.inventory_experience) :
            self.inventory_experience[self.inventory[self.inventory.index(self.track)]] = self.experience
        elif self.track in self.inventory and index(self.inventory_experience[self.inventory[self.inventory.index(self.track)]]) > len(self.inventory_experience):
            self.inventory_experience.insert(self.inventory.index(self.track), self.track)
        else:
            print('Gag is not in inventory')

    def add_experience(self, track, experience):
        self.track = track
        self.exp = experience
        try:
            self.index = self.inventory_experience[self.inventory_experience.index(self.track)]
        except:
            self.index = None
        if self.inventory_experience[self.track] == self.index and self.track in self.inventory:
            self.inventory_experience[self.track] += self.exp
        elif self.track in self.inventory and self.inventory_experience[self.track] != self.index:
            self.inventory_experience.insert(self.inventory.index(self.track),0)
            self.inventory_experience[self.track] += self.exp
        else:
            print('{0} is not  a gag in your inventory {1}'.format(self.gag, self.inventory))
        if self.inventory_experience in self.dna:
            self.dna.insert(self.dna.index(self.dna[self.inventory_experience]), self.inventory_experience)
        else:
            self.dna.append(self.inventory_experience)
    def get_experience(self, track):
        return self.inventory_experience[self.inventory_experience.index(track)]

    def set_quests(self, quests, quest_id):
        self.quest_id = quest_id
        self.quests = quests
        if len(self.quests) >= self.carry_limit_quests:
            print("Can't add quest , already have max number of quests you can carry")    
        else:
            self.quests.append(quest_id)
            self.current_quests = self.quests
            if self.quests in self.dna:
                self.dna.insert(self.dna.index(self.dna[self.quests], self.current_quests))
            else:
                self.dna.append(self.current_quests)

    def add_quests(self, quest_id):
        self.quest_id = quest_id
        if len(self.current_quests) >= self.carry_limit_quests:
            print("Can't add quest , already have max number of quests you can carry")
        else:
            self.current_quests.append(quest_id)
            if self.quests in self.dna:
                self.dna.insert(self.dna.index(self.dna[self.quests], self.current_quests))

            else:
                self.dna.append(self.current_quests)
        
    def get_quests(self):
        print('Current tasks: {0}'.format(self.current_quests))
        return self.current_quests

    def set_hp(self, hp):
        self.previous_hp = self.hp 
        self.hp = hp
        if self.previous_hp in self.dna:
            self.dna.insert(self.dna.index)
        else:
            self.dna.append(self.hp)

    def set_max_hp(self, maxhp): 
        self.previous_hp = self.hp
        self.previous_max_hp = self.maxhp 
        
        self.maxhp = maxhp
        self.hp = set_hp(maxhp)
        if self.previous_max_hp in self.dna:
            self.dna.insert(self.dna.index(self.dna[self.previous_max_hp], self.maxhp))
        else:
            self.dna.append(self.maxhp)
        if self.previous_hp in self.dna:
            self.dna.insert(self.dna.index(self.dna[self.previous_hp]), self.hp)
        else:
            self.dna.append(self.hp)

    def add_max_hp(self, amount):
        self.previous_hp = self.hp
        self.previous_max_hp = self.maxhp 
        self.amount = amount
        self.maxhp += amount
        self.hp = self.maxhp
        if self.previous_maxhp in self.dna:
            self.dna.insert(self.dna.index(self.dna[self.previous_max_hp]), self.maxhp)
        else:
            self.dna.append(self.maxhp)
        if self.previous_hp in self.dna:
            self.dna.insert(self.dna.index(self.dna[self.previous_hp]), self.hp)
        else:
            self.dna.append(self.hp)
    def heal(self, amount):
        if self.hp < self.maxhp:
            self.set_hp(self.hp + amount)
        else:
            print('full on health')

    def lose_health(self, amount):
        self.set_hp(self.hp - amount)
    def get_hp(self):
         print('laff is {0}'.format(self.dna.hp))
         return self.dna.hp
    def get_max_hp(self):
        print('max laff is {0}'.format(self.dna.maxhp))
        return self.dna.maxhp 

    def set_inventory(self, inventory):
        self.previous_inventory = self.inventory
        self.inventory = inventory
        if self.previous_inventory not in self.dna:
            self.dna.append(self.inventory)
        else:
            self.dna.insert(self.dna.index(self.dna[self.previous_inventory]), self.inventory)
    
    def add_gag_to_inventory(self, gag, inventory):
        self.gag = gag
        self.previous_inventory = self.inventory
        self.inventory = inventory
        if self.gag not in self.inventory:
            self.inventory.append(self.gag)
        else:
            print('inventory already has gag {0} in inventory: {1}'.format(self.gag, self.inventory))
        if self.previous_inventory in self.dna:
            self.dna.insert(self.dna.index(self.dna[self.previous_inventory]), self.inventory)
        else:
            self.dna.append(self.inventory)
    def get_inventory(self):
        print('Gag access: {0}'.format(self.dna.inventory))
        return self.dna.inventory


class Tutorial(object):
    def __init__(self):
        self.tutorial_suit = None
        self.toon = None
        self.tutorial_task = None
        self.tutorial_dialog = ''
        self.tutorial_npc = 'Tutorial Tom'
        

    def start(self):
        print('This part of the game is still in development!')
        #self.start_dialog()
        #self.tutorial_suit = TutorialSuit()
        #self.tutorial_suit.generate()

    def start_dialog(self):
        print('{0}: Hello there! Welcome to toontown!')
        #TODO

    def set_defaults(self):
        self.toon = Toon()
        self.toon.set_max_hp(15)
        self.toon.add_quests(self.get_tutorial_task)
        self.toon.set_throw_gags('Cupcake')
        self.toon.set_squirt_gags('Squirting Flower')
        self.toon.set_quest_carry_limit(1)
        self.toon.set_gag_pouch(20)
        self.toon.set_inventory(('Throw', 'Squirt'))
        self.toon.set_experience('Throw', 0)
        self.toon.set_experience('Squirt', 0)


class TutorialSuit(object):
    def __init__(self):
        self.hp = 6
        self.maxhp = 6
        self.name = 'Flunky Level 1'
        
    def generate(self):
        self.set_name('Flunky')
        self.set_max_hp(6)
        #TODO
        #self.set_default_damage()
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name 
    
    def set_max_hp(self, maxhp):
        self.maxhp = maxhp
        self.hp = maxhp
    def get_max_hp(self):
        return self.maxhp

    def set_hp(self, hp):
        self.hp = hp 
    def get_hp(self):
        return self.hp

StartGame()
