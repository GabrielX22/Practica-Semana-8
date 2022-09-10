from queue import Empty
from modulo1 import valusu
from modulo2 import valcontra
usu = Empty
con = Empty
usua = Empty
contras = Empty

while True:
    print("----------Bienvenido---------")
    print("Ingrese el numero de la opcion:")
    print("1-Registrarse")
    print("2-Iniciar sesion")
    print("3-Salir")
    op = int(input())
    if op == 1:
      usu =input("Ingrese su usuario: ")
      valusu(usu)
      con =input("Ingrese su contraseña: ")
      valcontra(con)
      if(len(usu) >= 6 and len(usu) <= 12 and usu.isalnum() == True and len(con) >= 8):
        print("Usuario Registrado correctamente")
      else:
        print("Usuario no se ha podido registrar")
        usu = Empty
        con = Empty
    elif op == 2:
        usua = input("Ingrese su usuario: ")
        contras = input("Ingrese su contraseña: ")
        if(usua == usu and contras == con):
           print(f"Bienvenido {usua} al programa")
           break
        else:
           print("Inicio incorrecto, intente de nuevo o registrese") 
    elif op == 3:
       print("Gracias por usar el programa")
       break
    else:
        print("Ingrese una opcion valida")

    