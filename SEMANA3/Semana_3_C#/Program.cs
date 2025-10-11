using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana_3_C_
{
    internal class Program
    {
        // Ejercicios de "Presentación - Semana 03"
        static void Main(string[] args)
        {
            ejer19();
            Console.ReadKey();
        }
        static void ejer1()
        {
            //INICIO
            double T1, EP, T2, EF, PuntoT1 = 0.15, PuntoEP = 0.30, PuntoT2 = 0.15, PuntoEF = 0.40, Promedio;

            //PROCESO
            Console.Write("Ingrese la nota de su T1: ");
            T1 = double.Parse(Console.ReadLine());
            Console.Write("Ingrese la nota que obtuvo en su Evaluación Parcial: ");
            EP = double.Parse(Console.ReadLine());
            Console.Write("Ingrese la nota de su T2: ");
            T2 = double.Parse(Console.ReadLine());
            Console.Write("Ingrese la nota que obtuvo en su Evaluación Final: ");
            EF = double.Parse(Console.ReadLine());

            Promedio = (T1 * PuntoT1) + (EP * PuntoEP) + (T2 * PuntoT2) + (EF * PuntoEF);

            //FIN
            Console.WriteLine("El promedio que ha obtenido es de: " + Math.Round(Promedio, 2) + " puntos.");

        }

        static void ejer2()
        {
            //Inicio
            double Km, PrecioCombustible, GastosOperativos, Ganancia, Total, PrecioPasaje;
            int Pasajero = 40, Galon;

            //Proceso
            Console.Write("Buen día. Ingrese la cantidad de km que recorrerá: ");
            Km = double.Parse(Console.ReadLine());
            Console.Write("Ingrese el precio del galón de combustible: S/");
            PrecioCombustible = double.Parse(Console.ReadLine());

            Galon = (int)(Km / 20);
            GastosOperativos = PrecioCombustible * Galon;
            Ganancia = GastosOperativos * 0.60;
            Total = GastosOperativos + Ganancia;
            PrecioPasaje = Total / Pasajero;

            //Fin
            Console.WriteLine("Se usarán un total de: " + Galon + " galones.");
            Console.WriteLine("Gastos operativos: S/" + Math.Round(GastosOperativos, 2));
            Console.WriteLine("Ganancia: S/" + Math.Round(Ganancia, 2));
            Console.WriteLine("Costo por pasaje: S/" + Math.Round(PrecioPasaje, 2));
        }         
        static void ejer3()
        {
            //Inicio
            double CFinal, CInicial, Interes, Tiempo;

            //Proceso
            Console.Write("Buen día. Ingrese el monto del préstamo que desea solicitar: S/");
            CInicial = double.Parse(Console.ReadLine());
            Console.Write("Ingrese el interés que pagará por año: ");
            Interes = double.Parse(Console.ReadLine());
            Console.Write("Ingrese el tiempo (en años) que durará el préstamo: ");
            Tiempo = double.Parse(Console.ReadLine());

            CFinal = CInicial * Math.Pow((1 + Interes / 100), Tiempo);

            
            //Fin
            Console.WriteLine("———————-----");
            Console.WriteLine(" RESULTADOS ");
            Console.WriteLine("———————-----");
            Console.WriteLine("Capital Final: S/" + Math.Round(CFinal, 2));
            Console.WriteLine("Monto extra: S/" + Math.Round((CFinal - CInicial), 2));
        }

        // Ejercicios de "JP - Semana 03"
        static void ejer4()
        {
            //INICIO
            string Nombre, Carrera;

            //PROCESO
            Console.Write("Buen día. Ingrese su nombre, por favor: ");
            Nombre = Console.ReadLine();
            Console.Write("Ingrese su carrera: ");
            Carrera = Console.ReadLine();

            //FIN
            Console.WriteLine("<" + Nombre + ">, bienvenido al curso de Fundamentos de Algoritmos de la carrera <" + Carrera + ">");
        }        
        static void ejer5()
        {
            //Inicio
            string Nombre;

            //Proceso
            Console.Write("Buen día. Ingrese su nombre, por favor: ");
            Nombre = Console.ReadLine();

            //Fin
            Console.WriteLine("\"" + Nombre + "\"");
        }        
        static void ejer6()
        {
            //INICIO
            int Num1, Num2;

            //PROCESO
            Console.Write("Buen día. Ingrese su primer número entero, por favor: ");
            Num1 = int.Parse(Console.ReadLine());
            Console.Write("Ingrese su segundo número entero: ");
            Num2 = int.Parse(Console.ReadLine());

            //FIN
            Console.WriteLine("Suma: " + (Num1 + Num2));
            Console.WriteLine("Resta: " + (Num1 - Num2));
            Console.WriteLine("Multiplicación: " + (Num1 * Num2));
            Console.WriteLine("División: " + ((double)Num1 / Num2));
        }        
        static void ejer7()
        {
            //Inicio
            double Decimal;

            //Proceso
            Console.Write("Buen día. Ingrese un número decimal, por favor: ");
            Decimal = double.Parse(Console.ReadLine());

            //Fin
            Console.WriteLine("Raíz cuadrada: " + Math.Sqrt(Decimal));
            Console.WriteLine("Redondeado a entero: " + (int)Math.Round(Decimal));
            Console.WriteLine("Decimal al cubo: " + Math.Pow(Decimal, 3));
            Console.WriteLine("Raíz cúbica: " + Math.Pow(Decimal, 1.0 / 3));
        }        
        static void ejer8()
        {
            //INICIO
            string NumeroTexto;
            int Entero;
            double Decimal;

            //PROCESO
            Console.Write("Buen día. Ingrese un número, por favor: ");
            NumeroTexto = Console.ReadLine();
            Entero = int.Parse(NumeroTexto);
            Decimal = double.Parse(NumeroTexto);

            //FIN
            Console.WriteLine("El resto al dividir entre 2 ese número es: " + (Entero % 2));
            Console.WriteLine("Resultado al dividir es número entre 3: " + (Decimal / 3));
        }
        static void ejer9()
        {
            //Inicio
            int Segundos, Minutos, Horas, SegundosRestantes;

            //Proceso
            Console.Write("Buen día. Ingrese una cantidad de segundos: ");
            Segundos = int.Parse(Console.ReadLine());
            Horas = Segundos / 3600;
            Minutos = (Segundos % 3600) / 60;
            SegundosRestantes = Segundos % 60;

            //Fin
            Console.WriteLine("Horas: " + Horas);
            Console.WriteLine("Minutos: " + Minutos);
            Console.WriteLine("Segundos restantes: " + SegundosRestantes);
        }

        // Ejercicios de "Ejercicios Propuestos"
        static void ejer10()
        {
            //INICIO
            string Contraseña, ClaveGuardada = "contraseña";

            //PROCESO
            Console.Write("Buen día. Ingrese una contraseña: ");
            Contraseña = Console.ReadLine();
            if (Contraseña.ToLower() == ClaveGuardada.ToLower())
            {
                Console.WriteLine("Contraseña coincidente.");
            }
            else
            {
                Console.WriteLine("Contraseña no coincide.");
            }
        }
        static void ejer11()
        {
            //Inicio
            int Num1, Num2;

            //Proceso
            Console.Write("Buen día. Ingrese su primer número: ");
            Num1 = int.Parse(Console.ReadLine());
            Console.Write("Ingrese su segundo número: ");
            Num2 = int.Parse(Console.ReadLine());
            if (Num2 == 0)
            {
                Console.WriteLine("Error.");
            }
            else
            {
                Console.WriteLine("Resultado de la división: " + (Num1 / Num2));
            }
        }
        static void ejer12()
        {
            //INICIO
            int Num;

            //PROCESO
            Console.Write("Buen día. Ingrese un número: ");
            Num = int.Parse(Console.ReadLine());
            if (Num % 2 == 0)
            {
                Console.WriteLine("Su número es par.");
            }
            else
            {
                Console.WriteLine("Su número es impar.");
            }
        }
        static void ejer13()
        {
            //Inicio
            int Edad;
            double Salario;

            //Proceso
            Console.Write("Buen día. Ingrese su edad: ");
            Edad = int.Parse(Console.ReadLine());
            if (Edad > 16)
            {
                Console.Write("Ingrese su sueldo: S/");
                Salario = double.Parse(Console.ReadLine());
                if (Salario >= 1000.00)
                {
                    Console.WriteLine("Le corresponde tributar.");
                }
                else
                {
                    Console.WriteLine("No le corresponde tributar debido a su salario.");
                }
            }
            else
            {
                Console.WriteLine("No le corresponde tributar debido a su edad.");
            }
        }
        static void ejer14()
        {
            //INICIO
            double Pago;
            int Tiempo, Horas;

            //PROCESO
            Console.Write("Buen día. Ingrese el tiempo de estacionamiento en minutos: ");

            Tiempo = int.Parse(Console.ReadLine());
            Horas = (int)Math.Ceiling((double)Tiempo / 60);
            Pago = Horas * 2.50;

            //Fin
            Console.WriteLine("Pago por el estacionamiento: S/" + Math.Round(Pago, 2));
        }
        static void ejer15()
        {
            //Inicio
            int Num;

            //Proceso
            Console.Write("Buen día. Ingrese un número: ");
            Num = int.Parse(Console.ReadLine());
            if (Num % 2 == 0)
            {
                Console.WriteLine("Su número es par.");
            }
            else
            {
                Console.WriteLine("Su número es impar.");
            }
            if (Num >= 0)
            {
                Console.WriteLine("Su número es positivo.");
            }
            else
            {
                Console.WriteLine("Su número es negativo.");
            }
        }
        static void ejer16()
        {
            //INICIO
            int Unidades, Obsequio = 0;
            double Precio, Docena, Descuento = 0.10, Monto, MontoDescuento, MontoPagar;

            //PROCESO
            Console.Write("Buen día. Ingrese la cantidad de productos a comprar (unidades): ");
            Unidades = int.Parse(Console.ReadLine());
            Docena = Unidades / 12.0;
            Console.Write("Ingrese el precio unitario: S/");
            Precio = double.Parse(Console.ReadLine());

            Monto = Precio * Unidades;

            if (Docena > 3)
            {
                Descuento = 0.15;
                Obsequio = 1;
            }

            MontoDescuento = Monto * Descuento;
            MontoPagar = Monto - MontoDescuento;

            //Fin
            Console.WriteLine("———————-----");
            Console.WriteLine(" RESULTADOS ");
            Console.WriteLine("———————-----");
            Console.WriteLine("Monto de la compra: S/" + Math.Round(Monto, 2));
            Console.WriteLine("Monto del descuento: S/" + Math.Round(MontoDescuento, 2));
            Console.WriteLine("Monto a pagar: S/" + Math.Round(MontoPagar, 2));
            Console.WriteLine("# de unidades de obsequio: " + Obsequio);

        }
        static void ejer17()
        {
            //Inicio
            int Num, Cifra1, Cifra2, Cifra3;

            //Proceso
            Console.Write("Buen día. Por favor, ingrese su número de 3 cifras: ");
            Num = int.Parse(Console.ReadLine());

            Cifra1 = Num / 100;
            Cifra2 = (Num / 10) % 10;
            Cifra3 = Num % 10;

            if (Cifra1 == Cifra3)
            {
                Console.WriteLine("El número es igual al revés.");
            }
            else
            {
                Console.WriteLine("El número no es igual al revés.");
            }
        }        
        static void ejer18()
        {
            //INICIO
            double Monto = 60.00, MontoAdicional = 0, PrecioImpuesto, PrecioPagar;
            int Km, KmExceso = 0;

            //PROCESO
            Console.Write("Buen día. Ingrese la cantidad de KM a recorrer: ");
            Km = int.Parse(Console.ReadLine());
            if (Km <= 300)
            {
                MontoAdicional = 0;
            }
            else
            {
                if (Km > 300 && Km <= 1000)
                {
                    KmExceso = Km - 300;
                    MontoAdicional = KmExceso * 1.50;
                }
                else
                {
                    if (Km > 1000)
                    {
                        KmExceso = Km - 1000;
                        MontoAdicional = (700 * 1.50) + (KmExceso * 1.10);
                    }
                }
            }

            PrecioPagar = Monto + MontoAdicional;
            PrecioImpuesto = PrecioPagar * 20 / 120;
            Console.WriteLine("Monto a pagar: S/" + Math.Round(PrecioPagar, 2));
            Console.WriteLine("Monto incluído del impuesto: S/" + Math.Round(PrecioImpuesto, 2));
        }        
        static void ejer19()
        {
            //Inicio
            int Nota1, Nota2, Nota3, Nota4, NotaEliminada;
            double Promedio;

            //Proceso
            Console.Write("Buen día, Ingrese su primera nota: ");
            Nota1 = int.Parse(Console.ReadLine());
            Console.Write("Ingrese su segunda nota: ");
            Nota2 = int.Parse(Console.ReadLine());
            Console.Write("Ingrese su tercera nota: ");
            Nota3 = int.Parse(Console.ReadLine());
            Console.Write("Ingrese su última nota: ");
            Nota4 = int.Parse(Console.ReadLine());
            if (Nota1 < Nota2 && Nota1 < Nota3 && Nota1 < Nota4)
            {
                NotaEliminada = Nota1;
            }
            else
            {
                if (Nota2 < Nota1 && Nota2 < Nota3 && Nota2 < Nota4)
                {
                    NotaEliminada = Nota2;
                }
                else
                {
                    if (Nota3 < Nota1 && Nota3 < Nota2 && Nota3 < Nota4)
                    {
                        NotaEliminada = Nota3;
                    }
                    else
                    {
                        NotaEliminada = Nota4;
                    }
                }
            }
            Promedio = ((Nota1 + Nota2 + Nota3 + Nota4) - NotaEliminada) / 3.0;
            Console.WriteLine("Nota Eliminada: " + NotaEliminada);
            Console.WriteLine("Su promedio de prácticas es: " + Math.Round(Promedio, 2));
        }        
    }
}
