import os
os.system("cls")  

def analizar_numeros(*args, **kwargs):
    # Vamos a ver si queremos mostrar los pares o no. Si no se pone nada, asumimos que sí.
    mostrar_pares = kwargs.get('mostrar_pares', True)  
    # Igual para los impares, por defecto también los mostramos
    mostrar_impares = kwargs.get('mostrar_impares', True)  

    # Aquí vamos a guardar los números que sean pares
    pares = []
    # Y aquí los números que sean impares
    impares = []

    # Ahora miramos cada número que nos pasaron
    for num in args:
        if num % 2 == 0:  # Si el número se puede dividir por 2, es par
            pares.append(num)  # Lo ponemos en la lista de pares
        else:  # Si no, es impar
            impares.append(num)  # Lo ponemos en la lista de impares

    # Si queremos mostrar los pares, los imprimimos y también decimos cuántos hay
    if mostrar_pares:
        print(f"Números pares: {pares}")  
        print(f"Cantidad de pares: {len(pares)}")  

    # Si queremos mostrar los impares, los imprimimos y decimos cuántos hay
    if mostrar_impares:
        print(f"Números impares: {impares}")
        print(f"Cantidad de impares: {len(impares)}")
 #prueba       
analizar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)