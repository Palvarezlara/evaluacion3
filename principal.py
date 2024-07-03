import funciones as fn

while True:
    jugadores =[{'Id jugador' : 'id_jugador',
        'Nombre': 'nombre',
        'Apellido': 'apellido',
        'Fornite': 'fornite',
        'Fifa': 'fifa',
        'Valorant': 'valorant',
        'Tipo': 'tipo',}, {'Id jugador' : 'id_jugador',
        'Nombre': 'nombre',
        'Apellido': 'apellido',
        'Fornite': 'fornite',
        'Fifa': 'fifa',
        'Valorant': 'valorant',
        'Tipo': 'tipo'},{'Id jugador' : 'id_jugador',
        'Nombre': 'nombre',
        'Apellido': 'apellido',
        'Fornite': 'fornite',
        'Fifa': 'fifa',
        'Valorant': 'valorant',
        'Tipo': 'tipo'}]
    jugador={}
    print('\n====eSports “eShirlitos”====')
    print('')
    print('1.Registrar puntajes torneo')
    print('2.Listar los todos puntajes')
    print('3.Imprimir por Tipo')
    print('4.Salir del programa')
    try:
        opcion = int(input('\nIngrese su opción: '))

    except:
        print('Debe ingresar un valor númerico')
    if opcion == 1:
        fn.registrar_puntajes(jugadores, jugador)
    elif opcion ==2:
        fn.listar_todos_puntajes(jugadores)
    elif opcion == 3:
        fn.imprimir_tipo(jugadores)
    elif opcion == 4:
        print('Saliendo del programa')
        break
    else:
        print('Opción no existe. ')    
    