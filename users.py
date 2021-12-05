""" Intentions of this class is to be able to tell if it is a new user or old user and welcome them appropriately."""
import json

class UserName():
    """ Simple class that ask a user to input his name and records that name in a new file for every new user"""
    def __init__(self, username):
    	self.username = username

    def greet_user(self):
    	file_name = self.username

    	with open(file_name, "w") as f_name:
    		json.dump(self.username, f_name)
    		print("We'll remember you when you come back, " + self.username + "!.")