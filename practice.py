
def main():
   
   user_input = input("Please provide a word: ")

   middle_3(user_input)
   loop(user_input)

   my_list = ["This", "is",4,  "a random", 3]
   loop(my_list)


def middle_3(the_string):
   mid = len(the_string)//2
   print(the_string[mid-1:mid+2])

def loop(the_sequence):
   print(the_sequence)
   for x in the_sequence:
      print(x)


main()