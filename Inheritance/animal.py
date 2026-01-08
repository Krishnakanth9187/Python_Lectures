class Animal:
    def __init__(self):
        self.name = "meenu"
        self.heart = True

    def speak(self):
        print("The animal makes a sound")




class Dog(Animal): # Dog inherits from Animal
    def __init__(self):
        super().__init__()
        self.bark = True
        self.legs = 4
    def speak(self):
        super().speak()
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"meowwwwwwwwwwwwwwwww")  

#================================================================================
class Flyable:
    def fly(self):
        print("Can fly")




class Swimmable:
    def swim(self):
        print("Can swim")


class Fish(Swimmable):
    pass
    


class Duck(Flyable, Swimmable):
    pass

#=====================================================================================

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
     print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass

#======================================================================================
# If relationship is "has-a", not "is-a"

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

#==========================================================================

class Person:
    def __init__(self, name):
        self.name = name # public

#=============================================================================
class BankAccount:
    def __init__(self, balance):
        self.balance = balance # private


    def deposit(self, amount):
        self.balance += amount


    def get_balance(self, password):
        if password =="pass":
            return self.balance
        else:
            print("password incorrect")


