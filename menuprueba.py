from gestionUsuario import gestionusuario
while True:
    print('---------menu--------')
    print('1. Gestion de usuarios')
    print('0. salir')
    op = input('ingrese una opcion: ')

    match(op):
        case '1':
            gestionusuario()
        case '0':
            break
        case _:
            print('no hay xd')
