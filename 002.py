class amount:
    
    def calc_bill(self,total,disc ):
        self.total=total
        self.disc =disc
        amt = self.total*(100-self.disc)/100
        print(f"The total amount payable is {amt}")

table1=amount()
table1.calc_bill(100,15)

table2=amount()
table2.calc_bill(250,20)
table3=amount()
table3.calc_bill(500,10)

"""
class jodo:
    a,b =0,0
    def do(self,a,b):
        print(a+b)

f=jodo()
f.do(2,3)
"""
# Python3 program to
# demonstrate instantiating
# a class


"""class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
#print(Rodger.attr1)
Rodger.fun()
"""

"""class Dog:
   
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(f"This is a {a} and {b} dog.")

labrador=Dog("loving","Trustworthy")
puppy=Dog("Small","Cute")
print(Dog.__doc__)"""

class convert:
    """This docstring could be called upon."""
    def __init__(self):
        self.a=int(input("Please enter a value in degree Celcius :"))
        fahr=self.a*1.8+32
        print(f"{self.a} degree celsius is equal to {int(fahr)} fahrenheit")
anup=convert()


