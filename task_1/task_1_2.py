from pympler import asizeof


class Road1:

    def __init__(self, length, width):
        self.__length__ = length
        self.__width__ = width

    def weight_road(self):
        weight = f'{self.__length__ * self.__width__ * 25 * 5 / 1000} т'

        return weight


class Road2:
    __slots__ = ('__length', '__width')

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight_road(self):
        weight = f'{self.__length * self.__width * 25 * 5 / 1000} т'

        return weight


road_1 = Road1(20, 5000)
road_2 = Road2(20, 5000)
print(asizeof.asizeof(road_1))
print(asizeof.asizeof(road_2))


'''
344 - не оптимизированный
112 - оптимизированный
Использовали slots для уменьшения используемой памяти
'''
