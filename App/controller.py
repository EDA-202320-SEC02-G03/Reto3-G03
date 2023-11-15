"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    a = model.new_data_structs()
    return a


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for sismo in input_file:
        model.add_data(control, sismo)
    return control


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def print_carga(control):
    a = model.carga(control)
    return a

def req_1(control, initialDate, finalDate):
    """
    Retorna el resultado del requerimiento 1
    """
    a = model.req_1(control, initialDate, finalDate)
    return a

def req_2(control, mag_ini, mag_fin):
    """
    Retorna el resultado del requerimiento 2
    """
    a = model.req_2(control, mag_ini, mag_fin)
    return a

def req_3(control,magnitud,profundidad):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    a,length1 = model.req_3(control,magnitud,profundidad)
    return a,length1

def req_4(control, sig, distancia):
    """
    Retorna el resultado del requerimiento 4
    """
    a = model.req_4(control, sig, distancia)
    return a

def req_5(control, profundidad, estacion):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    a,tam = model.req_5(control, profundidad, estacion)
    return a,tam

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control, año, titulo, propiedad, bins):
    """
    Retorna el resultado del requerimiento 7
    """
    a = model.req_7(control, año, titulo, propiedad, bins)
    return a

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
