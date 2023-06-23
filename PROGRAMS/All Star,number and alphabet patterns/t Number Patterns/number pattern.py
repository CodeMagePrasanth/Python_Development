n = 4
sp = 3
spa = 1
for i in range(n + 1, 1, -1):
    print('-' * sp, end='')
    for j in range(i, n + 2):
        print(i, end='')
    for j in range(i, n + 1):
        print(i, end='')
    sp -= 1
    print()
for a in range(n - 1, n + 2):
    print('-' * spa, end='')
    for b in range(a, n + 2):
        print(a, end='')
    for c in range(a + 1, n + 2):
        print(a, end='')
    spa += 1
    print()

'''
output:

---5
--444
-33333
2222222
-33333
--444
---5

'''