def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    count = 0
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    else:
        maximum = int_list[0]
        for i in range(len(int_list)):
            if int_list[i] > maximum:
                maximum = int_list[i]
        # elif int_list(i) <= int_list(i+1):
        #    continue
    return maximum


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    else:
        if (len(int_list)==0):
            return int_list
        return((int_list[len(int_list)-1:]) + reverse_rec(int_list[:len(int_list)-1]))



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    if high == target:
        return high
    elif low == target:
        return low
    elif ((len(int_list)-1)//2) == target:
        return (len(int_list)-1)//2
    if target<int_list((len(int_list)-1)//2):
        bin_search(target,low,(len(int_list)-1)//2,int_list)
    if target>int_list((len(int_list)-1)//2):
        bin_search(target,(len(int_list)-1)//2,high,int_list)
    return None





