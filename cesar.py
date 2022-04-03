
import string

MODULE = len(string.ascii_lowercase) # 26 para el alfabeto ASCII inglés

def intercambio(caracter, cambio):
    if caracter.isalpha():
        aux = ord(caracter) + cambio
        z = 'z' if caracter.islower() else 'Z'
        if aux > ord(z):
            aux -= MODULE
        caracter = chr(aux)
    return caracter

def reverso(caracter, cambio):
    if caracter.isalpha():
        aux = ord(caracter) - cambio
        z = 'z' if caracter.islower() else 'Z'
        if aux > ord(z):
            aux -= MODULE
        caracter = chr(aux)
    return caracter

def cesar(texto, key):
    return ''.join(map(lambda caracter: intercambio(caracter, key), texto))

def cesar_reverso(texto, key):
    return ''.join(map(lambda caracter: reverso(caracter, key), texto))


eleccion = int(input("Teclea una de las siguientes opciones:\n  1 - Para encriptar una frase \n  2 - Para Desencriptar una frase \n"))

if eleccion == 1 :
    frase = str(input("Frase a Encriptar? "))
    cambio_posicion = int(input("Numero posiciones? "))
    print("Frase para encriptar:", frase)
    print(cesar(frase, cambio_posicion))
    

if eleccion == 2:
    frase = input("Frase a Desencriptar? ")
    cambio_posicion = int(input("Numero posiciones? "))
    print("Frase para Desencriptar:", frase)
    print(cesar_reverso(frase, cambio_posicion))
   



    
    


