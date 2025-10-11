#Clase remota:
def ejer1():
    def suma(a,b):
        print("\nLa suma de ambos números es: ", a+b)

    a = int(input("Buen día. Ingrese su primer número: "))
    b = int(input("Ingrese su segundo número: "))

    suma(a,b)

#Con retorno
def ejer2():
    def suma(a,b):
        resultado = a + b
        return resultado

    a = int(input("Buen día. Ingrese su primer número: "))
    b = int(input("Ingrese su segundo número: "))

    print("\nLa suma de ambos números es: ", suma(a,b))

#Otro método
def ejer3():
    def suma():
        a = int(input("Buen día. Ingrese su primer número: "))
        b = int(input("Ingrese su segundo número: "))
        print("\nLa suma de ambos números es: ",a+b)

    suma()

#Método sin parámetros y return
def ejer4():
    def suma():
        a = int(input("Buen día. Ingrese su primer número: "))
        b = int(input("Ingrese su segundo número: "))
        return a+b

    print("\nLa suma de ambos números es: ", suma())

#Ejercicio 5: Un poco más largo
def ejer5():
    def suma(a,b): print("\nLa suma de ambos números es: ", a+b)
    def resta(a,b): print("\nLa resta de ambos números es: ", a-b)
    def multiplicacion(a,b): print("\nLa multiplicación de ambos números es: ", a*b)
    def division(a,b): 
        if b != 0: print("\nLa división de ambos números es: ", a/b)
        else: print("\nError. Denominador no válido.")

    def operaciones():
        while True:
            print("----- Menú de operaciones -----")
            print("\n1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")

            opc = int(input("Ingrese una opción: "))

            a = int(input("\nIngrese su primer número: "))
            b = int(input("Ingrese su segundo número: "))

            match opc:
                case 1: suma(a,b)
                case 2: resta(a,b)
                case 3: multiplicacion(a,b)
                case 4: division(a,b)
                case _: print("¡Opción no válida!")

            conti = input("¿Desea continuar? (y = sí): ")

            if conti.lower() != "y":
                print("\nPrograma finalizado!")
                break
    operaciones()

def ejer6():
    dolar = 3.78
    euro = 4.20
    while True:
        soles = float(input("Ingrese el monto en soles: "))

        def conv_d():
            return round(soles / dolar)
        def conv_e():
            return round(soles / euro)

        print("\nBienvenido al sistema de conversión de monedas.")
        print("\n1. Dólares")
        print("2. Euros")

        opc = int(input("Ingrese una opción: "))

        if opc in(1,2):
            if opc == 1:
                print("Conversión a dólares: ", conv_d())
            else:
                print("Conversión a euros: ", conv_e())
        else:
            print("¡Opción inválida!")

        conti = input("\n¿Desea continuar? (y = sí): ")

        if conti.lower() != "y":
            print("\nPrograma finalizado!")
            break
ejer6()
