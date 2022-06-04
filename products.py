class Product:
    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight
        self.calories = calories


class Product1:
    def __init__(self, name):
        self.name = name


class Product2:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Protein(Product):
    def __init__(self, name, weight, calories):
        super().__init__(name, weight, calories)


class Carbs(Product):
    def __init__(self, name, weight, calories):
        super().__init__(name, weight, calories)


class Fats(Product):
    def __init__(self, name, weight, calories):
        super().__init__(name, weight, calories)


class Fruits(Product):
    def __init__(self, name, weight, calories):
        super().__init__(name, weight, calories)


class SummerVegetables(Product1):
    def __init__(self, name):
        super().__init__(name)


class WinterVegetables(Product1):
    def __init__(self, name):
        super().__init__(name)


class PartyFood:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


