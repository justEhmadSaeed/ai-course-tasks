import random

def intersection(a, b):
    return list(set(a) & set(b))

a = []
b = []
for i in range(0, 10):
    a.append(random.randint(0, 20))
    b.append(random.randint(5, 20))
print(a)
print(b)

print(intersection(a, b))