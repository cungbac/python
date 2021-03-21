def get_unique_string(m):
    """get unique characters of a string"""
    string = ''
    full = ''
    for i in range(len(m)):
        if full.find(m[i]) < 0:
            string = m[i]
            full = full + string
    return full

# Input and Output
a = input()
a = get_unique_string(a)
print(len(a))