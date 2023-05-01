s = "Be ConSisTent"
res = ''
for i in s:
    if ('A' <= i <= 'Z'):
        res += chr(ord(i)+32)
    elif ('a' <= i <= 'z'):
        res += chr(ord(i)-32)
    else:
        res += i
print(res)


# reverse  it


s = "Be ConSisTent"
res = ''
for i in s:
    if ('a' <= i <= 'z'):
        res += chr(ord(i) - 32)
    elif ('A' <= i <= 'Z'):
        res += chr(ord(i) + 32)
    else:
        res += i
print(res)
for i in range(0,13,-1):
    res += s[i]
print(res)