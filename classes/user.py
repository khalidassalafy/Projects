""" this module stores  user class and its child admin class"""
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


class Admin (User):
    """Represents a specific user, the admin  """
    def __init__(self,first_name,last_name,age,city,country):
        """Initialize admin with all the attributes in the paren class
           then initialize attributes specific to admin"""
        super().__init__(first_name,last_name,age,city,country)
        self.privileges=["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        """ Displays the privileges of an admin"""
        print ('The Admin has the following privileges: ')
        for privilege in self.privileges:
            print(f'-{privilege}')