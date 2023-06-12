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


s = "Be ConSisTent"
res = ''
for i in range(-1,-13,-1):
    res += s[i]
    for i in s:
        if ('A' <= i <= 'Z'):
            res += chr(ord(i) + 32)
        elif ('a' <= i <= 'z'):
            res += chr(ord(i) - 32)
        else:
            res += i
print(res)
