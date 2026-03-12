import os
os.system("cls")

# esta funcion es para ingresar un numero positivo
n = int(input("Ingrese un numero entero positivo: "))

tabla = 1

#  este ciclo recorre desde 1 hasta el numero que se ingresa
for i in range(1, n + 1):
    print("Tabla del", i)
 # esto sirve para indicar que la multiplicacion toma los numero 1 y 10
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

print("La tabla mas larga generada fue la del", tabla)
