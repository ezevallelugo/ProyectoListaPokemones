import csv
import json
import re
from pokemon_funciones import (crear_lista_auxiliar,crear_diccionario_segun_tipo)

def parser_csv(path:str) -> list:
    '''
    Brief: abre un archivo a modo de lectura y guarda la informacion a una lista de diccionarios y lo devuelve
    Parameters: 
        path: es la ruta de donde se abre el archivo
    return: retorna una lista si tiene éxito, sino devuelve -1
    '''
    if type(path) == str:       
        try:
            with open(path, 'r') as archivo:
                lista = []
                reader = csv.reader(archivo)
                next(reader)
                for line in archivo:
                    register = re.split(",|\n",line)
                    pokemon = {}
                    pokemon["N° Pokedex"] = register[0]
                    pokemon["Nombre"] = register[1]
                    pokemon["Tipo"] = register[2]
                    pokemon["Poder de Ataque"] = register[3]
                    pokemon["Poder de Defensa"] = register[4]
                    pokemon["Habilidades"] = register[5]
                    lista.append(pokemon)
                retorno = lista
        except:
            print("No se encontro el archivo")
            retorno = -1 
    else:
        print("Tipo de dato no admitido")
        retorno = -1    
    return retorno

def guardar_csv(path:str,lista:list):
    if type(path) == str:
        try:
            with open(path, 'w') as archivo:
                for i in lista:
                    archivo.write(i)
                
        except:
            print("No se pudo escribir el archivo")
            retorno = -1
    else:
        retorno = -1
    return retorno

def parser_json(path:str):
    '''
    Brief: abre a modo de lectura el archivo json creado segun la ruta como parametro y devuelve el diccionario
        path: es la ruta elegida por el usuario
    Return: retorna el diccionario en caso de tener exito, caso contrario retorna -1
    '''
    if type(path) == str:
        try:
            with open(path,"r") as archivo:
                data = json.load(archivo)
            retorno = data
        except:
            print("Archivo no encontrado")
            retorno = -1
    else:
        print("Tipo de dato no admitido")
        retorno = -1
    return retorno

def guardar_json(diccionario:dict,path:str):
    '''
    Brief: abre el archivo en modo escritura para guardar en formato json segun la ruta elegida por el usuario
    Parameters:
        diccionario: es el diccionario que se usa para guardar en formato json
        path: es la ruta elegida por el usuario para guardar el archivo
    Return: retorna 1 en caso de tener exito, caso contrario retorna -1
    '''
    if type(diccionario) == dict and type(path) == str:
        try:
            with open(path,"w") as archivo:
                json.dump(diccionario,archivo,indent=4)
            retorno = 1
        except:
            print("No se pudo escribir el archivo")
            retorno = -1
    else:
        print("Tipo de dato no admitido")
        retorno = -1
    return retorno

def crear_json_segun_tipo(lista:list,path:str):
    '''
    Brief: crea el archivo json segun el tipo que el usuario ingrese, lista los tipos primero
    para que el usuario elija, si encuentra coincidencia se guarda el pokemon en un diccionario para 
    luego guardarlo en un archivo json
    Parameters:
        lista: es la lista que se usa para listar los tipos y crear el diccionario
        path: es la ruta elegida por el usuario para guardar el archivo
    Return: retorna 1 si el archivo fue creado, caso contrario retorna -1
    '''
    if type(lista) == list and type(path) == str:
        lista_auxiliar = crear_lista_auxiliar(lista,"Tipo")
        for i in lista_auxiliar:
            print(i)
        tipo = input("Ingrese el tipo a guardar: ")
        tipo = tipo.strip().capitalize()
        if tipo in lista_auxiliar:
            diccionario = crear_diccionario_segun_tipo(lista,tipo)
            if guardar_json(diccionario,path) == 1:
                print("Archivo JSON creado")
                retorno = 1
            else:
                retorno = -1
        else:
            print("No se encuentra coincidencia del tipo")
            retorno = -1
    else:
        print("Tipo de dato no admitido")
        retorno = -1
    return retorno

