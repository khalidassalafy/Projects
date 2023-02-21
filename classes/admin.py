"""This module stores Admin class that is a child of User class """

# let's import its parent first into the module
from users import User

#Let's define the class
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