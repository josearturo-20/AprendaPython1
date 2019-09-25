acumulado=int(0)
numero=str("")

while True:
    numero=input("dame un numero: ")
    if numero=="":
        print("Vacío.Salida del programa")
        break
    else:
        acumulado+=int(numero)
        salida= "monto acumulado: {}"
        print (salida.format(acumulado))