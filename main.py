from os import system
from pokemon_parser import (parser_csv,parser_json,crear_json_segun_tipo)
from pokemon_funciones import (menu_principal,listar_cantidad_por_tipo,listar_pokemones_por_tipo,
                               listar_pokemones_por_habilidad, listar_pokemones_ordenados)  
from pokemon_normalizar import (normalizar_datos)



#######################################################################################################

system("cls")

bandera_normalizar = False
while True:
    opcion = menu_principal()
    match opcion:
        case "1":
            lista_pokemon = parser_csv("pokemones.csv")
            if normalizar_datos(lista_pokemon) == 1:
                bandera_normalizar = True
        case "2":
            if bandera_normalizar == True:
                if listar_cantidad_por_tipo(lista_pokemon) == -1:
                    print("No se pudo listar la cantidad por tipo")
            else:
                print("Los datos no estan normalizados")
        case "3":
            if bandera_normalizar == True:
                if listar_pokemones_por_tipo(lista_pokemon) == -1:
                    print("No se pudo listar los pokemones por tipo")
            else:
                print("Los datos no estan normalizados")
        case "4":
            if bandera_normalizar == True:
                if listar_pokemones_por_habilidad(lista_pokemon) == -1:
                    print("No se pudo listar los pokemones por habilidad")
            else:
                print("Los datos no estan normalizados")
        case "5":
            if bandera_normalizar == True:
                if listar_pokemones_ordenados(lista_pokemon) == -1:
                    print("No se pudo ordenar los pokemones")
            else:
                print("Los datos no estan normalizados")
        case "6":
            if bandera_normalizar == True:
                if crear_json_segun_tipo(lista_pokemon,"archivo_pokemon.json") == -1:
                    print("No se creo el archivo")
            else:
                print("Los datos no estan normalizados")
        case "7":
            lista_json = parser_json("archivo_pokemon.json")
            if lista_json == -1:
                print("No se puede leer el archivo")
            else:
                for i in lista_json["pokemones_tipo"]:
                    print(f"{i['Nombre']} - {i['Mayor valor']} - {i['Tipo de poder']}")
        case "S":
            print("Programa finalizado")
            break
        case _:
            print("Error. Intente otra vez")

