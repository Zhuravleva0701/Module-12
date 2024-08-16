class Vehicle:
    __color_variants = ['red', 'white', 'black', 'blue']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя {self.__engine_power}')

    def get_color(self):
        print(f'Цвет {self.__color}')


    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец {self.owner}')

    def set_color(self, new_color):
        __color_variants = ['red', 'white', 'black', 'blue']
        new_color = new_color.lower()
        for color in __color_variants:
            if new_color in __color_variants:
                self.__color = new_color
            else:
                print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):

    def __init__(self, owner, __model, __engine_power, __color, __passengers_limit=5):
        super().__init__(owner, __model, __engine_power, __color)
        self.__passengers_limit = __passengers_limit



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()