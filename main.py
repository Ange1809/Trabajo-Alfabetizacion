from suma import sumar
from resta import resta
from multiplicacion import multiplicacion

def calcular():
    print("Calculadora Simple")
    print("Operaciones: + (suma), - (resta), * (multiplicación)")

    while True:
        try:
            num1 = float(input("Ingrese primer número: "))
            operador = input("Ingrese operador: ")
            num2 = float(input("Ingrese segundo número: "))
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números válidos.")
            continue

        # Lógica de operaciones
        if operador == '+':
            resultado = sumar(num1, num2)
        elif operador == '-':
            resultado = resta(num1, num2)
        elif operador == '*':
            resultado = multiplicacion(num1, num2)
        else:
            print("Operador inválido. Use +, - o *")
            continue

        # Mostrar resultado
        print(f"Resultado: {num1} {operador} {num2} = {resultado}\n")

        # Preguntar por otra operación
        continuar = input("¿Otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    calcular()
