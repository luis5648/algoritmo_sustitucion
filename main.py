#!/usr/bin/python3.6

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

llave = "cab"
palabra = input("introduzca la palabra a encriptar (3 letras): ").lower()

if len(palabra) == len(llave):
    for x,y in zip(palabra,llave):
        p =  abecedario.index(x) + 1
        l =  abecedario.index(y)
        encrip = p+l
        print(abecedario[encrip].upper(),end="")

else:
    print("la palabra es demasiado grande!")


    
