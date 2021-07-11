# Time complexity O(log2(n))

from random import randint

def binary_search(sequence,item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

a = [randint(0,100) for i in range(20)]
a.sort()

print(binary_search(a,66))