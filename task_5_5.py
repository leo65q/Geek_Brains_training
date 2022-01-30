src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for x in src:
    y = 0
    for a in src:
        if x == a:
            y += 1
    if y == 1:
        result.append(x)
print(result)
