import math 

# Ejercicios de "Presentación - Semana 03"
def ejer1():
    PuntoT1 = 0.15
    PuntoEP = 0.30
    PuntoT2 = 0.15
    PuntoEF = 0.40

    T1 = float(input("Ingrese la nota de su T1: "))
    EP = float(input("Ingrese la nota de su Evaluación Parcial: "))
    T2 = float(input("Ingrese la nota de su T2: "))
    EF = float(input("Ingrese la nota de su Evaluación Final: "))
    
    Promedio = (T1 * PuntoT1) + (EP * PuntoEP) + (T2 * PuntoT2) + (EF * PuntoEF)
    
    print("\nEl promedio que ha obtenido es de: ", Promedio, " puntos.")

def ejer2():
    Pasajero = 40
    Km = float(input("Buen día. Ingrese la cantidad de km que recorrerá: "))
    PrecioCombustible = float(input("Ingrese el precio del galón de combustible: S/"))
    
    Galon = Km / 20
    GastosOperativos = PrecioCombustible * Galon
    Ganancia = GastosOperativos * 0.60
    Total = GastosOperativos + Ganancia
    PrecioPasaje = Total / Pasajero

    print("\nSe usarán un total de: ", Galon, " galones.")
    print("Gastos operativos: S/", GastosOperativos)
    print("Ganancia: S/", Ganancia)
    print("Costo por pasaje: S/", PrecioPasaje)

def ejer3():
    CInicial = float(input("Buen día. Ingrese el monto del préstamo que desea solicitar: S/"))
    Interes = float(input("Ingrese el interés que pagará por año: "))
    Tiempo = float(input("Ingrese el tiempo (en años) que durará el préstamo: "))

    CFinal = CInicial * math.pow((1 + Interes / 100), Tiempo)

    print("\n--------------")
    print("| RESULTADOS |")
    print("--------------")
    print("Capital Final: S/", CFinal)
    print("Monto Extra: S/", (CFinal - CInicial))

# Ejercicios de "JP - Semana 03"
def ejer4():
    Nombre = input("Buen día. Ingrese su nombre, por favor: ")
    Carrera = input("Ingrese su carrera: ")

    print("\n<", Nombre, ">, bienvenido al curso de Fundamentos de Algoritmos de la carrera <", Carrera, ">")

def ejer5():
    Nombre = input("Buen día. Ingrese su nombre, por favor: ")

    print('\n"',Nombre,'"')

def ejer6():
    Num1 = int(input("Buen día. Ingrese su primer número entero, por favor: "))
    Num2 = int(input("Ingrese su segundo número entero: "))

    print("\nSuma: ", (Num1 + Num2))
    print("Resta: ", (Num1 - Num2))
    print("Multiplicación: ", (Num1 * Num2))
    print("División: ", (Num1 / Num2))

def ejer7():
    Decimal = float(input("Buen día. Ingrese un número decimal, por favor: "))

    print("\nRaíz cuadrada: ", (Decimal ** 1/2))
    print("Redondeado a entero: ", round(Decimal))
    print("Decimal al cubo: ", pow(Decimal, 3))
    print("Raíz cúbica: ", (Decimal ** 1/3))

def ejer8():
    NumeroTexto = input("Buen día. Ingrese un número, por favor: ")
    
    Entero = int(NumeroTexto)
    Decimal = float(NumeroTexto)

    print("\nEl resto al dividir entre 2 ese número es: ", (Entero % 2))
    print("Resultado al dividir ese número entre 3: ", (Decimal / 3))

def ejer9():
    Segundos = int(input("Buen día. Ingrese una cantidad de segundos: "))
    
    Horas = Segundos / 3600
    Minutos = (Segundos % 3600) / 60
    SegundosRestantes = Segundos % 60

    print("\nHoras: ", Horas)
    print("Minutos: ", Minutos)
    print("Segundos restantes: ", SegundosRestantes)

# Ejercicios de "Ejercicios Propuestos"
def ejer10():
    Contrasena = input("Buen día. Ingrese una contraseña: ")
    ClaveGuardada = input("Vuelva a ingresar la contraseña: ")
    
    if Contrasena.lower() == ClaveGuardada.lower():
        print("\nContraseña coincidente.")
    else:
        print("\nContraseña no coincide.")

def ejer11():
    Num1 = int(input("Buen día. Ingrese su primer número: "))
    Num2 = int(input("Ingrese su segundo número: "))

    if Num2 == 0:
        print("\nError.")
    else:
        print("\nResultado de la división: ", (Num1 / Num2))

def ejer12():
    Num = int("Buen día. Ingrese un número: ")

    if Num % 2 == 0:
        print("\nSu número es par.")
    else:
        print("\nSu número es impar.")

def ejer13():
    Edad = int(input("Buen día. Ingrese su edad: "))

    if Edad > 16:
        Salario = int(input("Ingrese su sueldo: S/"))

        if Salario >= 1000.00:
            print("\nLe corresponde tributar.")
        else:
            print("\nNo le corresponde tributar debido a su salario.")
    else:
        print("\nNo le corresponde tributar debido a su edad.")

def ejer14():
    Tiempo = int(input("Buen día. Ingrese el tiempo de estacionamiento en minutos: "))

    Horas = math.ceil(Tiempo / 60)
    Pago = Horas * 2.50

    print("\nPago por el estacionamiento: S/", Pago)

def ejer15():
    Num = int(input("Buen día. Ingrese un número: "))

    if Num % 2 == 0:
        print("\nSu número es par.")
    else:
        print("\nSu número es impar.")

    if Num >= 0:
        print("\nSu número es positivo.")
    else:
        print("\nSu número es negativo.")

def ejer16():
    Descuento = 0.10
    Obsequio = 0

    Unidades = int(input("Buen día. Ingrese la cantidad de productos a comprar (unidades): "))

    Docena = Unidades / 12

    Precio = float(input("Ingrese el precio unitario: S/"))

    Monto = Precio * Unidades

    if Docena > 3:
        Descuento = 0.15
        Obsequio = 1

    MontoDescuento = Monto * Descuento
    MontoPagar = Monto - MontoDescuento

    print("\n--------------")
    print("| RESULTADOS |")
    print("--------------")
    print("Monto de la compra: S/", Monto)
    print("Monto del descuento: S/", MontoDescuento)
    print("Monto a pagar: S/", MontoPagar)
    print("# de unidades de obsequio: ", Obsequio)

def ejer17():
    Num = int(input("Buen día. Por favor, ingrese un número de 3 cifras: "))

    Cifra1 = Num / 100
    Cifra2 = (Num / 10) % 10
    Cifra3 = Num % 10

    if Cifra1 == Cifra3:
        print("\nEl número es igual al revés.")
    else:
        print("\nEl número no es igual al revés.")

def ejer18():
    Monto = 60.00

    Km = float(input("Buen día. Ingrese la cantidad de KM a recorrer: "))

    if Km <= 300:
        MontoAdicional = 0
    else:
        if Km > 300 and Km <= 1000:
            KmExceso = Km - 300
            MontoAdicional = KmExceso * 1.50
        else:
            if Km > 1000:
                KmExceso = Km - 1000
                MontoAdicional = (700 * 1.5) + KmExceso * 1.10

    PrecioPagar = Monto + MontoAdicional
    PrecioImpuesto = PrecioPagar * 20 / 120

    print("\nMonto a pagar: S/", PrecioPagar)
    print("Monto incluído del impuesto: S/", PrecioImpuesto)

def ejer19():
    Nota1 = int(input("Buen día. Ingrese su primera nota: "))
    Nota2 = int(input("Ingrese su segunda nota: "))
    Nota3 = int(input("Ingrese su tercera nota: "))
    Nota4 = int(input("Ingrese su última nota: "))

    if Nota1 < Nota2 and Nota1 < Nota3 and Nota1 < Nota4:
        NotaEliminada = Nota1
    else:
        if Nota2 < Nota1 and Nota2 < Nota3 and Nota2 < Nota4:
            NotaEliminada = Nota2
        else:
            if Nota3 < Nota1 and Nota3 < Nota2 and Nota3 < Nota4:
                NotaEliminada = Nota3
            else:
                NotaEliminada = Nota4

    Promedio = ((Nota1 + Nota2 + Nota3 + Nota4) - NotaEliminada) / 3

    print("\nNota eliminada: ", NotaEliminada)
    print("Su promedio de prácticas es: ", Promedio)

ejer19()