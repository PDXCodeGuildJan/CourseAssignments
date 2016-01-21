""" A series of various sort algorithm implementations.
    Author: Tiffany

"""

def main():

   # Use insertion sort
   sorted_list = insertion_sort(["E", "Z", "L", "O", "B", "F"])
   print(sorted_list)

def swap(the_list, index_a, index_b):
   """Swaps two items in a list."""

   the_list[index_a], the_list[index_b] = the_list[index_b], the_list[index_a]

   # # Make a temp to hold one value
   # temp = the_list[index_a]

   # # Swap the values
   # the_list[index_a] = the_list[index_b]
   # the_list[index_b] = temp

   # Return list with swapped items
   return the_list

def insertion_sort(the_list):
   """Sort the list using the insertion algorithm."""

   for start_index, value in enumerate(the_list):

      # make a temp variable for the index of the thing
      # we're currently sorting
      lost_index = start_index
      lost_value = value

      # Look for where the lost index's value belongs
      while (lost_value < the_list[lost_index - 1] 
            and lost_index > 0):

         # Swap the lost value with it's adjacent value
         the_list = swap(the_list, lost_index, lost_index-1)

         # Decrement the lost_index
         lost_index -= 1

   # Return the sorted list
   return the_list

# Call main to sort the things
if __name__ == "__main__":
   main()

