
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   count = 0
   maximum= 0
   for i in range(len(int_list)-1):
      if int_list(i) > int_list(i+1):
         maximum = int_list(i)
      # elif int_list(i) <= int_list(i+1):
      #    continue
      elif len(int_list) ==0:
         return None
      elif int_list == None:
         raise ValueError


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
