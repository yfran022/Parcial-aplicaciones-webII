import os
os.system("cls")  # Limpia la pantalla de la consola

# Función que calcula el precio final de un producto con impuesto del 19%
def calcular_impuesto(valor, impuesto=19):
    # Se calcula el impuesto multiplicando el valor por el porcentaje
    total = valor + (valor * impuesto / 100)
    
    # Se retorna el valor final con el impuesto incluido
    return total


total = 0  # Variable acumuladora para guardar el total a pagar

# el ciclo que se repite 3 veces para pedir los tres productos
for i in range(3):
    
    # Se solicita al usuario ingresar el precio del producto
    valor = float(input("Ingrese el valor del producto: "))
    
    # Se llama a la función para calcular el precio con impuesto
    precio_final = calcular_impuesto(valor)
    
    # Se muestra el precio del producto después de aplicar el impuesto
    print("Precio con impuesto:", precio_final)
    
    # Se suma el precio con impuesto al total general
    total += precio_final


# Al terminar el ciclo se muestra el total a pagar por todos los productos
print("Total a pagar:", total)