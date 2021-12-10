"""I am starting over on this file because i encountered some errors trying to get my previouse class working"""

class User():
    """Starting this class to pass user input and return a neatly formatted string,
       after getting this class to work i will run some python test to make sure my code does not break"""
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def greet_user(self):
        full_name = self.first + " " + self.last
        return full_name.title()