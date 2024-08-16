class House():
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        setattr(House, self.numberOfFloors, floors)
        print(House.numberOfFloors)