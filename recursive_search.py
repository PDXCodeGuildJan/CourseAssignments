"""Search functions, including Binary. """

from sorts import insertion_sort

def main():
   # Make the list to look through, and the target value
   unsorted_list = ["E", "Z", "L", "O", "B", "F"]
   sorted_list = insertion_sort(unsorted_list)
   target_value = "B"

   # Call the search function, catch what it returns
   target_index = binary_search(sorted_list, target_value, 0, 6)

   # Print out our solutions
   print("I found", target_value, "It's at", target_index)

def binary_search(sorted_list, target_value, start, end):
   """Implements the Binary Search algorithm."""   
   # Search for the target value
   print("Start:", start, "End:", end)

   # Find length of current segment
   length = len(sorted_list[start:end])

   # if len >= 1, look for target:
   if length >= 1:
      #  Find the current length and mid point of the segment we're looking in
      mid = start + (length // 2)

      # Determine if middle value is greater or less than, or equal
      # If equal, we've found it, return middle
      if sorted_list[mid] == target_value:
         print("Found!", mid)
         return mid

      # If greater than, reduce segment to left half from middle, repeat loop
      elif sorted_list[mid] > target_value:
         end = mid

      # If less than, reduce segment to right half from middle, repeat loop
      elif sorted_list[mid] < target_value:
         start = mid + 1

      return binary_search(sorted_list, target_value, start, end)
         
   # If we can't find the index, return -1
   else: 
      print("Didn't find")
      return -1


# Call main to sort the things
if __name__ == "__main__":
   main()

