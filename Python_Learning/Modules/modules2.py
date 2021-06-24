import math

tuplet = ('name','space')

list = [1,2,3,4,5,6]

dict = {
    'name':"name",
    'password':'password'}

class myClass:
    def __init__(self,name,password,keycode):
        self.name = name
        self.password = password
        self.keycode = keycode

def printer():
    print("Print from module2 pi ",math.pi)

def anotherModule2():
    print("AnotherFunctionModule2")