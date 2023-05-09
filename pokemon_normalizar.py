import re

def sanitizar_entero(numero:str):
    '''
    Brief: sanitiza el string validando que sean solo numeros y que sea positivo,
    luego lo castea a entero y lo retorna
    Parameters:
        numero: es el string que se valida si contiene caracteres alfabeticos
    return: si el string contiene un caracter alfabetico retorna -1, en caso de ser negativo retorna -2,
    si es 0 u otro error retorna -3. Si tiene exito retorna el entero postivo
    '''
    if type(numero) == str:
        numero = numero.strip()
        resultado = numero.isdigit()
        if resultado == False:
            retorno = -1
        else:
            entero = int(numero)
            if entero > 0:
                retorno = entero
            elif entero < 0:
                retorno = -2
            else:
                retorno = -3
    else:
        retorno = -3    
    return retorno

def sanitizar_flotante(numero:str):
    '''
    Brief: sanitiza el string validando que sean solo numeros y que sea positivo,
    luego lo castea a flotante y lo retorna
    Parameters:
        numero: es el string que se valida si contiene caracteres alfabeticos
    return: si el string contiene un caracter alfabetico retorna -1, en caso de ser negativo retorna -2,
    si es 0 u otro error retorna -3. Si tiene exito retorna el flotante postivo
    '''
    if type(numero) == str:
        numero = numero.strip()
        resultado = numero.replace(".","").isdigit()
        if resultado == False:
            retorno = -1
        else:
            flotante = float(numero)
            if flotante > 0:
                retorno = flotante
            elif flotante < 0:
                retorno = -2
            else:
                retorno = -3
    else:
        retorno = -3
    return retorno

def sanitizar_string(cadena:str):
    '''
    Brief: sanitiza el string validando si contiene simbolos y si contiene numeros, 
    si tiene exito se retorna el string
    Parameters:
        valor_str: es el string que se valida
    return: retorna el string si tiene exito, retonra N/A si hubo algun error
    '''
    if type(cadena) == str:
        cadena = cadena.strip()
        valor_str = cadena
        valor_str = re.sub(r"[^\w]+"," ", valor_str)
        resultado = valor_str.replace(" ","").isalpha()
        if resultado == True:
            retorno = cadena
        else:
            retorno = "N/A"
    else:
        retorno = "Error. Tipo de datos incorrectos"
    return retorno

def sanitizar_dato(pokemon:dict,clave:str,tipo_dato:str) -> bool:
    '''
    Brief: sanitiza el dato segun el tipo de dato en el parametro elegido del diccionario pokemon y su clave.
    Segun el resultado de la sanitizacion del tipo de dato elegido resultara en un exito o un error
    Parameters:
        pokemon: es el diccionario elegido para sanitizar el dato
        clave: es la clave que se busca en el diccionario para sanitizar el valor
        tipo_dato: es el tipo de dato que se quiere sanitizar
    return: si tuvo exito en alguna sanitizacion devuelve True, sino devuelve False
    '''
    bandera = False
    if type(pokemon) == dict and type(clave) == str and type(tipo_dato) == str:
        if clave in pokemon:
            tipo_dato = tipo_dato.lower()
            if tipo_dato == "string":
                pokemon[clave] = sanitizar_string(pokemon[clave])
                bandera = True
            elif tipo_dato == "flotante":
                resultado = sanitizar_flotante(pokemon[clave])
                if resultado == -1:
                    print(f"Error. Existen caracteres alfabeticos en {clave}")
                    print(pokemon)
                elif resultado == -2:
                    print(f"Error. El numero es negativo en {clave}")
                    print(pokemon)
                elif resultado == -3:
                    print(f"Error. El valor es 0 en {clave}")
                    print(pokemon)
                else:
                    pokemon[clave] = resultado
                    bandera = True
            elif tipo_dato == "entero":
                resultado = sanitizar_entero(pokemon[clave])
                if resultado == -1:
                    print(f"Error. Existen caracteres alfabeticos en {clave}")
                    print(pokemon)
                elif resultado == -2:
                    print(f"Error. El numero es negativo en {clave}")
                    print(pokemon)
                elif resultado == -3:
                    print(f"Error. El valor es 0 en {clave}")
                    print(pokemon)
                else:
                    pokemon[clave] = resultado
                    bandera = True
            else:
                print("Tipo de dato no reconocido")  
        else:
            print("La clave especificada no existe en el pokemon")
    else:
        print("Error. Tipo de datos incorrectos")
    return bandera

def guardar_en_coleccion(valor:str):
    '''
    Brief: guarda en una coleccion las cadenas alfabeticas separadas por un separador.
    Cambia el formato de escritura de cada cadena a Capitalize
    Parameters:
        valor: es la cadena que se quiere guardar en una coleccion
    Return: retorna la lista nueva con el nuevo formato de escritura si tiene exito, sino devuelve -1
    '''
    if type(valor) == str:
        lista_valor = re.findall(r"[\w ]+",valor)
        lista_nueva = []
        for elemento in lista_valor:
            elemento = elemento.capitalize()
            lista_nueva.append(elemento)
        retorno = lista_nueva
    else:
        print("Tipo de dato no admitido")
        retorno = -1
    return retorno

def normalizar_datos(lista:list):
    '''
    Brief: normaliza los datos elegidos de cada elemento en la lista.
    En el caso de 'tipo' y 'habilidades' se guardan en una coleccion si tiene exito en la sanitizacion
    Parameters:
        lista: es la lista en la que se trabaja para normalizar los datos de cada elemento
    return: Retorna 1 si los datos fueron normalizados con exito, -1 si hubo un error
    '''
    if type(lista) == list and len(lista) > 0:
        bandera = True
        datos_normalizados = True
        for pokemon in lista:
            if sanitizar_dato(pokemon,"N° Pokedex","entero") == False:
                bandera = False
            if sanitizar_dato(pokemon,"Nombre","string") == False:
                bandera = False
            if sanitizar_dato(pokemon,"Tipo","string") == False:
                bandera = False
            else:
                pokemon["Tipo"] = guardar_en_coleccion(pokemon["Tipo"])
            if sanitizar_dato(pokemon,"Poder de Ataque","entero") == False:
                bandera = False
            if sanitizar_dato(pokemon,"Poder de Defensa","entero") == False:
                bandera = False
            if sanitizar_dato(pokemon,"Habilidades","string") == False:
                bandera = False
            else:
                pokemon["Habilidades"] = guardar_en_coleccion(pokemon["Habilidades"])
            if bandera == False:
                datos_normalizados = False
        if datos_normalizados == False:
            print("Error. No se pudo normalizar todos los datos")
            retorno = -1
        else:
            print("Datos normalizados")
            retorno = 1
    else:
        print("Tipo de dato no admitido / Lista vacía")
        retorno = -1
    return retorno