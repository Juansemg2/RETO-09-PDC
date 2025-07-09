# pedimos al usuario tamaño de la lista
tamano_listas = int(input("Ingrese la cantidad de elementos de los arreglos "))
# creamos las listas
lista1 = []
lista2 = []
# pedimos los elementos de la lista1
for n in range(tamano_listas):
    numero1 = float(input("Ingrese el valor " + str(n + 1) + " del primer arreglo: "))
    lista1.append(numero1)
# pedimos los elementos de la lista2
for n in range(tamano_listas):
    numero2 = float(input("Ingrese el valor " + str(n + 1) + " del segundo arreglo: "))
    lista2.append(numero2)
# calculamos producto punto
producto_punto = 0
for n in range(tamano_listas):
    producto_punto = producto_punto + (lista1[n] * lista2[n])
# Imprimir el resultado
print("El producto punto es: " + str(producto_punto))