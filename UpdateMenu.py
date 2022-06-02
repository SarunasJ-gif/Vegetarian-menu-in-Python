from tabulate import tabulate
from ProductsLists import *
from Products import *


proteins = protein_menu()
fats = fat_menu()
carbs = carbs_menu()
fruits = fruits_menu()
summer_vegetables = summer_vegetables_menu()
winter_vegetables = winter_vegetables_menu()
partyMenu = party_food_menu()


def adding_protein(name, weight, calories):
    new_protein = Protein(name, weight, calories)
    proteins.append(new_protein)


def adding_carbs(name, weight, calories):
    new_carb = Carbs(name, weight, calories)
    carbs.append(new_carb)


def adding_fats(name, weight, calories):
    new_fat = Fats(name, weight, calories)
    fats.append(new_fat)


def adding_fruits(name, weight, calories):
    new_fruit = Fruits(name, weight, calories)
    fruits.append(new_fruit)


def adding_summer_vegetables(name, weight, calories):
    new_summer_vegetable = SummerVegetables(name, weight, calories)
    summer_vegetables.append(new_summer_vegetable)


def adding_winter_vegetables(name, weight, calories):
    new_winter_vegetables = WinterVegetables(name, weight, calories)
    winter_vegetables.append(new_winter_vegetables)


def adding_party_food(name, weight, calories):
    new_party_food = PartyFood(name, weight, calories)
    partyMenu.append(new_party_food)


def delete_protein(name):
    count = 0
    for protein in proteins:
        if name == protein.name:
            proteins.remove(protein)
            count += 1
    if count == 0:
        print("There is no such food in the list")
    else:
        print(f"{name} was deleted from list")


def delete_carbs(name):
    count = 0
    for carb in carbs:
        if name == carb.name:
            carbs.remove(carb)
            count += 1
    if count == 0:
        print("There is no such food in the list")
    else:
        print(f"{name} was deleted from list")


def delete_fats(name):
    count = 0
    for fat in fats:
        if name == fat.name:
            carbs.remove(fat)
            count += 1
    if count == 0:
        print("There is no such food in the list")
    else:
        print(f"{name} was deleted from list")


def delete_fruits(name):
    count = 0
    for fruit in fruits:
        if name == fruit.name:
            fruits.remove(fruit)
            count += 1
    if count == 0:
        print("There is no such food in the list")
    else:
        print(f"{name} was deleted from list")


def delete_party_food(name):
    count = 0
    for party in partyMenu:
        if name == party.name:
            partyMenu.remove(party)
            count += 1
    if count == 0:
        print("There is no such food in the list")
    else:
        print(f"{name} was deleted from list")


def delete_summer_vegetables(name):
    count = 0
    for summer_vegetable in summer_vegetables:
        if name == summer_vegetable.name:
            summer_vegetables.remove(summer_vegetable)
            count += 1
    if count == 0:
        print("There is no such food in the list")
    else:
        print(f"{name} was deleted from list")


def delete_winter_vegetables(name):
    count = 0
    for winter_vegetable in winter_vegetables:
        if name == winter_vegetable.name:
            winter_vegetables.remove(winter_vegetable)
            count += 1
    if count == 0:
        print("There is no such food in the list")
    else:
        print(f"{name} was deleted from list")

#
def print_protein_list():
    for index, protein in enumerate(proteins):
        print((index + 1) + "." + protein.name + " " + protein.weight + "g" + " " + protein.calories + "kCal")


def print_carbs_list():
    for index, carb in enumerate(carbs):
        print((index + 1) + "." + carb.name + " " + carb.weight + "g" + " " + carb.calories + "kCal")


def print_fats_list():
    for index, fat in enumerate(fats):
        print((index + 1) + "." + fat.name + " " + fat.weight + "g" + " " + fat.calories + "kCal")


def print_fruits_list():
    for index, fruit in enumerate(fruits):
        print((index + 1) + "." + fruit.name + " " + fruit.weight + "g" + " " + fruit.calories + "kCal")


def print_summer_vegetables_list():
    for index, summer_vegetable in enumerate(summer_vegetables):
        print((index + 1) + "." + summer_vegetable.name + " " + summer_vegetable.weight + "g" + " " + summer_vegetable.calories + "kCal")


def print_winter_vegetables_list():
    for index, winter_vegetable in enumerate(winter_vegetables):
        print((index + 1) + "." + winter_vegetable.name + " " + winter_vegetable.weight + "g" + " " + winter_vegetable.calories + "kCal")


def print_party_food_list():
    for index, party_food in enumerate(partyMenu):
        print((index + 1) + "." + party_food.name + " " + party_food.weight + "g" + " " + party_food.calories + "kCal")
