# input
n = int(input())
the_list = list(map(int,input().split()))
 
negative_num = 0
for i in range(len(the_list)):
    if the_list[i] > 0:
        negative_num += 1
 
positive_num = 0
for i in range(len(the_list)):
    if the_list[i] > 0:
        positive_num += 1
 
if positive_num == 0:
# array 2
    array_2 = []
    for i in range(len(the_list)):
        if the_list[i] != 0:
            array_2.append(the_list[i])
            if len(array_2) > 1:
                break
    
    array_1 = []
    for i in range(len(the_list)):
        if the_list[i] not in array_2 and the_list[i] != 0:
            array_1.append(the_list[i])
            break
        
    # array 3
    array_3 = []
    for i in range(len(the_list)):
        if the_list[i] not in array_1 and the_list[i] not in array_2:
            array_3.append(the_list[i])
else:
    array_1 = []
    for i in range(len(the_list)):
        if the_list[i] < 0:
            array_1.append(the_list[i])
            break
    
    array_2 = []
    for i in range(len(the_list)):
        if the_list[i] > 0:
            array_2.append(the_list[i])
    
    array_3 = []
    for i in range(len(the_list)):
        if the_list[i] not in array_1 and the_list[i] not in array_2:
            array_3.append(the_list[i])
 
 
# print
print(len(array_1), end = ' ')
for i in range(len(array_1)):
    print(array_1[i], end= ' ')

print(len(array_2), end= ' ')
for i in range(len(array_2)):
    print(array_2[i], end= ' ')

print(len(array_3), end= ' ')
for i in range(len(array_3)):
    print(array_3[i], end= ' ')