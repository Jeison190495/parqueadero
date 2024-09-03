import datetime

print ('Bienvenido al parqueadero')

hora=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def vehiculo():
    placa=input('Ingrese la placa del vehiculo: ')
    return placa
    
    
def init():
    try:
        while True:
            #moto, carro, bicicleta=tvehiculo
            print(f'oprima 1 para ingresar vehiculo')
            print(f'oprima 2 para retirar vehiculo vehiculo')
            print(f'oprima 3 para salir de la aplicacion')
            opcion = int(input(': '))
            print('Ingrese 1 para moto, 2 para carro y 3 para bicicleta:')
            tvehiculo = int(input())

            if(tvehiculo==1):   tvehiculo='moto'
            elif(tvehiculo==2):  tvehiculo= 'carro'
            elif(tvehiculo==3):   tvehiculo='bicicleta'
            else:   
                print('opcion invalida') 
                continue

            if (opcion==1):
                placa=vehiculo()
                print(f"Ingresando {tvehiculo} de placa: {placa}, {hora}")
            
            elif (opcion==2):
                print('Retirando vehiculo')
                placa=vehiculo()
                print(f"vehiculo de placa {placa} saliendo a {hora}")
            
            elif (opcion==3):
                print('Esta seguro que desea salir?')
                print('1:Si 2:No')
                salir=int(input(': '))
                if(salir==1):
                    break
                else:
                    print ('Bienvenido al parqueadero')
            
            else:
                print('opcion invalida')
    except:
        print('valor erroeneo')
init()