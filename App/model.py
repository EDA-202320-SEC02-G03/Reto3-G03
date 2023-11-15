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
import matplotlib.pyplot as plt
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
    data = {"carga": None,
            "times": None,
            "magnitudes": None,
            "significance": None,
            "estacion": None,
            "fechas": None}

    data["carga"] = lt.newList("ARRAY_LIST")
    data["times"] = om.newMap(omaptype="RBT")
    data["magnitudes"] = om.newMap(omaptype="RBT")
    data["significance"] = om.newMap(omaptype="RBT")
    data["estacion"] = om.newMap(omaptype="RBT")
    data["fechas"] = mp.newMap(50000,
                                   maptype='CHAINING',
                                   loadfactor=4)

    return data

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    carga_datos(data_structs["carga"], data)
    updateDateIndex(data_structs["times"], data)
    updateMagIndex(data_structs["magnitudes"], data)
    updateSigIndex(data_structs["significance"], data)
    updateEstacionIndex(data_structs["estacion"], data)
    addFechas(data_structs["fechas"], data)

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

def carga_datos(lst, sismo):
    lt.addLast(lst, sismo)
    return lst

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

def updateSigIndex(map, sismo):
    sig = int(sismo["sig"])
    entry = om.get(map, sig)
    if entry is None:
        datentry = newDataEntry(sismo)
        om.put(map, sig, datentry)
    else:
        datentry = me.getValue(entry)
        lst = datentry["sismos"]
        lt.addLast(lst, sismo)
    return map

def updateDistanceIndex(map, sismo):
    gap = float(sismo["gap"])
    entry = om.get(map, gap)
    if entry is None:
        datentry = newDataEntry(sismo)
        om.put(map, gap, datentry)
    else:
        datentry = me.getValue(entry)
        lst = datentry["sismos"]
        lt.addLast(lst, sismo)
    return map

def addFechas(data_structs, sismo):
    fechas = data_structs
    linea = sismo['time']
    fecha = linea[0:4]
    existe = mp.contains(fechas, fecha)
    #existe retorna True o False
    if existe:
        pareja = mp.get(fechas, fecha)
        valor = me.getValue(pareja)
        lt.addLast(valor["sismos"],sismo)
    else:
        valor = newDataEntry(sismo)
        mp.put(fechas, fecha, valor)
        
def updateProfundidadIndex(map, sismo):
    depth = float(sismo["depth"])
    entry = om.get(map, depth)
    if entry is None:
        datentry = newDataEntry(sismo)
        om.put(map, depth, datentry)
    else:
        datentry = me.getValue(entry)
        lst = datentry["sismos"]
        lt.addLast(lst, sismo)
    return map
    
def updateEstacionIndex(map, sismo):
    nst = sismo["nst"]
    entry = om.get(map, nst)
    if entry is None:
        datentry = newDataEntry(sismo)
        om.put(map, nst, datentry)
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

def carga(data_structs):
    x = data_structs["carga"]
    a = [lt.getElement(x,lt.size(x)),
         lt.getElement(x,lt.size(x)-1),
         lt.getElement(x,lt.size(x)-2),
         lt.getElement(x,lt.size(x)-3),
         lt.getElement(x,lt.size(x)-4),
         lt.getElement(x,5),
         lt.getElement(x,4),
         lt.getElement(x,3),
         lt.getElement(x,2),
         lt.getElement(x,1)]
    head = ["code", "time", "lat", "long", "mag", "title", "depth", "felt", "cdi", "mmi", "tsunami"]
    k = []
    for seis in a:
        l = {}
        for header in head:
            l[header] = seis[header]
        k.append(l)
    
    t = tabulate(k, headers="keys", tablefmt="grid")
    datos = lt.size(x)
    return (t, datos)

def req_1(data_structs, initialDate, finalDate):
    """
    Función que soluciona el requerimiento 1
    """
    lst = om.values(data_structs["times"], initialDate, finalDate)
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
        if lt.size(x) > 6:
            z = lt.newList("ARRAY_LIST")
            o = quk.sort(x, compare_dates)
            lt.addLast(z,lt.getElement(o,lt.size(o)))
            lt.addLast(z,lt.getElement(o,lt.size(o)-1))
            lt.addLast(z,lt.getElement(o,lt.size(o)-2))
            lt.addLast(z,lt.getElement(o,3))
            lt.addLast(z,lt.getElement(o,2))
            lt.addLast(z,lt.getElement(o,1))
            x = z
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


def req_3(data_structs,magnitud,profundidad):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    listabrutos = om.values(data_structs["magnitudes"],magnitud, om.maxKey(data_structs["magnitudes"]))
    listadatos = lt.newList("ARRAY_LIST")
    for i in lt.iterator(listabrutos):
        for j in lt.iterator(i["sismos"]):
            lt.addLast(listadatos,j)
    prof = om.newMap(omaptype="RBT")
    for k in lt.iterator(listadatos):
        if k["depth"] != "":
            updateProfundidadIndex(prof, k)
    listabrutos = om.values(prof, om.minKey(prof), profundidad)
    listadatos = lt.newList("ARRAY_LIST")
    for l in lt.iterator(listabrutos):
        for m in lt.iterator(l["sismos"]):
            lt.addLast(listadatos, m)
    lenght1 = lt.size(listadatos)
    listaorganizar= quk.sort(listadatos, compare_dates)
    #Creacion Sublista primeros 10 Eventos
    listaprint = [lt.getElement(listaorganizar,lt.size(listaorganizar)),
         lt.getElement(listaorganizar,lt.size(listaorganizar)-1),
         lt.getElement(listaorganizar,lt.size(listaorganizar)-2),
         lt.getElement(listaorganizar,lt.size(listaorganizar)-7),
         lt.getElement(listaorganizar,lt.size(listaorganizar)-8),
         lt.getElement(listaorganizar,lt.size(listaorganizar)-9)]
    #Generacion tabulate
    head = ["mag", "lat", "long", "depth", "sig", "gap", "nst", "title", "cdi", "mmi", "magType", "type", "code"]
    n = []
    for f in listaprint:
        l = {}
        for header in head:
            l[header] = f[header]
        
        m = tabulate([l], headers="keys", tablefmt="grid")
        date = f["time"]
        events = 1
        lista = [date, events, m]
        n.append(lista)
    
    t = tabulate(n, headers=["time","events","details"], tablefmt="grid")
    return t,lenght1
            


def req_4(data_structs, sig, distancia):
    """
    Función que soluciona el requerimiento 4
    """
    lst = om.values(data_structs["significance"], sig, om.maxKey(data_structs["significance"]))
    x = lt.newList("ARRAY_LIST")
    for cada in lt.iterator(lst):
        for elements in lt.iterator(cada["sismos"]):
            lt.addLast(x, elements)
    az = om.newMap(omaptype="RBT")
    for cu in lt.iterator(x):
        if cu["gap"] != "":
            updateDistanceIndex(az, cu)
    lst = om.values(az, om.minKey(az), distancia)
    x = lt.newList("ARRAY_LIST")
    for cada in lt.iterator(lst):
        for elements in lt.iterator(cada["sismos"]):
            lt.addLast(x, elements)
    o = lt.subList(quk.sort(x, compare_dates_inv),1,15)
    a = [lt.getElement(o,1),
         lt.getElement(o,2),
         lt.getElement(o,3),
         lt.getElement(o,lt.size(o)),
         lt.getElement(o,lt.size(o)-1),
         lt.getElement(o,lt.size(o)-2)]
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

def req_5(data_structs, profundidad, estacion):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    lst = om.values(data_structs["estacion"], estacion, om.minKey(data_structs["estacion"]))
    lst2 = lt.newList("ARRAY_LIST")
    for i in lt.iterator(lst):
        for j in lt.iterator(i["sismos"]):
            lt.addLast(lst2, j)
    prof = om.newMap(omaptype="RBT")
    for k in lt.iterator(lst2):
        if k["depth"] != "":
            updateProfundidadIndex(prof, k)
    lst = om.values(prof, om.maxKey(prof), profundidad)
    lst2 = lt.newList("ARRAY_LIST")
    for l in lt.iterator(lst2):
        for m in lt.iterator(l["sismos"]):
            lt.addLast(lst2, m)
    tamanio = lt.size(lst2)
    sorteo = quk.sort(lst2, compare_dates)
    lprint = [lt.getElement(sorteo, lt.size(sorteo)),
              lt.getElement(sorteo, lt.size(sorteo)-1),
              lt.getElement(sorteo, lt.size(sorteo)-2),
              lt.getElement(sorteo, lt.size(sorteo)-17),
              lt.getElement(sorteo, lt.size(sorteo)-18),
              lt.getElement(sorteo, lt.size(sorteo)-19)]
    
    head = ["mag", "lat", "long", "depth", "sig", "gap", "nst", "title", "cdi", "mmi", "magType", "type", "code"]
    w = []
    for x in lprint:
        y = {}
        for header in head:
            y[header] = x[header]
        z = tabulate([1], headers="keys", tablefmt="grid")
        date = x["time"]
        events = 1
        lista = [date, events, z]
        w.append(lista)
        
    tab = tabulate(w, headers=["time", "events", "details"], tablefmt="grid")
    return tab,tamanio


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs, año, titulo, propiedad, bins):
    """
    Función que soluciona el requerimiento 7
    """
    x = lt.newList("ARRAY_LIST")
    a = me.getValue(mp.get(data_structs["fechas"],año))
    for cu in lt.iterator(a["sismos"]):
        if titulo in cu["title"]:
            lt.addLast(x,cu)
    datos = []
    for todos in lt.iterator(x):
        datos.append(todos[propiedad])
    datos.sort()
    x = quk.sort(x,compare_dates)
    o = [lt.getElement(x,lt.size(x)),
         lt.getElement(x,lt.size(x)-1),
         lt.getElement(x,lt.size(x)-2),
         lt.getElement(x,3),
         lt.getElement(x,2),
         lt.getElement(x,1)]
    k = []
    head = ["time", "lat", "long", "title", "code", "mag"]
    for seis in o:
        l = {}
        for header in head:
            l[header] = seis[header]
        k.append(l)
    
    t = tabulate(k, headers="keys", tablefmt="grid")
    return (datos, t)
    


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
    date1 = datetime.datetime.strptime(date1["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date2 = datetime.datetime.strptime(date2["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    d1 = str(date1.date())
    d2 = str(date2.date())
    if (d1 < d2):
        return d1<d2
    else:
        return date1<date2

def compare_dates_inv(date1, date2):
    """
    Compara dos fechas
    """
    date1 = datetime.datetime.strptime(date1["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date2 = datetime.datetime.strptime(date2["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    d1 = str(date1.date())
    d2 = str(date2.date())
    if (d1 > d2):
        return d1>d2
    else:
        return date1>date2
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
