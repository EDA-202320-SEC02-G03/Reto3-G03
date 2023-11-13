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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from tabulate import tabulate
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data = {"fechas": None,
            "magnitudes": None}

    data["fechas"] = om.newMap(omaptype="RBT")
    data["magnitudes"] = om.newMap(omaptype="RBT")

    return data

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    updateDateIndex(data_structs["fechas"], data)
    updateMagIndex(data_structs["magnitudes"], data)

    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def newDataEntry(sismo):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {"sismos": None}
    entry["sismos"] = lt.newList("ARRAY_LIST")
    lt.addLast(entry["sismos"], sismo)
    return entry

def updateDateIndex(map, sismo):
    """
    Se toma la fecha del sismo y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de sismos.
    """
    occurreddate = sismo["time"]
    date = datetime.datetime.strptime(occurreddate, "%Y-%m-%dT%H:%M:%S.%fZ")
    entry = om.get(map, date.date())
    if entry is None:
        datentry = newDataEntry(sismo)
        om.put(map, date.date(), datentry)
    else:
        datentry = me.getValue(entry)
        lst = datentry["sismos"]
        lt.addLast(lst, sismo)
    return map

def updateMagIndex(map, sismo):
    mag = float(sismo["mag"])
    entry = om.get(map, mag)
    if entry is None:
        datentry = newDataEntry(sismo)
        om.put(map, mag, datentry)
    else:
        datentry = me.getValue(entry)
        lst = datentry["sismos"]
        lt.addLast(lst, sismo)
    return map



# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, initialDate, finalDate):
    """
    Función que soluciona el requerimiento 1
    """
    lst = om.values(data_structs["fechas"], initialDate, finalDate)
    x = lt.newList("ARRAY_LIST")
    for cada in lt.iterator(lst):
        for elements in lt.iterator(cada["sismos"]):
            lt.addLast(x, elements)
    a = [lt.getElement(x,lt.size(x)),
         lt.getElement(x,lt.size(x)-1),
         lt.getElement(x,lt.size(x)-2),
         lt.getElement(x,3),
         lt.getElement(x,2),
         lt.getElement(x,1)]
    head = ["mag", "lat", "long", "depth", "sig", "gap", "nst", "title", "cdi", "mmi", "magType", "type", "code"]
    k = []
    for seis in a:
        l = {}
        for header in head:
            l[header] = seis[header]
        
        m = tabulate([l], headers="keys", tablefmt="grid")
        date = seis["time"]
        events = 1
        lista = [date, events, m]
        k.append(lista)
    
    t = tabulate(k, headers=["time","events","details"], tablefmt="grid")
    
    return t


def req_2(data_structs, mag_ini, mag_fin):
    """
    Función que soluciona el requerimiento 2
    """
    lst = om.values(data_structs["magnitudes"], mag_ini, mag_fin)
    
    a = [lt.getElement(lst,lt.size(lst)),
         lt.getElement(lst,lt.size(lst)-1),
         lt.getElement(lst,lt.size(lst)-2),
         lt.getElement(lst,3),
         lt.getElement(lst,2),
         lt.getElement(lst,1)]
    head = ["time", "lat", "long", "depth", "sig", "gap", "nst", "title", "cdi", "mmi", "magType", "type", "code"]
    k = []
    for elementos in a:
        x = elementos["sismos"]
        t = []
        for cada_uno in lt.iterator(x):
            l = []
            for header in head:
                l.append(cada_uno[header])
            t.append(l)
        mag = lt.getElement(x, 1)["mag"]
        events = lt.size(x)
        m = tabulate(t, headers=head, tablefmt="grid")
        lista = [mag, events, m]
        k.append(lista)    
    
    
    t = tabulate(k, headers=["mag","events","details"], tablefmt="grid")
    return t


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

def compare_dates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
