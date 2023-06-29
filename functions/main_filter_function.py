import functions.find_functions as filter

def filter_function(filter_value):
    match filter_value:
                case 1:
                    print("---------------------------------------------------------------")
                    ingredient = input("Ingrese el ingrediente buscado: ").lower()
                    print("---------------------------------------------------------------", "Resultado: ", sep="\n")
                    filter.find_by_ingredient(ingredient)

                case 2:
                    price = float(input("Ingrese el precio buscado: "))
                    print("---------------------------------------------------------------", "Resultado: ", sep="\n")
                    filter.find_by_price(price)

                case 3:
                    calories = int(input("Ingrese cantidad de calorias"))
                    print("---------------------------------------------------------------", "Resultado: ", sep="\n")
                    filter.find_by_calories(calories)

                case 4:
                    print("---------------------------------------------------------------", "Resultado: ", sep="\n")
                    filter.find_vegan_food()
