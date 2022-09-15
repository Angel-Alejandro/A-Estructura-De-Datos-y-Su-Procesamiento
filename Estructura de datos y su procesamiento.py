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

# Creamos nuestros diccionarios vacios en este caso , asiganmos 3 diccionarios , ya que nos facilitran el
# guardado de nuestra informacion en las opciones siguientes

Reserva={}

Usuarios={}

Salas={}

# En la primera opción usamos un def en cual su argumento es accion1 , el cual usamos una variable que pregunte
# el evento lo guarde en una variable, en la siguiente línea creamos una variable que guarde el turno, usamos un 
# el cual si se omite la variable reservas, rompe el ciclo , después usamos un else, en el cual la función de esto
# creamos una variable el cual se iguala con la fecha de la máquina, en la siguiente linea creamos un variable que 
# guarde el valor de 2, después creamos una variable y usamos la variable el cual guarda el valor de la máquina, usamos datetime
# para sumar la cant dias de la variable la cual son 2 , después preguntamos , cual es la fecha al usuario , 
# la cual la convierte a dato tipo fecha, lo siguiente es , creamos una variable la cual usa la función de max 
# convierte el diccionario a lista y se la asigana una clave automáticamente, usamos el diccionario, agregamos la variable anterior
# a unos corchetes le damos el valor de igual a los campos que queremos que gurde en nuestro diccionario, usamos 
# unpacking para desempaquetar, el siguiente if es usado en la fecha , okey volviendo a lo anterior si la fecha que se ingreso ,
# es menor a la de la maquina con dos dias sumados entonces, imprime a pantalla un mensaje que la fecha no ha sido procesada
# si la fecha ingresada es mayor a la de la maquina con días sumandos entonces imprime a pantalla un mensaje de que la fecha 
# ha sido procesada

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

# En la siguiente opcion,la cual usamos un ciclo el cual usamos un while true, creamos una variable la cual pregunta
# la clave , usamos un if para recorrer nuestro diccionario , creamos otra variable la cual pregunte , el nuevo
# nombre del evento , usamos el unpacking para , la cual es clave , la cual es del diccionario , ingresamos los campos
# que tiene nuestro diccionario en unos corchetes, de nuestro diccionario en .items() para mostrar los datos
# usamos el if para comparar la clave que ingresamos y lo comparamos igual a la clave existente, si si es asi 
# usamos el update para actualizar, el diccionario ahora con clave y los campos de nuevo sustituyendo el campo ddel
# nombre por la variable que pregunta el nombre nuevo, el  print nos muestra el cambio ya hecho.                        

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
                    
# En la siguiente opción, usamos un while True , usamos una variable la cual pregunte la clave 
# usamos el if para que no se omita nada, después usamos el else para continuar el programa, usamos el print para 
# mostrar el texto de Nombre Turno Fecha, usamos otro print para mostrar el diccionario, y solo la clave que se menciono
# en la variable que pregunta.

def accion3():
    while True:
        Selecciona=int(input("Ingresa la clave "))
        if Selecciona =="":
            break
        else:
            print("Nombre/Turno/Fecha")
            print(Reserva.get(Selecciona))
# En la Siguiente, usamos un while True , creamos una variable que pregunte el usuario nuevo , usamos el if 
# para que no se omitan,  si se omite rompemos el ciclo con break , si no se omite continuamos con el else
# creamos una nueva variable la cual use max para el valor máximo , que convierta a lista , el diccionario
# y se le asigne una clave por default y que se guarden en el diccionario, desempaquetamos toda con un unpacking
# y mostramos la clave y el usuario, pero ya todo se a guardado en el diccionario de Usuario.
            
def accion4():
    while True:
             Usuario=input("Ingresa un usuario: " )
             if Usuario=="":
                 break
             else:
                  Tercera_llave=max(list(Usuarios.keys()),default=0) + 1
                  Usuarios[Tercera_llave] = (Usuario) 
             for clave,datos in list(Usuarios.items()):
                 print(f"Tu clave de usuario es:   {clave}   Tu usuario es:   {datos}")
# En la siguiente, usamos el while True, creamos una variable que pregunte el nombre de la sala, usamos el if 
# para que no se omitan, si se omite rompemos con un break, usamos el else para continuar, en la siguiente 
# variable preguntamos la capacidad que solo se acepten datos enteros, en la segunda línea , es el valor máximo
# se convierte en lista y se agrega clave por default, luego desempacamos todo un unpackign y que se muestre los datos
# en una tabla.

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

# En la siguiente, usamos el for para desempaquetar el diccionario, por la clave y los datos en el , los estilizamos
# al final solo muestra el mensaje de finalización y un comando de voz, que reproduzca el audio

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