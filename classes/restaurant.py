""" This is module  that stores restaurant class"""
class Restaurant:
    """ This is a class that models restaurant """
    def __init__(self,restaurant_name,cuisine_type):
        """ Initializes a restaurant name and its type of cuisine  """
        self.name=restaurant_name
        self.cuisine=cuisine_type


    def describe_restaurant(self):
        """ Describes a restaurant  """
        print(f'\nThis restaurant is called {self.name}, it serves {self.cuisine} cuisine')


    def open_restaurant(self):
        """ It tells if a restaurant is open """
        print (f'\n{self.name} is open!')