def bienvenida():
    print("Bienvenido a nuestro codificador")
    print("Creado por: Santiago Gonzalez y Patron Garcia")
    print("Escribe un comando o 'quit' para salir ")


def comandos(comando, llave):
    partes = comando.strip().split()

    if partes == "":
        return "ERROR! Expresión no válida", llave

    instruccion = partes[0]

    if instruccion == "quit":
        return "quit", llave
    else: 
        return "comando no reconocido", llave

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