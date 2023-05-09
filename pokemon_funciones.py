
def calcular_promedio(numero1,numero2):
    '''
    Brief: calcula el promedio entre la suma de los dos numeros elegidos como parametros y dividido por 2
    Parameters:
        numero1: es el primer numero a sumar
        numero2: es el segundo numero a sumar
    Return: retorna el resultado en positivo si tuvo exito, si hubo algun error retorna -1
    '''
    if (type(numero1) == int or type(numero1) == float) and (type(numero2) == int or type(numero2) == float):
        suma = numero1 + numero2
        if suma > 0:
            resultado = suma / 2
            retorno = resultado
        else:
            print("Promedio no valido. La suma da un numero negativo o 0")
            retorno = -1
    else:
        print("No se pudo calcular el promedio. Tipo de dato no compatible")
        retorno = -1
    return retorno

def crear_lista_auxiliar(lista:list,clave:str):
    '''
    Brief: crea una lista auxiliar segun la clave que se quiera buscar y guarda todos sus valores en una lista,
    luego se eliminan los repetidos y queda en limpio
    Parameters:
        lista: es la lista que se usa para buscar la clave
        clave: es la clave que se quiere guardar sus valores
    Return: devuelve la lista en limpio si tuvo exito, sino devuelve -1
    '''
    if type(lista) == list and type(clave) == str and len(lista) > 0:
        lista_auxiliar = []
        nueva_lista = []
        for elemento in lista:
            valor = elemento[clave]
            lista_auxiliar.append(valor)
        for sublista in lista_auxiliar:
            for elemento in sublista:
                nueva_lista.append(elemento)
        nueva_lista = list(set(nueva_lista))
        retorno = nueva_lista
    else:
        print("Tipo de dato no admitido / Lista vacia")
        retorno = -1
    return retorno

def buscar_coincidencia_en_sublista(busqueda:str,sublista:list):
    '''
    Brief: busca una coincidencia entre la cadena a buscar y los elementos de la sublista
    Parameters:
        busqueda: es la cadena que se quiere buscar coincidencias
        sublista: es la lista en la que se busca las coincidencias
    Return: si tiene exito al encontrar una coincidencia devuelve 1, sino devuelve -1
    '''
    if type(busqueda) == str and type(sublista) == list:
        bandera = False
        for i in sublista:
            if i == busqueda:
                bandera = True
        if bandera == True:
            retorno = 1
        else:
            retorno = -1
    else:
        print("Tipo de dato no admitido")
        retorno = -1
    return retorno

def listar_cantidad_por_tipo(lista:list):
    '''
    Brief: lista la cantidad que existe y coincida por cada tipo que exista
    Parameters: 
        lista: es la lista que se utiliza para contar las existencias de cada tipo
    Return: retorna 1 en caso de imprimir todos los contadores, -1 si hubo un error
    '''
    if type(lista) == list and len(lista) > 0:
        lista_auxiliar = crear_lista_auxiliar(lista,"Tipo") 
        for tipo in lista_auxiliar:
            contador = 0
            for pokemon in lista:
                if buscar_coincidencia_en_sublista(tipo,pokemon["Tipo"]) == 1:
                    contador += 1        
            print(f"{tipo}: {contador}")
        retorno = 1
    else:
        print("Tipo de dato no admitido / Lista vacia")
        retorno = -1
    return retorno 

def listar_pokemones_por_tipo(lista:list):
    '''
    Brief: lista el nombre y poder de ataque del pokemon que coincida por cada tipo que exista
    Parameters:
        lista: es la lista que se utiliza para listar los pokemones
    Return: retorna 1 en caso de imprimir los pokemones, -1 si encontro un error
    '''
    if type(lista) == list and len(lista) > 0:
        lista_auxiliar = crear_lista_auxiliar(lista,"Tipo") 
        for tipo in lista_auxiliar:
            print(tipo)
            for pokemon in lista:
                if buscar_coincidencia_en_sublista(tipo,pokemon["Tipo"]) == 1:
                    print(f"Nombre: {pokemon['Nombre']} | Poder de ataque: {pokemon['Poder de Ataque']}")
            print("================================================================")
        retorno = 1
    else:
        print("Tipo de dato no admitido / Lista vacia")
        retorno = -1
    return retorno  



def listar_pokemones_por_habilidad(lista:list):
    '''
    Brief: lista los pokemones segun la habilidad que ingresa el usuario, imprime las habilidades existentes
    y por esa habilidad imprime cada pokemon que encuentra coincidencia junto con su nombre, tipo y promedio entre ataque y defensa
    Parameters:
        lista: es la lista que se usa para crear una lista auxiliar y busqueda de coincidencias
    Return: si tiene exito al imprimir los pokemones devuelve 1, sino devuelve -1
    '''
    if type(lista) == list and len(lista) > 0:
        lista_auxiliar = crear_lista_auxiliar(lista,"Habilidades")
        for i in lista_auxiliar:
            print(i)
        habilidad = input("Ingrese la habilidad: ")
        habilidad = habilidad.strip()
        resultado = habilidad.replace(" ","").isalpha()
        if resultado == True:
            habilidad = habilidad.capitalize()
            if habilidad in lista_auxiliar:               
                print(habilidad)
                for pokemon in lista:
                    if buscar_coincidencia_en_sublista(habilidad,pokemon["Habilidades"]) == 1:
                        promedio = calcular_promedio(pokemon["Poder de Ataque"],pokemon["Poder de Defensa"])
                        print(f"Nombre: {pokemon['Nombre']} | Tipo: {pokemon['Tipo']} | Promedio: {promedio:.2f}")
                retorno = 1
            else:
                print("Error. No se encuentran coincidencias")
                retorno = -1
        else:
            print("Error. Cadena no alfabetica")
            retorno = -1
    else:
        print("Tipo de dato no admitido / Lista vacia")
        retorno = -1
    return retorno

def listar_todos_los_pokemones(lista:list):
    if type(lista) == list:
        for pokemon in lista:
            print(f"""
            N° POKEDEX:         {pokemon['N° Pokedex']}
            NOMBRE:             {pokemon['Nombre']}
            TIPO:               {pokemon['Tipo']}
            PODER DE ATAQUE:    {pokemon['Poder de Ataque']}
            PODER DE DEFENSA:   {pokemon['Poder de Defensa']}
            HABILIDADES:        {pokemon['Habilidades']}   
            """)
        retorno = 1
    else:
        retorno = -1
    return retorno

def listar_pokemones_ordenados(lista:list):
    '''
    Brief: lista los pokemones ordenados de mayor a menor poder de atque, y de la A a la Z en 
    casos iguales de poder, luego imprime la lista ordenada
    Parameters:
        lista: es la lista que se usa para el ordenamiento de pokemones
    Return: retorna 1 en caso de tener exito, sino devuelve -1
    '''
    if type(lista) == list and len(lista) > 0:
        for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                if lista[i]["Poder de Ataque"] < lista[j]["Poder de Ataque"]:
                    lista[i],lista[j] = lista[j],lista[i]
                elif lista[i]["Poder de Ataque"] == lista[j]["Poder de Ataque"]:
                    if lista[i]["Nombre"] > lista[j]["Nombre"]:
                        lista[i],lista[j] = lista[j],lista[i]
        for pokemon in lista:            
            print(f"N°: {pokemon['N° Pokedex']:<5} Nombre: {pokemon['Nombre']:<15} PA: {pokemon['Poder de Ataque']:<5} PD: {pokemon['Poder de Defensa']:<5} Tipo: {pokemon['Tipo']} Habilidades: {pokemon['Habilidades']}")
        retorno = 1
    else:
        print("Tipo de dato no admitido / Lista vacia")
        retorno = -1
    return retorno

def crear_diccionario_segun_tipo(lista:list,tipo:str):
    '''
    Brief: crea un diccionario con un valor tipo lista para guardar en formato json. Se guarda 
    solamente el tipo de pokemon que el usuario haya ingresado como parametro
    Parameters:
        lista: es la lista que se usa para buscar coincidencias del tipo de pokemon
        tipo: es el tipo de pokemon que el usuario ingresa para guardar
    Return: retorna el diccionario en caso de tener exito, sino devuelve -1
    '''
    if type(lista) == list and type(tipo) == str and len(lista) != 0:
        diccionario = {}
        diccionario["pokemones_tipo"] = []    
        for pokemon in lista:
            if buscar_coincidencia_en_sublista(tipo,pokemon["Tipo"]) == 1:
                if pokemon["Poder de Ataque"] > pokemon["Poder de Defensa"]:
                    mayor_valor = pokemon["Poder de Ataque"]
                    poder = "Ataque"
                elif pokemon["Poder de Ataque"] < pokemon["Poder de Defensa"]:
                    mayor_valor = pokemon["Poder de Defensa"]
                    poder = "Defensa"
                else:
                    mayor_valor = pokemon["Poder de Ataque"]
                    poder = "Ambos"
                diccionario["pokemones_tipo"].append({"Nombre":pokemon['Nombre'],"Mayor valor":mayor_valor,"Tipo de poder":poder})
        if len(diccionario["pokemones_tipo"]) != 0:
            retorno = diccionario
        else:
            print("No se encontro coincidencia con Pokemon")
            retorno = -1
    else:
        print("Tipo de dato no admitido / Lista vacia")
        retorno = -1
    return retorno

def imprimir_menu():
    '''
    Brief: imprime el menu con las opciones disponibles
    '''
    print("""
    MENU PRINCIPAL
    ==================================================
    1 - Traer datos desde archivo CSV
    2 - Listar cantidad por tipo
    3 - Listar pokemones por tipo
    4 - Listar pokemones por habilidad
    5 - Listar pokemones ordenados por poder de ataque
    6 - Guardar en JSON
    7 - Leer JSON
    S - Salir
    ==================================================
    """)
    
def menu_principal():
    '''
    Brief: imprime el menu principal y le pide al usuario para que elija una opcion
    '''
    imprimir_menu()
    opcion = input("Ingrese su opcion: ")
    opcion = opcion.strip()
    if opcion.isalpha() == True:
        opcion = opcion.upper() 
    return opcion

