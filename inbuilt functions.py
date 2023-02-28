L = ['we','are','ganjini']
print('@')
print('@'.join(L))
print('-'.join(L))
print('#'.join(L))
print('-1-'.join(L))
print('@'.join(L))
L.append(L[2])
print(L)

S =['NEED CLASS ON MONDAY',2,3,-3,4]
S.extend (S[0].split())
S.insert(S[2],S[-2])

T = (233,94,934,934,)
print(T.index (T[3]))
print(T)

W = (78,'abc',85,0,900,)
print(W.index(W[1]))
print(W)
