class Counter:
    count = 0 # class attribute — shared across instances


    def __init__(self):
        self.id = Counter.count # give each instance an id
        Counter.count += 1

class Bag:
    items = [] # shared list — usually not what you want


    def __init__(self):
        pass


b1 = Bag()
b2 = Bag()
b1.items.append('apple')
print(b2.items) # ['apple'] <-- surprise!
print(Bag.items)


c1 = Counter()
c2 = Counter()
print(c1.id, c2.id) 
print(Counter.count) # 2