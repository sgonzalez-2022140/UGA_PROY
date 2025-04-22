# Autores: Jonathan Garcia | Santiago Gonzalez 
# Carnet: 25001306 | 25000328
# Sección: A 

import os

#Aqui mostramos el mensaje de Bienvenida
def bienvenida():
    print("Bienvenido a nuestro codificador")
    print("Creado por: Santiago Gonzalez y Jonathan  Garcia")
    print("Escribe un comando o 'quit' para salir ")

#Convierte una letra en su posición correspondiente dentro del abecedario (A=0, B=1,...).
def letra_numero(letra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return abecedario.index(letra.upper())

#Convierte un número (0-25) en su letra correspondiente del abecedario.
def numero_letra(numero):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return abecedario[numero % 26]

# Construcción de la tabla Vigenère, al parecer desplaza el abecedario por medio de una matriz
vinegre = []
for fila_num in range(26):
    fila = []
    for col_num in range(26):
        letra = numero_letra(fila_num + col_num)
        fila.append(letra)
    vinegre.append(fila)

#Codifica una letra usando una letra clave con la tabla Vigenère.
def codificar_letra(letra, clave_letra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letra.upper() not in abecedario:
        return letra

    if clave_letra.upper() not in abecedario:
        return letra

    mayuscula = letra.isupper()
    fila = letra_numero(clave_letra)
    columna = letra_numero(letra)
    nueva_letra = vinegre[fila][columna]
    return nueva_letra if mayuscula else nueva_letra.lower()

#Decodifica una letra usando una letra clave con la tabla Vigenère.
def decodificar_letra(letra, clave_letra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letra.upper() not in abecedario:
        return letra

    if clave_letra.upper() not in abecedario:
        return letra

    mayuscula = letra.isupper()
    fila = letra_numero(clave_letra)
    fila_letras = vinegre[fila]
    columna = fila_letras.index(letra.upper())
    original = numero_letra(columna)
    return original if mayuscula else original.lower()

#Codifica un texto completo utilizando una llave previamente establecida.
def codificar_texto(texto, clave):
    if not clave:
        return "ERROR! No se ha establecido una llave"
    resultado = ""
    j = 0
    for letra in texto:
        if letra.isalpha():
            letra_clave = clave[j % len(clave)]
            resultado += codificar_letra(letra, letra_clave)
            j += 1
        else:
            resultado += letra
    return resultado

#Decodifica un texto completo utilizando una llave previamente establecida.
def decodificar_texto(texto, clave):
    if not clave:
        return "ERROR! No se ha establecido una llave"
    resultado = ""
    j = 0
    for letra in texto:
        if letra.isalpha():
            letra_clave = clave[j % len(clave)]
            resultado += decodificar_letra(letra, letra_clave)
            j += 1
        else:
            resultado += letra
    return resultado

#Codifica el contenido de un archivo y guarda el resultado en un nuevo archivo
def codificar_archivo(nombre_archivo, clave):
    if not os.path.exists(nombre_archivo):
        return "ERROR! El archivo " + nombre_archivo + " no existe"

    try:
        with open(nombre_archivo, 'r', encoding='latin-1') as archivo:
            contenido = archivo.read()

        codificado = codificar_texto(contenido, clave)
        nombre_salida = nombre_archivo.replace('.txt', '.gcf')

        contador = 1
        while os.path.exists(nombre_salida):
            nombre_salida = nombre_archivo.replace('.txt', '(' + str(contador) + ').gcf')
            contador += 1

        with open(nombre_salida, 'w', encoding='latin-1') as archivo_salida:
            archivo_salida.write(codificado)

        return "archivo codificado en " + nombre_salida
    except Exception as e:
        return "ERROR! Archivo " + nombre_archivo + " esta corrupto: " + str(e)

#Decodifica un archivo .gcf y guarda el resultado en un archivo .txt
def decodificar_archivo(nombre_archivo, clave):
    if not os.path.exists(nombre_archivo):
        return "ERROR! El archivo " + nombre_archivo + " no existe"

    try:
        with open(nombre_archivo, 'r', encoding='latin-1') as archivo:
            contenido = archivo.read()

        decodificado = decodificar_texto(contenido, clave)
        nombre_salida = nombre_archivo.replace('.gcf', '-decoded.txt')

        contador = 1
        while os.path.exists(nombre_salida):
            nombre_salida = nombre_archivo.replace('.gcf', '-decoded(' + str(contador) + ').txt')
            contador += 1

        with open(nombre_salida, 'w', encoding='latin-1') as archivo_salida:
            archivo_salida.write(decodificado)

        return "archivo codificado en " + nombre_salida
    except Exception as e:
        return "ERROR! Archivo " + nombre_archivo + " esta corrupto: " + str(e)

# -------------- COMANDOS -----------------------
def comandos(comando, llave):
    if not comando:
        return "ERROR! Expresión no válida", llave

    if comando == "quit":
        return "quit", llave

    elif comando.startswith("setkey "):
        partes = comando.split()
        if len(partes) == 2 and partes[1].isalpha():
            return "nueva llave aceptada", partes[1]
        else:
            return "ERROR! Llave no válida", llave

    elif comando.startswith("encode-text "):
        texto = comando[len("encode-text "):]
        return codificar_texto(texto, llave), llave

    elif comando.startswith("decode-text "):
        texto = comando[len("decode-text "):]
        return decodificar_texto(texto, llave), llave

    elif comando.startswith("encode-file"):
        partes = comando.split()
        if len(partes) == 3:
            clave_archivo = partes[1]
            nombre = partes[2]
            return codificar_archivo(nombre, clave_archivo), llave
        elif len(partes) == 2:
            nombre = partes[1]
            return codificar_archivo(nombre, llave), llave
        else:
            return "ERROR! Expresión no válida", llave

    elif comando.startswith("decode-file"):
        partes = comando.split()
        if len(partes) == 3:
            clave_archivo = partes[1]
            nombre = partes[2]
            return decodificar_archivo(nombre, clave_archivo), llave
        elif len(partes) == 2:
            nombre = partes[1]
            return decodificar_archivo(nombre, llave), llave
        else:
            return "ERROR! Expresión no válida", llave

    else:
        return "ERROR! Comando no reconocido", llave

#Función principal que inicia el programa e interactúa con el usuario.
def main():
    llave = ""
    bienvenida()

    while True:
        entrada = input("codificador >> ").strip()
        resultado, llave = comandos(entrada, llave)

        if resultado == "quit":
            print("Saliendo ...")
            print("Gracias por usar nuestro codificador.")
            break
        else:
            print("resultado >>", resultado)

#Llama a la función principal para iniciar el programa.
main()
