import math

w = 7  # семь белых носков.
r = 5  # пять красных носков.
b = 3  # три черных носка.

wwrr = (7/15) * (6/14) * (5/13) * (4/12)  # вероятность события ББКК.

# Число различных возможностей:
p = math.factorial(4) / (math.factorial(2) * math.factorial(2))  # перестановки с повторениями.

wwbb = (7/15) * (6/14) * (3/13) * (2/12)  # вероятность события ББЧЧ.

rrbb = (5/15) * (4/14) * (3/13) * (2/12)  # вероятность события ККЧЧ.

print((wwrr + wwbb + rrbb) * p)
