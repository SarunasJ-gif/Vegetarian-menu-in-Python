from products import Protein
from products import Fats
from products import Carbs
from products import Fruits
from products import SummerVegetables
from products import WinterVegetables
from products import PartyFood


def protein_menu():
    list_protein = []
    soy = Protein("Soy", 100, 337)
    beans = Protein("Beans", 100, 290)
    lenses = Protein("Lences", 100, 312)
    fish_fillets = Protein("Fish fillets", 100, 183)
    curd = Protein("Curd", 100, 160)
    shrimp = Protein("Shrimp", 100, 70)
    tuna = Protein("Tuna", 100, 186)
    caviar = Protein("Caviar", 100, 267)
    egg_whites = Protein("Egg whites", 100, 49)
    list_protein.append(soy)
    list_protein.append(beans)
    list_protein.append(lenses)
    list_protein.append(fish_fillets)
    list_protein.append(curd)
    list_protein.append(shrimp)
    list_protein.append(tuna)
    list_protein.append(caviar)
    list_protein.append(egg_whites)
    return list_protein


def fat_menu():
    fats_list = []
    nuts = Fats("Nuts", 100, 658)
    egg_yolk = Fats("Egg yolk", 100, 359)
    linseed = Fats("Linseed", 100, 365)
    spanish_sage_seeds = Fats("Spanish sage seeds", 100, 453)
    avocado = Fats("Avocado", 100, 224)
    fats_list.append(nuts)
    fats_list.append(egg_yolk)
    fats_list.append(linseed)
    fats_list.append(spanish_sage_seeds)
    fats_list.append(avocado)
    return fats_list


def carbs_menu():
    carbs_list = []
    buckwheat = Carbs("Buckwheat", 100, 349)
    rice = Carbs("Rice", 100, 344)
    rye_bread = Carbs("Rye bread", 100, 215)
    pasta = Carbs("Whole grain pasta", 100, 359)
    spaghetti = Carbs("Spaghetti", 100, 359)
    potatoes = Carbs("Potatoes", 100, 81)
    corn = Carbs("Corn", 100, 39)
    oatmeal = Carbs("Oatmeal", 100, 365)
    millet = Carbs("Millet", 100, 119)
    bolivian_pigeon = Carbs("Bolivian pigeon", 100, 120)
    barley_groats = Carbs("Barley groats", 100, 319)
    couscous = Carbs("Couscous", 100, 112)
    brown_rice = Carbs("Brown rice", 100, 353)
    wild_rice = Carbs("Wild rice", 100, 101)
    tortillas = Carbs("Tortillas whole grain", 100, 310)
    carbs_list.append(buckwheat)
    carbs_list.append(rice)
    carbs_list.append(rye_bread)
    carbs_list.append(pasta)
    carbs_list.append(spaghetti)
    carbs_list.append(potatoes)
    carbs_list.append(corn)
    carbs_list.append(oatmeal)
    carbs_list.append(millet)
    carbs_list.append(bolivian_pigeon)
    carbs_list.append(barley_groats)
    carbs_list.append(couscous)
    carbs_list.append(brown_rice)
    carbs_list.append(wild_rice)
    carbs_list.append(tortillas)
    return carbs_list


def fruits_menu():
    fruits_list = []
    bananas = Fruits("Bananas", 100, 97)
    apple = Fruits("Apple", 100, 53)
    persimmons = Fruits("Persimmons", 100, 70)
    orange = Fruits("Orange", 100, 43)
    fruit_salad = Fruits("Fruit salad", 100, 49)
    fruits_list.append(bananas)
    fruits_list.append(apple)
    fruits_list.append(persimmons)
    fruits_list.append(orange)
    fruits_list.append(fruit_salad)
    return fruits_list


def summer_vegetables_menu():
    summer_vegetables_list = []
    cucumber = SummerVegetables("Cucumber")
    dill = SummerVegetables("Dill")
    parsley = SummerVegetables("Parsley")
    tomatoes = SummerVegetables("Tomatoes")
    lettuce_leaves = SummerVegetables("Lettuce leaves")
    carrots = SummerVegetables("Carrots")
    green_onions = SummerVegetables("Green onions")
    cabbage = SummerVegetables("Cabbage")
    bitter_herbs = SummerVegetables("Bitter herbs")
    summer_vegetables_list.append(cucumber)
    summer_vegetables_list.append(dill)
    summer_vegetables_list.append(parsley)
    summer_vegetables_list.append(tomatoes)
    summer_vegetables_list.append(lettuce_leaves)
    summer_vegetables_list.append(carrots)
    summer_vegetables_list.append(green_onions)
    summer_vegetables_list.append(cabbage)
    summer_vegetables_list.append(bitter_herbs)
    return summer_vegetables_list


def winter_vegetables_menu():
    winter_vegetables_list = []
    pickled_garlic = WinterVegetables("Pickled garlic")
    sauerkraut = WinterVegetables("Sauerkraut")
    boiled_beetroot = WinterVegetables("Boiled beetroot")
    tanned_cucumbers = WinterVegetables("Tanned cucumbers")
    roasted_peppers = WinterVegetables("Roasted peppers")
    carrots = WinterVegetables("Carrots")
    sour_tomatoes = WinterVegetables("Sour tomatoes")
    canned_peas = WinterVegetables("Canned peas")
    sour_beets = WinterVegetables("Sour beets")
    fried_onions = WinterVegetables("Fried onions")
    canned_asparagus = WinterVegetables("Canned asparagus")
    winter_vegetables_list.append(pickled_garlic)
    winter_vegetables_list.append(sauerkraut)
    winter_vegetables_list.append(boiled_beetroot)
    winter_vegetables_list.append(tanned_cucumbers)
    winter_vegetables_list.append(roasted_peppers)
    winter_vegetables_list.append(carrots)
    winter_vegetables_list.append(sour_tomatoes)
    winter_vegetables_list.append(canned_peas)
    winter_vegetables_list.append(sour_beets)
    winter_vegetables_list.append(fried_onions)
    winter_vegetables_list.append(canned_asparagus)
    return winter_vegetables_list


def party_food_menu():
    party_food_list = []
    ice_cream = PartyFood("Ice creams", 8)
    cake = PartyFood("Snickers cake", 1)
    donuts = PartyFood("Donuts", 8)
    chocolate_cake = PartyFood("Chocolate cakes with Riccota cheese filling and light cream, flavored with fresh "
                               "raspberries", 8)
    tiramisu = PartyFood("Tiramisu flavored with amaret and dark chocolate", 8)
    berries = PartyFood("Containers with Crème brûlée cream and berries", 8)
    berry_cheese = PartyFood("Wild berry and cream cheese pies", 8)
    cheese_balls = PartyFood("Crispy cheese balls", 8)
    avocado_shrim = PartyFood("Cucumber bites with avocado and shrim", 8)
    broccoli_and_cheese = PartyFood("Crispy bits of broccoli and cheese", 8)
    lavash_rolls = PartyFood("Fried lavash rolls with cheese", 8)
    orion_rings = PartyFood("Crispy onion rings in batter", 8)
    avocado = PartyFood("Avocado appetizers with herring and mangoes", 8)
    olives = PartyFood("Pickled olives", 8)
    stuffed_dates = PartyFood("Stuffed dates", 8)
    chocolate_truffles = PartyFood("Chocolate truffles", 8)
    party_food_list.append(ice_cream)
    party_food_list.append(cake)
    party_food_list.append(donuts)
    party_food_list.append(chocolate_cake)
    party_food_list.append(tiramisu)
    party_food_list.append(berries)
    party_food_list.append(berry_cheese)
    party_food_list.append(cheese_balls)
    party_food_list.append(avocado_shrim)
    party_food_list.append(broccoli_and_cheese)
    party_food_list.append(lavash_rolls)
    party_food_list.append(orion_rings)
    party_food_list.append(avocado)
    party_food_list.append(olives)
    party_food_list.append(stuffed_dates)
    party_food_list.append(chocolate_truffles)
    return party_food_list


