class Persona:
        def __init__(self,nombre,fecha_nac,cedula):
                self.nombre= nombre
                self.fecha_nac = fecha_nac
                self.cedula = cedula
                self.nivel_energia = 80
                self.entretenimiento = 80

        def comerSano(self):
                print(f"{self.nombre} está comiendo sano")
                self.nivel_energia += 30
                print("Tu nivel de energia subio a:", self.nivel_energia )

        def dormir(self):
                print(f"{self.nombre} está durmiendo")
                self.nivel_energia += 100
                print("Tu nivel de energia subio a: ", self.nivel_energia)

        def ComerSinRestri(self):
                print(f"{self.nombre} está comiendo sin restricciones")
                self.nivel_energia += 75
                print("Tu nivel de energia subio a: ", self.nivel_energia)

        def correr (self):
                print(f"{self.nombre} está corriendo")
                self.nivel_energia -= 20
                print(f"Energia:{self.nivel_energia}")


        def informacion(self):
                print("Datos ingresados: ")
                print(f"Nombre :{self.nombre} ")
                print(f"fecha nacimiento :{self.fecha_nac} ")
                print(f"Cedula :{self.cedula} ")
                print(f"Energia :{self.nivel_energia} ")

        def ver_tv(self):
                print(f"{self.nombre} Esta viendo Tv")
                self.entretenimiento += 30
                print("Tu nivel de entretenimiento subio a: ", self.entretenimiento)

        def salir_amigos(self):
                print(f"{self.nombre} Salio a correr con amigos")
                self.entretenimiento += 20
                self.nivel_energia -= 20 
                # print(f"Energia:{self.nivel_energia}")
                # print(f"Entretenimiento:{self.entretenimiento}") 


        def estudiar(self):
                print (f"{self.nombre} Esta estudiando")
                self.entretenimiento -=30           
                
        def comprobar(self):    
                
                print(f"Energia :{self.nivel_energia} ")
                print(f"Entretenimiento:{self.entretenimiento}")
                        #20 - 40      20   40
                if self.nivel_energia >= 20 and self.nivel_energia <=40 :
                        # self.nivel_energia = 0
                        print(f"{self.nombre} esta por debajo y se desmayará", self.nivel_energia )
                elif self.nivel_energia >=0 and self.nivel_energia <= 19:
                        print(f"{self.nombre} Ha muerto por que su energia se agotó ", self.nivel_energia) 
                # else:
                #         print("Tu nivel de energia actual es: ", self.nivel_energia)


                if self.entretenimiento >= 20 and self.entretenimiento <40 :
                        # self.entretenimiento = 0
                        print(f"{self.nombre}) Esta aburrido", self.entretenimiento )
                elif self.entretenimiento >=0 and self.entretenimiento <= 19:
                        print(f"{self.nombre} Murio de aburrimiento ", self.entretenimiento) 

                elif self.entretenimiento >100:
                        print(f"{self.nombre} llego a su limite de entretenimiento")
                # else:
                #         print("su nivel de entretenimiento actual es: ", self.entretenimiento)
        

Ejecutar = Persona("Huber","12-07-1992","1115")
Ejecutar.comerSano()
Ejecutar.salir_amigos()
Ejecutar.salir_amigos()
Ejecutar.salir_amigos()
Ejecutar.salir_amigos()
Ejecutar.estudiar()
Ejecutar.estudiar()
Ejecutar.estudiar()
Ejecutar.estudiar()
Ejecutar.estudiar()

Ejecutar.comprobar()    