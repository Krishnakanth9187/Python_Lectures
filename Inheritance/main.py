from animal import Animal, Dog, Cat, Fish, Duck, A, B, C, D, BankAccount

d = Dog()
print(d.legs, d.name)

m = Cat()

d.speak()

m.speak()

f = Fish()

f.swim()

duck = Duck()
duck.swim()
duck.fly()

t = D()
t.show()
print(D.mro())


meenu = BankAccount(100)
# print(meenu.get_balance("pass1"))
# print(meenu.__balance)

meenu.balance = 120
print(meenu.balance)


