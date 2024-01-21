def binary_search(l, target, low=None, high=None):
    """binary search"""
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1
    
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)

l = [1, 3, 5, 10, 12]
print(binary_search(l, 10))
