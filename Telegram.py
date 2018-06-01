#Se importan las librerias necesarias para la ejecuci�n correcta del bot
import sys
import time
import random
import datetime
import telepot
import os
#Se declaran las variables globales que se van a ocupar durante el transcurso del proggrama
usuario = 'Prueba'
numusuario = '0'
contra = '*****'
numcontra = '0'
intentos = 3
#Se coloca la informaci�n necesaria para que el bot corra en telegram
bot = telepot.Bot('') #Se coloca el id del bot en los espacios entre los corchetes que te genera el BotFather de esa plataforma
print 'Estoy escuchando...' #Imprime en la pantalla de la Raspberry

def handle(msg): #Definici�n del m�dulo principal que se ejecuta dentro del bot

    chat_id = msg['chat']['id'] #Se coloca en la variable los datos necesarios para que se envien los mensajes
    command = msg['text'] #Variable que obtiene el texto que coloco el individuo en el bot

    print 'Got command: %s' % command #Imprime en la pantalla de la raspberry el texto que el usuario coloco

    if "/start" == command: #Se condiciona el texto que ingreso el usuario, entra si se coloca el comando /start
        #Env�o al bot del texto con los comandos que se observan a continuaci�n.
        bot.sendMessage(chat_id, "Hola, \n Mi nombre es @Sistemas_Raspberry_bot.")
        bot.sendMessage(chat_id, "Fui hecho por un equipo de la materia de Taller de Sistemas Operativos de la carrera de Ingenieria en Sistemas Computacionales para el uso en la domotica apoyandome de una RASPBERRY como servidor\n"
         + "Para poder saber los privilegios que tienes dentro del hogar te realizare dos cuestionamientos.")
        bot.sendMessage(chat_id, "Cual es tu nombre")

    elif 'Micho' in command: #Entra si coloca el nombre del usuario definido en el sistema de la raspberry
        #Se menciona que las variables que se van a usar son las globales, para que no se pierdan en el ciclo del bot
        global usuario
        global numusuario

        if '0' in numusuario: #Entra si ingresa por primera vez con ese usuario, pidiendo la contrase�a
            usuario='Micho'
            numusuario = '1'
            bot.sendMessage(chat_id, "Introduce la contrasena:")

    elif 'Micho' in usuario: #Entra si en la variable global se encuentra el nombre de usuarios

        if '123' in command: #Entra si coloca de forma correcta la contrae�a del usuario
            if '0' in numcontra:
                #Se menciona que las variables que se van a usar son las globales, para que no se pierdan en el ciclo del bot
                global contra
                global numcontra
                # Declaraci�n de variables a utilizar
                contra = command
                numcontra = '1'
                #Texto que se imprime en el chat de Telegram
                bot.sendMessage(chat_id, "Bienvenido de vuelta a tu sistema domotico, Mario Josue del Toro Morales")
                bot.sendMessage(chat_id, "Las acciones que puedes realizar dentro de este sistema se enlistan a continuacion:\n"
                            +"/EncenderTelevision" + " - Enciende la television de tu cuarto\n"
                            +"/EncenderLuz" + " - Enciende la luz de la sala principal\n"
                            +"/EncenderAire" + " - Enciende el aire acondicionado de la casa\n"
                            +"/AbrirCochera" + " - Abre la cochera de la casa\n"
                            +"/ApagarTelevision" + " - Apaga la television de tu cuarto\n"
                            +"/ApagarLuz" + " - Apaga la luz de la sala principal\n"
                            +"/ApagarAire" + " - Apaga el aire acondicionado de la casa\n"
                            +"/CerrarCochera" + " - Cierra la cochera de la casa\n"
                            +"/CerrarSesion" + " - Cierra la sesion actual")

        elif '123'in contra: #Entra si en la variable global est� la contrase�a correcta

            bot.sendMessage(chat_id, "Bienvenido de vuelta a tu sistema domotico, Mario Josue del Toro Morales")
            bot.sendMessage(chat_id, "Las acciones que puedes realizar dentro de este sistema se enlistan a continuacion:\n"
                            +"/EncenderTelevision" + " - Enciende la television de tu cuarto\n"
                            +"/EncenderLuz" + " - Enciende la luz de la sala principal\n"
                            +"/EncenderAire" + " - Enciende el aire acondicionado de la casa\n"
                            +"/AbrirCochera" + " - Abre la cochera de la casa\n"
                            +"/ApagarTelevision" + " - Apaga la television de tu cuarto\n"
                            +"/ApagarLuz" + " - Apaga la luz de la sala principal\n"
                            +"/ApagarAire" + " - Apaga el aire acondicionado de la casa\n"
                            +"/CerrarCochera" + " - Cierra la cochera de la casa\n"
                            +"/CerrarSesion" + " - Cierra la sesion actual")
            #Ejecuci�n de los comandos que hacen que se prenda los leds, seg�n el comando que el usuario coloque
            if "EncenderTelevision" in command:
                os.system('python encendertelevision.py')
            elif "EncenderLuz" in command:
                os.system('python encenderluz.py')
            elif "EncenderAire" in command:
                os.system('python encenderaire.py')
            elif "AbrirCochera" in command:
                os.system('python abrircochera.py')
            elif "ApagarTelevision" in command:
                os.system('python apagartelevision.py')
            elif "ApagarLuz" in command:
                os.system('python apagarluz.py')
            elif "ApagarAire" in command:
                os.system('python apagaraire.py')
            elif "CerrarCochera" in command:
                os.system('python cerrarcochera.py')
            elif "CerrarSesion" in command: #Comando que sirve para cerrar sesi�n
                global usuario
                global numusuario
                global contra
                global numcontra
                global intentos
                #Se inicializan las variables globales para que se reinicie el proceso
                usuario = 'Prueba'
                numusuario = '0'
                contra = '*****'
                numcontra = '0'
                intentos = 3
                #Se apagan los aparatos que tenia prendidos en el sistema
                os.system('python apagartelevision.py')
                os.system('python apagarluz.py')
                os.system('python apagaraire.py')
                os.system('python cerrarcochera.py')

                bot.sendMessage(chat_id, "Sesion cerrada de forma exitosa")
            else: #Entra si el comando ingresado no se ubica entre los comandos establecidos
                bot.sendMessage(chat_id, "Comando no encontrado")

        else: #Entra si coloca de forma incorrecta la contrase�a
            global intentos #Declaraci�n de la variable global a usar
            intentos -= 1 #Inicializaci�n de la variable que cuente los intentos
            bot.sendMessage(chat_id,"La contrasena que introdujo es incorrecta")
            mensaje = "Favor de volver a ingresar la contrasena\nTe quedan "+ str(intentos) + " intentos"
            bot.sendMessage(chat_id, mensaje)

            if intentos == 0: #Entra si se llega a 0 intentos permitidos de contrase�a erronea
                #Declaraci�n de las variables globales a usar
                global usuario
                global numusuario
                global contra
                global numcontra
                global intentos

                bot.sendMessage (chat_id, "Acaba de llegar al limite de contrasenas introducidas,\n El sistema lo sacara, para que reinicie el proceso")
                bot.sendMessage (chat_id, "Cual es tu nombre:")
                #Se inicializan las variables globales que sirven para cerrar sesi�n
                usuario = 'Prueba'
                numusuario = '0'
                contra = '*****'
                numcontra = '0'
                intentos = 3

    elif 'Didi' in command: #Entra si el usuario coloca el usuario que esta en el sistema de la RASPBERRY
        #Declaraci�n de las variables globales a usar
        global usuario
        global numusuario

        if '0' in numusuario: #Entra si es la primera vez que coloca el usuario
            usuario='Didi'
            numusuario = '1'
            bot.sendMessage(chat_id, "Introduce la contrasena:")

    elif 'Didi' in usuario: # Entra cuando coloca la contrae�a del usuario

        if '234' in command: #Entra si coloca la contrase�a correcta
            if '0' in numcontra: #Entra si es la primera vez que ingresa en este apartado
                global contra
                global numcontra

                contra = command
                numcontra = '1'
                 #Se despliegan las acciones que puede realizar el usuario
                bot.sendMessage(chat_id, "Bienvenido de vuelta a tu sistema domotico, Diego Aldahir Cortez Zamano")
                bot.sendMessage(chat_id, "Las acciones que puedes realizar dentro de este sistema se enlistan a continuacion:\n"
                            +"/EncenderTelevision" + " - Enciende la television de tu cuarto\n"
                            +"/AbrirCochera" + " - Abre la cochera de la casa\n"
                            +"/ApagarTelevision" + " - Apaga la television de tu cuarto\n"
                            +"/CerrarCochera" + " - Cierra la cochera de la casa\n"
                            +"/CerrarSesion" + " - Cierra la sesion actual")

        elif '234'in contra: #Entra al ciclo que mostrara las acciones que el usuario puede realizazr

            bot.sendMessage(chat_id, "Bienvenido de vuelta a tu sistema domotico, Diego Aldahir Cortez Zamano")
            bot.sendMessage(chat_id, "Las acciones que puedes realizar dentro de este sistema se enlistan a continuacion:\n"
                            +"/EncenderTelevision" + " - Enciende la television de tu cuarto\n"
                            +"/AbrirCochera" + " - Abre la cochera de la casa\n"
                            +"/ApagarTelevision" + " - Apaga la television de tu cuarto\n"
                            +"/CerrarCochera" + " - Cierra la cochera de la casa\n"
                            +"/CerrarSesion" + " - Cierra la sesion actual")
            #Checan los comandos que el usuario ingresa
            if "EncenderTelevision" in command:
                os.system('python encendertelevision.py')
            elif "AbrirCochera" in command:
                os.system('python abrircochera.py')
            elif "ApagarTelevision" in command:
                os.system('python apagartelevision.py')
            elif "CerrarCochera" in command:
                os.system('python cerrarcochera.py')
            elif "CerrarSesion" in command: #Entra para cerrar la sesi�n, cuando se ingresa el comando necesario
                global usuario
                global numusuario
                global contra
                global numcontra
                global intentos
                #Inicializaci�n de las variables globales, para que se cierre la sesi�n
                usuario = 'Prueba'
                numusuario = '0'
                contra = '*****'
                numcontra = '0'
                intentos = 3
                #apaga los aparatos que dejo prendido el usuario
                os.system('python apagartelevision.py')
                os.system('python cerrarcochera.py')

                bot.sendMessage(chat_id, "Sesion cerrada de forma exitosa")
            else: #Entra si el comando colocado no es encontrado
                bot.sendMessage(chat_id, "Comando no encontrado")

        else: #Entra si se coloca mal la contrase�a
            global intentos
            intentos -= 1
            bot.sendMessage(chat_id,"La contrasena que introdujo es incorrecta")
            mensaje = "Favor de volver a ingresar la contrasena\nTe quedan "+ str(intentos) + " intentos"
            bot.sendMessage(chat_id, mensaje)

            if intentos == 0: #Entra si se llega al l�mite de veces que se coloca la contrase�a de forma correcta
                global usuario
                global numusuario
                global contra
                global numcontra
                global intentos
                #Muestra el respectivo mensaje que indique la situaci�n de la sesi�n
                bot.sendMessage (chat_id, "Acaba de llegar al limite de contrasenas introducidas,\n El sistema lo sacara, para que reinicie el proceso")
                bot.sendMessage (chat_id, "Cual es tu nombre:")
                #Se inicializan las variables globales para cerrar la sesi�n
                usuario = 'Prueba'
                numusuario = '0'
                contra = '*****'
                numcontra = '0'
                intentos = 3

    elif 'JM' in command: #Entra si se coloca el usuario que se puso en la RASPBERRY
        #Declaraci�n de las variables globales a usar
        global usuario
        global numusuario

        if '0' in numusuario: #Entra si es la primera vez que ingresa el usario
            usuario='JM'
            numusuario = '1'
            bot.sendMessage(chat_id, "Introduce la contrasena:")

    elif 'JM' in usuario: # Entra cuando hace la vuelta al ciclo

        if '345' in command: #Entra si se coloca la contrase�a correcta de la RASPBERRY
            if '0' in numcontra: #Entra si es la primera vez que se ingresa con este usuario
                global contra
                global numcontra
                #Declaraci�n de las variables necesarias
                contra = command
                numcontra = '1'
                #Manda mensaje al bot
                bot.sendMessage(chat_id, "Bienvenido de vuelta a tu sistema domotico, Jose Miguel Galvan Perez")
                bot.sendMessage(chat_id, "Las acciones que puedes realizar dentro de este sistema se enlistan a continuacion:\n"
                            +"/EncenderLuz" + " - Enciende la luz de la sala principal\n"
                            +"/EncenderAire" + " - Enciende el aire acondicionado de la casa\n"
                            +"/ApagarLuz" + " - Apaga la luz de la sala principal\n"
                            +"/ApagarAire" + " - Apaga el aire acondicionado de la casa\n"
                            +"/CerrarSesion" + " - Cierra la sesion actual")

        elif '345'in contra: #Entra si se coloco la contrase�a y da la vuelta al ciclo
            #Env�o del mensaje al bot
            bot.sendMessage(chat_id, "Bienvenido de vuelta a tu sistema domotico, Jose Miguel Galvan Perez")
            bot.sendMessage(chat_id, "Las acciones que puedes realizar dentro de este sistema se enlistan a continuacion:\n"
                            +"/EncenderLuz" + " - Enciende la luz de la sala principal\n"
                            +"/EncenderAire" + " - Enciende el aire acondicionado de la casa\n"
                            +"/ApagarLuz" + " - Apaga la luz de la sala principal\n"
                            +"/ApagarAire" + " - Apaga el aire acondicionado de la casa\n"
                            +"/CerrarSesion" + " - Cierra la sesion actual")
            #Checa los comandos ingresados por el usuario en Telegram
            if "EncenderLuz" in command:
                os.system('python encenderluz.py')
            elif "EncenderAire" in command:
                os.system('python encenderaire.py')
            elif "ApagarLuz" in command:
                os.system('python apagarluz.py')
            elif "ApagarAire" in command:
                os.system('python apagaraire.py')
            elif "CerrarSesion" in command: #entra si se va a cerrar sesi�n
                global usuario
                global numusuario
                global contra
                global numcontra
                global intentos
                #Inicializa las variables globales para cerrar sesi�n
                usuario = 'Prueba'
                numusuario = '0'
                contra = '*****'
                numcontra = '0'
                intentos = 3
                #Apaga los dispositivos que el usuario tiene a su disposici�n.
                os.system('python apagarluz.py')
                os.system('python apagaraire.py')

                bot.sendMessage(chat_id, "Sesion cerrada de forma exitosa")
            else: #Entra si se coloca un comando que no se encuentra
                bot.sendMessage(chat_id, "Comando no encontrado")

        else: #Entra si se coloca una contrase�a erronea para el usuario JM
            global intentos
            intentos -= 1
            bot.sendMessage(chat_id,"La contrasena que introdujo es incorrecta")
            mensaje = "Favor de volver a ingresar la contrasena\nTe quedan "+ str(intentos) + " intentos"
            bot.sendMessage(chat_id, mensaje)

            if intentos == 0: #Entra si se llega a un l�mite de intentos de colocar la contrase�a para el usuario
                global usuario
                global numusuario
                global contra
                global numcontra
                global intentos
                #Muestra el mensaje en el bot de lo que esta pertinente.
                bot.sendMessage (chat_id, "Acaba de llegar al limite de contrasenas introducidas,\n El sistema lo sacara, para que reinicie el proceso")
                bot.sendMessage (chat_id, "Cual es tu nombre:")
                #Inicializan las variables globales para que se cierre la sesi�n
                usuario = 'Prueba'
                numusuario = '0'
                contra = '*****'
                numcontra = '0'
                intentos = 3

    else: #Entra si no se encuentra el usuario en el sistema
        bot.sendMessage(chat_id, "No se encontro a ese usuario en el sistema,\nFavor de volver a ingresar el nombre de usuario")

bot.message_loop(handle) #Manda a llamar al ciclo al inicializar el bot

while 1: #Ciclo que hace que se hiberne el bot tras el tiempo establecido en la condici�n de time
     time.sleep(10)