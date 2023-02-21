"""Tis model stores only user class """
class User:
    """ This is a class that models a user """
    def __init__(self,first_name,last_name,age,city,country):
        """ initializes a user profile """
        self.first=first_name
        self.last=last_name
        self.age=age
        self.city=city
        self.country=country


    def describe_user(self):
        """ Prints summary of user information """
        print(f'\nThis user is called {self.first} {self.last}. \nHe is {self.age} years old. \nHe is from { self.city} city, {self.country}')


    def greet_user(self):
        """ Prints personalized greeting for a user  """
        print(f'Hello, {self.first} {self.last}')