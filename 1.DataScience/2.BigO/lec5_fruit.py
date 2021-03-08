n = int(input())
the_list = []

for i in range(n):
    x = list(map(int,input().split()))
    the_list.append(x)

def get_max_tao(a):
    max = 0
    for i in range(len(a)):
        if a[i][0] > max:
            max = a[i][0]
    return max
max_tao = get_max_tao(the_list)

def get_max_cam(a):
    max = 0
    for i in range(len(a)):
        if a[i][0] == max_tao and a[i][1] > max:
            max = a[i][1]
    return max
max_cam = get_max_cam(the_list)

def count_max(a):
    x = 0
    for i in range(len(a)):
        if a[i][0] == max_tao:
            x += 1
    return x

no_of_max = count_max(the_list)

for i in range(n):
    if no_of_max == 1:
      if the_list[i][0] == max_tao:
        	index = i + 1
        	break
    if no_of_max > 1:
    	if the_list[i][0] == max_tao and the_list[i][1] == max_cam:
        	index = i + 1
        	break
print(index)