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
assert cf
import datetime


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
    #TODO: Inicializar las estructuras de datos
    analyzer = {'sismos': None,
                'dateIndex': None
                }

    analyzer['sismos'] = lt.newList('SINGLE_LINKED', comparesismos)
    analyzer['dateIndex'] = om.newMap(omaptype='BST',
                                      cmpfunction=compareDates)
    return analyzer

def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'Magnitud-Prof': None, 'Significancia-distancia':None,'Profundidad-estaciones':None, 'listasismos': None}
    entry['Magnitud-Prof'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=comparemagnitud)
    entry['Significancia-distancia'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=comparesignificancia)
    entry['Profundidad-estaciones'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compareprofundidad)
    entry['listasismos'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry


# Funciones para agregar informacion al modelo

def addsismo(analyzer, sismo):
    """
    funcion que agrega un crimen al catalogo
    """
    lt.addLast(analyzer['sismos'], sismo)
    updateDateIndex(analyzer['dateIndex'], sismo)
    return analyzer

def updateDateIndex(map, sismo):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = sismo['time']
    sismotime = datetime.datetime.strptime(occurreddate, '%Y-%m-%dT%H:%M:%S.%fZ')
    entry = om.get(map, sismotime.date())
    if entry is None:
        datentry = newDataEntry(sismo)
        om.put(map, sismotime.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, sismo)
    return map

def addDateIndex(datentry, sismo):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['listasismos']
    lt.addLast(lst, sismo)
    magnitudes = datentry['Magnitud-Prof']
    newmagnitud = mp.get(magnitudes, sismo['mag'])
    if (newmagnitud is None):
        entry = nuevamagnitud(sismo['mag'], sismo)
        lt.addLast(entry['listasismo'], sismo)
        mp.put(magnitudes, sismo['mag'], entry)
    else:
        entry = me.getValue(newmagnitud)
        if "lstoffenses" not in entry:
            entry['lstoffenses'] = lt.newList()
        lt.addLast(entry['lstoffenses'], sismo)
    return datentry

def nuevamagnitud(magnitud, sismo):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    entradamagnitud = {'magnitud': None, 'listasismo': None}
    entradamagnitud['magnitud'] = magnitud
    entradamagnitud['listasismo'] = lt.newList('SINGLE_LINKED', comparemagnitud)
    return entradamagnitud

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


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


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


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

def comparesismos(sismo1, sismo2):
    """
    Compara dos crimenes
    """
    if (sismo1 == sismo2):
        return 0
    elif sismo1 > sismo2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def comparemagnitud(magnitud1, magnitud2):
    """
    Compara dos tipos de magnitudes
    """
    magnitud = me.getKey(magnitud2)
    if (magnitud1 == magnitud):
        return 0
    elif (magnitud1 > magnitud):
        return 1
    else:
        return -1

def comparesignificancia(significancia1, significancia2):
    """
    Compara dos tipos de significancias
    """
    significancia = me.getKey(significancia2)
    if (significancia1 == significancia):
        return 0
    elif (significancia1 > significancia):
        return 1
    else:
        return -1

def compareprofundidad(profundidad1, profundidad2):
    """
    Compara dos tipos de profundiades
    """
    profundidad = me.getKey(profundidad2)
    if (profundidad1 == profundidad):
        return 0
    elif (profundidad1 > profundidad):
        return 1
    else:
        return -1