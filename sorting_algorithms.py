def selection_sort(alist):
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

alist = [5,4,3,2,1]
selection_sort(alist)
print(alist)
