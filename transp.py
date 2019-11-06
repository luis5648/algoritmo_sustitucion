
#!/usr/bin/python3.6
#programa de transposicion.

def encryptMessage(key, message):
#Cada cadena de texto en el mensaje cifrado representa una columna en la matriz
    ciphertext = [''] * key

    # recorremos las colimnas
    for col in range(key):
        pointer = col

        #Lee cada elemento de la columna
        while pointer < len(message):
            # Pone el caracter que encuentra en el indice de la matriz
            ciphertext[col] += message[pointer]

            #mueve el puntero al siguiente elemento de la columna
            pointer += key

    # Convertimos la lista en una cadena de texto y  lo retornamos
    return ''.join(ciphertext)


#Ejecución del algoritmo:

mensaje = input("Introduzca el mensaje a cifrar: ")
llave = int(input("Introduzca la profundidad para el cifrado: "))

palabraCifrada = encryptMessage(llave,mensaje)

print(palabraCifrada)