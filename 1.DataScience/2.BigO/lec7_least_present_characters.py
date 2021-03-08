
def get_unique_string(m):
    """get unique characters of a string"""
    string = ''
    full = ''
    for i in range(len(m)):
        if full.find(m[i]) < 0:
            string = m[i]
            full = full + string
    return full

def get_max(a):
    """get a max number of a list"""
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

def count_string(m,n):
    """get a charater which appears least time in another string"""
    m = m.lower()
    n = n.lower()
    count_list = []
    # get count of a character (of m) in n
    for i in range(len(m)):
        p = m[i]
        x = 0
        for j in range(len(n)):
            if n[j] == p:
                x += 1
        count_list.append(x)
        x = 0
    # get min of count
    min = get_max(count_list)
    for i in range(len(count_list)):
        if count_list[i] < min:
            min = count_list[i]

    # extract list of strings have min
    string_list = []
    for i in range(len(count_list)):
        if count_list[i] == min:
            w = m[i]
            string_list.append(w)
    
    # find min ord of ASCII code of the min string_list
    min_ord = 1000
    for i in range(len(string_list)):
        if ord(string_list[i]) < min_ord:
            min_ord = ord(string_list[i])

    # extract the string which has minimum ASCII number
    for i in range(len(string_list)):
        if ord(string_list[i]) == min_ord:
            text = string_list[i]
    return text.upper()

# Input and Output
n = int(input())
a = []
for i in range(n):
    temp = input()
    a.append(temp)

for text in a:
    print(count_string(get_unique_string(text),text))
