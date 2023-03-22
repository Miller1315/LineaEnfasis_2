# Codigo visto en clase #4

import random

print ("Juego piedra, papel o tijeras \n _______________________________\n")

options = ["piedra","papel", "tijeras"]


def user():

    option_user = input("Elige y escribe una de estas opciones: \n Piedra \n Papel \n Tijeras \n")
    print("user " , option_user)
    
    option_machine = random.choice(options)
    print("machine", option_machine)
    
    if option_user not in options:
        print("opcion no valida")
        user()
    else:
        compare(option_machine, option_user)


def compare(pc,player):

    if pc == player:
        print("Empate!!")
    elif player == "piedra" and pc == "tijeras":      
        print("Ganaste humano!!")
    elif player == "papel" and pc == "piedra":      
        print("Ganaste humano!!")
    elif player == "tijeras" and pc == "papel":      
        print("Ganaste humano!!")
    else: 
        print("maquina ganó, El humano perdio") 



def jugar():
    while True:
        user()
        res =input ("Escribe 'S' para volver a jugar o 'N' para terminar: ").lower()
        if res !="s":
            break
jugar()








