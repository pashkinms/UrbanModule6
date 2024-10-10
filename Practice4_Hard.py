from math import pi, sqrt


class Figure:
    sides_count = 0
    __sides = []
    __color = []

    def __init__(self, color: list, *sides):
        self.__sides = list(sides)
        self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        flag = False
        args = list(args)
        for i in range(0, len(args)):
            if args[i] == round(args[i]) and args[i] >= 0:
                flag = True
            else:
                flag = False
                print("Invalid data")
        if len(args) == self.sides_count and flag:
            return True
        else:
            return False

    def get_sides(self):

        return self.__sides

    def __len__(self):
        result = sum(self.__sides)

        return result

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = list(args)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, side):
        __radius = side / (2 * pi)
        super().__init__(color, side)

    def __len__(self):
        a = self.get_sides()
        return a[0]


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = self.__len__() / 2
        sides = self.get_sides()
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        sides = [side] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        a = self.get_sides()
        return a[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
