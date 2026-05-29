
espacio = 60
ocupado_espacio = 0

print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")
while True:

    eleccion = (input("=== MENÚ PRINCIPAL ===\n1. Espacios disponibles\n2. Ocupar espacio\n3. Liberar espacio\n4. Espacios actualmente ocupados\n5. Salir\n"))
    while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5":
        print("Error. selecciona del 1 al 5")
        eleccion = (input("=== MENÚ PRINCIPAL ===\n1. Espacios disponibles\n2. Ocupar espacio\n3. Liberar espacio\n4. Espacios actualmente ocupados\n5. Salir\n"))
        
    if eleccion == "1":
        print(f"Espacios disponibles actualmente: {espacio}")
        
    if eleccion == "2":
        while True:
            try:
                ocu_espacio = int(input("¿Cuantos espacios desea ocupar?\n"))
                
                if ocu_espacio <= 0:
                    print("Cantidad inválida. Ingresa un número entero mayor a 0.")
                elif ocu_espacio > espacio:
                    print("No hay suficientes espacios disponibles para realizar la ocupación.")
                
                else:
                    espacio = espacio - ocu_espacio
                    ocupado_espacio = ocupado_espacio + ocu_espacio
                    
                    print("Ocupacion exitosa")
                    break
            except ValueError:
                print("Error, Escriba solo numeros")
    
  
    if eleccion == "3":
        while True:
            try:
                liberar = int(input("¿Cuantos espacios desea liberar?\n"))
                if liberar <= 0:
                    print("Cantidad inválida. Ingresa un número entero mayor a 0.")
                
                elif liberar > ocupado_espacio:
                    print(f"Error. No puedes liberar {liberar} espacios porque actualmente solo hay {ocupado_espacio} espacios ocupados.")
  
                else:
                    espacio = espacio + liberar             
                    ocupado_espacio = ocupado_espacio - liberar  
                    
                    print("Liberación exitosa. Los espacios han sido devueltos al almacén.")
                    break 
                    
            except ValueError:
                print("Error. Escriba solo números enteros.")
    if eleccion == "4":
        print(f"Espacios actualmente ocupados: {ocupado_espacio}")
    
    if eleccion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break