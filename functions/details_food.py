# Funcionalidad extra: ver detalle de comida completo. Adaptado para ambos casos (con o sin receta)

from functions.json_functions import get_json

def view_details(element):
    food_list = get_json()
    food = food_list[element]

    print("Nombre:", food["title"])
    print("Precio:", food["price"])
    print("Calorias:", food["calories"])
    print("Tiempo de coccion:", food["time_cook"])
    print("Vegano:", "si" if food["vegan"] == True else "no")

    print("-------------------")

    print("Ingredientes:")
    for ingredient in food["ingredients"]:
        print(ingredient.capitalize())
    
    print("-------------------")
    if "recipe" in food:
        print("Receta:")
        step = 1
        for steps in food["recipe"]:
            print(f"{step}: {steps}")
            step +=1