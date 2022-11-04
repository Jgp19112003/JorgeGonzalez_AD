

f = open ('ejercicio1-100.txt','w')
print("Introduzca numero entre el 1 y el 100: ")
num = input()
f.write(num)
with open("ejercicio1-100.txt", "r") as f:
    print(f.read())
f.close()
