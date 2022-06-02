from datetime import date
from Menu import *
from UpdateMenu import *

def calories_of_day():
    calories = int(input("Please enter your preferred daily caloric intake: "))
    return calories


def run():
    pass

def choose_option():
    print("Make your choice: ")
    print("If you want vegetarian food menu list for all week press 'menu': ")
    print("If you want vegetarian food menu for party press 'party': ")
    print("If you want add food to menu 'add': ")
    print("If you want delete food from menu 'delete': ")
    print("If you want print all food in the list press 'print': ")
    print("Print a list of available actions press 'options': ")
    print("If you want exit press 'exit': ")
    menu_choice = input("->")
    return menu_choice


def vegetables_by_season():
    today = date.today().month
    if today == 10 or today == 11 or today == 12 or today == 1 or today == 2:
        return winter_time_vegetables_random_list()
    else:
        return summer_time_vegetables_random_list()



