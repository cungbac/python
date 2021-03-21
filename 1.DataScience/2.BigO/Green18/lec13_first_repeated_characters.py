def get_index(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a')
    return ord(c) - ord('A') + 26

cnt = [0]*52
a = input()
ans = 'null'

for str in a:
    idx = get_index(str)
    cnt[idx] += 1
    if cnt[idx] == 2:
        ans = str
        break
print(ans)

# --------------------------------------------

def get_unique_string(m):
    """get unique characters of a string"""
    string = ''
    full = ''
    for i in range(len(m)):
        if full.find(m[i]) < 0:
            string = m[i]
            full = full + string
    return full

# Input & Output

a = input()
b = get_unique_string(a)


if b == a:
    print('null')
else:
    count = 0
    c = []
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                count += 1
        c.append(count)
        count = 0

    d = []
    for i in range(len(c)):
        if c[i] > 1:
            d.append(b[i])


    count = 0
    e = [i*0 for i in range(len(d))]
    for i in range(len(a)):
        for j in range(len(d)):
            if a[i] == d[j]:
                e[j] += 1
            m = e[j]
            if m == 2:
                idx = j
                break
        else:
            continue
        break

    print(d[idx])

