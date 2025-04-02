
# Autores: Jonathan Garcia |Santiago Gonzalez 
# Carnet: 25001306 | 25000328
# Sección: A 

def letra_numero(letra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return abecedario.index(letra.upper())

def numero_letra(numero):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return abecedario[numero % 26]

VIGENERE_TABLE = []
for fila_num in range(26):
    fila = []
    for col_num in range(26):
        letra = numero_letra(fila_num + col_num)
        fila.append(letra)
    VIGENERE_TABLE.append(fila)

clave = None

def codificar_letra(letra, clave_letra):
    mayuscula = letra.isupper()
    fila = letra_numero(clave_letra)
    columna = letra_numero(letra)
    nueva_letra = VIGENERE_TABLE[fila][columna]
    return nueva_letra if mayuscula else nueva_letra.lower()

def decodificar_letra(letra, clave_letra):
    mayuscula = letra.isupper()
    fila = letra_numero(clave_letra)
    fila_letras = VIGENERE_TABLE[fila]
    columna = fila_letras.index(letra.upper())
    original = numero_letra(columna)
    return original if mayuscula else original.lower()

def codificar_texto(texto):
    if not clave:
        return "ERROR! No se ha establecido una llave"
    resultado = ""
    j = 0
    for posicion in range(len(texto)):
        letra = texto[posicion]
        if letra.isalpha():
            letra_clave = clave[j % len(clave)]
            resultado += codificar_letra(letra, letra_clave)
            j += 1
        else:
            resultado += letra
    return resultado

def decodificar_texto(texto):
    if not clave:
        return "ERROR! No se ha establecido una llave"
    resultado = ""
    j = 0
    for posicion in range(len(texto)):
        letra = texto[posicion]
        if letra.isalpha():
            letra_clave = clave[j % len(clave)]
            resultado += decodificar_letra(letra, letra_clave)
            j += 1
        else:
            resultado += letra
    return resultado

# NOTA: 
# Falta implementar encode-file y decode-file
# Estas funciones deben leer y escribir archivos usando la clave actual u otra indicada
# Falta verificar si el archivo existe, si está corrupto y manejar nombres duplicados
print("Bienvenido al codificado")
print("Desarrollado por Jonathan Garcia | Santiago Gonzalez")

while True:
    comando = input("codificador >> ")

    if comando == "quit":
        print("Saliendo ...")
        print("Gracias por usar nuestro codificador.")
        break

    elif comando.startswith("setkey "):
        partes = comando.split()
        if len(partes) == 2 and partes[1].isalpha():
            clave = partes[1]
            print("resultado >> nueva llave aceptada")
        else:
            print("resultado >> ERROR! Expresion no valida")

    elif comando.startswith("encode-text "):
        texto = comando[len("encode-text "):]
        if texto:
            print("resultado >>", codificar_texto(texto))
        else:
            print("resultado >> ERROR! Expresion no valida")

    elif comando.startswith("decode-text "):
        texto = comando[len("decode-text "):]
        if texto:
            print("resultado >>", decodificar_texto(texto))
        else:
            print("resultado >> ERROR! Expresion no valida")

    else:
        print("resultado >> ERROR! Expresion no valida")
