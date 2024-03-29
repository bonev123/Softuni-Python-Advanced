class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price
        else:
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients and quantity > self.ingredients[ingredient] > 0:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= ingredient_price

    def make_order(self):
        self.ordered = True
        ingredients = [f"{key}: {value}" for key, value in self.ingredients.items()]
        return f"You've ordered pizza {self.name} prepared with {', '.join(ingredients)} and the price will be {self.price}lv."