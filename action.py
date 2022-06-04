from datetime import date
from menu import *
from updateMenu import *


def run():
    menu_choice = choose_option()
    run_application = True
    while run_application:
        match menu_choice:
            case "menu":
                menu = Menu(calories())
                week_days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
                for day in week_days:
                    print("\n" + day + ":")
                    print(menu.breakfast_menu_random_list())
                    print(vegetables_by_season())
                    print(menu.lunch_menu_random_list())
                    print(vegetables_by_season())
                    print(menu.dinner_menu_random_list())
                    print(vegetables_by_season())
                menu_choice = choose_option()
            case "party":
                menu2 = Menu(1)
                correct_dishes_input = False
                while not correct_dishes_input:
                    try:
                        dishes_amount = int(input("Please enter as many dishes as you want to order: "))
                        correct_dishes_input = True
                    except ValueError:
                        print("Not valid input, please enter the number: ")
                correct_participants_input = False
                while not correct_participants_input:
                    try:
                        number_of_participants = int(
                            input("Please enter how many participants will attend the party: "))
                        correct_participants_input = True
                    except ValueError:
                        print("Not valid input, please enter the number: ")
                menu2.party_menu_random_list(dishes_amount, number_of_participants)
                menu_choice = choose_option()
            case "add":
                add_food()
                menu_choice = choose_option()
            case "delete":
                delete_food_from_list()
                menu_choice = choose_option()
            case "print":
                print_lists()
                menu_choice = choose_option()
            case "options":
                menu_choice = choose_option()
            case "exit":
                run_application = False
            case _:
                print("Invalid choice, choose one more time: ")
                menu_choice = choose_option()


def choose_option():
    print("\n\nMake your choice: ")
    print("If you want vegetarian food menu list for all week press 'menu': ")
    print("If you want vegetarian food menu for party press 'party': ")
    print("If you want add food to menu 'add': ")
    print("If you want delete food from menu 'delete': ")
    print("If you want print all food in the list press 'print': ")
    print("Print a list of available actions press 'options': ")
    print("If you want exit press 'exit': ")
    menu_choice = input("-> ").lower()
    return menu_choice


def vegetables_by_season():
    menu1 = Menu(1)
    today = date.today().month
    if today == 10 or today == 11 or today == 12 or today == 1 or today == 2:
        return menu1.winter_time_vegetables_random_list()
    else:
        return menu1.summer_time_vegetables_random_list()


def print_lists():
    print("Choice which list to print:\npress:")
    print("1 - print protein list\n" +
          "2 - print carbs list\n" +
          "3 - print fat list\n" +
          "4 - print fruits list\n" +
          "5 - print summer time vegetables list\n" +
          "6 - print winter time vegetables list\n" +
          "7 - print party food menu list.")
    option = input("-> ")
    match option:
        case "1":
            print("Protein food list: ")
            print_protein_list()
        case "2":
            print("Carbohydrate food list: ")
            print_carbs_list()
        case "3":
            print("Food fat source list: ")
            print_fats_list()
        case "4":
            print("Fruits list: ")
            print_fruits_list()
        case "5":
            print("List of vegetables for the summer season: ")
            print_summer_vegetables_list()
        case "6":
            print("List of vegetables for the winter season: ")
            print_winter_vegetables_list()
        case "7":
            print("Party food list: ")
            print_party_food_list()
        case _:
            print("Invalid input...")
            print()


def add_food():
    print("Choice to add to the list:\npress:")
    print("1 - add to protein list\n" +
          "2 - add to carbs list\n" +
          "3 - add to fat list\n" +
          "4 - add to fruits list\n" +
          "5 - add to summer time vegetables list\n" +
          "6 - add to winter time vegetables list\n" +
          "7 - add to party food menu list.")
    option_to_add = input("-> ")
    match option_to_add:
        case "1":
            protein_name = input("Please enter food name: ")
            correct_weight_input = False
            while not correct_weight_input:
                try:
                    protein_weight = int(input("Please enter food weight: "))
                    correct_weight_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            correct_calories_input = False
            while not correct_calories_input:
                try:
                    protein_calories = int(input("Please enter food calories: "))
                    correct_calories_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            adding_protein(protein_name, protein_weight, protein_calories)
        case "2":
            carbs_name = input("Please enter food name: ")
            correct_weight_input = False
            while not correct_weight_input:
                try:
                    carbs_weight = int(input("Please enter food weight: "))
                    correct_weight_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            correct_calories_input = False
            while not correct_calories_input:
                try:
                    carbs_calories = int(input("Please enter food calories: "))
                    correct_calories_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            adding_carbs(carbs_name, carbs_weight, carbs_calories)
        case "3":
            fat_name = input("Please enter food name: ")
            correct_weight_input = False
            while not correct_weight_input:
                try:
                    fat_weight = int(input("Please enter food weight: "))
                    correct_weight_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            while not correct_calories_input:
                try:
                    fat_calories = int(input("Please enter food calories: "))
                    correct_calories_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            adding_fats(fat_name, fat_weight, fat_calories)
        case "4":
            fruit_name = input("Please enter food name: ")
            correct_weight_input = False
            while not correct_weight_input:
                try:
                    fruit_weight = int(input("Please enter food weight: "))
                    correct_weight_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            correct_calories_input = False
            while not correct_calories_input:
                try:
                    fruit_calories = int(input("Please enter food calories: "))
                    correct_calories_input = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            adding_fruits(fruit_name, fruit_weight, fruit_calories)
        case "5":
            summer_vegetables_name = input("Please enter food name: ")
            adding_summer_vegetables(summer_vegetables_name)
        case "6":
            winter_vegetables_name = input("Please enter food name: ")
            adding_winter_vegetables(winter_vegetables_name)
        case "7":
            party_dish_name = input("Enter the name of the dish: ")
            correct_amount = False
            while not correct_amount:
                try:
                    quantity = int(input("Please enter the amount of food in units: "))
                    correct_amount = True
                except ValueError:
                    print("Not valid input, please enter the number: ")
            adding_party_food(party_dish_name, quantity)
        case _:
            print("Invalid input...")


def delete_food_from_list():
    print("Choice to delete from the list:\npress:")
    print("1 - delete from protein list\n" +
          "2 - delete from carbs list\n" +
          "3 - delete from fat list\n" +
          "4 - delete from fruits list\n" +
          "5 - delete from summer time vegetables list\n" +
          "6 - delete from winter time vegetables list\n" +
          "7 - delete from party food menu list.")
    option_to_delete = input("-> ")
    match option_to_delete:
        case "1":
            protein_name = input("Please enter food name: ")
            delete_protein(protein_name)
        case "2":
            carbs_name = input("Please enter food name: ")
            delete_carbs(carbs_name)
        case "3":
            fat_name = input("Please enter food name: ")
            delete_fats(fat_name)
        case "4":
            fruit_name = input("Please enter food name: ")
            delete_fruits(fruit_name)
        case "5":
            summer_vegetables_name = input("Please enter food name: ")
            delete_summer_vegetables(summer_vegetables_name)
        case "6":
            winter_vegetables_name = input("Please enter food name: ")
            delete_winter_vegetables(winter_vegetables_name)
        case "7":
            party_food_name = input("Please enter food name: ")
            delete_party_food(party_food_name)
        case _:
            print("Invalid input...")


def calories():
    print("Please enter your preferred daily caloric intake: ")
    correct_input = False
    while not correct_input:
        try:
            calories_per_day = int(input("-> "))
            correct_input = True
        except ValueError:
            print("Please enter the number: ")
    return calories_per_day
