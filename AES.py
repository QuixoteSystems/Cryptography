
from Crypto import Random
from Crypto.Cipher import AES
import os

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def decrypt(data, key):    
    nonce = data[:AES.block_size]
    tag = data[AES.block_size:AES.block_size * 2]
    ciphertext = data[AES.block_size * 2:]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
print(" ")
print("----------------------------------------------------------------------------------------- ")
print("Script Simple para Encriptar un texto mediante AES con una contraseña privada compartida ")
print("----------------------------------------------------------------------------------------- ")
print(" ")
eleccion = int(input("Escribe el número de la opción que quieras:\n\n  1 - Encriptar un texto \n  2 - Desencriptar un texto \n\n"))

print(" ")

if eleccion == 1 :
    key = os.urandom(256)[:16]
    print("Esta es tu Clave Privada aleatoria: ")
    print(" ")
    #print(key)
    key_arreglada = str(key).encode("ISO-8859-1").decode()
    #key_arreglada = str(key).encode().decode()
    key_arreglada = key_arreglada.replace("b'",'')
    key_arreglada = key_arreglada.replace('b"','')
    key_arreglada = key_arreglada[:-1]

    print(key_arreglada)
    print(" ")
    
    frase = input("Escribe el texto a Encriptar\n ").encode()
    print(" ")
    print("Este es tu texto Encriptado: " + frase.decode() + "\n")
    
    resultado = encrypt(frase, key)

    print("Texto Encriptado: \n")
    
    resultado = str(resultado).encode("ISO-8859-1").decode()
    resultado = resultado.replace("b'",'')
    resultado = resultado.replace('b"','')
    resultado = resultado[:-1]

    print(resultado)
    print(" ")


elif eleccion == 2 :
    key = input("Escribe tu clave Privada\n ").encode()
    key = key.decode('unicode-escape').encode("ISO-8859-1")
    print(" ")

    frase = input("Escribe el texto Encriptado:\n ").encode()
    frase = frase.decode('unicode-escape').encode("ISO-8859-1")

    resultado = decrypt(frase, key)

    print(" ")
    print("Texto Desencriptado:\n ")
    print(resultado.decode("utf-8"))
    print(" ")
