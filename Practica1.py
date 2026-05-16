while True:
    numero = input ("Pon un numero del 1 al 10: ")
    if numero.isdigit():
        numero = int(numero)

        if 1 <= numero <= 10:
            print ("Numero valido")

            break
        else:
            print("Fuera de rango (1-10)")

    else:
        print("Debes ingresar solo números")