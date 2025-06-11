def calcular():
    print("Calculadora Simple")
    print("Operaciones: + (suma)")
    
    while True:
        # Entrada de usuario
        num1 = float(input("Ingrese primer número: "))
        operador = input("Ingrese operador: ")
        num2 = float(input("Ingrese segundo número: "))
        
        # Lógica de operaciones
        if operador == '+':
            resultado = num1 + num2
    
            if num2 == 0:
                print("¡Error! No se puede dividir por cero")
                continue
            resultado = num1 / num2
        else:
            print("Operador inválido. Use +, -, * o /")
            continue
        
        # Mostrar resultado
        print(f"Resultado: {num1} {operador} {num2} = {resultado}\n")
        
        # Preguntar por otra operación
        continuar = input("¿Otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    calcular()