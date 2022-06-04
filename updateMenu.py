
from tabulate import tabulate
from productsLists import *
from products import *

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


def adding_summer_vegetables(name):
    new_summer_vegetable = SummerVegetables(name)
    summer_vegetables.append(new_summer_vegetable)


def adding_winter_vegetables(name):
    new_winter_vegetables = WinterVegetables(name)
    winter_vegetables.append(new_winter_vegetables)


def adding_party_food(name, quantity):
    new_party_food = PartyFood(name, quantity)
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


def print_protein_list():
    protein_list = []
    for index, protein in enumerate(proteins):
        items_list = [index, protein.name, protein.weight, protein.calories]
        protein_list.append(items_list)
    print(tabulate(protein_list, headers=("Nr.", "Name", "Weight g", "Calories kCal")))


def print_carbs_list():
    carbs_list = []
    for index, carb in enumerate(carbs):
        items_list = [index, carb.name, carb.weight, carb.calories]
        carbs_list.append(items_list)
    print(tabulate(carbs_list, headers=("Nr.", "Name", "Weight g", "Calories kCal")))


def print_fats_list():
    fats_list = []
    for index, fat in enumerate(fats):
        items_list = [index, fat.name, fat.weight, fat.calories]
        fats_list.append(items_list)
    print(tabulate(fats_list, headers=("Nr.", "Name", "Weight g", "Calories kCal")))


def print_fruits_list():
    fruits_list = []
    for index, fruit in enumerate(fruits):
        items_list = [index, fruit.name, fruit.weight, fruit.calories]
        fruits_list.append(items_list)
    print(tabulate(fruits_list, headers=("Nr.", "Name", "Weight g", "Calories kCal")))


def print_summer_vegetables_list():
    summer = []
    for index, summer_vegetable in enumerate(summer_vegetables):
        items_list = [index, summer_vegetable.name, "100g"]
        summer.append(items_list)
    print(tabulate(summer, headers=("Nr.", "Name", "Weight g")))


def print_winter_vegetables_list():
    winter = []
    for index, winter_vegetable in enumerate(winter_vegetables):
        items_list = [index, winter_vegetable.name, "100g"]
        winter.append(items_list)
    print(tabulate(winter, headers=("Nr.", "Name", "Weight g")))


def print_party_food_list():
    party = []
    for index, party_food in enumerate(partyMenu):
        items_list = [index, party_food.name, party_food.quantity]
        party.append(items_list)
    print(tabulate(party, headers=("Nr.", "Name", "pcs.")))
