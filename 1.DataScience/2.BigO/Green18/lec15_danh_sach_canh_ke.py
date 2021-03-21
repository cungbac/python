
class edge:
    def __init__(self,u = None, v = None):
        self.u = u
        self.v = v

n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

edge_list = []
flag = True
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 1:
            temp = edge(i,j)
            edge_list.append(temp)

print(len(edge_list))
for i in range(len(edge_list)): 
    print(edge_list[i].u,edge_list[i].v)