from suma import sumar


def main():
    print("Bienvenido a la calculadora.")
    print("Opciones: suma")

    opcion = input("Elige una operación: ").lower()
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "suma":
        print("Resultado:", sumar(a, b))
    

if __name__ == "__main__":
    main()
