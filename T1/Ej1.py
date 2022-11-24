

num = int(input("Introduzca numero entre el 1 y el 100: "))
with open("ejercicio2-tabla.txt", "w") as f:
    for i in range(1,11):
        f.write(str(num) + "x" + str(i) + "=" + str(num*i) + "\n")
f.close()

