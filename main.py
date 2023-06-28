import crud_functions as crud
from json_functions import save_data, delete_json_content, update_element
from main_filter_function import filter_function
from recipe_function import add_recipe
from details_food import view_details

def main_function():
    print("1) Mostrar comidas rapidas",
        "2) Agregar nueva comida rapida", 
        "3) Borrar una comida", 
        "4) Modificar una comida",
        "5) Ver detalle de una comida",
        "6) Filtrar comidas",
        "7) Agregar receta a una comida",
        sep="\n")
    print("---------------------------------------------------------------")
    input_option = int(input("Ingrese la opcion que desea ejecutar: "))

    match input_option:
        case 1:
            print("---------------------------------------------------------------")
            crud.show_fast_food_list()
            
        case 2:
            print("---------------------------------------------------------------")
            save_data(crud.add_fast_food())
        
        case 3:
            crud.show_fast_food_list()
            to_delete = (int(input("Ingrese el numero de la comida que desea eliminar: "))) -1 
            print("---------------------------------------------------------------")
            delete_json_content(crud.to_delete(to_delete))
            
        case 4:
            crud.show_fast_food_list()
            to_delete = (int(input("Ingrese el numero de la comida que desea modificar: "))) -1
            print("---------------------------------------------------------------")

            update_element(crud.to_update(to_delete))
        
        case 5:
            crud.show_fast_food_list()
            detail = (int(input("Ingrese el numero de la comida que desea visualizar: "))) -1
            print("---------------------------------------------------------------")

            view_details(detail)
     
        case 6:
            print("Filtrar comidas por:", "1) Ingredientes", "2) Precio", "3) Calorias", "4) Comida vegana", sep="\n")
            print("---------------------------------------------------------------")
            filter_option = int(input("Ingrese la opcion de filtro: "))

            filter_function(filter_option)
        
        case 7:
            crud.show_fast_food_list()
            to_add_recipe = (int(input("Ingrese el numero de la comida para agregar receta: "))) -1
            print("---------------------------------------------------------------")

            update_element(add_recipe(to_add_recipe))

            
main_function()