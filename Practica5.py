from random import randint 
import sys

print("Bienvenido a un juego simple\nTienes 100 de vida y tendras 5 intentos en los que iras perdiendo vida, si sovrevives ganas.")

vida = 100

intento = 5
while intento > 0:


    numero = randint(1,10)

    respuesta = input("Presiona (S) para hacer un intento: ").upper()
    if respuesta == "S":
        if numero >= 1 and numero <=5:
            vida = vida - (40)

            if vida <= 0:
                vida = 0

            print("Haz perdido (40) de vida")
    
            print("vida restante: ", vida)
    
        elif numero >=6 and numero <=10:
            print("Te haz salvado")
    
        if vida <= 0:
            print("Haz muerto")
            sys.exit()


        intento = intento-1
        print(f"Aun vives, te quedan: {intento} intentos")

        if intento == 0:
            print("Haz sovrevivido")