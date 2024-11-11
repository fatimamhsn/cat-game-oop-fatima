# Our Cat Entity
class Cat:
    # The constructor
    # - The constructor will create a cat for is in code
    # - To create a cat, we need a given_name and a given_colour
    # - self is the cat that we are creating

    def __init__(self, given_name, given_colour):
        # Name attribute
        self.name = given_name
        # Colour attribute
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 20
        self.weight = 30
        

    
    def train(self):
        print(f"{self.name} is training...")
        self.energy -= 5
        self.intelligence += 1
        self.weight -= 1
        self.age += 0.1

    def feed(self):
        print(f"{self.name} is eating...")
        self.energy += 10
        self.weight += 1
        self.age += 0.1
    
    def play(self):
        print(f"{self.name} is playing...")
        self.energy -= 5
        self.weight -= 0.5
        self.age += 0.1
    
    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy += 8
        self.age += 0.1
    
    def showstats(self):
        print(f" Age: {self.age} \n Weight: {self.weight}  \n Energy: {self.energy} \n Intelligence: {self.intelligence}")

    
    def check(self):
        if self.age<20:
            return False
        elif self.energy<5:
            return False
        elif self.weight<5:
            return False
        elif self.weight>30:
            return False
        else:
            return True