class Building:
    total = 0

    def __init__(self, totalhigh):
        self.totalhigh = totalhigh
        Building.total += 1


list = []
for i in range(40):
    list.append(Building(5))

for j in list:
    print(j)
print(Building.total)
