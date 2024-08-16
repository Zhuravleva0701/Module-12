class Cars:
    price = 1000000

    def horse_powers(self, horse_powers):
        print(f'У этой машины {horse_powers}, лошадиных сил')


class Nissan(Cars):
    price = 800000


class Kia(Cars):
    price = 600000




nissan = Nissan()
kia = Kia()
print(Cars.price)
print(Nissan.price)
print(nissan.horse_powers(200))
print(Kia.price)
print(kia.horse_powers(100))