# ESTO ES COMO FUNCIONA EL RETURN DESDE VIDEOS DE YOUTUBE
def total_suma():
    a, b, = int(input("Ingresa el año actual: ")), int(input("ingresa el año de nacimiento: "))
    total = a - b
    while total <= 0 :
        print("El no ha nacido es imposible calcular la edad")
        a, b, = int(input("Ingresa el año actual: ")), int(input("ingresa el año de nacimiento: "))
        total = a - b
    return(total)


print(f'La edad es: ', total_suma())
