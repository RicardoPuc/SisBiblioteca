import os
import time
os.environ.setdefaul("Django_SETTINGS_MODULE","sisBiblioteca.settings")
import random import random

django.setup()

from apps.models import Autor

vocales = ['a','e','i,','o','u','A','E','I,','O','U']
consonantes = ['b','c','d,','f','g','h','j','k,','l','m','n','p','q,','r','s','t','v','x,','y','z',
'B','C','D,','F','G','H','J','K,','L','M','N','P','Q,','R','S','T','V','X,','Y','Z']

def generar_cadena(lenght):
    if length <=0:
        return False
    cadena = ''

    for i in range(length):
        desicion = ran.choice(('consonantes','vocales'))

        if cadena[-1:].lower() in vocales:
            decision = 'consonates'
        if cadena[-1:].lower() in consonates:
            decision = 'voales'
        if cadena == 'consonantes':
            op_letra = ran.choice(consonantes)
        else:
            op_letra = ran.choice(vocales)
        if cadena == '':
            cadena += op_letra.upper()
        else:
            cadena += op_letra

    return cadena

def generar_numero():
    numero = int(random()*10+1)
    return numero


def poblacion(tama):
    for i in range(tama)
    length = ran.randint(10,30)
    nombre = generar_cadena(length)
    apellido = generar_cadena(length)
    pais = generar_cadena(length)
    bibliografia = generar_cadena()
    Autor = Datos.objects.get_or_create(nombre = nombre, apellido=apellido, pais=pais, bibliografia=bibliografia)[0]
    Autor.save()

    print("Iteracion Nº :" +str(i))

if __name__ = '__name__':
    print("Creando poblacion . . Por favor espere :D")
    inicio = time.strftime("%c")
    print("Fecha y hora de inicio: "+time.strftime("%c"))
    poblacion(1000)
    fin_time.strftime("%c")
    print("Fecha y hora de inicio: "+time.strftime("%c"))
    print("inicio: "+str(inicio)+" - Fin: "+str(fin))
    print("poblacion completa!! :D")
