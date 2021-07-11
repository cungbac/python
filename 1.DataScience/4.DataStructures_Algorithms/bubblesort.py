# Time complexity O(n2)

def bubble_sort(lst):
    index = len(lst) - 1
    sorted = False # Variable for while loop

    while not sorted: # Run while loop until sorted = True
        sorted = True # Break the while loop whenever gone through all the values

        for i in range(index):
            x = lst[i]
            y = lst[i + 1]
            if lst[i] > lst[i+1]:
                sorted = False # Keep continue if sorting is not finished
                lst[i], lst[i+1] = lst[i+1], lst[i] # switch values
    return lst

def bubble_sort_2(lst):
    index = len(a) - 1
    while index >= 0:
        for i in range(index):
            x = lst[i]
            y = lst[i + 1]
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        index -= 1
    return lst

a = [1,6,4,30,7,20,2]
# print(bubble_sort(a))
print(bubble_sort_2(a))