
class Product:
    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight
        self.calories = calories


class Protein(Product):
    def __init__(self, name, weight, calories):
        super().__init__(name, weight, calories)


class Carbs(Product):
    def __init__(self, name, weight, calories):
        super().__init__(name, weight, calories)


class Fats(Product):
    def __init__(self, name, weight, calories):
        super(). __init__(name, weight, calories)


class Fruits(Product):
    def __init__(self, name, weight, calories):
        super().__init__(name, weight, calories)


class SummerVegetables(Product):
     def __init__(self, name):
            super(). __init__(name)


class WinterVegetables(Product):
    def __init__(self, name):
        super(). __init__(name)


class PartyFood(Product):
    def __init__(self, name, quantity):
        super(). __init__(name)
        self.quantity = quantity