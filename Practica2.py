while True:
    numero = input ("Pon un numero: ")
    if numero.lstrip("-").isdigit():
        numero = int(numero)
        break

if numero < 0:
    print ("El numero es negativo")

elif numero == 0:
    print("Es cero")

else:
    print ("El numero es positivo")