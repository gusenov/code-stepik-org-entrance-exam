import sys


def expr(x):
    a = x / (x - 2018)
    b = (x - 500) / (x - 2500)
    c = a - b
    return c < 0


cnt = 0
for n in range(1, sys.maxsize):
    # print("n = %d" % n)
    if (n == 2018) or (n == 2500):
        continue
    if expr(n):
        cnt += 1
        print("cnt = %d" % cnt)
