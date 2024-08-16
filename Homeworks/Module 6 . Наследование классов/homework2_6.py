class Vehicle:
    vehicle_type = None


class Cars:
    price = 1000000

    def horse_powers(self, horse_powers):
        print(f'У этой машины {horse_powers} лошадиных сил')

class Nissan(Vehicle, Cars):
    vehicle_type = True
    price = 800000

    def horse_powers(self, horse_powers):
        print(f'У моей машины {horse_powers} лошадиных сил')



nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.horse_powers(150))
print(nissan.price)

