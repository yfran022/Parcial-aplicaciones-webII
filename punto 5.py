import os
os.system("cls")  

while true:
    nombre = input("ingrese nombre del producto(fin para terminar): ")
    if nombre.lower()=="fin":
       break
    precio = float(input("ingrese el precio del producto: "))
    producto = {
      "nombre"= nombre,
      "precio" = precio
    }
    productos.append(producto)
 
def total_productos(lista):
   return len(lista)

def precio_promedio
 sum = 0
 for x in lista.
  suma +- = x["precio"]
 return suma / len(lista)

def producto_mas_caro
