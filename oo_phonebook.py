"""A Phonebook program implemented with classes."""

__author__ = "Tiffany Caires"

class Contact:
   """Defines the Contact object to store information about people."""

   def __init__(self, f_name, l_name):
      # Assign passed arguments to their corresponding properties
      self.first_name = f_name
      self.last_name = l_name

      self.phone_num = ""
      self.addresses = {}
      self.email = ""

   def update_address(self, addy_key, street="",
         unit="", city="", state="", zip="", country=""):
      """Update the address at addy_key with the info passed."""
      pass

   def format_phone_num(self, phone_num):
      """Format the phone number of the contact all pretty-like."""
      pass

   def print_contact(self):
      """Print out the contact's info, all pretty-like."""
      pass


class Address:
   """Defines the Address object to be used with Contact."""

   def __init__(self):
      self.street = ""
      self.unit = ""
      self.city = ""
      self.state = ""
      self.zip_code = ""
      self.country = ""

   def __str__(self):
      """Print out the address, formated all pretty-like."""
      formated_str = self.street
      
      if self.unit != "":
         formated_str += "\n" + self.unit

      formated_str += "\n" + self.city + " " +self.state 
      formated_str += " " + self.zip_code 
      formated_str += "\n" + self.country

      return formated_str





