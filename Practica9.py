from random import randint

numero_secreto = randint(1,50)
if numero_secreto == 13:
    numero_secreto = numero_secreto + 1 

intento = 1

print("intenta adivinar el numero que esta entre el 1 al 50")

numero_elegido = int(input(f"Intento numero ({intento}) Pon tu primer numero: "))
while True:

    if intento >= 2:
          numero_elegido = int(input(f"Intento numero ({intento}) Pon tu siguiente numero: "))
   
    if numero_elegido == numero_secreto:
        print(f"Felicidades haz ganado. intentos totales: {intento}")
        break
    
    if numero_elegido < numero_secreto:
        print("El numero es mayor")
    
    elif numero_elegido > numero_secreto:
            print("El numero es menor")
    intento = intento + 1