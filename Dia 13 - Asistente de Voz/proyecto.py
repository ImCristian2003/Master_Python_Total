import pyttsx3#librería para hablar con python (pip)
import speech_recognition as sr#reconocimiento de voz (pip). Se debe installar PyAudio también para que funcione
import pywhatkit#permitir al asistente conectarse a sitios como youtube y demás (pip)
import yfinance as yf#conexión a la bolsa de valores (pip)
import pyjokes#"bromas" (pip)
import webbrowser#manejar el navegador de internet
import datetime
import wikipedia#librería para consulta

#ver las voces disponibles
# e = pyttsx3.init()

# for voz in e.getProperty('voices'):
#     print(voz)
v1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
v2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#escuchar el micrófono y devolver el audio como texto
def transformar_audio_a_texto():

    #Almacenar el recognizer en variable
    r = sr.Recognizer()

    #configurar el micrófono
    with sr.Microphone() as origen:

        #tiempo de espera para escuchar
        r.pause_threshold = 0.8

        #informar que comenzó la grabación
        print("hable")

        #variable para guardar el audio escuchado
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language = 'es-co')

            #prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            #devolver a pedido
            return pedido
        
        #en caso de que no comprenda el audio
        except sr.UnknownValueError:
            #prueba de que no comprendió el audio
            print("Ups! No entendí")
            #devolver error
            return "Sigo esperando"
        
        #en caso de no resolver el pedido
        except sr.RequestError:
            #prueba de que no comprendió el audio
            print("Ups! No hay servicio")
            #devolver error
            return "Sigo esperando"
        
        #error inesperado
        except sr.RequestError:
            #prueba de que no comprendió el audio
            print("Ups! Algo salió mal")
            #devolver error
            return "Sigo esperando"
        

#función para que el asistente sea escuchado
def hablar(mensaje):

    #encender el motor de pyttsx3
    engine = pyttsx3.init()#inicializar
    engine.setProperty('voice', v1)#setear la propiedad voz

    #pronunciar mensaje
    engine.say(mensaje)#pronunciar el mensaje
    engine.runAndWait()#correr el mensaje


#informa el día de la semana
def pedir_dia():

    #crear variable con datos de hoy
    hoy = datetime.date.today()
    #print(hoy)

    #crear variable para el día de la semana
    dia_semana = hoy.weekday()
    
    #diccionario con el nombre de los días
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    #print(calendario[dia_semana])
    #decir el día de la semana

    hablar(f'Hoy es {calendario[dia_semana]}')


#informar la hora actual
def pedir_hora():

    #crear variable con los datos actuales
    hora = datetime.datetime.now()
    hora = f'En este momentos son las, {hora.hour} con {hora.minute} minutos y {hora.second} segundos'

    #decir la hora
    hablar(hora)


#función saludo inicial
def saludo_inicial():

    #decir el saludo
    hablar('Oe, soy Jacinto. Qué necesita parcero')


#función central del asistente
def pedir_cosas():

    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop
    while comenzar:

        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_a_texto().lower()

        #abrir youtube
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo YouTube')
            webbrowser.open("https://www.youtube.com")
            continue

        elif 'abrir navegador' in pedido:
            hablar('Con gusto, estoy abriendo el navegador')
            webbrowser.open("https://www.google.com")
            continue

        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue

        elif 'qué hora es' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')#reemplazar wikipedia por vacío para la búsqueda
            wikipedia.set_lang('es')#dar a entender que busque en Español
            resultado = wikipedia.summary(pedido, sentences = 1)#buscar el pedido y me traiga solo el primer párrafo
            continue

        elif 'busca en internet' in pedido:
            hablar('Buscando en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)#buscar en internet
            hablar('Esto encontré')
            continue

        elif 'reproducir' in pedido:
            hablar('Reproduciendo')
            pywhatkit.playonyt(pedido)#reproducir en internet
            continue

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip() #tratar de encontrar la acción
            #crear diccionario con las acciones
            cartera = {
                'apple': 'APPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precion_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precion de {accion} es {precion_actual}')
                continue

            except:
                hablar("No la encontré")
                continue
        
        elif 'adiós' in pedido:
            hablar("Suerte socio")
            break


saludo_inicial()