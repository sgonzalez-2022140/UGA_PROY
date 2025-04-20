# Autores: Jonathan Garcia | Santiago Gonzalez 
# Carnet: 25001306 | 25000328
# Sección: A 

def bienvenida():
    print("Bienvenido a nuestro codificador")
    print("Creado por: Santiago Gonzalez y Jonathan  Garcia")
    print("Escribe un comando o 'quit' para salir ")


def letra_numero(letra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return abecedario.index(letra.upper())

def numero_letra(numero):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return abecedario[numero % 26]

def comandos(comando, llave):
    partes = comando.strip().split()

    if partes == "":
        return "ERROR! Expresión no válida", llave

    instruccion = partes[0]

    if instruccion == "quit":
        return "quit", llave
    else: 
        return "comando no reconocido", llave

# Construcción de la tabla Vigenère
vinegre = []
for fila_num in range(26):
    fila = []
    for col_num in range(26):
        letra = numero_letra(fila_num + col_num)
        fila.append(letra)
    vinegre.append(fila)

def codificar_letra(letra, clave_letra):
    mayuscula = letra.isupper()
    fila = letra_numero(clave_letra)
    columna = letra_numero(letra)
    nueva_letra = vinegre[fila][columna]
    return nueva_letra if mayuscula else nueva_letra.lower()

def decodificar_letra(letra, clave_letra):
    mayuscula = letra.isupper()
    fila = letra_numero(clave_letra)
    fila_letras = vinegre[fila]
    columna = fila_letras.index(letra.upper())
    original = numero_letra(columna)
    return original if mayuscula else original.lower()



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


main()