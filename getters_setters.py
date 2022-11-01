#! /usr/bin/env python3

class Python_Noob: 
    def __init__(self, age = 0): 
         self._age = age 
         print(f"constructor created age for this class: {age}")
      
    
    def get_age(self): 
        return self._age 
      
    
    def set_age(self, x): 
        if x > 30:
            x = 10
            print(f"this setter method changed age to: {x}")
        self._age = x 
  
me = Python_Noob() 
  
me.set_age(99) 
  
print(f"get_age method get_age will now show age: {me.get_age()}") 
  
print(f"new_class.age also shows: {me._age}")