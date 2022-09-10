def valusu(val):
    if( len(val) <= 6):
        print("El nombre de usuario debe contener minimo 6 caracteres")
    elif( len(val) >= 12):
        print("El nombre de usuario no debe contener mas de 12 caracteres")
    elif(val.isalnum() == False):
        print("El nombre de usuario solamente puede contener letras y numeros")
    else:
        print("Usuario valido")


