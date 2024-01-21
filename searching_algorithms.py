def binary_search(alist, target, low=None, high=None):
    '''Performs a binary search on a list.

    Args:
        alist (list): The list that will be searched
        target (int): The item the function will search for
        low (int): The index of the lower bound of the list slice
            (default is None)
        high (int): The index of the upper bound of the list slice
            (default is None)
    '''
    
    if low is None:
        low = 0
    if high is None:
        high = len(alist) - 1
    if high < low:
        return -1
    
    midpoint = (low + high) // 2

    if alist[midpoint] == target:
        return midpoint
    elif target < alist[midpoint]:
        return binary_search(alist, target, low, midpoint-1)
    else:
        return binary_search(alist, target, midpoint+1, high)

alist = [1, 3, 5, 10, 12]
print(binary_search(alist, 10))
