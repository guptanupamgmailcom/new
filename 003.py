"""class temp_convert:#Not working
    b=(int(input("Enter a value : ")))
    def __init__(self):
        self.a=((input("Do you want to convert from Celsius to Fahrenheit? ")))
        if self.a == "1":
            fahr=temp_convert.b*1.8+32
            print(f"{temp_convert.b} degrees celsius is equal to {fahr} fahrenheits.")
        elif self.a == "0":
            cel = (temp_convert.b-32)/1.8
            print(f"{temp_convert.b} fahrenheits is equal to {cel} degrees celsius.")
        else:
            print(f"Please enter a valid response in True or False{self.a}")
        return temp_convert"""


class Converter:
    def celsius2Fahrenheit(self,a) :
        self.b=a*1.8+32
        print(f"{a} degrees celsius is {self.b} fahrenheit. ")

    def fahrenheit2celsius(self,x):
        self.y=(x-32)/1.8
        print(f"{x} fahrenheits is {self.y} degrees celsius. ")

ab=Converter()
bd=Converter()
ab.celsius2Fahrenheit(20)
bd.fahrenheit2celsius(68)

