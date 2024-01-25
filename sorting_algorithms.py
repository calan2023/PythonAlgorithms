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
    
alist = [2, 1, 3, 4, 5]
shell_sort(alist)
print(alist)
