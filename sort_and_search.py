import random
from sorting_algorithms import *
from searching_algorithms import *

def random_list():
    lower_bound = input("What is the smallest item you want in the list?: ")
    while not lower_bound.isnumeric():
        print("Invalid input. Try again")
        lower_bound = input("What is the smallest item you want in the list?: ")
        
    upper_bound = input("What is the biggest item you want in the list?: ")
    while not upper_bound.isnumeric() or int(upper_bound) < int(lower_bound):
        print("Invalid input. Try again")
        upper_bound = input("What is the biggest item you want in the list?: ")
        
    num_items = input("How many items do you want in the list?: ")
    while not num_items.isnumeric():
        print("Invalid input. Try again")
        num_items = input("How many items do you want in the list?: ")
        
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)
    num_items = int(num_items)
    alist = []
    for i in range(num_items):
        rand_num = random.randint(lower_bound, upper_bound)
        alist.append(rand_num)
    return alist

def custom_list():
    alist = []
    stop = False
    while not stop:
        new_item = input("Input a new item to put in the list (or type 'D' to "\
                         "delete last item added, or type 'Q' to stop) and "\
                         "press Enter: ")
        if new_item.isnumeric():
            new_item = int(new_item)
            alist.append(new_item)
            print(f"\n{alist}")
        elif new_item in ['D', 'd']:
            alist.pop()
            print(f"\n{alist}")
        elif new_item in ['Q', 'q']:
            stop = True
        else:
            print("Invalid input. Try again")
    return alist

def sorting(alist):
    print('''\nSorting Algorithms:
1. Selection
2. Bubble
3. Insertion
4. Shell
5. Merge
6. Quick''')
    sorting_type = input("What type of sorting algorithm do you want to use?: ")
    while sorting_type not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid input. Try again")
        sorting_type = input("What type of sorting algorithm do you want to use?: ")
    if sorting_type == '1':
        selection_sort(alist)
    elif sorting_type == '2':
        bubble_sort(alist)
    elif sorting_type == '3':
        insertion_sort(alist)
    elif sorting_type == '4':
        shell_sort(alist)
    elif sorting_type == '5':
        merge_sort(alist)
    elif sorting_type == '6':
        quick_sort(alist)
    print(alist)

def searching(alist):
    ordered = True
    stop = False
    index = 1
    while not stop and index < len(alist):
        if alist[index-1] > alist[index]:
            ordered = False
            stop = True
        else:
            index += 1
            
    if ordered:
        print('''\nSearching Algorithms for Ordered Lists:
1. Linear Search
2. Ordered Linear Search
3. Binary Search
4. Hash Table Search''')
    else:
        print('''\nSearching Algorithms for Unordered Lists:
1. Linear Search
2. Hash Table Search''')
        
    searching_type = input("What type of searching algorithm do you want to use?: ")
    if ordered:
        while searching_type not in ['1', '2', '3', '4']:
            print("Invalid input. Try again")
            searching_type = input("What type of searching algorithm do you want to use?: ")
    else:
        while searching_type not in ['1', '2']:
            print("Invalid input. Try again")
            searching_type = input("What type of searching algorithm do you want to use?: ")            

    target = input("What item do you want to find in the list?: ")
    while not target.isnumeric():
        print("Invalid input. Try again")
        target = input("What item do you want to find in the list?: ")
    target = int(target)

    if ordered:
        if searching_type == '1':
            linear_search(alist, target)
        elif searching_type == '2':
            ordered_linear_search(alist, target)
        elif searching_type == '3':
            binary_search(alist, target)
        elif searching_type == '4':
            print('''\nHash Table Types:
1. Linear
2. Quadratic
3. Chaining''')
            hashtable_type = input("What type of hash table do you want to use?: ")
            while hashtable_type not in ['1', '2', '3']:
                print("Invalid input. Try again")
                hashtable_type = input("What type of hash table do you want to use?: ")
            hashtable_size = input("How many slots do you want your hash table to have?"\
                                   "\n(Note: if number of slots is less than number of items "\
                                   "in list, the program will automatically change number of slots"\
                                   "to be equal to the number of items in list + 1): ")
            while not hashtable_size.isnumeric():
                print("Invalid input. Try again")
                hashtable_size = input("How many slots do you want your hash table to have?: ")
            hashtable_size = int(hashtable_size)
            
            if hashtable_type == '1':
                hashtable_search(alist, target, 'Linear', hashtable_size)
            elif hashtable_type == '2':
                hashtable_search(alist, target, 'Quadratic', hashtable_size)
            elif hashtable_type == '3':
                hashtable_search(alist, target, 'Chaining', hashtable_size)
    else:
        if searching_type == '1':
            linear_search(alist, target)
        elif searching_type == '2':
            print('''\nHash Table Types:
1. Linear
2. Quadratic
3. Chaining''')
            hashtable_type = input("What type of hash table do you want to use?: ")
            while hashtable_type not in ['1', '2', '3']:
                print("Invalid input. Try again")
                hashtable_type = input("What type of hash table do you want to use?: ")
            hashtable_size = input("How many slots do you want your hash table to have?"\
                                   "\n(Note: if number of slots is less than number of items "\
                                   "in list, the program will automatically change number of slots"\
                                   "to be equal to the number of items in list + 1): ")
            while not hashtable_size.isnumeric():
                print("Invalid input. Try again")
                hashtable_size = input("How many slots do you want your hash table to have?: ")
            hashtable_size = int(hashtable_size)
            
            if hashtable_type == '1':
                hashtable_search(alist, target, 'Linear', hashtable_size)
            elif hashtable_type == '2':
                hashtable_search(alist, target, 'Quadratic', hashtable_size)
            elif hashtable_type == '3':
                hashtable_search(alist, target, 'Chaining', hashtable_size)

def main():
    print('''List Types:
1. Random List
2. Custom List''')
    list_type = input("What type of list do you want to make?: ")
    while list_type not in ['1', '2']:
        print("Invalid input. Try again")
        list_type = input("What type of list do you want to make?: ")      
    if list_type == '1':
        alist = random_list()
    elif list_type == '2':
        alist = custom_list()
    print(alist)
    
    print('''\nAlgorithm Types:
1. Sorting
2. Searching''')
    algorithm_type = input("What type of algorithm do you want to use?: ")
    while algorithm_type not in ['1', '2']:
        print("Invalid input. Try again")
        algorithm_type = input("What type of algorithm do you want to use?: ")
    if algorithm_type == '1':
        sorting(alist)
    elif algorithm_type == '2':
        searching(alist)

if __name__ == '__main__':
    main()
