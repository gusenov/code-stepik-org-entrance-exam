lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst)

cnt = 0
while True:
    changed = False
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            t = lst[i - 1]
            lst[i - 1] = lst[i]
            lst[i] = t
            changed = True
            break
    if changed:
        print(lst)
        cnt += 1
    else:
        break

print("cnt = ", cnt)
print("cnt^2 = ", cnt**2)
