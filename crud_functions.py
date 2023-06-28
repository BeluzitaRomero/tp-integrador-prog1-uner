# necesario registrar los
# siguientes datos:

# De las comidas rápidas que ofrecen en el menú:

# ● Código de Identificación (código número entero positivo),
# ● Descripción (nombre de la comida),
# ● Precio (en Pesos Argentinos)
# ● Lista de ingredientes (de uno a varios ingredientes),
# ● Tiempo de elaboración (en minutos).
# ● Calorías (en gramos)
# ● Vegana (Si o No)

# Requerimientos que se deberán programar en Python.
# La información debe ser registrada en un único archivo en formato JSON.
# Se debe contar con interfaces de usuario interactivas que permitan acceder a las siguientes opciones (debajo
# adjuntamos un ejemplo):

# 1. En referencia a las comidas rápidas:
# ● Mostrar las existentes.
# ▪ Agregar una nueva.
# ▪ Modificar los datos existentes.
# ▪ Borrar una seleccionada.



# 4. OPCIONAL: a este punto lo dejamos a su imaginación para implementar alguna funcionalidad extra
# que ustedes imaginen.


from json_functions import get_json

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
    # for food in food_list:
    #     if food["id"] == id:
    #         to_delete = food
    #         break

    return to_delete

def to_update(position_in_list):
    food_list = get_json()
    print("Cual es la informacion que quiere modificar?:\n1: Titulo\n2: Precio\n3: Ingredientes\n4: Tiempo de coccion\n5: Calorias\n6: Vegano")
    print("---------------------------------------------------------------")
    key_to_update = int(input("Ingrese el numero: "))

    to_update = food_list[position_in_list]

    if key_to_update == 3:
        new_ingredients = []
        input_ingredients = input("'Enter' para comenzar a ingresar ingredientes. Luego 'fin' para terminar: ").lower()
        while input_ingredients != "fin":
            input_ingredients = input("Ingregiente / fin: ").lower()
            if input_ingredients != 'fin': new_ingredients.append(input_ingredients)
        keys = list(to_update.keys())
        to_update[keys[key_to_update]] = new_ingredients
        updated_food = to_update
                
    else:
        #todo HACER OTRAS CONDICIONES PARA DISTINGUIR TYPE STRING, INT Y FLOAT
        new_value = input("Ingrese la nueva informacion: ")
        keys = list(to_update.keys())
        to_update[keys[key_to_update]] = new_value
        updated_food = to_update
    

        
    return updated_food














    


