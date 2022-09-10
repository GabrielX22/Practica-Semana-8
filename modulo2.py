def valcontra(val):
    espacio = val.isspace()
    for i in range(len(val)):
       if val[i] == " ":
        espacio = True
        break
       else:
        espacio = False 
    if(len(val) >= 8):
      if espacio == True:
        print("Contraseña no es segura")
      else:
        print("Contraseña valida")     
    else:
        print("La contraseña debe contener minimo 8 caracteres")
    