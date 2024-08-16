import random

n = range (3, 21)
win = random.choice(n)

print(win)
key = []
for i in range(1, win):
    j = i + 1
    for j in range(1, win):
        if win % (i + j) == 0 and i != j:
            key.append(i)
            key.append(j)

print(key)


