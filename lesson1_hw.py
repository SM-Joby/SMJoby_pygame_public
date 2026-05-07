class car:
    def __init__(self,model,colour, milage):
        self.model = model 
        self.colour = colour
        self.milage = milage
    def intro(self):
        print("Hello this car is a", self.model)
        print("it is", self.colour, "in colour")
        print("It has", self.milage, "miles")

c1= car("Mercedes", "Gray-brown", 600000)
c2= car("BMW", "Blue", 750000)
c1.intro()
c2.intro()