#Ejercicio realizado nuevamente en forma de practica

import random

valores=["piedra", "papel", "tijeras" ]
usuario = ''
pc_aleatorio = ''

def datos():
      global usuario, pc_aleatorio
      usuario=input("Ingrese:\n piedra \n papel \n tijeras \n")
      usuario=usuario.lower() 

      pc_aleatorio= random.choice(valores)

      while usuario not in valores:
            usuario = input("Datos no validos Ingrese:\n piedra \n papel \n tijeras \n ")
    
      print("El usuario ha escogido", usuario)
      
      print("El pc ha escogido", pc_aleatorio)


def juego(jugador, pc):
    if (jugador=="piedra" and pc=="tijeras"):
            print("EL jugador Gana")
    elif(jugador=="papel" and pc=="piedra"):
          print("El jugador gana")
    elif(jugador=="tijeras" and pc =="papel"):
          print("El jugador gana")
    elif(jugador==pc):
          print("Empate")
    else:
          print("La maquina ganó")


def repetir():
      while True:
            datos()
            juego(usuario, pc_aleatorio)
            opcion=input("¿Desea volver a jugar? \nDigita si para continuar \n")

            if (opcion!="si"):
                  break 

repetir()


    