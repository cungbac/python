def sumEvenNum(lst,n):
    if n - 1 == 0:
        if lst[n-1] % 2 == 0:
            return lst[n-1]
    else:
        x = lst[n-1]
        if x % 2 == 0:
            return x + sumEvenNum(lst,n-1)
        else:
            return 0 + sumEvenNum(lst,n-1)

a = [4,1,3,6,2,5]
sumEvenNum(a,len(a))