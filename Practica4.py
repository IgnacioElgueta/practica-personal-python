from random import randint
import sys

intento = 3 
print("Bienvenido al juego de la muerte , si caes en el numero 3, 4, 8 pierdes")
while intento > 0:
    numero = randint(1, 10)
    print("Numero: ", numero)

    if numero == 3:
        print("Mueress")
        sys.exit()

    elif numero == 4:
        print("Mueress")
        sys.exit()
    
    elif numero == 8:
        print("Mueress")
        sys.exit()

    else:
        intento = intento-1
        print(f"Haz sobrevivido te quedan, {intento} intentos para ganar")
        while True:
            tecla = input("Escribe S para el siguiente intento: ").upper()
            if tecla == "S":
                break
        
        if intento == 0:
            print("Haz ganado el juego")
            sys.exit()
