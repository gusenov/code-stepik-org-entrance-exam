import sys

c = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

lim = max(c) + 1

for n in range(1, lim):
    if n % 2 == 0:
        c.discard(n)

for n in range(0, lim):
    if n % 3 == 0:
        if (n in c) or (-n in c):
            print(n, end=' ')
