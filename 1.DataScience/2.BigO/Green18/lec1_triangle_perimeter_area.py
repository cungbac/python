a, b, c = map(float,input().split())
print('{:.2f}'.format(a+b+c),'{:.2f}'.format((((a+b+c)/2)*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**(1/2)))