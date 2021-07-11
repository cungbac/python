# a = binary(100000000000000)
a = '10110101111001100010000011110100100000000000000'

def max_binary(a):
    flag = True
    count = 0
    max = 0
    for i in a:
        if int(i) == 1:
            count += 1
            if count > max:
                max = count
        if int(i) == 0:
            count = 0
    return max

print(max_binary(a))