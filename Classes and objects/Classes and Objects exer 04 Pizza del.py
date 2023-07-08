class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        # if we already have this ingredient in our pizza, increase the ingredient quantity with the given one
# and update the pizza price by adding the ingredient price for the given quantity
        if ingredient in self.ingredients