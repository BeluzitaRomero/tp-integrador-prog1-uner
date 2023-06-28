# 2. Funciones de búsqueda de comidas rápidas a partir de los siguientes criterios:
# ▪ Buscar por ingrediente.
# ▪ Buscar por precio.
# ▪ Buscar por calorías.
# ▪ Las comidas veganas disponibles.


from json_functions import get_json

def find_by_ingredient(ingredient):
    food_list = get_json()
    filtered_list = []

    for food in food_list:
        if ingredient.lower() in food["ingredients"]:
            filtered_list.append(food)

    if len(filtered_list) > 0:
        item = 1
        for item_list in filtered_list:
            ui_list = f"{item}: {item_list['title'].capitalize()}"
            item += 1
            print(ui_list)
    else:
        print("No existen comidas con el ingrediente buscado")

def find_by_price(price):
    food_list = get_json()
    filtered_list = []

    for food in food_list:
        if price == food["price"]:
            filtered_list.append(food)

    if len(filtered_list) > 0:
        item = 1
        for item_list in filtered_list:
            ui_list = f"{item}: {item_list['title'].capitalize()}"
            item += 1
            print(ui_list)
    else:
        print("No existen comidas con el precio buscado")

def find_by_calories(calories):
    food_list = get_json()
    filtered_list = []

    for food in food_list:
        if calories == food["calories"]:
            filtered_list.append(food)

    if len(filtered_list) > 0:
        item = 1
        for item_list in filtered_list:
            ui_list = f"{item}: {item_list['title'].capitalize()}"
            item += 1
            print(ui_list)
    else:
        print("No existen comidas con las calorias buscadas")


def find_vegan_food():
    food_list = get_json()
    filtered_list = []
  
    for food in food_list:
        if food["vegan"] == True:
            filtered_list.append(food)
    
    if len(filtered_list) > 0:
        item = 1
        for item_list in filtered_list:
            ui_list = f"{item}: {item_list['title'].capitalize()}"
            item += 1
            print(ui_list)
    else:
        print("No existen comidas veganas")

