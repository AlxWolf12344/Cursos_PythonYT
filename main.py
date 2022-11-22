

LIST = [2,45,1,5,6,87]
def pruebas():
    ordenar_la_lista = input("Quieres ordenar la lista?: ")
    if ordenar_la_lista == 'si':
        LIST.sort()
    else:
        ordenar_la_lista == 'no'
        print("Ok"), print("*"*40)
        return LIST

print(pruebas())