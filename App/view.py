"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import datetime
import traceback
import matplotlib.pyplot as plt

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

filename = "earthquakes//temblores-utf8-large.csv"

def new_controller():
    """
        Se crea una instancia del controlador
    """
    a = controller.new_controller()
    return a


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Conocer los eventos sísmicos entre dos fechas")
    print("3- Conocer los eventos sísmicos entre dos magnitudes")
    print("4- Consultar los 10 eventos más recientes según una magnitud y profundidad indicadas")
    print("5- Consultar los 15 eventos sísmicos más recientes según su significancia y una distancia azimutal")
    print("6- Consultar los 20 eventos más recientes para una profundidad dada y registrados por un cierto número de estaciones")
    print("7- Reportar el evento más significativo y los N eventos más próximos en el área alrededor de un punto indicado")
    print("8- Graficar un histograma anual de los eventos ocurridos según la región y propiedades de los eventos")
    print("9- Visualizar los eventos sísmicos de cada requerimiento en un mapa interactivo")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    a = controller.load_data(control, filename)
    return a 

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass
def print_carga(control):
    a = controller.print_carga(control)
    print("Se cargaron: " + str(a[1]) + " Datos")
    return print(a[0])

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    start_time = controller.get_time()
    initialDate = input("Fecha inicial: ")
    inicial = datetime.datetime.strptime(initialDate, "%Y-%m-%dT%H:%M")
    i = inicial.date()
    finalDate = input("Fecha final: ")
    final = datetime.datetime.strptime(finalDate, "%Y-%m-%dT%H:%M")
    f = final.date()
    a = controller.req_1(control, i, f)
    end_time = controller.get_time()
    elapsed_time = controller.delta_time(start_time, end_time)
    print(f"Tiempo tomado para cargar: {elapsed_time} ms")
    return print(a)

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    start_time = controller.get_time()
    mag_ini = float(input("Magnitud inicial: "))
    mag_fin = float(input("Magnitud final: "))
    a = controller.req_2(control, mag_ini, mag_fin)
    end_time = controller.get_time()
    elapsed_time = controller.delta_time(start_time, end_time)
    print(f"Tiempo tomado para cargar: {elapsed_time} ms")
    return print(a)

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    start_time = controller.get_time()
    print("=============Req No. 3 Inputs =============")
    magnitud = float(input("Min magnitud: "))
    profundidad =float(input("Max Depth: "))
    print("=============Req No. 3 Results =============")
    a,length1 = controller.req_3(control,magnitud,profundidad)
    end_time = controller.get_time()
    elapsed_time = controller.delta_time(start_time, end_time)
    print(f"Tiempo tomado para cargar: {elapsed_time} ms")
    print("Total different dates: ", length1)
    print("Total events between dates:",length1)
    print("Selectin the first 10 results...")
    print("Counsult size: ", length1, "The first an last 3 of the 10 results are: ")
    return print(a)

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    start_time = controller.get_time()
    sig = int(input("Ingrese la significancia minima: "))
    distancia = float(input("Ingrese la distancia azimutal maxima: "))
    a = controller.req_4(control, sig, distancia)
    end_time = controller.get_time()
    elapsed_time = controller.delta_time(start_time, end_time)
    print(f"Tiempo tomado para cargar: {elapsed_time} ms")
    return print(a)

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    start_time = controller.get_time()
    print("=============Req No. 5 Inputs =============")
    profundidad = float(input("Min depth: "))
    estacion = str(input("Max nst (seismic stations): "))
    print("=============Req No. 5 Results =============")
    a,tam = controller.req_5(control, profundidad, estacion)
    end_time = controller.get_time()
    elapsed_time = controller.delta_time(start_time, end_time)
    print(f"Tiempo tomado para cargar: {elapsed_time} ms")
    print("Total different dates: ", tam)
    print("Total events between dates:", tam)
    print("Selecting the first 20 results...")
    print("Counsult size: ", tam, "The first and last 3 of the 20 results are: ")
    return print(a)

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    start_time = controller.get_time()
    año = str(input("Year: "))
    titulo = str(input("Area of interest: "))
    propiedad = str(input("property of interest (mag/ Depth/ sig): "))
    bins = int(input("Number of bins: "))
    a = controller.req_7(control, año, titulo, propiedad, bins)
    end_time = controller.get_time()
    elapsed_time = controller.delta_time(start_time, end_time)
    print(f"Tiempo tomado para cargar: {elapsed_time} ms")
    plt.hist(a[0], bins, density=True)
    plt.title("Histogram of " + propiedad + " in " + titulo + " in " + año)
    plt.xlabel(propiedad)
    plt.ylabel("No. Events")
    plt.show()
    return print(a[1])

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print_carga(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
