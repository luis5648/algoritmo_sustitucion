#!/usr/bin/python3.6

listaDePrueba = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

llave = "cab"
palabra = input("introduzca la palabra a encriptar: ").lower()

for x,y in zip(palabra,llave):
    p =  listaDePrueba.index(x) + 1
    l =  listaDePrueba.index(y)
    encrip = p+l
    print(listaDePrueba[encrip],end="")
    
