#! /usr/bin/env python3


class Python_Noob:
    description = "sucks at python"

    def __init__(self, a, n):
        self.age = a
        self.name = n
        print(f"object created with: \n\tname: {self.name} \n\tage: {self.age} \n\tdescription: {self.description}\n")

    def say_hi(self):
        print(f"hi! {self.name} is {self.age} years old and {self.description}")


