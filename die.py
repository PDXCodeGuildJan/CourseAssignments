from random import randint

# Create a die function that returns a random number, as if 
# the user rolled a die.
def die():
   roll = randint(1, 6)
   print(roll)


# Make a function called custom_die that takes a range 
# and print a random number in that range.
def custom_die(num1, num2):
   roll = randint(num1, num2)

   print("{} {}".format(roll, "Critical Miss!" if roll == min 
        else "Critical Hit!" if roll == max else ""))

   if roll == num1:
      print("{} Critical Fail!".format(roll))
   elif roll == num2:
      print("{r} Critical Hit!".format(r=roll))
   else:
      print(roll)

   "{1} is {0} and is from {2}".format(name, age, place)
   
   # Determine if roll is the max possible result
   # or if roll is the min possible result

   # This will also need to change some ;)
   print(roll)


def main():
   print("Welcome to Die Roller. Enter q to exit.")

   entree = ""

   # Wrap the core logic of the function in a while loop,
   # so that it keeps asking to roll, until we exit.
   while entree != "q":

      # Ask the user how many dice to roll
      entree = input("How many Dice rolls do you want to roll? ")
      if entree.lower() == "q":
         # Exit the program
         exit()

      total_rolls = int(entree)

      #Find out how big the Dice are
      entree = input("How many sides on the Dice? ")
      if entree == "q":
         #Exit the program
         exit()

      max_num = int(entree)

      # Roll that many dice
      for something in range(0, total_rolls):
         custom_die(1, max_num)

main()










