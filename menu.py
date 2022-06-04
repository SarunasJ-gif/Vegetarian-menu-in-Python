import random
from updateMenu import *


class Menu:
    def __init__(self, calories):
        self.calories = calories
        self.protein_day_calories = calories * 0.2
        self.fat_day_calories = calories * 0.2
        self.carbs_day_calories = calories * 0.6

    def breakfast_menu_random_list(self):
        print("\nBreakfast: ")
        random_carbs = random.choice(carbs)
        breakfast_carbs_weight = int(
            random_carbs.weight * (self.carbs_day_calories / random_carbs.calories * 0.5 * 0.8))
        carb_dish = random_carbs.name + " " + str(breakfast_carbs_weight) + "g"
        random_fruits = random.choice(fruits)
        breakfast_fruits_weight = int(
            random_fruits.weight * (self.carbs_day_calories / random_fruits.calories * 0.5 * 0.2))
        fruit_dish = random_fruits.name + " " + str(breakfast_fruits_weight) + "g"
        return carb_dish + "\n" + fruit_dish

    def lunch_menu_random_list(self):
        print("\nLunch: ")
        random_carbs = random.choice(carbs)
        lunch_carbs_weight = int(random_carbs.weight * (self.carbs_day_calories / random_carbs.calories * 0.4))
        carbs_dish = random_carbs.name + " " + str(lunch_carbs_weight) + "g"
        random_proteins = random.choice(proteins)
        lunch_proteins_weight = int(
            random_proteins.weight * (self.protein_day_calories / random_proteins.calories * 0.5))
        proteins_dish = random_proteins.name + " " + str(lunch_proteins_weight) + "g"
        random_fats = random.choice(fats)
        lunch_fats_weight = int(random_fats.weight * (self.fat_day_calories / random_fats.calories * 0.5))
        fats_dish = random_fats.name + " " + str(lunch_fats_weight) + "g"
        return carbs_dish + "\n" + proteins_dish + "\n" + fats_dish

    def dinner_menu_random_list(self):
        print("\nDinner: ")
        random_carbs = random.choice(carbs)
        dinner_carbs_weight = int(random_carbs.weight * (self.carbs_day_calories / random_carbs.calories * 0.1))
        carbs_dish = random_carbs.name + " " + str(dinner_carbs_weight) + "g"
        random_proteins = random.choice(proteins)
        dinner_proteins_weight = int(
            random_proteins.weight * (self.protein_day_calories / random_proteins.calories * 0.5))
        proteins_dish = random_proteins.name + " " + str(dinner_proteins_weight) + "g"
        random_fats = random.choice(fats)
        dinner_fats_weight = int(random_fats.weight * (self.fat_day_calories / random_fats.calories * 0.5))
        fats_dish = random_fats.name + " " + str(dinner_fats_weight) + "g"
        return carbs_dish + "\n" + proteins_dish + "\n" + fats_dish

    def summer_time_vegetables_random_list(self):
        summer_vegetable = random.choice(summer_vegetables)
        return summer_vegetable.name + " 100g"

    def winter_time_vegetables_random_list(self):
        winter_vegetable = random.choice(winter_vegetables)
        return winter_vegetable.name + " 100g"

    def party_menu_random_list(self, number_of_dishes, participants):
        portion = 0
        if participants <= 8:
            portion = 1
        elif 8 < participants <= 16:
            portion = 2
        else:
            portion = 3
        print("\nParty menu: ")
        counting = []
        i = 0
        while i < number_of_dishes:
            x = random.randint(0, (len(partyMenu) - 1))
            if x in counting:
                continue
            else:
                y = x
                counting.append(y)
                print(partyMenu[x].name + " " + str(portion * partyMenu[x].quantity) + "pcs.")
                i += 1
