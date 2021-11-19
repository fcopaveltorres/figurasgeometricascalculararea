# Importar el otro archivo que es donde se hace el calculo
import calculo

# Triple comilla te permite hacer interlineado
menu="""
Figuras geometricas para calular su area
1.Cuadrado
2.Circulo
3.Triángulo
4.Trapecio
5.Rectángulo
6.Elipse
7.Salir
"""
continuar = True
# Ciclo while mientras el valor continuar sea verdadero seguira realizando calculos de areas  
while continuar == True:
    # try y except sirve para que no truene la aplicacion por error de tipo de dato
    # en este caso se utlizo por si usuario escribe letras y no numeros
    # sin esto truena la aplicaion al tratar de convertir el dato en numerico
    try:
        print(menu)
        # Convertir dato escrito por el usuario a numero
        op= int(input("Escribe la figura geometrica para calcular: "))
        
        # Condicion numerica que escribio el usuario
        if op == 1:
            L = int(input('Ingrese el lado: '))
            calculo.area_cuadrado(L)
        elif op == 2:
            R = int(input('Ingrese el radio del circulo: '))
            calculo.area_circulo(R)
        elif op == 3:
            b = int(input('Ingrese la base: '))
            h = int(input('Ingrese la altura: '))
            calculo.area_triangulo(b, h)
        elif op == 4:
            B = int(input('Ingrese la base 1: '))
            b = int(input('Ingrese la base 2: '))
            h = int(input('Ingrese la altura: '))
            calculo.area_trapecio(B, b, h)
        elif op == 5:
            b = int(input('Ingrese la base: '))
            h = int(input('Ingrese la altura: '))
            calculo.area_rectangulo(b, h)
        elif op == 6:
            a = int(input('Ingrese el eje menor: '))
            b = int(input('Ingrese el eje mayor: '))
            calculo.area_elipse(a, b)
        elif op == 7:
            i = input("\nSalir de calculo de areas? s/n: ")
            if i == 's' or i == 'S':
                continuar=False
        else:
            # Color para texto en consola
            # Referencia https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal?rq=1
            print('\x1b[0;37;41m' + 'Error ingresa una opcion valida!' + '\x1b[0m')
    # Trono el programa continua pero envia el mensaje por consola
    except:
        print('\x1b[0;37;41m' + 'Error ingresa una opcion valida!' + '\x1b[0m')