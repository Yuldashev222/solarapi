lst = [10, 20, 30, 12, 4, 23, 35, 44, 55, 66, 77, 88, 11, 34, 54, 1]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        a, b = lst[i], lst[j]
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)
