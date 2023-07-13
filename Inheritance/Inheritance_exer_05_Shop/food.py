from typing import ClassVar
from Inheritance_exer_05_Shop.product import Product


class Food(Product):
    QUANTITY: ClassVar[int] = 15

    def __init__(self, name: str) -> None:
        super().__init__(name, self.__class__.QUANTITY)
