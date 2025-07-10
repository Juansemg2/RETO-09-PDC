#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

#pedimos al usuario el tamaño de la lista
tamano_lista=int(input("Ingrese el tamaño de su lista: "))
#creamos dos listas donde una almacene la lista inicial y otra almacene los ceros
lista = []
contador_ceros = []
#creamos lista que se muestre como el arreglo que ingreso el usuario
Lista_original = []
#para cada numero en el rango del tamaño de la lista ingresar un valor y colocarlo al final de ella
for n in range(tamano_lista):
    numero = float(input("Ingrese el valor " + str(n + 1) + ": "))
    #los ceros se van al arreglo del contador  y los demas numeros a lista
    if numero != 0:
        lista.append(numero)
        Lista_original.append(numero)
    else:
        contador_ceros.append(numero)
        Lista_original.append(numero)
#imprimimos la lista del usuario
print(Lista_original)
#concatenamos las listas separadas
lista_final = lista+contador_ceros
print(lista_final)