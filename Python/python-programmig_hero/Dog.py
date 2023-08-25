from ast import Return
from itertools import count
from telnetlib import DO


class Dog:
    num_of_dogs = 0

    def __init__(self,name="unkwon"):
        self.name = name

        Dog.num_of_dogs += 1

    def __str__(self):
        return self.name

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))
      
    
    def main():
        seif = Dog("Seif")
        jack = Dog("Jack")
        lex = Dog("Lex")
        Dog.get_num_of_dogs()



a = Dog()
print(a.main)