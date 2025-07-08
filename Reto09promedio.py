#1.Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
 
#pedimos al usuario el tamaño de la lista
tamano_lista=int(input("Ingrese el tamaño de su lista: "))
#creacion lista
lista = []
#para cada numero en el rango del tamaño de la lista ingresar un valor y colocarlo al final de ella
for n in range(tamano_lista):
    numero = float(input("Ingrese el valor " + str(n + 1) + ": "))
    lista.append(numero)
#variable que suma cada valor en la lista
contador=0
#sumamos valores de la lista en contador
for i in lista:
    contador+= i

#sacamos el promedio dividiendo el valor sumado de la lista entre el tamaño de la lista
promedio = contador/(len(lista))
print(promedio)