from random import randint

# Create a die function that returns a random number, as if 
# the user rolled a die.
def die():
   roll = randint(1, 6)
   print(roll)


# Make a function called custom_die that takes a range 
# and print a random number in that range.
def custom_die(num1, num2):
   print(randint(num1, num2))


def main():
   # Ask the user how many dice to roll
   total_rolls = input("How many Dice rolls do you want to roll? ")
   total_rolls = int(total_rolls)

   #Find out how big the Dice are
   max_num = int(input("How many sides on the Dice? "))

   # Roll that many dice
   for something in range(0, total_rolls):
      custom_die(1, max_num)


main()