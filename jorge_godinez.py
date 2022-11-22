# agarrense por que esto lo hice a las 3  de la mañana con cafe y mucho sueño

CONTADOR = []


def registro_numerico():
    list_trigger = False
    final_list = False
    cuenta = int(input("cuantos numeros vas a ingresar?: "))
    cuenta = range(0, cuenta, 1)
    for i in cuenta:
        CONTADOR.append(input("Ingresa el numero y da enter para continuar: "))
    add_more = input(f'Has añadido {len(CONTADOR)} numeros quieres añadir mas numeros? (y) para si (Pulse otra tecla) para no: ')
    while not final_list:
        while not list_trigger:
            if add_more == 'y':
                cuenta = int(input("Cuantos numeros mas quieres añadir?: "))
                cuenta = range(0, cuenta, 1)
                for j in cuenta:
                    CONTADOR.append(input("Ingrese el numero y presione enter para continuar: "))
            else:
                print("Muy bien")
                print("*" * 40)
                list_trigger = True
            add_more = input("Quieres añadir mas numeros? (y)Si, (Cualquier otra tecla)No: ")
        if add_more == "y":
            cuenta = int(input("Cuantos numeros mas quieres añadir?: "))
            cuenta = range(0, cuenta, 1)
            for y in cuenta:
                CONTADOR.append(input("Ingrese el numero y presione enter para continuar: "))
            final_list = True
        else:
            print("Muy bien")
            print("*" * 40)
            final_list = True
    print("Tipos de organización, de menor a mayor [Si], Mayor a menor [No]")
    orden_numerico = input("Como quieres ordenar los numeros ingresados?: ")
    if orden_numerico == 'si':
        CONTADOR.sort()
        return CONTADOR
    else:
        CONTADOR.sort(reverse=True)
        return CONTADOR


print(registro_numerico())
