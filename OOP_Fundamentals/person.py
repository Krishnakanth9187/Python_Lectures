class Person:
    """A simple Person class showing constructor, attributes and methods."""


    # class attribute (shared by all instances)
    species = 'Homo sapiens'


    def __init__(self, name, age):
        # instance attributes (unique to each object)
        print(f"=============={self}")
        self.name1 = name
        self.age = age
        self._friend_names = [] # an internal list representing state


    def greet(self):
        """Instance method: uses `self` to access instance attributes."""
        return f"Hi, I'm {self.name1} and I'm {self.age} years old."


    def add_friend(self, friend_name):
        """Modify the object's state stored in instance attributes."""
        self._friend_names.append(friend_name)


    def get_friends(self):
        return list(self._friend_names) # return a copy for safety


    @classmethod
    def common_species(cls):
        """Class method: receives the class itself as `cls`."""
        return cls.species


    @staticmethod
    def is_adult(age):
        """Static method: utility function that doesn't access class/instance data."""
        return age >= 18
    

class Counter:
    count = 0 # class attribute — shared across instances


    def __init__(self):
        self.id = Counter.count # give each instance an id
        Counter.count += 1