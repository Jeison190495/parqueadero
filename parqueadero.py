import datetime
import cx_Oracle
#import psycopg2

#conectar base dedatos oracle

def conectar_oracle():
    try:
        connection = cx_Oracle.connect("SYSTEM", "Sistemas.2023", "localhost:1521/xe")
        print("Conectado a Oracle")
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"Error al conectar a Oracle: {e}")

# Conectar a la base de datos PostgreSQL
'''def conectar_postgres():
    try:
        connection = psycopg2.connect(
            dbname="nombre_db", 
            user="usuario", 
            password="contraseña", 
            host="localhost", 
            port="5432"
        )
        print("Conectado a PostgreSQL")
        return connection
    except psycopg2.DatabaseError as e:
        print(f"Error al conectar a PostgreSQL: {e}")'''

# Uso de las conexiones
oracle_conn = conectar_oracle()
#postgres_conn = conectar_postgres()

# No olvides cerrar las conexiones al finalizar
if oracle_conn:
    oracle_conn.close()
#if postgres_conn:
 #   postgres_conn.close()




print ('Bienvenido al parqueadero')

horaIngreso=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
horaSalida=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def vehiculo():
    placa=input('Ingrese la placa del vehiculo: ')
    return placa
    
def precio():
     tiempopagar = (horaSalida - horaIngreso).total_seconds() / 60
     tvehiculo={'moto':50,
               'carro':70,
               'bicicleta':40
               }
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
                print(f"Ingresando {tvehiculo} de placa: {placa}, {horaIngreso}")
            
            elif (opcion==2):
                print('Retirando vehiculo')
                placa=vehiculo()
                print(f"vehiculo de placa {placa} saliendo a {horaSalida}")
            
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