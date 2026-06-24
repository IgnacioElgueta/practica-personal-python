def nombre_producto(nombre):
    return nombre.strip() != ""

def stock_bodega(stock):
   return stock >= 0 
    
def precio_producto(precio):
   return precio >= 0

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("=====================================")

def leer_menu():
    while True:
        try:
            opcion = int(input("Selecciona una opcion\n- "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opcion no valida")
        except ValueError:
            print("Error")

def agregar_producto(lista):
    print("\n---Registrar nuevo producto---")
    nombre = input("Ingrese el nombre del producto\n- ")
    if not nombre_producto(nombre):
        print("Error, no puede estar vacio el nombre")
        return
    try:
        stock = int(input("Ingrese la cantidad de stock que desea agregar\n- "))
        if not stock_bodega(stock):
            print("Error , debe ser un numero entero mayor o igual a 0")
            return
        
        precio = float(input("Ingrese el precio del producto\n- "))
        if not precio_producto(precio):
            print("error, el precio debe ser un numero decimal mayor a 0")
            return
    
    except ValueError:
        print("Error")
        return
    
    producto = {
        "nombre": nombre,
        "stock": stock,
        "precio": precio,
        "disponible": False
    }
    lista.append(producto)
    print("Producto agregado")

def Buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre.lower():
            return i
    return -1

def eliminar_producto(lista):
    eliminar = input("¿Que producto desea eliminar?\n- ")
    posicion = Buscar_producto(lista, eliminar)

    if posicion == -1:
        print(f"Error, el producto '{eliminar}' no se encuentra registrado")
    else:
        del lista[posicion]
        print(f"El producto '{eliminar}' ha sido eliminado con exito")

def actualizar_disponibilidad(lista):
    if len(lista) == 0:
        print("no hay productos por actualizar")
        return
    
    for producto in lista:
        if producto["stock"] > 0:
            producto["disponible"] = True
        elif producto["stock"] == 0:
            producto["disponible"] = False
    
    print("Disponibilidad actualizada")

lista_productos = []

while True:
    mostrar_menu()
    opcion = leer_menu()

    if opcion == 1:
        agregar_producto(lista_productos)
    
    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto\n- ")
        posicion = Buscar_producto(lista_productos, nombre)

        if posicion == -1:
            print("Error: Producto no encontrado en el sistema.")
        
        else:
            print("Producto encontrado")
            print(f"nombre: {lista_productos[posicion]['nombre']}")
            print(f"stock: {lista_productos[posicion]['stock']}")
            print(f"precio: {lista_productos[posicion]['precio']}")
    
    elif opcion == 3:
        eliminar_producto(lista_productos)
    
    elif opcion == 4:
        actualizar_disponibilidad(lista_productos)
    
    elif opcion == 5:
        if len(lista_productos) == 0:
            print("No hay productos registrados")
        else:
            for p in lista_productos:
                disponibilidad = "disponible" if p["disponible"] else "no disponible"
                print(f"nombre: {p['nombre']} | stock: {p['stock']} | precio: {p['precio']} | disponiblididad: {disponibilidad}")
                print("-" * 40)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto") 
        break
    
