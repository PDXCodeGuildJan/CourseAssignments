"""Implements a very simple Phonebook using a Dictionary."""

__author__ = "Tiffany Caires"

import re

# Initialize our dictionary, which will store our phone numbers
phonebook = {}

def main():
   """The main driver function of our Phonebook."""
   
   print("Welcome to the BEST Phonebook ever.")

   option = ""

   while option != "E":
      # Ask the user what they want to do.
      option = input("You can:\n\t(A)dd\n\t(D)elete\n\t(S)earch with Name\n\t(N)umber Search\n\t(P)rint\n\t(E)xit\nWhich would you like to do? ")

      if option.upper() == "A":
         name = input("What is the new contact's name? ")
         number = input("What is " + name + "'s number? ")
         add_contact(name, number)
      elif option.upper() == "D":
         name = input("What contact are you removing? ")
         delete_contact(name)
      elif option.upper() == "E":
         print("Good-bye!")
         exit()
      elif option.upper() == "P":
         print_phonebook()
      elif option.upper() == "S":
         name = input("What contact do you want to find? ")
         search(name)
      elif option.upper() == "N":
         number = input("What number are you looking for a contact with? ")
         search_by_number(number)
      else:
         print("I'm sorry, I did not understand.")


def add_contact(name, phonenumber):
   """Does an addition to the Phonebook with the given contact info."""

   # Remove any lingering whitespace that might have been added
   regex = "\s+\Z"
   thing_you_replace_with = ""
   scrubbed_name = re.sub(regex, thing_you_replace_with, name)

   # Scrub and reformat the phone number to follow (xxx) xxx-xxxx pattern
   # Remove all but the numbers
   regex = "[0-9]+"
   nums = re.findall(regex, phonenumber)
   new_num = ""
   for every_num in nums:
      new_num += every_num

   # Introduce the correct formatting
   formated_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]

   phonebook[scrubbed_name] = formated_num
   print("New Contact:", scrubbed_name, "was added with number", formated_num, "\n")

def delete_contact(name):
   """Removes the given contact from the Phonebook."""
   if name in phonebook:
      del phonebook[name]
      print(name, "was removed from the Phonebook.\n")

   else: 
      print("That contact already does not exist.\n")

def search(name):
   """Find and print the info of a contact, given their name."""
   if name in phonebook:
      number = phonebook[name]
      print(name, "'s number is", number, "\n")
   else:
      print("Sorry, no contact exists with that name.\n")

def search_by_number(search_number):
   """Find who a certain number is associated with."""
   result = ""
   for name, number in phonebook.items():
      if search_number == number:
         print(number, "'s name is", name, "/n")
         result = name        

   if result == "":
      print("Sorry, no contact has that number.\n")



def print_phonebook():
   """Prints every contact in the Phonebook in a pretty way."""

   print("Contacts:")
   print("-----------------------------------------")
   for name in phonebook:
      print(name, ":\t", phonebook[name], "\n")













if __name__ == '__main__':
   main()