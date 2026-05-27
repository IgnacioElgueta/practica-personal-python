pikachu_roll = 4500
otaku_roll = 5000
pulpo_venenoso_roll = 5200
anguila_electrica_roll = 4800
import sys
print("Bienvenvenido al delivery sushi")

lista_sushi = []
sub_total = 0
producto = 0
descuento = 0

opcion1 = input("1.Ir a comprar\n2.Salir de la pagina\n")
while opcion1 != "1" and opcion1 != "2":
    print("Seleccione 1 o 2")
    opcion1 = input("¿Que desea hacer?\n1.Continuar la compra de sushis\n2.Salir de comprar\n")
if opcion1 == "2":
    sys.exit()
if opcion1 == "1":
    while True:
        
        opcion = input("¿Que desea hacer?\n1.Comprar sushis\n2.Terminar de comprar\n")
        while opcion != "1" and opcion != "2":
            print("Seleccione 1 o 2")
            opcion = input("¿Que desea hacer?\n1.Comprar sushis\n2.Terminar de comprar\n")
        
        if opcion == "1":

            print("Sushis dispoibles:\n1.pikachu_roll\n2.otaku_roll\n3.pulpo_venenoso_roll\n4.anguila_electrica_roll")

            sushi = input("Seleccione algún tipo de sushi del 1 al 4: ")
            while sushi != "1" and sushi != "2" and sushi != "3" and sushi != "4":
                print("Solo puedes usar del 1 al 4")
                sushi = input("Seleccione algún tipo de sushi del 1 al 4: ")
            if sushi == "1":
                sushi = "pikachu roll"
                sub_total = sub_total + pikachu_roll
                producto = producto + 1
            if sushi == "2":
                sushi = "otaku roll"
                sub_total = sub_total + otaku_roll
                producto = producto + 1
            if sushi == "3":
                sushi = "pulpo venenoso roll"
                sub_total = sub_total + pulpo_venenoso_roll
                producto = producto + 1
            if sushi == "4":
                sushi = "anguila electrica roll"
                sub_total = sub_total + anguila_electrica_roll
                producto = producto + 1
                
            lista_sushi.append(sushi)
            print("sushi agregado")

        if opcion == "2":
            break

    # Descuento
    desc_opcion = input("¿Posee el codigo de descuento?\n1.Si\n2.No\n").lower()

    while True:
        while desc_opcion != "1" and desc_opcion != "2":
            print("Escriba 1 o 2")
            desc_opcion = input("¿Posee algún tipo de descuento?\n1.Si\n2.No\n").lower()

        if desc_opcion == "2":
            break

        respuesta = input("Ingrese el codigo de descuento: ")
        if respuesta == "soyotaku":
            print("Usted tiene un (10%) de descuento")
            descuento = 0.9
            break
           
        else:
            print("Codigo invalido")
            intento = input("1.Intentar otra vez\n2.Salir\n")
            while intento != "1" and intento != "2":
                print("Selecciona 1 o 2")
                intento = input("1.Intentar otra vez\n2.Salir\n")
            if intento == "2":
                break    
    
desc = sub_total * descuento
Total = sub_total - desc

print(f"******************************\nTotal productos: {producto}\n******************************")

print("Sushis escogidos")
for sushi in lista_sushi:
    print(sushi)
print("******************************")
print(f"Valor subtotal: {sub_total}")
print(f"Descuento por el codigo: {desc}")
print(f"Total: {Total}")