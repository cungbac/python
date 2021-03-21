
def inverse_string(a):
    list_1 = a.split()
    text = ''
    list_2  = []
    for i in range(len(list_1)):
        m = len(list_1[i])
        while m > 0:
            m -= 1
            text = text + list_1[i][m]
        list_2.append(text)
        text = ''
    return list_2

def manipulate_string_to_list(a):
    b = inverse_string(a)
    c = []
    for i in range(len(b)):
        m = len(b[i])
        if b[i].find('.') == 0:
            x = i + 1
            c.append(x)
    u = []    
    flag = True
    for j in range(len(b)):
        for i in c:
            if i == j:
                x = 'Yes'
                break
            else:
                x = 'No'
        u.append(x)
    return u

def get_clear_list(a):
    if len(a.split()) <= 1:
        u = a.split()
    else:
        b = manipulate_string_to_list(a)
        c = a.split()
        u = []
        m = ''
        n = ''
        for i in range(len(c)):
            for j in range(len(c[i])):
                if b[i] == 'Yes':
                    if j == 0:
                        m = m + c[i][j].upper()
                    else:
                        m = m + c[i][j]
                else:
                    m = m + c[i][j]
            u.append(m)
            m = ''
    return u

# Input and Output

the_list = input()
u = get_clear_list(the_list)
text = ''
for i in range(len(u)):
    if i == 0:
        text = text + u[i]
    else:
        text = text + ' ' + u[i]

print(text)