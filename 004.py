class land_animal:
    """used as inheritance of OOPS concept"""
    def function(self):
        print(f"{self} walks on land")

class marine_animal(land_animal):
    '''use print command to call a docstring'''
    def function(self):
        print(f"{self} can swim easily")

class flying_animal(marine_animal):
    '''docstrings can be called only if placed right after the class'''
    def function(self):
       print(f"{self} can fly. ")
ab=land_animal()
marine_animal.function("fish")  
land_animal.function("Dog")
flying_animal.function("Some birds")
print(land_animal.__doc__)
print(marine_animal.__doc__)
print("Hey")
