cuota_mensual = 12000
kit_inicial = 15000


integrantes = int(input("Ingrese integrantes del hogar: "))
quintil = int(input("Ingrese su quintil del 1 al 5: "))


if quintil in [1,2,3]:
    kit_inicial = kit_inicial * 0.88

if integrantes >= 4:
    kit_inicial = kit_inicial * 0.95

if integrantes >= 5 and quintil in [1,2]:
    cuota_mensual = cuota_mensual * 0.75


elif integrantes >=5 and quintil in [3,4]:
    cuota_mensual = cuota_mensual * 0.82
   

elif 2 <= integrantes <= 5 and quintil in [1,2]:
    cuota_mensual = cuota_mensual * 0.85


elif 2 <= integrantes <= 5 and quintil in [3,4]:
    cuota_mensual = cuota_mensual * 0.9


else:
    quintil = 5 or integrantes < 2



print(f"Integrantes del hogar: {integrantes}")
print(f"quintil: {quintil}")
print(f"El valor de la cuota es: {cuota_mensual}")
print(f"El valor del kit incial es: {kit_inicial}")

