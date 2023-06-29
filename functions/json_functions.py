from os import getcwd
from os.path import exists
import json


dir_actual = getcwd()

# ------------------TRAER info del json --------------#
def get_json():
    if file_exists():
        f = open(dir_actual + "/json/lista-comidas.json", "r")
        json_content = f.read()
        json_parse = json.loads(json_content)
        f.close()
        return json_parse
   


# ------------------ACTUALIZAR info del json (Utilizada en la funcion de SAVE) --------------#
def update_json(element):

    json_content = get_json()
    json_content.append(element)

    with open(dir_actual + "/json/lista-comidas.json", "w") as file:
        file.write(json.dumps(json_content))

# -------------VERIFICA si el archivo existe (Utilizada en la funcion de SAVE) --------------#
def file_exists():
    file_exists = exists(dir_actual +"/json/lista-comidas.json" )
    return file_exists


# ------------CREAR datos en el json-------#
# Crea un json con los datos a guardar y si ya existe el archivo,
# ejecuta la funcion de update para no sobreescribir y perder los datos previamente guardados
def save_data(data):
    if not file_exists():
        with open(dir_actual + "/json/lista-comidas.json" , "w") as f:

            #Voy a utilizar una sintaxis expandida, similar al spread operator en javascript
            # para agregar el id al diccionario al guardarlo
            json.dump([{"id":1, **data}], f)
    else:
        food_list = get_json()
        id = food_list[-1]["id"] + 1
        update_json({"id":id, **data})


def update_element(element):
    food_list = get_json()
    for food in food_list:
        if food["id"] == element["id"]:
            index_to_update = food_list.index(food)
            food_list[index_to_update] = element

    with open(dir_actual + "/json/lista-comidas.json", "w") as file:
        file.write(json.dumps(food_list))




#-------------ELIMINAR un elemento del json --------------#
def delete_json_content(element):
    food_list = get_json()
    food_list.pop(food_list.index(element))
    
    with open(dir_actual + "/json/lista-comidas.json", "w") as file:
        file.write(json.dumps(food_list))