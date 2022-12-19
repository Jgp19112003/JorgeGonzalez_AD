unidades = ["cero", "uno", "dos" ,"tres" ,"cuatro" ,"cinco" , "seis" ,"siete" ,"ocho" ,"nueve","diez"]
especiales = ["once", "doce","trece","catorce", "quince", "diezciseis", "diecisiete", "dieciocho", "diecinueve"]
decenas = ["veinte", "treinta","cuarenta","cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

num = int(input("Ingrese un numero entre 0-99: "))
digitos = list(str(num))

if (num >=0 and num <11):
    print (unidades[num])

elif (num < 20):
    print (especiales[num-11])

elif (num <100):
    
    unidad = num % 10
    
    decena = int(digitos[0])
    if (unidad == 0):
        print (decenas[decena-2]) 
    else:
        print (decenas[decena-2], "y" , unidades[unidad])
else:
    print ("El numero debe ser menor a 100"  )