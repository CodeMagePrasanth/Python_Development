n = 5
for star in range(1, n + 1):
    print('*' * star)
print()
n = 5
for star in range(n, 0, -1):
    print('*' * star)

print()

n = 5
for star in range(1, n + 1):
    print('{}{}'.format(' ' * (n - star), '*' * (star)))

print()

n = 5
for star in range(n, 0, -1):
    print('{}{}'.format(' ' * (n - star), '*' * (star)))

print()

n = 5
for star in range(1, n + 1):
    print('{}{}{}'.format(' ' * (n - star), '*' * star, '*' * (star - 1)))
print()

n = 5
for star in range(n, 0, -1):
    print('{}{}{}'.format(' ' * (n - star), '*' * (star), '*' * (star - 1)))

print()


