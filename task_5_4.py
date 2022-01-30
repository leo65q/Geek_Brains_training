src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[x] for x in range(1, len(src)) if src[x] > src[x - 1] and src[x]]
print(result)
