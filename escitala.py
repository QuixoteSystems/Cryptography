


import numpy as np
import math

def escitala(text, key):
    rows = key
    cols = math.ceil(rows)
    m = np.array(list(text.ljust(rows*cols, ' '))).reshape((rows, cols))
    return ''.join([''.join(row) for row in m.transpose()]).strip()


frase = str(input("Frase a Encriptar o Desencriptar?\n "))
key = int(input("Tamaño Vara? "))
print(escitala(frase, key))
