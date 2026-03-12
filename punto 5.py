def analizar_numeros(*args, **kwargs):

 pares = []
 impares = []

for n in args:

 if n % 2 == 0:
 pares.append(n)
else:
  impares.append(n)

if kwargs.get("mostrar_pares") == True:
 print("Numeros pares:", pares, "Total:", len(pares))

if kwargs.get("mostrar_impares") == True:
 print("Numeros impares:", impares, "Total:", len(impares))


# prueba
analizar_numeros(1,2,3,4,5,6, mostrar_pares=True) 