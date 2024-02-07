'''The module containing functions for the different kinds of sorting algorithms.
All functions print the number of key comparisons and/or the number of swaps made.
'''

def selection_sort(alist):
    '''Performs a selection sort on a list.

    Args:
        alist (list): The list that will be sorted
    '''
    
    comparisons = 0
    swaps = 0
    sorted_items = 0
    last_slot = -1
    for i in alist:
        currentmaxindex = 0
        for j in range(1, len(alist)-sorted_items):
            comparisons += 1
            if alist[j] > alist[currentmaxindex]:
                currentmaxindex = j
        swaps += 1
        alist[last_slot], alist[currentmaxindex] = alist[currentmaxindex], alist[last_slot]
        last_slot -= 1
        sorted_items += 1
    print('Selection sort: {} comparisons, {} swaps'.format(comparisons, swaps))

def bubble_sort(alist):
    '''Performs a bubble sort on a list.

    Args:
        alist (list): The list that will be sorted
    '''
    
    comparisons = 0
    swaps = 0
    sorted_items = 0
    for i in alist:
        exchanges = False
        for j in range((len(alist)-1)-sorted_items):
            comparisons += 1
            if alist[j] > alist[j+1]:
                exchanges = True
                swaps += 1
                alist[j], alist[j+1] = alist[j+1], alist[j]
        sorted_items += 1
        if not exchanges:
            break
    print('Bubble sort: {} comparisons, {} swaps'.format(comparisons, swaps))

def insertion_sort(alist):
    '''Performs an insertion sort on a list.

    Args:
        alist (list): The list that will be sorted
    '''
    
    comparisons = 0
    swaps = 0
    for i in range(1, len(alist)):
        curr_position = i
        comparisons += 1
        while curr_position > 0 and alist[curr_position-1] > alist[curr_position]:
            swaps += 1
            alist[curr_position-1], alist[curr_position] = alist[curr_position], alist[curr_position-1]
            curr_position -= 1
            if curr_position <= 0:
                break
            else:
                comparisons += 1
    print('Insertion sort: {} comparisons, {} swaps'.format(comparisons, swaps))

def shell_sort(alist):
    '''Performs a shell sort on a list.

    Args:
        alist (list): The list that will be sorted
    '''
    comparisons = 0
    swaps = 0
    gap = len(alist) // 2
    while gap > 0:
        for pos_start in range(gap):
            for i in range(pos_start+gap, len(alist), gap):
                curr_value = alist[i]
                curr_position = i
                comparisons += 1
                while curr_position >= gap and alist[curr_position-gap] > curr_value:
                    swaps += 1
                    alist[curr_position] = alist[curr_position-gap]
                    curr_position = curr_position - gap
                    if curr_position >= gap:
                        comparisons += 1
                alist[curr_position] = curr_value
        gap = gap // 2
    print('Shell sort: {} comparisons, {} swaps'.format(comparisons, swaps))

def merge_sort(alist):
    '''Performs a merge sort on a list.

    Args:
        alist (list): The list that will be sorted
    '''

    comparisons = 0
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        comparisons += merge_sort(left_half)
        comparisons += merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] <= right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
    print("Merging", alist)
    print('Merge sort: {} comparisons'.format(comparisons))
    return comparisons

def quick_sort(alist, first=None, last=None):
    '''Performs a merge sort on a list.

    Args:
        alist (list): The list that will be sorted
        first (int): The index of the first item in the list slice
            (default is None)
        last (int): The index of the last item in the list slice
            (default is None)
    '''
    
    comparisons = 0
    swaps = 0
    
    if first is None:
        first = 0
    if last is None:
        last = len(alist) - 1
        
    if first < last:
        pivot_val = alist[first]
        left_mark = first + 1
        right_mark = last
        done = False

        while not done:
            if left_mark <= right_mark:
                comparisons += 1
            while left_mark <= right_mark and alist[left_mark] <= pivot_val:
                left_mark = left_mark + 1
                if left_mark <= right_mark:
                    comparisons += 1

            if left_mark <= right_mark:
                comparisons += 1
            while left_mark <= right_mark and alist[right_mark] >= pivot_val:
                right_mark = right_mark - 1
                if left_mark <= right_mark:
                    comparisons += 1
                    
            if right_mark < left_mark:
                done = True
            else:
                swaps += 1
                alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
                left_mark += 1
                right_mark -= 1

        if first != right_mark:
            swaps += 1
        alist[first], alist[right_mark] = alist[right_mark], alist[first]
        split = right_mark
        
        comps_swaps = quick_sort(alist, first, split - 1)
        comparisons += comps_swaps[0]
        swaps += comps_swaps[1]
        
        comps_swaps = quick_sort(alist, split + 1, last)
        comparisons += comps_swaps[0]
        swaps += comps_swaps[1]

    print('Quick sort: {} comparisons, {} swaps'.format(comparisons, swaps))        
    return (comparisons, swaps)
