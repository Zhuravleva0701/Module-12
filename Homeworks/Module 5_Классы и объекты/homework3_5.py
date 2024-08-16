class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        return isinstance(other, Building) and self.buildingType == other.buildingType \
               and self.numberOfFloors == other.numberOfFloors


h1 = Building(2, 'деревянный дом')
h2 = Building(2, 'деревянный дом')
print(h1 == h2)