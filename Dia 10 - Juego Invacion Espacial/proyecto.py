import pygame#importar pygame
from pathlib import Path
import os
import random
import math
from pygame import mixer#trabajar con sonidos

#inicialiar todas las funciones de pygame
pygame.init()

#crear la pantalla en px
pantalla = pygame.display.set_mode((800, 600))

os.chdir(Path('C:/PUPy/Dia 10 - Juego Invacion Espacial'))

#configuración del título e ícono
pygame.display.set_caption("Invasión Espacial")#título
icono = pygame.image.load("resources/ovni.png")#cargar el ícono
pygame.display.set_icon(icono)#añadir el ícono a la ventana
fondo = pygame.image.load("resources/fondo.jpg")#cargar la imagen de pantalla

#agregar música
mixer.music.load('resources/MusicaFondo.mp3')#cargar sonido
mixer.music.set_volume(0.2)#organizar el volúmen de la música
mixer.music.play(-1)#repetir cada que termine

#crear jugador
img_jugador = pygame.image.load("resources/nave_espacial.png")#cargar la imagen del jugador
jugador_x = 368#asignar posición del jugador en el eje x
jugador_y = 500#asignar posición del jugador en el eje y
jugador_x_cambio = 0

#crear enemigo
#listas para crear varios enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

#ciclo para crear varios enemigos
for e in range(cantidad_enemigos):

    img_enemigo.append(pygame.image.load("resources/enemigo.png"))#cargar la imagen del enemigo
    enemigo_x.append(random.randint(0, 736))#asignar posición del enemigo en el eje x
    enemigo_y.append(random.randint(50, 200))#asignar posición del enemigo en el eje y
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(50)

#crear bala
#balas = []
img_bala = pygame.image.load("resources/bala.png")#cargar la imagen del bala
bala_x = 0#asignar posición del bala en el eje x
bala_y = 500#asignar posición del bala en el eje y
bala_x_cambio = 0
bala_y_cambio = 0.3
bala_visible = False

#puntaje
puntaje = 0
fuente = pygame.font.Font('resources/orange juice 2.0.ttf', 32)#fuente del puntaje
#coordenadas del puntaje
texto_x = 10
texto_y = 10

#texto final de juego
fuente_final = pygame.font.Font('resources/orange juice 2.0.ttf', 60)#fuente del Game Over

def texto_final():
    mi_fuente_final = fuente_final.render("Game Over Manito", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 200))


#función mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#funcionalidad del jugador
def jugador(x, y):
    pantalla.blit(img_jugador,(x, y))#función que pone al jugador en la pantalla


#funcionalidad del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene],(x, y))#función que pone al enemigo en la pantalla


#funcionalidad de la bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x + 16, y + 10))#función que pone al bala en la pantalla


#función calcular distancia (detercar colision)
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow((x_1 - x_2), 2) + math.pow((y_2 - y_1), 2))#formula para calcular la distancia
    if distancia < 27:
        return True
    else:
        return False


#variable para el while
se_ejecuta = True
while se_ejecuta:

    pantalla.blit(fondo, (0, 0))#fondo de la pantalla

    #iterar todos los eventos que ocurran para encontrar cuando se le da a la X (QUIT)
    for evento in pygame.event.get():
        #validar si encuentra QUIT() para cerrar el ciclo (mostrar pantalla)
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #validar si el jugador presiona una tecla
        if evento.type == pygame.KEYDOWN:
            #validar cuál tecla fue presionada
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3#mover hacia la izquierda

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3#mover hacia la derecha

            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('resources/disparo.mp3')
                sonido_bala.play()

                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)#hacer funcionar la bala cuando se presione espacio

        #validar si el jugador suelta una tecla
        if evento.type == pygame.KEYUP:
            #validar la tecla soltada
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0#detener el jugador cuando se suelte la tecla

    #asignar al eje x el cambio de posición
    jugador_x += jugador_x_cambio

    #mantener dentro de los border (límites)
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #asignar al eje x el cambio de posición
    for e in range(cantidad_enemigos):

        #validar si el enemigo alcanza la nave
        if enemigo_y[e] > 500:
            #ir a cada enemigo
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break


        enemigo_x[e] += enemigo_x_cambio[e]

        #mantener dentro de los border (límites)
        if enemigo_x[e] <= 5:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 731:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]

        #verificar colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        
        if colision:
            sonido_colision = mixer.Sound('resources/Golpe.mp3')
            sonido_colision.play()

            bala_y = 500
            bala_visible = False
            puntaje += 1

            enemigo_x[e] = random.randint(0, 736)#reiniciar posición del enemigo en el eje x cuando colisione
            enemigo_y[e] = random.randint(50, 200)#reiniciar posición del enemigo en el eje y cuando colisione

        enemigo(enemigo_x[e], enemigo_y[e], e)#función para ejecutar el enemigo
    
    #moviento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    jugador(jugador_x, jugador_y)#función para ejecutar el jugador
    mostrar_puntaje(texto_x, texto_y)#función para mostrar el puntaje
    

    pygame.display.update()#Cargar todo lo del juego/Actualizar