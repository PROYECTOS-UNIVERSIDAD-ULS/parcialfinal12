import random

# Funcion para crear la lista aleatoria
def crear_lista():
    lista = []
    for i in range(10):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista


# Ordenamiento burbuja
def burbuja(lista):
    iteraciones = 0
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            iteraciones += 1
            if lista[j] > lista[j + 1]:
                # intercambiar
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista, iteraciones


# Ordenamiento por seleccion
def seleccion(lista):
    iteraciones = 0
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            iteraciones += 1
            if lista[j] < lista[minimo]:
                minimo = j
        # intercambiar
        temp = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = temp
    return lista, iteraciones


# Programa principal
lista_original = crear_lista()
iter_burbuja = 0
iter_seleccion = 0
burbuja_usado = False
seleccion_usado = False

print("Lista generada:", lista_original)

opcion = 0
while opcion != 4:
    print("\n----- MENU -----")
    print("1. Ordenar con Burbuja")
    print("2. Ordenar con Seleccion")
    print("3. Comparar algoritmos")
    print("4. Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        copia = lista_original.copy()
        ordenada, iter_burbuja = burbuja(copia)
        burbuja_usado = True
        print("Lista ordenada:", ordenada)
        print("Iteraciones burbuja:", iter_burbuja)

    elif opcion == 2:
        copia = lista_original.copy()
        ordenada, iter_seleccion = seleccion(copia)
        seleccion_usado = True
        print("Lista ordenada:", ordenada)
        print("Iteraciones seleccion:", iter_seleccion)

    elif opcion == 3:
        if burbuja_usado == True and seleccion_usado == True:
            print("Burbuja:", iter_burbuja, "iteraciones")
            print("Seleccion:", iter_seleccion, "iteraciones")
            if iter_burbuja < iter_seleccion:
                print("Burbuja uso menos iteraciones")
            elif iter_seleccion < iter_burbuja:
                print("Seleccion uso menos iteraciones")
            else:
                print("Ambos usaron las mismas iteraciones")
        else:
            print("Primero debes ejecutar los dos algoritmos (opciones 1 y 2)")

    elif opcion == 4:
        print("Adios!")

    else:
        print("Opcion no valida")



# Ordenamiento por seleccion
def seleccion(lista):
    iteraciones = 0
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            iteraciones += 1
            if lista[j] < lista[minimo]:
                minimo = j
        # intercambiar
        temp = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = temp
    return lista, iteraciones


# Programa principal
lista_original = crear_lista()
iter_burbuja = 0
iter_seleccion = 0
burbuja_usado = False
seleccion_usado = False

print("Lista generada:", lista_original)

opcion = 0
while opcion != 4:
    print("\n----- MENU -----")
    print("1. Ordenar con Burbuja")
    print("2. Ordenar con Seleccion")
    print("3. Comparar algoritmos")
    print("4. Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        copia = lista_original.copy()
        ordenada, iter_burbuja = burbuja(copia)
        burbuja_usado = True
        print("Lista ordenada:", ordenada)
        print("Iteraciones burbuja:", iter_burbuja)

    elif opcion == 2:
        copia = lista_original.copy()
        ordenada, iter_seleccion = seleccion(copia)
        seleccion_usado = True
        print("Lista ordenada:", ordenada)
        print("Iteraciones seleccion:", iter_seleccion)

    elif opcion == 3:
        if burbuja_usado == True and seleccion_usado == True:
            print("Burbuja:", iter_burbuja, "iteraciones")
            print("Seleccion:", iter_seleccion, "iteraciones")
            if iter_burbuja < iter_seleccion:
                print("Burbuja uso menos iteraciones")
            elif iter_seleccion < iter_burbuja:
                print("Seleccion uso menos iteraciones")
            else:
                print("Ambos usaron las mismas iteraciones")
        else:
            print("Primero debes ejecutar los dos algoritmos (opciones 1 y 2)")

    elif opcion == 4:
        print("Adios!")

    else:
        print("Opcion no valida")