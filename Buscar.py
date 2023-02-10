lista = [1,2,3,4,5,6,7,8]

'''ALGORITMO 1
def busqueda1(lista_a_buscar,numero_a_buscar):
    for i in range(len(lista_a_buscar)):
        if lista_a_buscar[i] == numero_a_buscar:
            encontrado = True
            break
        else:
            encontrado = False
    
    if encontrado == True:
        print("El numero esta en la lista en la posicion " + str(lista_a_buscar.index(numero_a_buscar)))
    else:
        print("El numero no esta en la lista")

busqueda1(lista,6)
'''


'''ALGORITMO 2
def busqueda2(lista_a_buscar,numero_a_buscar):
    encontrado = False
    posicion = round(len(lista_a_buscar)/2)
    if (lista_a_buscar[0]) == numero_a_buscar:
        print("El numero esta en la lista")
        encontrado = True
        
    if lista_a_buscar[posicion] > numero_a_buscar:
            for i in range(posicion):
                lista_a_buscar.pop(-1)
                    
    elif lista_a_buscar[posicion - 1] < numero_a_buscar:
            for i in range(posicion):
                lista_a_buscar.pop(0)
                
    if len(lista_a_buscar) == 1 and lista_a_buscar[0] != numero_a_buscar:
        print("El numero NO esta en la lista")
        encontrado == True
    else:
        if encontrado != True:
            busqueda2(lista_a_buscar,numero_a_buscar)
        
                    
busqueda2(lista,8)
'''
