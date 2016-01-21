__author__ = "Tiffany Caires"

"""Implements the merge sort algorithm, recursively, in Python."""

def main():
   """Take a random list and use merge_sort to sort it"""

   unsorted = [4, 7, 14, 2, 94, 38, 2]
   sorted = merge_sort(unsorted)
   print(sorted)


def merge_sort(unsorted):
   """Implement the merge sort algorithm"""
   
   # Third Simplest
   pass

   # merge_sort
   #    Split the list into two halves, if list length more than 1
   #    first_sorted = sort the first half using merge_sort
   #    second_sorted = sort the second half using merge_sort
   #    merge the two sorted halves back together into a merged list
   #    return the merged, sorted list


def merge(list_1, list_2):
   """Given two lists, merge them together into a third list,
      which is sorted."""

   # Second Simplest
   pass

if __name__ == '__main__':
   main()