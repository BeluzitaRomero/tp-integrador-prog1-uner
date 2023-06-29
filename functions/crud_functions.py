# 1. En referencia a las comidas rápidas:
# ● Mostrar las existentes.
# ▪ Agregar una nueva.
# ▪ Modificar los datos existentes.
# ▪ Borrar una seleccionada.

from functions.json_functions import get_json

def add_fast_food():
    title = input("Ingrese nombre del producto: ").capitalize()
    price = float(input("Ingrese el precio del producto en pesos: "))

    ingredients = []
    input_ingredients = input("Presione 'enter' para comenzar a ingresar ingredientes. Luego 'fin' para terminar: ").lower() 
    while input_ingredients != "fin":
        input_ingredients = input("Ingregiente / fin: ").lower()

        if input_ingredients != 'fin': ingredients.append(input_ingredients)
    
    time_cook = int(input("Ingrese el tiempo de coccion en minutos: "))
    calories = int(input("Ingrese las calorias en gramos: "))
    vegan = input("¿Es vegano?:(si/no) ")

    food = {"title": title,
            "price": price,
            "ingredients": ingredients,
            "time_cook": time_cook,
            "calories":calories,
            "vegan": True if vegan == "si" else False}
    return food


def show_fast_food_list():
    food_list = get_json()
    index = 1
    for food in food_list:
        ui = f"{str(index)}: {food['title']}"
        print(ui)
        index +=1

def to_delete(position_in_list):
    food_list = get_json()
    to_delete = food_list[position_in_list]

    return to_delete

def to_update(position_in_list):
    food_list = get_json()

    print("Cual es la informacion que quiere modificar?:\n1: Titulo\n2: Precio\n3: Ingredientes\n4: Tiempo de coccion\n5: Calorias\n6: Vegano")
    print("---------------------------------------------------------------")
    key_to_update = int(input("Ingrese el numero: "))

    to_update = food_list[position_in_list]

    if key_to_update == 1:
        new_value = input("Ingrese la nueva informacion: ")
        keys = list(to_update.keys())
        to_update[keys[key_to_update]] = new_value
        updated_food = to_update
        
    elif key_to_update == 2:
        new_value = input("Ingrese la nueva informacion: ")
        keys = list(to_update.keys())
        to_update[keys[key_to_update]] = float(new_value)
        updated_food = to_update

    elif key_to_update == 3:
            new_ingredients = []
            input_ingredients = input("'Enter' para comenzar a ingresar ingredientes. Luego 'fin' para terminar: ").lower()
            while input_ingredients != "fin":
                input_ingredients = input("Ingregiente / fin: ").lower()
                if input_ingredients != 'fin': new_ingredients.append(input_ingredients)
            keys = list(to_update.keys())
            to_update[keys[key_to_update]] = new_ingredients
            updated_food = to_update
    
    elif key_to_update == 4 or key_to_update == 5:
        new_value = input("Ingrese la nueva informacion: ")
        keys = list(to_update.keys())
        to_update[keys[key_to_update]] = int(new_value)
        updated_food = to_update
         
    elif key_to_update == 6:
        new_value = input("Ingrese la nueva informacion: ")
        keys = list(to_update.keys())
        to_update[keys[key_to_update]] = True if new_value == "si" else False
        updated_food = to_update
    
    return updated_food














    


