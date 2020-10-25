a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = list()
for x in a:
    if x < 5:
        newList.append(x)

print(newList)