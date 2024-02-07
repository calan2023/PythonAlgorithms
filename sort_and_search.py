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
        pass
    elif algorithm_type == '2':
        pass

if __name__ == '__main__':
    main()
