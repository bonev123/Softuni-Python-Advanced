from typing import ClassVar

from Encapsulation_exer_04_Restaurant_100pts.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS: ClassVar[int] = 22

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, self.__class__.GRAMS)