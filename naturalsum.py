import sys

n = int(sys.stdin.readline().rstrip())

s = 0
while n > 0:
    val = int(sys.stdin.readline().rstrip())
    if val % 2 == 0:
        s += val
    n -= 1

print(s)
