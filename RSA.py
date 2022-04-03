
from os import lseek
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


# Script para generar una Clave Pública y Privada con contrasena
# Genera dos archivos, uno por clave
# Y también para encriptar un texto nuestra Clave

print(" ")
print("----------------------------------------------------------------------------------------- ")
print("Script Simple para Encriptar un texto mediante RSA con clave asimetrica ")
print("----------------------------------------------------------------------------------------- ")
print(" ")
eleccion = int(input("Escribe el número de la opción que quieras:\n\n  \
    1 - Crear Clave Privada y Publica \n  \
    2 - Encriptar texto \n  \
    3 - Desencriptar texto\n "))

print(" ")

if(eleccion == 1):
    
    # Generamos la Clave Privada
    key = RSA.generate(2048)
    clave_privada = key.export_key()
    file_out = open("clavePrivada.pem", "wb")
    file_out.write(clave_privada)
    file_out.close()

    #file_out = open("clavePrivada.bin", "wb")
    #file_out.write(encrypted_key)
    #file_out.close()

    print(" ")
    print("Impresion Clave Privada:\n")
    print(clave_privada)
    print(" ")

    # Derivamos la clave Publica
    print("Impresion Clave Publica:\n ")
    print(key.publickey().export_key())

    file_out = open("clavePublica.pem", "wb")
    file_out.write(key.publickey().export_key())
    file_out.close()

elif(eleccion == 2):

    texto = input("Escribe el texto a encriptar: \n").encode()
    file_out = open("datos_encriptados.bin", "wb")

    clave_publica = RSA.import_key(open("clavePublica.pem").read())
    clave_sesion = get_random_bytes(16)

    # Encriptamos con la clave Publica RSA y una clave de sesion aleatoria
    cipher_rsa = PKCS1_OAEP.new(clave_publica)
    enc_session_key = cipher_rsa.encrypt(clave_sesion)

    # Encriptamos el archivo con la clave de sesion AES
    cipher_aes = AES.new(clave_sesion, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(texto)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()

elif(eleccion == 3):

    nombre_archivo = input("Escribe el texto a encriptar: \n")
    archivo = open(nombre_archivo, "rb")
    print(" ")

    # Anadimos el nombre del archivo donde se guarda la Clave Privada
    private_key = RSA.import_key(open("clavePrivada.pem").read())

    enc_session_key, nonce, tag, ciphertext = \
   [ archivo.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

    # Desencriptamos la clave de sesion con la clave Privada RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Desencriptamos el archivo con la clave de sesion AES
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print(data.decode("utf-8"))