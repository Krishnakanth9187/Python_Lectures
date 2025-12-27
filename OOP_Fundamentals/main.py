from person import Person
from person import Counter

meenu = Person('Meenakshi', 23)
bob = Person('Bob', 17)

print(f"Name: {bob.name1}, Age: {bob.age}")

c = Counter()


print(meenu.greet()) # Hi, I'm Alice and I'm 30 years old.
print(Person.common_species())# Homo sapiens
print(Person.is_adult(bob.age)) # False




# meenu.add_friend('Bob')
# print(meenu.get_friends()) # ['Bob']
# print(bob.get_friends()) # [] <-- different instance state
