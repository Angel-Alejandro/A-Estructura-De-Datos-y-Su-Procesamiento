"Estructura de datos y su procesamiento"
"Evidencia 1 "

# Especificaciones del caso a desarrollar:
# Un negocio dedicado a la renta de espacios de coworking desea automatizar su sistema de reserva de salas de reuniones atendiendo las siguientes 
# indicaciones:
# 1) Supuestos:
#     a) Se cuenta con una cantidad determinada de salas con cupo variado dependiendo de la sala.
#     b) La renta de la sala se hace por turnos consistentes en: mañana, tarde y noche incluso en días festivos.

# 2) Condiciones:
#      a) La reserva de la sala se debe hacer, por lo menos, dos días antes y debe indicarse el nombre del evento al momento de realizar la reservación.
#      b) Solamente pueden reservar una sala aquellos que son # lientes registrados.
#      c) No puede reservarse una sala para dos eventos al mismo tiempo.
#      d) Para cada reservación se debe generar un folio único.


# 3)	Funcionalidad que se debe cumplir:
#     a)	Se presentará un menú principal que ofrezca acceso a:
#              R i)	Registrar la reservación de una sala
#               ii)	Editar el nombre del evento de una reservación ya hecha.
#               iii)	Consultar las reservaciones existentes para una fecha específica.
#               iv)	Registrar a un nuevo cliente con los siguientes datos:
#                           (1)	Una clave única, generada automáticamente, para el cliente.
#                           (2)	Nombre del cliente.
#                v)	Registrar una sala con los siguientes datos:
#                            (1)	Una clave única, generada automáticamente, para la sala.
#                            (2)	Nombre de la sala.
#                            (3)	Cupo de la sala.
#               vi)	Salir


# En este caso , importaremos pyttsx3 el cual nos ayudara con nuestro modulo de voz con el siguiente comando:
# pip install pyttsx3
from ast import While
from mailbox import NoSuchMailboxError
from re import U
from select import select
from traceback import format_tb
import pyttsx3
# importamos la libreria datetime para el manejo de fechas el cual usaremos en este codigo 
import datetime
# En este caso , le daremos un poco mas de diseño , a nuestro programa el cual , usaremos la libreria colorama
# usando el siguiente comando (Nota: se usa el Fore para cambiar el color de un texto): 
from colorama import Fore,init
init()

# En este bloque de codigo se configura nuestro modulo de voz el cual presentara nuestro programa

engine = pyttsx3.init()
voice_id = 'spanish-latin-am'
voice_id = 'mbrola-es1'
engine.setProperty('voice', voice_id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
string="Bienvenidos a nuestro menu "   # Aqui se guarda en una variable el texto que queramos que se reproduzca.

print(Fore.BLUE + " Bienvenido a nuestro menu Coworking\n")

# Aqui se utiliza este comando , para reproducir el audio
engine.say(string)
engine.runAndWait()

# En este caso, crearemos una funcion la cual su argumento se llamara mostrar_menu , el cual entre parentisis 
# ingresamos se podria llamar variable , la cual su valor es un diccionario , el cual contiene nuestras opciones
# a mostrar el cual , utilizamos un print para , que imprima a pantalla selecione su opcion , pero todavia 
# no obtengamos un valor por el usuario , usamos un for para desempaquetar.

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

# En este caso , crearemos otra funcion la cual su argumento se llamara leer_opcion , el cual entre parentisis 
# ingresaremo se podria llamar variable , la cual su valor es un diccionario , el cual contiene nuestras opciones
# , en el siguiente linea usamos un ciclo el cual usamos una variable llamada ingresa el cual pregunta la opcion, 
# la cual si no ingresa una opcion se repite de nuevo la pregunta.

def leer_opcion(opciones):
    while (Ingresa := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return Ingresa

# En este caso , crearemos otra funcion la cual su argumento se llamara ejecutar_opcion la cual su variable se 
# llamara opcion (Okey bueno en este la funcion que tiene es que accede a la clave del diccionario y opciones accede al 
# diccionario el cual ejecuta como opcion. 

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

# En este caso creamos un funcion , le mencionamos un argumento llamada menu_principal lo cual esta funcion 
# sea crea un Diccionario el cual se muestra la clave la cual es la opcion, seguido de ello , se muestra 
# la opcion , y por ultimo asociamos un argumento.
def menu_principal():
    opciones={
         "1":("Registrar la reservacion de una sala",accion1),
         "2":("Editar el nombre del evento de una reservacion ya hecha",accion2),
         "3":("Consultar las reservaciones existentes para una fecha específica",accion3),
         "4":("Registrar a un nuevo cliente con los siguientes datos",accion4),
         "5":( "Registrar una sala con los siguientes datos" ,accion5),
         "6":( "Salir",salir)
    }
    generar_menu(opciones, '6')

Reserva={}

Usuarios={}

Salas={}

def accion1():
    while True:
            Reservas=input(Fore.LIGHTRED_EX + "Ingresa el nombre del evento: " )
            Turno = input(Fore.LIGHTCYAN_EX + " Ingresa el turno: Matutino/Vespertino/Nocturno ")
            if Reservas=="":
                 break
            else:
                    fecha_actual:fecha_actual = datetime.date.today()
                    cant_dias= 2
                    nueva_fecha= fecha_actual + datetime.timedelta(days=+cant_dias)
                    fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
                    fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
                    Cuarta_llave=max(list(Reserva.keys()),default= 0) + 1
                    Reserva[Cuarta_llave] = (Reservas,Turno,fecha_procesada)
                    for clave,datos in list(Reserva.items()):
                     print(f"Tu Usuario es {clave}\t El Turno es {datos[1]}" )
                    if fecha_procesada < nueva_fecha: 
                        print(f"Tu fecha no ha sido procesado tienes que hacerlo con por lo menos 2 dias")
                        break
                    else:
                        fecha_procesada > nueva_fecha
                        print(f"Tu fecha ha sido procesada") 
                                             
def accion2():
    while True:
        Seccion=int(input("Ingresa la clave: "))
        if Seccion in Reserva.keys():
            nuevo_nombre=input("Ingresa el nuevo nombre: ")
            for clave,[Reservas,Turno,fecha_procesada] in Reserva.items():
                if Seccion == clave:
                    Reserva.update({clave:[nuevo_nombre,Turno,fecha_procesada]})
                    print(f" Cambio exitoso {Reserva}")
                else:
                    print("Funcion Invalida")

def accion3():
    while True:
        Selecciona=int(input("Ingresa la clave "))
        if Selecciona =="":
            break
        else:
            print("Nombre/Turno/Fecha")
            print(Reserva.get(Selecciona))
    
def accion4():
    while True:
             Usuario=input("Ingresa un usuario: " )
             if Usuario==0:
                 break
             else:
                  Tercera_llave=max(list(Usuarios.keys()),default=0) + 1
                  Usuarios[Tercera_llave] = (Usuario) 
             for clave,datos in list(Usuarios.items()):
                 print(f"Tu clave de usuario es:   {clave}   Tu usuario es:   {datos}")

def accion5():
    while True:
             Nombre=input("Ingresa el nombre de la sala: " )
             if Nombre=="":
                 break
             else:
                 Capacidad_=int(input("Ingresa el capacidad de la salas: " ))
                 Segunda_llave=max(list(Salas.keys()),default=0) + 1
                 Salas [Segunda_llave] = (Nombre,Capacidad_) 
             for clave,datos in list(Salas.items()):
                 print(Fore.BLACK + "Clave\t" + "Nombre\t"  + "Capacidad\t")
                 print(f"{clave}\t{datos[0]}\t{datos[1]}")

def salir():
    for clave,datos in list(Reserva.items()):
        print(f"{'*' * 10} Reporte {'*' * 10}")
        print(f"La Clave es        {clave}")
        print(f"La nombre es       {datos[0]}")
        print(f"La turno es        {datos[1]}")
        print(f"La fecha es        {datos[2]}")
                 
        print(f"{'*' * 10} FIN {'*' * 10}")
        print("Gracias por usar nuestro programa :)")
        string_2="Gracias por Usar nuestro programa "
        engine.say(string_2)
        engine.runAndWait()
            
if __name__ == '__main__':
    menu_principal()