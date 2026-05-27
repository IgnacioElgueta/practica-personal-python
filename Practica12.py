goblins = 1500
caravana = 3500
dragon = 12000
espia = 5000
golem = 8000

print("!Bienvenido al registro de misiones del gremio de aventureros¡")

while True:

    nombre = input("Escriba su nombre: ")
    if nombre.isdigit():
        print("Solo escribalo con palabras")

    else:
        break

while True:
    try:  
        id = int(input("Ingrese su id de licencia de aventurero. Asegurese que sea de 6 digitos: "))

        if len(str(id)) != 6:
            print("Recuerde que es de 6 digitos")

        else:
            break
    except ValueError:
        print("Ingrese solo numeros")

acu_misiones = []
valor_total = 0

while True:
    opcion = input("Escriba (aceptar mision) para aceptar una o mas misiones\nEscriba (terminar registro) para terminar de aceptar misiones o salir\n").lower()
    while opcion != "aceptar mision" and opcion != "terminar registro":
        print("Escriba correctamente una de las dos opciones a elegir")
        opcion = input("Escriba (aceptar mision) para aceptar una o mas misiones\nEscriba (terminar registro) para terminar de aceptar misiones o salir\n").lower()
        
    if opcion == "aceptar mision":
        print("Misiones disponibles\nCazeria de goblins 1500: monedas de plata\ncaravana: 3500 monedas de plata\nDerrotar al dragon: 12000 monedas de plata\nmision de espia: 5000 monedas de plata\nSubyugar un golem: 8000 monedas de plata")

        misiones = input("¿Que mision desea aceptar?: ").lower()
        while misiones != "cazeria de goblins" and misiones != "caravana" and misiones != "derrotar al dragon" and misiones != "mision de espia" and misiones != "subyugar un golem":
            print("Escriba correctamente la mision que desea hacer")
            misiones = input("¿Que mision desea aceptar?: ").lower()

        acu_misiones.append(misiones)
        print("Mision agregada")

        if misiones == "cazeria de goblins":
            valor_total = valor_total + goblins
        elif misiones == "caravana":
            valor_total = valor_total + caravana
        elif misiones == "derrotar al dragon":
            valor_total = valor_total + dragon
        elif misiones == "mision de espia":
            valor_total = valor_total + espia
        elif misiones == "subyugar un golem":
            valor_total = valor_total + golem
        
    if opcion == "terminar registro":
        break


print(f"nombre del aventurero: {nombre} (id de aventurero): {id}")
print("misiones aceptadas")
for misiones in acu_misiones:
    print(f"- {misiones}")
print(f"Plata total por las misiones: {valor_total}")