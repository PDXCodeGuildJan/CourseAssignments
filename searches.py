"""Search functions, including Binary. """

from sorts import insertion_sort

def main():
   # Make the list to look through, and the target value
   unsorted_list = ["E", "Z", "L", "O", "B", "F"]
   target_value = "B"

   # Call the search function, catch what it returns
   sorted_list, target_index = binary_search(unsorted_list, target_value)

   # Print out our solutions
   print("I found", target_value, "It's at", target_index)

def binary_search(the_list, target_value):
   """Implements the Binary Search algorithm."""

   # First, sort the list
   sorted_list = insertion_sort(the_list)
   
   # Search for the target value

   # Find length of current segment
   length = len(sorted_list)

   # Initialize start and end variables
   start = 0
   end = length

   # if len >= 1, look for target:
   while length >= 1:
      #  Find the current length and mid point of the segment we're looking in
      mid = start + (length // 2)

      # Determine if middle value is greater or less than, or equal
      # If equal, we've found it, return middle
      if sorted_list[mid] == target_value:
         return (sorted_list, mid)

      # If greater than, reduce segment to left half from middle, repeat loop
      elif sorted_list[mid] > target_value:
         end = mid

      # If less than, reduce segment to right half from middle, repeat loop
      elif sorted_list[mid] < target_value:
         start = mid + 1

      # Reevaluate length before the loop runs again
      length = len(sorted_list[start:end])
         
   # If we can't find the index, return -1
   return (sorted_list, -1)


# Call main to sort the things
if __name__ == "__main__":
   main()

