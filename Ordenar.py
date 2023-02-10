lista_numeros = [40,21,4,9,10,35]

''' ALGORITMO 1
def ordenarLista(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista) - 1):
            if(lista[j+1] < lista[j]):
                conteo = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = conteo
    print(lista)
      
    
    
ordenarLista(lista_numeros)

ALGORITMO 2
def ordenarLista2(lista):
    for j in range(len(lista) - 1):
        for i in range((len(lista) - 1) - j):
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                
    print(lista)
    print(len(lista))
    
ordenarLista2(lista_numeros)
'''