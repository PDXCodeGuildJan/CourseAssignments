__author__ = "Tiffany Caires"
"""A module that can be used to read and write morse code messages."""

from morse import morse
import re

def read_code(file):
   """Reads the message in the given file and returns the English translation."""
   
   # Open the file
   mess_file = open(file, "r")

   # Read in it's contents
   message = mess_file.read()

   # Close the file
   mess_file.close()

   # Translate the message and return it
   return morse_to_message(message)

def write_code(message, file):
   """Translates the given message to morse code and writes it to the file."""
   
   # First, translate the message
   translation = message_to_morse(message)

   # Open the file
   new_file = open(file, "w")
   # Write to the file
   new_file.write(translation)
   # Close the file
   new_file.close()

def message_to_morse(message):
   translation = ""
   for char in message.upper():
      if char in morse:
         translation += morse[char]
         translation += "   "
      elif char == " ":
         translation += "       "
      
   return translation

def morse_to_message(message):
   translation = ""

   # Break the message into words
   words = re.split("\s{7}", message)
   # For every word in the message
   for word in words:

      # Break the word into letters
      letters = re.split("\s{3}", word)
      # For every letter in a word
      for char in letters:
         # Find the key for the morse letter
         for letter,code in morse.items():
            if code == char:
               translation += letter
               
      # Add a space between each word
      translation += " "

   return translation


def main():
   
   print(read_code("test_code.txt"))

   write_code(
         "Corgis are the best breed of dog, I don't care what you say.", 
         "test_code.txt")


if __name__ == '__main__':
   main()