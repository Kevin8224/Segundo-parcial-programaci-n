# Nombre: Kevin
# Apellido: Villalba
# Division: 212-1
# Asignatura: Programación 1
# Instancia: Recuperatorio segundo parcial


# Se importa pygame y todos los datos necesarios para crear el juego
import pygame
from datos import lista as preguntas
from funciones import *
from assets.recursos import *


pygame.init() #Se inicia pygame
pygame.mixer.init() #Se inicia la ejecución de sonidos

ancho_pantalla = 1289 #Se establece el ancho de pantalla (X)
alto_pantalla = 700 #Se establece el alto de pantalla (Y)

pantalla = pygame.display.set_mode([ancho_pantalla, alto_pantalla]) #Se crea el display del juego

#Se establecen los fondos de juego
fondo_inicio = pygame.transform.scale(
                                        pygame.image.load("Programación I/Segundo_parcial/preguntados/assets/fondo_de_inicio.jpg"), 
                                        (ancho_pantalla, alto_pantalla)
                                        )
fondo_jugando = pygame.transform.scale(
                                        pygame.image.load("Programación I/Segundo_parcial/preguntados/assets/fondo_jugando.jpg"), 
                                        (ancho_pantalla, alto_pantalla)
                                        )

#Guardo en listas los sonidos usados en cada ventana
sonidos_ventana_inicio = [
    musica_inicio, 
    sonido_de_click
    ]

sonidos_ventana_jugando = [
    musica_jugando, 
    sonido_de_click, 
    sonido_resp_correcta, 
    sonido_resp_incorrecta
    ]

sonidos_ventana_puntaje = [
    musica_puntaje, 
    sonido_de_click
]

#Guardo la paleta de colores usada en botones y textos
color_principal = (245, 98, 49)
color_secundario = (255, 255, 255)

juego_en_curso = True #Bandera de arranque
ventana = "inicio" #Variable que controla qué ventana se muestra
mute = False  #Bandera para controlar si se silencia o no el juego

while juego_en_curso: #Se inicia el juego
    if ventana == "inicio": #Se ejecuta la ventana de inicio
        if mute == False: #Se verifica si la música del juego está silenciada o no, en caso de que no, se reproduce.
            musica_inicio.play(loops=-1)
        
        #Se muestra la ventana de inicio y se toma el botón presionado, en la función se pasan por parámetros todos los assets (Sonidos, 
        #fondo, colores y font).
        boton_presionado = mostrar_inicio(pantalla, sonidos_ventana_inicio, fondo_inicio, fuente, color_principal, color_secundario, mute)
        
        if boton_presionado == "salir": #Se verifica si el botón presionado es salir
            juego_en_curso = False
        else: #De lo contrario se toma el botón y se muestra la ventana elegida
            ventana = boton_presionado
            musica_inicio.stop() #Se detiene la música de la ventana inicio

    if ventana == "jugando": #Se ejecuta la ventana de juego
        if mute == False:
            musica_jugando.play(loops=-1)
        
        #Se muestra la ventana de juego, se pasan por parámetros todos los assets y solo si el jugador "gana" 
        #se guarda en un json el nombre del jugador (a partir de un campo de texto) y el puntaje
        mostrar_pantalla_juego(pantalla, sonidos_ventana_jugando, fondo_jugando, fuente, fuente_titulo, color_principal, color_secundario, preguntas, mute)
        
        #En caso de que el bucle de la ventana juego sea terminado por algún botón o por la misma carga de datos se muestra la ventana de inicio
        ventana = "inicio" 
        musica_jugando.stop() #Se detiene la música de la ventana jugando

    if ventana == "puntaje": #Se ejecuta la ventana de puntajes
        if mute == False:
            musica_puntaje.play(loops=-1)

        #Se muestra la ventana de puntajes, se pasan por parámetros todos los assets y si no hay puntajes guardados en el archivo puntajes.json
        #no se muestra nada, de lo contrario solo se muestran los nombres y puntajes de los tres mejores. 
        mostrar_puntajes(pantalla, sonidos_ventana_puntaje, fondo_inicio, fuente, fuente_semi_titulo, color_principal, color_secundario, mute)
        
        ventana = "inicio" #En caso de que finalice el bucle de la ventana puntajes, se muestra la ventana de inicio
        musica_puntaje.stop() #Se detiene la música de la ventana puntajes

    pygame.display.flip()

pygame.quit()