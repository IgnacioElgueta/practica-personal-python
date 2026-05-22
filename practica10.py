print("Bienvenido a la academia de musica")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        
        if edad < 12 or edad > 18:
            print("La academia solo acepta a personas con una edad de entre 12 y 18")

        else:
            break
     
    except ValueError:
       print ("Ingresa numeros porfavor")

print("Que instrumento desea aprender a tocar?\nintrumentos disponibles (guitarra) (piano) (bateria))")

instrumento = input("ingrese su instrumento: ").lower()
while instrumento != "guitarra" and instrumento != "piano" and instrumento != "bateria":
    print("Error, elija uno de los 3 instrumentos mencionados")
    instrumento = input("ingrese su instrumento: ").lower()

print(f"¡Inscripción exitosa!\nedad del alumno: {edad}\ninstrumento elegido: {instrumento}")