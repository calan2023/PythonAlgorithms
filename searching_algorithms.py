def linear_search(alist, target):
    '''Performs a linear search on an unordered list.

    Args:
        alist (list): The unordered list that will be searched
        target (int): The item the function will search for
    '''
    
    comparisons = 0
    found = False
    index = 0
    while not found and index < len(alist):
        comparisons += 1
        if alist[index] == target:
            found = True
        else:
            index += 1
        
    print('Unordered Linear Search: {} comparisons'.format(comparisons))
    if found:
        print('{} found at index {}'.format(target, index))
    else:
        print('{} is not in the list'.format(target))

def ordered_linear_search(alist, target):
    '''Performs a linear search on an ordered list.

    Args:
        alist (list): The ordered list that will be searched
        target (int): The item the function will search for
    '''
    
    comparisons = 0
    found = False
    stop = False
    index = 0
    while not stop and not found and index < len(alist):
        comparisons += 1
        if alist[index] == target:
            found = True
        else:
            if alist[index] > target:
                stop = True
            else:
                index += 1

    print('Ordered Linear Search: {} comparisons'.format(comparisons))
    if found:
        print('{} found at index {}'.format(target, index))
    else:
        print('{} is not in the list'.format(target))

def binary_search(alist, target, low=None, high=None, comparisons=0):
    '''Performs a binary search on a list via recursion.

    Args:
        alist (list): The ordered list that will be searched
        target (int): The item the function will search for
        low (int): The index of the lower bound of the list slice
            (default is None)
        high (int): The index of the upper bound of the list slice
            (default is None)
        comparions (int): The number of comparisons made so far
            (default is 0)
    '''
    
    if low is None:
        low = 0
    if high is None:
        high = len(alist) - 1
    if high < low:
        print('Binary Search: {} comparisons'.format(comparisons))
        print('{} is not in the list'.format(target))
        return
    
    midpoint = (low + high) // 2

    comparisons += 1
    if alist[midpoint] == target:
        print('Binary Search: {} comparisons'.format(comparisons))
        print('{} found at index {}'.format(target, midpoint))
        return
        
    comparisons += 1    
    if target < alist[midpoint]:
        return binary_search(alist, target, low, midpoint-1, comparisons)
    else:
        return binary_search(alist, target, midpoint+1, high, comparisons)

def hashtable_linearprobe_search(alist, target, table_size=11):
    comparisons = 0
    table = [None] * table_size
    for item in alist:
        hash_value = item % table_size
        while table[hash_value] is not None:
            hash_value = (hash_value + 1) % table_size
        table[hash_value] = item
        
    target_hash_value = target % table_size
    comparisons += 1
    while table[target_hash_value] != target and table[target_hash_value] is not None:
        target_hash_value = (target_hash_value + 1) % table_size
        comparisons += 1

    if table[target_hash_value] is None:
        print('Hash Table Search: {} comparisons'.format(comparisons))
        print('{} is not in the list'.format(target))
    else:
        print('Hash Table Search: {} comparisons'.format(comparisons))
        print('{} is in the list'.format(target))        
    print('Hash Table:', table)

alist = [1, 3, 5, 10, 12, 14, 4]
hashtable_linearprobe_search(alist, 0)
