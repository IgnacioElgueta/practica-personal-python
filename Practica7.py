matricula = 12000
curbasico = 18000
curavanzado = 28000
descuento = 0

print("Bienvenido a las Inscripciones de la Academia Armonía Urbana")

Nombre = input("Ingrese el nombre del estudiante: ")

while True:
    try:
        Edad = int(input("Ingrese su edad: "))

        break
    except ValueError:
        print("Error. Ingresa solo numeros")


print("Cursos disponibles")
print("basico")
print("avanzado")

curso = input("Ingrese su curso: ").lower()
while curso != "basico" and curso != "avanzado":
    print("Error. Curso no reconocido. Por favor escriba 'basico' o 'avanzado'.")
    curso = input("Ingrese su curso: ").lower()

Familia = input("¿Tiene familiares ya inscritos en la academia (SI) o (NO)?: ").upper()
while Familia != "SI" and Familia != "SI":
    print("Error. Escriba solamente SI o NO.")
    Familia = input("¿Tiene familiares ya inscritos en la academia (SI) o (NO)?: ").upper()

#Descuento por matricula

if Edad < 18:
    descuento = descuento + 0.1

if Familia == "SI":
    descuento = descuento + 0.15

#Descuento mensualidad curso basico

if Edad < 10 and curso == "basico":
    mensualidad = curbasico * 1

elif 10 <= Edad <= 17 and curso == "basico":
    mensualidad = curbasico * 0.8

elif Edad >= 18 and curso == "basico":
    mensualidad = curbasico * 0.95

#Descuento curso avanzado

if Edad < 15 and curso == "avanzado":
    mensualidad = curavanzado * 1

elif 15 <= Edad <= 17 and curso == "avanzado":
    mensualidad = curavanzado * 0.9

elif Edad >= 18 and curso == "avanzado":
    mensualidad = curavanzado * 0.92

#Finalizando

matricula = matricula - (matricula * descuento)
print(f"Nombre del estudiante: {Nombre}")
print(f"Curso elegido: {curso}")
print(f"Valor final a pagar la mensualidad: {mensualidad}")
print(f"Valor final a pagar la matricula: {matricula}")
