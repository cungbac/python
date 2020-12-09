a = float(input())
PI = 3.14
print('{:.2f}'.format(2*a*PI))
print('{:.2f}'.format(a**2*PI))

a, b, c = map(float,input().split())
print('{:.2f}'.format(a+b+c),'{:.2f}'.format((((a+b+c)/2)*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**(1/2)))

a = int(input())
b = float(input())
c = int(input())

print('{:.2f}'.format(a*b+c))

a = str(input())
print(int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4]))


print(a//10) # lay phan nguyen

(a%10 + (a // 10)%10 + ((a // 10) // 10)%10 + (((a // 10) // 10)//10)%10 + ((((a // 10) // 10)//10) //10)%10) %10 

