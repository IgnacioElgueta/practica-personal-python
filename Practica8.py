from random import randint

print("El primer numero debe ser menor al segundo")
while True:
    try:
        num1 = int(input("Ingrese su primer numero del 1 al 10: "))
        num2 = int(input("Ingrese su segundo numero del 1 al 10: "))
        
        if num1 < 1 or num1 > 10 or num2 < 1 or num2 > 10:
            print("Error. Ambos números deben estar entre el 1 y el 10.")
        
        elif num2 < num1:
            print("Error, el primer numero debe ser menor al segundo")
        
        else:
            break

    except ValueError:
        print ("Ingrese un numero entero")

numero = randint(num1, num2)

# Ajustado
if numero in [1,3,5,7,9]:
    if numero + 1 <= num2:
        numero = numero + 1
        
    else:
        numero = numero - 1

# Juego
intento = 1 
juego_anterior = 0  

while intento <= 3:
    juego = int(input(f"Intento {intento} - Adivina el número: "))

    if juego == numero:
        print("Felicitaciones, pudiste adivinar.")
        break  

    else:
        if numero > juego:
            print("El número es mayor.")
        elif numero < juego:
            print("El número es menor.")
            
        if intento == 2:
            distancia_actual = abs(numero - juego)
            distancia_anterior = abs(numero - juego_anterior)
            
            print("Te daré una pista:")
            if distancia_actual < distancia_anterior:
                print(f"El número que buscas está más cerca de {juego} que de {juego_anterior}")
            else:
                print(f"El número que buscas está más cerca de {juego_anterior} que de {juego}")

        juego_anterior = juego 
        
        intento = intento + 1

if intento > 3:
    print(f"Perdiste. El número era {numero}.")