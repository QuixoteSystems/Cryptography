

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

def vigenere(text, key, decrypt ):
    shifts = [ord(k) - ord('a') for k in key.lower()]
    i = 0
    def do_shift(char):
        nonlocal i
        if char.isalpha():
            shift = shifts[i] if not decrypt else MODULE - shifts[i]
            i = (i + 1) % len(key)
            return intercambio(char, shift)
        return char
    return ''.join(map(do_shift, text))


eleccion = int(input("Teclea una de las siguientes opciones:\n  1 - Para Encriptar una frase \n  2 - Para Desencriptar una frase \n"))

if eleccion == 1:
    encriptar = True
if eleccion == 2:
    encriptar = False

frase = str(input("Escribe la Frase a Encriptar o Desencriptar?\n "))
key = str(input("Escribe la Clave Compartida:\n "))
print(vigenere(frase, key, encriptar))