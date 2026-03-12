import os
os.system("cls")  

try:
 # PEDIR EL MOMTO EN NUMERO ENTERO
 saldo = int(input("Ingrese el saldo inicial: "))
 # ingresar el monto a retirar
 retiro = input("Ingrese el monto a retirar: ")
 
 retiro = int(retiro)

 if retiro < 0:
  # aparece un mensaje de error si el valor es negativo
  print("Error: No se permiten valores negativos")

 elif retiro > saldo:
  # mensajes del que  el monto es mayor que el saldo
  print("Error: Fondos insuficientes")
 #el saldo restante que te queda despues del retiro
 else:
  saldo = saldo - retiro
 print("Saldo restante:", saldo)
except:
 # si ingresas un moto negativo
 print("Error: Debe ingresar un numero valido")