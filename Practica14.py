print("==========Bienvenido al registro de habitaciones del hotel corporativo nacional==========")

total_suites = 0
total_estandar = 0

while True:
    try:
        habitacion = int(input("¿Cuantas habitaciones desea ingresar?\n"))
        if habitacion > 0:
            for i in range(habitacion):
                print("Habitacion", i + 1)

                while True:
                    numero = (input("Ingrese número de habitación, puede contener Numeros y Letras:\n"))
                    if (len(numero)) >= 6 and numero.isalnum() and not numero.isalpha() and not numero.isdigit():
                        break
                    else:
                        print("Debe tener 6 caracteres y no debe tener espacios, tampoco numeros negativos.")
                
                while True:
                    try: 
                        tarifa = int(input("Ingrese tarifa nocturna: "))
                        if tarifa <= 0:
                            print("Error. La tarifa debe ser un número positivo.")
                        else:
                            if tarifa > 90000:
                                tipo_habitacion = "Suite Ejecutiva"
                                total_suites = total_suites + 1
                            elif tarifa <= 90000:
                                tipo_habitacion = "Estándar" 
                                total_estandar = total_estandar + 1
                            
                            print(f"Habitacion registrada con exito como {tipo_habitacion}")
                            break

                    except ValueError:
                        print("Error. Debe ser un numero entero positivo")    
            break   
        else:
            print("Cantidad inválida! Ingresa un entero positivo para continuar")
    
    except ValueError: 
        print("Debe ser un numero entero positivo")

print("*************************************************************")
print(f"El hotel cuenta con {total_suites} Suites Ejecutivas y {total_estandar} Habitaciones Estándar  ¡Check-in disponible!")