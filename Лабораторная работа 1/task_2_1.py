import doctest

class TV:
    def init(self, screen_diagonal: int, channel: int):
        """
        Создание и подготовка к работе объекта "Телевизор"
        :param screen_diagonal: Диагональ экрана
        :param channel: Номер включенного канал

        Примеры:
        >>> TV1 = TV(32, 5) #инициализация экземпляра класса
        """
        if not isinstance(screen_diagonal, int):
            raise TypeError("Диагональ экрана должна быть целым числом")
        if screen_diagonal <= 19:
            raise ValueError("Диагональ экрана должна быть минимум 19 дюймов")
        self.screen_diagonal = screen_diagonal

        if not isinstance(channel, int):
            raise TypeError("Номер включенного канала должен быть целым числом")
        if channel <= 0:
            raise ValueError("Номер включенного канала должен быть больше нуля")
        self.channel = channel

    def TV_is_big(self) -> bool:
        """
        Функция, проверяющая большой ли телевизор
        :return: Включен ли телевизор

        Примеры:
        >>> TV1 = TV(32, 1)
        >>> TV1.TV_is_big()
        False
        """
        ...

    def switch_channel(self, new_channel: int) -> None:
        """
        Переключение канала
        :param new_channel: Новый включенный канал
        :return: Изменение включенного канала

        Примеры:
        >>> TV1 = TV(32,5)
        >>> TV1.switch_channel(10)
        TV1.channel = 10
        """
        if not isinstance(new_channel, int):
            raise TypeError("Номер нового канала должен быть целым числом")
        if new_channel <= 0:
            raise ValueError("Номер нового включенного канала должен быть больше нуля")
        ...


class Lamp:
    def init(self, glow_color: str, switch_position: str):
        """
        Создание и подготовка к работе объекта "Лампа"
        :param glow_color: Цвет свечения лампы
        :param switch_position: Положение переключателя включения и выключения

        Примеры:
        >>> lamp = Lamp("теплый", "вкл") #инициализация экземпляра класса
        """
        if not isinstance(glow_color, str):
            raise TypeError("Цвет свечения может быть только строкового типа")
        if not glow_color in ["теплый", "холодный"]:
            raise ValueError("Цвет свечения может иметь значение 'теплый' или 'холодный'")
        self.glow_color = glow_color

        if not isinstance(switch_position, str):
            raise TypeError("Положение переключателя может быть только строкового типа")
        if not switch_position in ["вкл", "выкл"]:
            raise ValueError("Положение переключателя может иметь значение 'вкл' или 'выкл'")
        self.switch_position = switch_position

    def lamp_is_on(self) -> bool:
        """
        Функция проверяет включена ли лампа
        :return: Включена ли лампа

        Примеры:
        >>> lamp = Lamp("теплый", "вкл")
        >>> lamp.lamp_is_on()
        True
        """
        ...

    def change_switch_position(self, position: str) -> None:
        """
        Изменение позиция переключателя включения и выключения лампы
        :param position: Позиция лампы

        Примеры:
        >>> lamp = Lamp("теплый", "выкл")
        >>> lamp.change_switch_position("вкл")
        lamp.switch_position = "вкл"
        """
        if not isinstance(position, str):
            raise TypeError("Положение переключателя может быть только строкового типа")
        if not position in ["вкл", "выкл"]:
            raise ValueError("Положение переключателя может иметь значение 'вкл' или 'выкл'")
        ...


class CarOrder:
    def init(self, number_of_cars: int, color_of_cars: str):
        """
        Создание заказа на покупку авто
        :param number_of_cars: Количество машин
        :param color_of_cars: Цвет машин Примеры:
        >>> cars = CarOrder(5, "белый")
        """
        if not isinstance(number_of_cars, int):
            raise TypeError("Количество машин может быть только целым числом")
        if number_of_cars <= 0:
            raise ValueError("Минимальный заказ от 1 авто")
        if number_of_cars > 5:
            raise ValueError("Вы не можете заказать больше 5 авто")
        self.number_of_cars = number_of_cars

        if not isinstance(color_of_cars, str):
            raise TypeError("Цвет авто может быть только строкового типа")
        if not color_of_cars in ["белый", "черный", "синий"]:
            raise ValueError("Цвет авто может иметь значение 'белый', 'черный' или 'синий'")
        self.color_of_cars = color_of_cars

    def increase_number_of_cars(self, number_of_cars_to_increase: int) -> None:
        """
        Функция увеличивает количество авто в заказе
        :param number_of_cars_to_increase: Число на которое увеличивается количество авто в заказе

        Примеры:
        >>> cars = CarOrder(2, "белый")
        >>> cars.increase_number_of_cars(3)
        cars.number_of_cars = 5
        """
        if not isinstance(number_of_cars_to_increase, int):
            raise TypeError("Количество машин может быть только целым числом")
        if number_of_cars_to_increase <= 0:
            raise ValueError("Вы можете увеличить заказ минимум на 1 авто")
        if number_of_cars_to_increase + number_of_cars > 5:
            raise ValueError("Вы не можете заказать больше 5 авто")
        ...

    def decrease_number_of_cars(self, number_of_cars_to_decrease: int) -> None:
        """
        Функция уменьшает количество авто в заказе
        :param number_of_cars_to_decrease: Число на которое уменьшается количество авто в заказе

        Примеры:
        >>> cars = CarOrder(3, "белый")
        >>> cars.decrease_number_of_cars(2)
        cars.number_of_cars = 1
        """
        if not isinstance(number_of_cars_to_decrease, int):
            raise TypeError("Количество машин может быть только целым числом")
        if number_of_cars_to_decrease <= 0:
            raise ValueError("Вы можете уменьшить заказ минимум на 1 авто")
        if number_of_cars - number_of_cars_to_decrease < 0:
            raise ValueError("Вы не можете убрать из заказа машин больше, чем заказали изначально")
        if number_of_cars - number_of_cars_to_decrease == 1:
            raise ValueError("В заказе должно быть хотя бы 1 авто")
        ...


if name == "main":
    doctest.testmod()
    pass
