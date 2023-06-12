# s = "Be ConSisTent"
# res = ''
# for i in s:
#     if ('A' <= i <= 'Z'):
#         res += chr(ord(i)+32)
#     elif ('a' <= i <= 'z'):
#         res += chr(ord(i)-32)
#     else:
#         res += i
# print(res)


# reverse  it


s = "Be ConSisTent"
res = ''
for i in s:
    if ('A' <= i <= 'Z'):
        res += chr(ord(i) + 32)
    elif ('a' <= i <= 'z'):
        res += chr(ord(i) - 32)
    else:
        res += i
for i in range(-1,-12,-1):
    res += s[i]
    print(res)

