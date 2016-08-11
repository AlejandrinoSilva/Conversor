import os
class Conversor():
    def Inicio(self):
        os.system('clear')
        print("==========================================\n=CONVERSOR DE TEMPERATURAS\n==========================================")
        print("===MENU===================================")
        print("> 1 Para convertir de Celsius => Farenheit")
        print("> 2 Para convertir de Farenheit => Celsius")
        print("> 0 Para Salir\n==========================================")
        x = input("Elija una opción")
        if x == "":
            print("Es necesario que ingrese una opción para continuar")
        
   
app = Conversor()
app.Inicio()
