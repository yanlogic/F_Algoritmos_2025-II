#Ejercicios resueltos de "Presentación Semana 04 – Ejercicios"
def ejer1():
    anios = int(input("Buen día. Ingrese la cantidad de años que lleva trabajando: "))
    ventas = float(input("Ingrese el monto de sus ventas: S/"))
    print("¿Usted posee hijos?")
    print("[1] - Sí")
    print("[2] - No")
    hijos = int(input("Respuesta: "))

    if anios >= 3 or ventas > 3500.00 or hijos == 1:
        print("\n¡Felicitaciones! Merece dicha bonificación")
    else:
        print("\nLo sentimos. No es acreedor de la bonificación.")

def ejer2():
    descuento = 0

    cantidad = int(input("Buen día. Ingrese la cantidad de productos a comprar: "))
    montototal = float(input("Ingrese el monto total a pagar (sin descuento): S/"))
    print("===================")
    print("[E] - Efectivo")
    print("[T] - Tarjeta")
    print("[R] - Transferencia")
    print("===================")
    pago = input("Seleccione su método de pago: ")

    if cantidad > 10 and pago.upper() == 'E':
        descuento = 0.15
    
    montodescuento = montototal * descuento
    montopagar = montototal - montodescuento

    print("\n----------")
    print("| MONTOS |")
    print("----------")
    print("Monto total: S/", montototal)
    print("Descuento: S/", descuento)
    print("Monto del descuento: S/", montodescuento)
    print("Monto total a pagar: S/", montopagar)

def ejer3():
    sueldo = 1500.00

    print("Buen día. ¿Usted trabaja de día?:")
    print("[S] - Sí")
    print("[N] - No")
    turnomanana = input("Respuesta: ")    
    print("¿Usted trabaja de noche?:")
    print("[S] - Sí")
    print("[N] - No")
    turnonoche = input("Respuesta: ")

    if (turnomanana.upper == 'S') != (turnonoche.upper == 'S'):
        print("\nSu sueldo es de: S/", sueldo)
    else:
        print("\nLo sentimos. No se le pagará el sueldo.")

def ejer4():
    sueldo = 0

    print("=====================")
    print("[G] -  Gerente")
    print("[A] -  Asistente")
    print("[D] -  Adiministrador")
    print("[S] -  Supervisor")
    print("[O] -  Operario")
    print("=====================")
    cargo = input("Buen día. Seleccione el tipo de cargo que ejerce: ")

    match cargo:
        case 'G'|'g':
            sueldo = 7500.00 
            
        case 'A'|'a':
            sueldo = 6000.00        
            
        case 'D'|'d':
            sueldo = 4200.00
            
        case 'S'|'s':
            sueldo = 3000.00
            
        case 'O'|'o':
            sueldo = 2500.00

        case _:
            sueldo = 0

    if sueldo == 0:
        print("\nIngrese una letra válida correspondiente al tipo de cargo.")
    else:
        print("\nEl sueldo que le corresponde es de: S/", sueldo)

def ejer5():
    ajuste = 0.0
    montofinal = 0.0
    descuento = 0.0

    productos = int(input("Buen día. Ingrese la cantidad de productos a comprar: "))
    totalpagar = float(input("Ingrese el monto a pagar: S/"))
    print("=================")
    print("[E] - Efectivo")
    print("[T] - Tarjeta")
    print("[R] - Transferencia")
    print("=================")
    pago = input("Seleccione el método de pago: ")

    if pago.upper() == 'E':
        ajuste = -0.07
    else:
        if pago.upper() == 'T': 
            print("=================")
            print("[D] - Débito")
            print("[C] - Crédito")
            print("=================")
            tarjeta = input("Seleccione el tipo de tarjeta con el que pagará: ")

            if tarjeta.upper() == 'D' and productos > 10:
                ajuste = -0.05
            else: 
                if tarjeta.upper() == 'C':
                    ajuste = 0.05
                else: 
                    print("Seleccione una letra válida.")

        else: 
            if pago.upper() == 'R' and totalpagar == 100.00:
                descuento = 10.00
                
    valorajuste = totalpagar * ajuste
    montofinal = totalpagar + valorajuste - descuento

    print("\n==================")
    print("Monto inicial a pagar: S/", totalpagar)
    if valorajuste < 0:
        print("Monto del descuento: -S/", abs(valorajuste))
    elif valorajuste > 0:
        print("Monto del incremento: +S/", valorajuste)
    else:
        print("No hay descuento ni incremento.")

    print("Monto final a pagar: S/", montofinal)

#Ejercicios resueltos de "Ejercicios Propuestos"
def ejer6():
    montopago = 0
    montohextras = 0
    bonificacionf = 0
    pagohora = 0
    horasextra = 0
    horasregulares = 0

    print("=====================")
    print("[G] -  Gerente")
    print("[A] -  Asistente")
    print("[D] -  Adiministrador")
    print("[S] -  Supervisor")
    print("[O] -  Operario")
    print("=====================")
    cargo = input("Buen día. Seleccione el tipo de cargo que usted tiene: ")

    if cargo.upper() == 'G':
        montopago = 8500.00
    else:
        if cargo.upper() == 'A':
            montopago = 7200.00
        else:
            if cargo.upper() == 'D':
                montopago = 5000.00
            else:
                if cargo.upper() == 'S' or cargo.upper() == 'O':
                    horas = int(input("Ingrese las horas que trabaja a la semana: "))

                    if horas > 40:
                        horasextra = horas - 40
                        horasregulares = horas - horasextra
                    else:
                        horasextra = 0
                        horasregulares = horas

                    if cargo.upper() == 'S':
                        pagohora = 50.50
                    else:
                         if cargo.upper() == 'O':
                             pagohora = 40.25

                    montopago = pagohora * horasregulares
                    montohextras = horasextra * (pagohora * 2)
    
    total = montopago + montohextras

    print("======")
    print("[S] - Sí")
    print("[N] - No")
    print("======")
    estadocivil = input("¿Usted es casado?: ")
    hijos = int(input("Ingrese la cantidad de hijos que usted tiene: "))

    if estadocivil.upper() == 'S' and hijos > 0:
        bonificacionf = 0.15
    else:
        if estadocivil.upper() == 'S' or hijos > 0:
            bonificacionf = 0.10

    montobonificacion = total * bonificacionf
    totalfinal = total + montobonificacion

    print("\n======================")
    print("Monto pago regular: S/", montopago)

    if cargo.upper() == 'S' or cargo.upper() == 'O':
        print("Monto pago horas extras: S/", montohextras)
        print("Horas regulares:", horasregulares)
        print("Horas extra:", horasextra)

    print("Monto por bonificación familiar: S/", montobonificacion)
    print("Total a pagar: S/", totalfinal)

#Ejercicios resueltos de "JP Ejercicios"
def ejer7():
    edad = int(input("Buen día. Ingrese su edad: "))

    if edad < 18:
        print("Usted es menor de edad.")
    else:
        if edad >= 18 and edad <= 64:
            print("Usted es adulto.")
        else:
            if edad >= 65:
                print("Usted es adulto mayor.")
            else:
                print("Aún no naces XD.")

def ejer8():
    anio = int(input("Ingrese el número del año con el cual desea trabajar: "))

    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print("El año es bisiesto.")
    else:
        print("El año no es bisiesto.")

    if anio % 2 == 0:
        print("El año es par.")
    else: 
        print("El año es impar.")

def ejer9():
    soles = float(input("Buen día. Ingrese el monto en soles peruanos que desea convertir a otro tipo de moneda: "))

    print("========")
    print("[D] - Dólar")
    print("[E] - Euro")
    print("========")
    moneda = input("Seleccione el tipo de moneda al que desea convertir el monto en soles: ")

    match moneda.upper():
        case 'D':
            conversion = soles / 3.75
            print("Tipo de moneda seleccionado: Dólar.")
            print("Monto en soles a dólares: S/", conversion)
        case 'E':
            conversion = soles / 4.05
            print("Tipo de moneda seleccionado: Euro.")
            print("Monto en soles a euros: S/", conversion)
        case _:
            print("Seleccione una letra válida.")

def ejer10():
    print("============")
    print("[1] - Cuadrado")
    print("[2] - Rectángulo")
    print("[3] - Triángulo")
    print("[4] - Círculo")
    print("============")
    figura = input("Buen día. Seleccione la figura a la cual desea hallar el área: ")

    match figura:
        case '1':
            ladocuadrado = float(input("Ingrese el lado del cuadrado: "))
            area = ladocuadrado * ladocuadrado
            print("Área del cuadrado:", area, "u2.")
        case '2':
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = base * altura
            print("Área del rectángulo:", area, "u2.")
        case '3':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
            print("Área del triángulo:", area, "u2.")
        case '4':
            radiocirculo = float(input("Ingrese el radio del círculo: "))
            area = 3.14 * (radiocirculo * radiocirculo)
            print("Área del círculo:", area, "u2.")
        case _:
            print("Valor ingresado incorrecto. Seleccione una opción válida.")

ejer10()
