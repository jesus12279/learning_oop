import unittest
from users import User

"""imported unittest from python built in functions to test that my User class worked corrrectly"""
class NameTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = User("janis", "joplin")
		self.assertEqual(formatted_name.greet_user(), "Janis Joplin")


unittest.main()