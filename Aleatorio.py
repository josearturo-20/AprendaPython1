import random
numero1=float(10.5)
def mifuncion():
    numero2=float(random.randrange(1,10))
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))
mifuncion()