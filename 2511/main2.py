from Moneda import moneda

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a:= input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Regristrar una moneda', accion1),
        '2': ('Cambiar moneda', accion2),
        '3': ('Salir', salir)
    }

    generar_menu(opciones, '3')


def accion1(self):
    lista = [*ProfileMoney]
    ProfileMoney = moneda("", "", "")
    lista.print()
    


def accion2():
    print('Modificando moneda')

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()
        
