#!/usr/bin/python3
"""
thi module defines User class
"""


class User():
    """ class that defines a user """

    def __init__(self):
        """ Initialization method """
        self.__email = None

    @property
    def email(self):
        """ get the email address of the user """
        return self.__email

    @email.setter
    def email(self, value):
        """ setter for attribute email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """
    Main function to demonstrate usage of the User class.
    """
    u = User()
    u.email = "john@snow.com"
    print(u.email)
