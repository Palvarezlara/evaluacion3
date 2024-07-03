
jugadores=[{'Id jugador' : 'Pamela',
        'Nombre': 'Pamela',
        'Apellido': 'Alvarez',
        'Fornite': '1200',
        'Fifa': '1333',
        'Valorant': '3000',
        'Tipo': 'Experto',}, 
        {'Id jugador' : 'Javier',
        'Nombre': 'Javierito',
        'Apellido': 'aSuarez',
        'Fornite': '1200',
        'Fifa': '0',
        'Valorant': 'valorant',
        'Tipo': 'tipo'},
        {'Id jugador' : 'Alecita',
        'Nombre': 'ale',
        'Apellido': 'Alejandra',
        'Fornite': '1200',
        'Fifa': '1300',
        'Valorant': '2000',
        'Tipo': 'tipo'}]

expertiz = ['Principiante', 'Avanzado', 'Experto']
def registrar_puntajes(jugadores, jugador):
    
    #ingreso los datos del usuario
    while True:
        try:    
            id_jugador= input('Ingrese su nombre usuario: ')
            nombre= input('Ingrese nombre del jugador: ')
            apellido = input('Ingrese apellido del jugador: ')
            tipo=input('Ingrese su categoria (Principiante - Avanzado - Experto): ').lower()
            tipo= tipo.title()
            if len(id_jugador)!=0 and len(nombre) !=0 and len(apellido) != 0 and len(tipo)!=0:
                break
            else:
                print('Debe rellenar todos los campos')   
        except:
            print('Debe ingresar algo. ')
    #pido los puntajes de los jugadores en cada categoria
    while True:
        try:
            print('''Ingrese el juego
                    1.- Fornite
                    2.- Fifa
                    3.- Valorant
                    4.- Continuar''')
            juego = int(input('--->'))
            if juego == 1:
                fornite = int(input('Ingrese su puntaje de Fornite: '))
            elif juego ==2:
                fifa = int(input('Ingrese su puntaje de Fifa: '))
            elif juego ==3:
                valorant = int(input('Ingrese su puntaje de Valorant: '))
            elif juego == 4:
                break
            else:
                print('opción no existe. ')
  
        except:
            print('Solo puede ingresar valores númericos.')
    jugador: {
        'Id jugador' : id_jugador,
        'Nombre': nombre,
        'Apellido': apellido,
        'Fornite': fornite,
        'Fifa': fifa,
        'Valorant': valorant,
        'Tipo': tipo,
    }
    #intente subir el jugador a la lista jugadores, no pude, me quito mucho tiempo. Y al no resultar no pude verificar todas las funciones.
    jugadores.append(jugador) 

    return jugadores

#Listar puntajes
#como no logre subir los jugadores a la lista, me fue imposible verlos aquí 
def listar_todos_puntajes(jugadores):
    for jugador in jugadores:
        for j, m in jugador.items():
            print(f'{j}: {m}', end='')
        print()
    

#Imprimir por Tipo, lo intente 

def imprimir_tipo(jugadores):
    ingreso = input('Ingrese el tipo de expertiz para imprimir los jugadores: ')
    ingreso= ingreso.title()
    jugadores_a_imprimir=[]
    
    if ingreso == 'Principiante':
        for ingreso in jugadores:
            jugadores_a_imprimir.append()
    elif ingreso == 'Avanzado':
        for ingreso in jugadores:
            jugadores_a_imprimir.append()
    elif ingreso == 'Experto':
        for ingreso in jugadores:
            jugadores_a_imprimir.append()
    else:
        print('tipo no encontrado')

    with open('archivo.txt', 'w', encoding='UTF-8') as file:
        for jugador in jugadores_a_imprimir:
            file.write(f'Id jugador{jugador['id_jugador']}\n ')
            file.write(f'Nombre {jugador['Nombre']}\n')
            file.write(f'Apellido {jugador['Apellido']}')
            file.write(f'Fornite {jugador['Fornite']}')
            file.write(f'Fifa {jugador['Fifa']}')
            file.write(f'Valorant {jugador['Valorant']}')
            file.write(f'Tipo {jugador['tipo']}')