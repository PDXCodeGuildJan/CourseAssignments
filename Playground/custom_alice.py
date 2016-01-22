"""A program to make a custom version of Alice in Wonderland,
   by replacing all instances of "Alice" with a user's input."""

__author__ = "Tiffany"

import re

def main():
   """Get a name from the user and then replace every instance 
      of "Alice" with the  given name."""

   # Welcome the users to the generator
   print("Wonderland Adventure Generator")
   print("-------------------------------------\n\n")

   # Prompt them for the name to use in the new version of the story
   new_name = input("Who do you wish to explore Wonderland? ")

   # Open the original story and grab all of the text.
   old_file = open("Alice_in_Wonderland.txt", "r")
   old_text = old_file.read()
   old_file.close()

   # Swap out all instances of Alice with the new name
   # First, replace any all-caps versions of Alice with 
   #     an all-caps version of the new name.
   new_text = re.sub("ALICE", new_name.upper(), old_text)

   # Then, replace all 'normal' versions of Alice with 
   #     'normal' versions of the new name.
   new_text = re.sub("Alice", new_name, new_text)

   # Write the new version of the story to a new file.
   file_name = new_name + "_in_Wonderland.txt"
   new_file = open(file_name, "w")
   new_file.write(new_text)
   new_file.close()

   # Tell the user we're done!
   print("Congratulations! The Adventures of", new_name, 
         "In Wonderland has been written to", file_name, "\n")
   print("Please remember that if you picked a male name, "
         "the book will still refer to them as a 'she'.\n\n\n")


   # Fin :D


if __name__ == '__main__':
   main()