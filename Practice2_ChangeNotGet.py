class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Model is {self.__model}'

    def get_horse_power(self):
        return f'Engine power is: {self.__engine_power}'

    def get_color(self):
        return f'Color is: {self.__color}'

    def print_info(self):
        print(self.get_model(), '\n', self.get_horse_power(), '\n', self.get_color(), '\n', f'Owner is: {self.owner}')

    def set_color(self, color):
        if color.casefold() in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print(f"Impossible to change current color to {color}")
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
