
import random








class JuegoPPT:

    def __init__(self) :
        self.opciones=["piedra", "papel", "tijeras" ]

    def jugar(self):
        while True:
            self.usuario()
            res = input("Escribe 'S Para volver a jugar o 'N' para terminar: ") .lower()
            if res != "s":
                break

    def usuario(self):

        opcion_usuario= input ("Elige y escibe una de estas opciones \n Piedra \n papel \n tijera\n ").lower()
        print("usuario ", opcion_usuario)

        opcion_maquina=random.choice(self.opciones)
        print("maquina", opcion_maquina)
        
        if opcion_usuario not in self.opciones:
            print("opcion no valida")
            self.usuario()
        else:
            self.comparar(opcion_maquina, opcion_usuario)

    def comparar(self, pc, jugador):
        if pc == jugador:
            print("Empate!!")
        elif jugador == "piedra" and pc == "tijeras":      
            print("Ganaste humano!!")
        elif jugador == "papel" and pc == "piedra":      
            print("Ganaste humano!!")
        elif jugador == "tijeras" and pc == "papel":      
            print("Ganaste humano!!")
        else: 
            print("maquina ganó, El humano perdio") 

juego = JuegoPPT()
juego.jugar()

