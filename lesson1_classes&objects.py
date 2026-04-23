#object oriented progeamming (OOP) - it's a way of writing code, where you organise everything into objects-each object bundles data(attributes) and behaviour(methods) together
#It contains classes and object, where a class is like a blueprint and an object is a real instance
class student:
    def __init__(self,name,age):
        self.name = name # init stands for initialsising function
                         #used to set the inital values and its first parameter is always self
        self.age = age
    def intro(self):
        print("Hello my name is", self.name)
        print("I am", self.age, "years old")

s1= student("Sarah", 16)
s2= student("Eric", 7)
s1.intro()
s2.intro()