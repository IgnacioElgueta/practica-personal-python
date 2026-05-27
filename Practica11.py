espada = 5000
arco = 7000
baston_magico = 9000
mandoble = 11000
lanza = 6000

print("Bienvenido a la tienda de armas")

# Usuario

while True:

    nombre = input("Ingrese su nombre de usuario: ")
    if nombre.isdigit():
        print("Ingrese solo palabras")
    else:
        break

while True:
    try:
        id = int(input("Ingrese su id de jugador de 8 digitos: "))
        if len(str(id)) != 8:
            print("Solo de 8 digitos Porfavor")
        else:
            
            break
    except ValueError:
        print("Ingrese solo numeros")

    # Sistema de articulos

comprados = []
valor_total = 0
while True:

    opcion = input("¿Que desea hacer?\n1. Comprar un articulo\n2. Salir\n")
    while opcion != "1" and opcion != "2":
        print("Ingrese solo 1 o 2")
        opcion = input("¿Que desea hacer?\n1. Comprar un articulo\n2. Salir\n")
    
    if opcion == "1":
        print("Articulos disponibles\nEspada. Precio: 5k\nArco. Precio: 7k\nBaston magico. Precio: 9k\nMandoble. Precio: 11k\nLanza. Precio: 6k")

        articulos = input("¿Que articulo decea comprar?: ").lower()
        while articulos != "espada" and articulos != "arco" and articulos != "baston magico" and articulos != "mandoble" and articulos != "lanza":
            print("Ingrese uno de los articulos ya mencionados")
            articulos = input("¿Que articulo decea comprar?: ").lower()
        
        comprados.append(articulos)
        print("Articulo agregado")

        if articulos == "espada":
            valor_total = valor_total + espada
        elif articulos == "arco":
            valor_total = valor_total + arco
        elif articulos == "baston magico":
            valor_total = valor_total + baston_magico
        elif articulos == "mandoble":
            valor_total = valor_total + mandoble
        elif articulos == "lanza":
            valor_total = valor_total + lanza
    
    if opcion == "2":
        break

print(f"Nombre del usuario: {nombre} (ID: {id})")
print("Articulos comprados")
for articulos in comprados:
    print(articulos)
print(f"Valor total de la compra: {valor_total}")