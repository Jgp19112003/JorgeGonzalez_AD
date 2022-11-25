''' Ejercicio 5 

while True:
    try:
            opcion=int(input("Introduce una opción del 1 al 3:"))
            if opcion==1:
                    print("opción 1")
            elif opcion==2:
                    print("opción 2")
            elif opcion==3:
                    print("opcion 3")
            else:
           
                break
           
    except ValueError:
        print("Ha pulsado una tecla, por favor introduzca un número")
        
 '''   

''' Ejercicio 6
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
telefono = int(input("Introduce tu teléfono: "))

print(nombre, apellido, "tiene", edad, "años y su teléfono es", telefono)

'''

''' Ejercicio 7.a
num = int(input("Introduce un numero: "))
with open ('C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/ficheroexam1.txt','w') as f:
        i = 1
        for i in range(i,num + 1):
                f.write("El numero es: " + str(i) + "\n")
        f.close()

'''

''' Ejercicio 7.b
num = int(input("Introduce un numero: "))
with open ('C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/ficheroexam1.txt','r+') as f:
        i = 1
        contenido = f.read()
        for i in range(i,num + 1):
                f.write("El numero es: " + str(i) + "\n")
        f.close()

'''

''' Ejercicio 8.a
a = int(input("Introduce primer numero: "))
b = int(input("Introduce segundo numero: "))
c = int(input("Introduce tercer numero: "))
resultado = (a+b)*c
with open ('C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/ficheroexam2.txt','w') as f:
        i = 1
        for i in range(i,resultado + 1):
                f.write("El calculo es "+ str(resultado) +" y esta es la linea : " + str(i) + "\n")
        f.close()
'''

''' Ejercicio 8.b
a = int(input("Introduce primer numero: "))
b = int(input("Introduce segundo numero: "))
c = int(input("Introduce tercer numero: "))
resultado = (a+b)
with open ('C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/ficheroexam2.txt','r') as f:
        i = 1
        print("Ahora se mostrara el contenido de calcular a+b =", resultado)
        for i in range(i,resultado + 1):
                print(f.readlines(i))
        f.close()
'''

''' Ejercicio 8.c
a = int(input("Introduce primer numero: "))
b = int(input("Introduce segundo numero: "))
c = int(input("Introduce tercer numero: "))
resultado = (a+b)
fichero = "ficheroexam2.txt"
try:
        with open ('C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/ficheroexam2.txt','r') as f:
                i = 1
                print("Ahora se mostrara el contenido de calcular a+b =", resultado)
                for i in range(i,resultado + 1):
                        print(f.readlines(i))
                f.close()
except FileNotFoundError:
        print("El fichero",fichero,"no existe!")
        
'''
''' Ejercicio 9
def Consulta_Errores(fichero):
        ruta = 'C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/'+fichero
        try:            
                with open (ruta,'r') as f:
                        print(f.read())
                        f.close()

        except FileNotFoundError:
                print("El fichero",fichero,"no existe!")
        
        
Consulta_Errores("ficheroexam4.txt")


def Existe_Error(fichero1,fichero2):
        ruta1 = 'C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/'+fichero1
        ruta2 = 'C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/'+fichero2        
        with open (ruta1,'r') as f:
                directorio = f.read()
                directorio = dict([tuple(line.split(",")) for line in directorio])
                directorio.update
                f.close()
                
        with open (ruta2,'r') as f:
                directorio2 = f.read()
                directorio2 = dict([tuple(line.split(",")) for line in directorio])
                directorio2.update
                f.close()
        
        
Existe_Error("ficheroexam3.txt", "ficheroexam4.txt")


def Borrar_Errores(fichero1, fichero2):
        ruta1  = 'C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/'+fichero1
        ruta2  = 'C:/Users/Usuario DAM2/Documents/GitHub/JorgeGonzalez_AD/T1/ExamenT1/'+fichero2
        with open (ruta1,'r') as f:
                for i in f:
                    linea1 = f.readline()
                f.close()
                
        with open (ruta2,'r') as f:
                for i in f:
                    linea2 = f.readline()
                f.close()
                
        if linea1 == linea2:
                                      
        
Borrar_Errores("ficheroexam4.txt","ficheroexam4.txt")

'''
JP