class Guitar:
    def __init__(self, n_strings=6): # initialize class
        self.n_strings = n_strings 
        self.play()  
        self.__cost = 50
    def play(self): 
        print("pam pam pam pam pam pam pam")

class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__(n_strings=8) # super() allows access to the parent class __init__ method
        self.color = ("#000000", "#FFFFFF")
    def play_louder(self):
        print("pam pam pam pam pam pam pam".upper())
    def __secret(self):
        print("this guitar actually cost me $", self._Guitar__cost, "only!")

class BassGuitar(Guitar):
    pass

my_guitar = ElectricGuitar()
my_guitar._ElectricGuitar__secret()
print("my bass guitar has", BassGuitar(4).n_strings, "strings")
print("my electric guitar has", my_guitar.n_strings, "strings")

### NOTES -----------------------------------
# `self.n_strings = 6` = attribute (accessible from outside of class definition)
# `self.play()` by putting the play method within the init method, it is beign automatically called every time we create a new object
# def `play(self):` passing self parameter turns `play` into a method
# `object.play()` you call a method ON something, functions stand alone

# `my_guitar.n_strings` calls on the self.n_string attribute
# `class ElectricGuitar(Guitar):` = inheritance, all data/functionality from Guitar class will be in ElectricGuitar class
# super() allows access to the parent class __init__ method, and all changes will only take place in child class
# self.__cost -> AttributeError: 'ElectricGuitar' object has no attribute '__cost'
# "private member" (ie. self.__cost) is NOT truly private
# If you do not specify value `def __init__(self, n_strings=6):` defaults to 6