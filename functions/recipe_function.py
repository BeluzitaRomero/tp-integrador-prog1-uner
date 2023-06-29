# 3. Generar un mecanismo para agregar a la información existente los pasos para la elaboración de una o
# varias comidas del menú.
from functions.json_functions import get_json

def add_recipe(element):
    food_list = get_json()
    to_add = food_list[element]

    recipe = []
    steps = 1
    print("A continuacion podra agregar uno a uno los pasos de la receta...")
    steps_description = input("Presione la tecla ENTER para comenzar...(ingresar 'fin' para finalizar)")
    while steps_description != 'fin':
        steps_description = input(f"PASO {steps}: ")
        if steps_description != 'fin': recipe.append(steps_description)
        steps += 1

    add_recipe = {**to_add, 'recipe': recipe}
    
    return add_recipe    
    

    