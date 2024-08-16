class House():
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        floor_list = list(range(1, new_floor))
        for floor in floor_list:
            print(floor)
            if floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
            else:
                pass


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(22)

