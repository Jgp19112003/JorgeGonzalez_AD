lista = []

while (True):
    def crearNodo():
        sublista = []
        if (len(lista) == 0):
    
            valor = int(input("Introduzca valor: "))
            sublista.append(0)
            sublista.append(valor)
            insertarNodo(sublista)
            
        else:
            valor = int(input("Introduzca valor: "))
            sublista.append(99)
            sublista.append(valor)
            insertarNodo(sublista)
            

    def insertarNodo(sublista):
        lista.append(sublista)
    

            
        if(lista[0][0] == 0 and len(lista) > 1):
            lista[0][0] = sublista[1]
            
        for i in range(len(lista) - 1):
            if(lista[i][1] == 99):
                lista[i][1] = lista[i+1][0]
                lista[len(lista) - 1][1] = 99
                
        ordenarLista(lista)
        
            
    
    def ordenarLista(lista):
        print(lista)
        
        for i in range(len(lista)):
            if len(lista) > 1:
                if (lista[i][1] < lista[i-1][1]):
                    lista[i-1][1] = lista[i+1][1]
                    lista[i][1] = lista[i-1][1]
        
    
    crearNodo()
    
    
    
