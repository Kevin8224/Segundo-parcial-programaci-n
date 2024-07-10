#Se importan las librerias para usar funciones específicas de pygame y json para guardar los datos del usuario
import pygame
import json 
import sys #Se importa la libreria sys para cerrar correctamente todas las ventanas, sin importar que esté en un bucle.

def crear_boton(pantalla: pygame.Surface, rect: pygame.Rect, color_btn: tuple, texto: list):
    """
        Dibuja un botón en pantalla con el texto especificado y con el rectángulo 
        ingresado por parámetros.
        
        pantalla: El display donde se dibujará el rectángulo
        rect: El rectángulo con las dimensiones y ubicación del botón
        color_btn: Tupla que almacena el color del botón que será dibujado
        texto: Lista con el texto del botón y su ubicación
    """
    pygame.draw.rect(pantalla, color_btn, rect, border_radius = 20) #Se dibuja el rectángulo
    pantalla.blit(texto[0], texto[1]) #Se blitea el texto


def crear_volver_atras(pantalla: pygame.Surface, color_btn: tuple) -> pygame.Rect:    
    """
        Se crea y dibuja un botón para volver a la ventana anterior.
        Se retorna el rectángulo para ser usado en la detección de eventos.
        
        pantalla: El display donde se dibujará el botón 
        color_btn: Tupla con el color de fondo que tendrá el botón.
    """
    rect_salir = pygame.Rect(40, 40, 55, 60)
    pygame.draw.rect(pantalla, color_btn, rect_salir, border_radius = 15)
    
    path = "Programación I/Segundo_parcial/preguntados/assets/logo_home.png"
    logo_home = pygame.transform.scale(pygame.image.load(path), (45, 44))
    pantalla.blit(logo_home, (44, 46))
    
    return rect_salir


def crear_boton_sonido(pantalla: pygame.Surface, color_btn: tuple, muteado: bool) -> pygame.Rect:
    """
        Se crea un botón para mutear o desmutear el sonido del juego.
        Si el sonido del juego está o no muteado, la imagen del botón lo muestra.
        Se retorna el rectánculo para ser usado en la detección de eventos.
        
        pantalla: El display donde se dibujará el botón
        color_btn: Tupla con el color de fondo que tendrá el botón
        muteado: Indica si el botón está o no muteado.
    """
    rect_sonido = pygame.Rect(1200, 40, 60, 60)
    pygame.draw.rect(pantalla, color_btn, rect_sonido, border_radius = 4)
    
    if muteado == False:
        path = "Programación I/Segundo_parcial/preguntados/assets/logo_sonido.png"
    else: 
        path = "Programación I/Segundo_parcial/preguntados/assets/logo_muteado.png"
    
    logo_sonido = pygame.transform.scale(pygame.image.load(path), (45, 43))
    pantalla.blit(logo_sonido, (1206, 46))
    
    return rect_sonido


def manejar_musica(musica: pygame.mixer.Sound, mutear: bool):
    """
        Controla si se reproduce o no la música en el juego, permitiendo mutear o desmutear.
        Si mutear es True, la música se detiene, de lo contrario si mutear es False, la música se reproduce.
    
        musica: El sonido que se está reproduciendo
        mutear: Indica si la debe ser muteada o no.
    """
    if mutear == True:
        musica.stop()
    else:
        musica.play(loops=-1)


def mostrar_inicio(pantalla: pygame.Surface, sonidos: list, fondo: pygame.image.load, fuente: pygame.font.Font, color_btn: tuple, color_txt: tuple, estado_mute: bool) -> str:
    """
        Crea, muestra la ventana de inicio y maneja las interacciones hechas por el jugador.
        Retorna el botón presionado que indica la ventana a la que ingresará el usuario luego de presionar uno de los botones.
        
        pantalla: El display donde se dibujará la pantalla de inicio.
        sonidos: Lista de los sonidos que serán usados en los eventos. 
        fondo: La imagen de fondo de la pantalla de inicio 
        fuente (pygame.font.Font): La fuente utilizada para renderizar el texto en los botones.
        color_btn : Tupla con el color de fondo para los botones
        color_txt : Tupla con el color del texto en los botones
        estado_mute: Indica si la música está muteada o no
    """
    activo = True
    presiono = None
    
    while activo: 
        pantalla.blit(fondo, (0, 0))
        
        rect_jugar = pygame.Rect(490, 150, 290, 70)
        rect_ver_puntaje = pygame.Rect(490, 260, 290, 70)
        rect_salir = pygame.Rect(490, 370, 290, 70)

        texto_jugar = fuente.render("Jugar", True, color_txt)
        texto_ver_puntaje = fuente.render("Ver puntaje", True, color_txt)
        texto_salir = fuente.render("Salir", True, color_txt)

        crear_boton(pantalla, rect_jugar, color_btn, [texto_jugar, (590, 165)])
        crear_boton(pantalla, rect_ver_puntaje, color_btn, [texto_ver_puntaje, (550, 275)])
        crear_boton(pantalla, rect_salir, color_btn, [texto_salir, (597, 385)])
        
        rect_boton_sonido = crear_boton_sonido(pantalla, color_btn, estado_mute)
        
        ##################### Eventos #####################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_jugar.collidepoint(event.pos):
                    sonidos[1].play()
                    presiono = "jugando"
                    activo = False
                    
                if rect_ver_puntaje.collidepoint(event.pos):
                    sonidos[1].play()
                    presiono = "puntaje"
                    activo = False
                    
                if rect_salir.collidepoint(event.pos):
                    sonidos[1].play()
                    presiono = "salir"
                    activo = False

                if rect_boton_sonido.collidepoint(event.pos):
                    sonidos[1].play()
                    if estado_mute == False:
                        estado_mute = True
                        manejar_musica(sonidos[0], estado_mute)
                    else:
                        estado_mute = False
                        manejar_musica(sonidos[0], estado_mute)
        ###################################################
        pygame.display.flip()
    
    return presiono


def mostrar_pantalla_juego(pantalla: pygame.Surface, sonidos: list, fondo: pygame.image.load, fuente: pygame.font.Font, fuente_titulo: pygame.font.Font, color_btn: tuple, color_txt: tuple, preguntas: list, estado_mute: bool):    
    """
        Muestra la pantalla de juego, muestra las preguntas, verifica las respuestas y maneja la interacción del usuario con los eventos.
        
        pantalla: El display donde se dibujará la pantalla de juego
        sonidos: Lista de sonidos que serán usados en los eventos como efectos
        fondo: La imagen de fondo para la pantalla de juego
        fuente: La fuente utilizada para renderizar el texto en los botones y preguntas
        fuente_titulo: La fuente utilizada para renderizar el texto del título
        color_btn: Tupla con el color de fondo para los botones
        color_txt: Tupla con el color del texto en los botones y preguntas
        preguntas: Lista con las preguntas y respuestas del juego
        estado_mute: Indica si la música está muteada o no
    """

    activo = True
    preguntando = False
    numero_pregunta = 0
    guardar_puntaje = False
    acierto = False
    mostrar_pregunta = True
    mostrar_boton_a = True
    mostrar_boton_b = True
    mostrar_boton_c = True
    
    puntaje = 0
    intentos = 2
    while activo:
        #Se crea la GUI inicial
        pantalla.blit(fondo, (0, 0))

        rect_preguntar = pygame.Rect(120, 50, 240, 60)
        rect_reiniciar = pygame.Rect(900, 50, 240, 60)

        texto_preguntar = fuente.render("Preguntar", True, color_txt)
        texto_reiniciar = fuente.render("Reiniciar", True, color_txt)

        crear_boton(pantalla, rect_preguntar, color_btn, [texto_preguntar, (160, 60)])
        crear_boton(pantalla, rect_reiniciar, color_btn, [texto_reiniciar, (945, 60)])    
        rect_respuesta_a = pygame.Rect(80, 400, 520, 70)
        rect_respuesta_b = pygame.Rect(680, 400, 520, 70)
        rect_respuesta_c = pygame.Rect(390, 540, 520, 70)
        
        pregunta = fuente.render(f"", True, color_txt)
        texto_respuesta_a = fuente.render(f"", True, color_txt)
        texto_respuesta_b = fuente.render(f"", True, color_txt)
        texto_respuesta_c = fuente.render(f"", True, color_txt)
        
        texto_game_over = fuente_titulo.render("GAME OVER", True, color_btn)

        salir = crear_volver_atras(pantalla, color_btn)
        rect_boton_sonido = crear_boton_sonido(pantalla, color_btn, estado_mute)
        ##################### Eventos #####################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if salir.collidepoint(event.pos):
                    sonidos[1].play()
                    activo = False
                    
                if rect_preguntar.collidepoint(event.pos):
                    if intentos > 0:
                        sonidos[1].play()
                        if preguntando == False:                          
                            puntaje = 0
                            intentos = 2
                            preguntando = True
                        elif preguntando == True and numero_pregunta < len(preguntas) - 1:
                            acierto = False
                            mostrar_boton_a = True
                            mostrar_boton_b = True
                            mostrar_boton_c = True  
                            numero_pregunta += 1
                            intentos = 2

                if rect_reiniciar.collidepoint(event.pos):
                    if preguntando == True:
                        sonidos[1].play()
                        acierto = False
                        mostrar_boton_a = True
                        mostrar_boton_b = True
                        mostrar_boton_c = True
                        puntaje = 0 
                        intentos = 2
                        numero_pregunta = 0            

                if rect_respuesta_a.collidepoint(event.pos):
                    if mostrar_boton_a == True and intentos > 0 and acierto == False:
                        if preguntas[numero_pregunta]["correcta"] == "a":
                            if numero_pregunta == len(preguntas)-1:
                                guardar_puntaje = True
                            sonidos[2].play()
                            acierto = True
                            puntaje += 10
                            texto_puntaje = fuente.render(f"Puntaje: {puntaje:03d}", True, color_txt)
                            mostrar_boton_b = False
                            mostrar_boton_c = False
                        else: 
                            sonidos[3].play()
                            intentos -= 1
                            mostrar_boton_a = False

                if rect_respuesta_b.collidepoint(event.pos):
                    if mostrar_boton_b == True and intentos > 0 and acierto == False:
                        if preguntas[numero_pregunta]["correcta"] == "b":
                            if numero_pregunta == len(preguntas)-1:
                                guardar_puntaje = True
                            sonidos[2].play()
                            acierto = True
                            puntaje += 10
                            texto_puntaje = fuente.render(f"Puntaje: {puntaje:03d}", True, color_txt)
                            mostrar_boton_a = False
                            mostrar_boton_c = False
                        else:                             
                            sonidos[3].play()
                            intentos -= 1
                            mostrar_boton_b = False

                if rect_respuesta_c.collidepoint(event.pos):
                    if mostrar_boton_c == True and intentos > 0 and acierto == False:
                        if preguntas[numero_pregunta]["correcta"] == "c":
                            if numero_pregunta == len(preguntas)-1:
                                guardar_puntaje = True
                            sonidos[2].play()
                            acierto = True
                            puntaje += 10
                            texto_puntaje = fuente.render(f"Puntaje: {puntaje:03d}", True, color_txt)
                            mostrar_boton_a = False
                            mostrar_boton_b = False
                        else: 
                            sonidos[3].play()
                            intentos -= 1
                            mostrar_boton_c = False
                
                if rect_boton_sonido.collidepoint(event.pos):
                    sonidos[1].play()
                    if estado_mute == False:
                        estado_mute = True
                        manejar_musica(sonidos[0], estado_mute)
                    else:
                        estado_mute = False
                        manejar_musica(sonidos[0], estado_mute)
        ###################################################

        if preguntando == True:
            texto_puntaje = fuente.render(f"Puntaje: {puntaje:03d}", True, color_txt)
            texto_intentos = fuente.render(f"Intentos: {intentos}", True, color_txt)
            pantalla.blit(texto_puntaje, (395, 60))
            pantalla.blit(texto_intentos, (680, 58))

            pregunta = fuente.render(f"{preguntas[numero_pregunta]['pregunta']}", True, color_txt)
            texto_respuesta_a = fuente.render(f"A. {preguntas[numero_pregunta]['a']}", True, color_txt)
            texto_respuesta_b = fuente.render(f"B. {preguntas[numero_pregunta]['b']}", True, color_txt)
            texto_respuesta_c = fuente.render(f"C. {preguntas[numero_pregunta]['c']}", True, color_txt)
            
            
            if mostrar_pregunta == True:
                pantalla.blit(pregunta, (200, 200))                        
            if mostrar_boton_a == True:
                crear_boton(pantalla, rect_respuesta_a, color_btn, [texto_respuesta_a, (90, 410)])
            if mostrar_boton_b == True:
                crear_boton(pantalla, rect_respuesta_b, color_btn, [texto_respuesta_b, (690, 410)])
            if mostrar_boton_c == True:
                crear_boton(pantalla, rect_respuesta_c, color_btn, [texto_respuesta_c, (400, 550)])
        
        if intentos == 0:
            pantalla.blit(texto_game_over, (395, 275))
            mostrar_pregunta = False
            mostrar_boton_a = False
            mostrar_boton_b = False
            mostrar_boton_c = False
            
        if guardar_puntaje == True:
            #Se pide el ingreso del nombre y se guarda el puntaje y nombre del jugador
            pedir_puntaje(pantalla, sonidos, puntaje, fuente, color_btn, color_txt)
            activo = False #Finaliza el juego
            
        pygame.display.flip()


def pedir_puntaje(pantalla: pygame.Surface, sonidos: list, puntaje: int, fuente: pygame.font.Font, color_btn: tuple, color_txt: tuple):
    """
        Muestra un campo de texto para ingresar el nombre del jugador y guardar el puntaje cuando se aprete enviar.
        La función guardar_puntaje() es utilizada y se guarda en un json el nombre y el puntaje del jugador.
        
        pantalla: El display donde se dibujará la pantalla de ingreso de puntaje
        sonidos: Lista de sonidos que serán usados en los eventos como efectos
        puntaje: El puntaje del jugador que será guardado en un json
        fuente: La fuente utilizada para renderizar el texto
        color_btn: Tupla con el color de fondo para los botones
        color_txt: Tupla con el color del texto
    """
    jugador = None
    nombre_usuario = ""
    activo = True

    while activo:  
        rect_guardar_puntaje = pygame.Rect(270, 270, 700, 100)
        pygame.draw.rect(pantalla, color_btn, rect_guardar_puntaje, border_radius = 2)

        rect_enviar = pygame.Rect(815, 285, 125, 70)
        text_enviar = fuente.render("Enviar", True, color_txt)

        crear_boton(pantalla, rect_enviar, (242, 42, 31), [text_enviar, (826, 300)])
        
        nombre = fuente.render(nombre_usuario, True, color_txt)
        pantalla.blit(nombre, (290,300))
        ##################### Eventos #####################
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_enviar.collidepoint(event.pos):
                    if len(nombre_usuario) > 2:
                        sonidos[1].play()
                        jugador = {"nombre": nombre_usuario, "puntaje": puntaje}
                        
                        activo = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:                    
                    nombre_usuario = nombre_usuario[0:-1]
                else:
                    if len(nombre_usuario) < 11:
                        nombre_usuario += event.unicode
        ###################################################

        pygame.display.flip()

    guardar_puntaje(jugador)


def mostrar_puntajes(pantalla: pygame.Surface, sonidos: list, fondo: pygame.image.load, fuente_normal: pygame.font.Font, fuente_semi_titulo: pygame.font.Font, color_btn: tuple, color_txt: tuple, estado_mute: bool):
    """
        Crea y muestra la pantalla puntajes.
        Se verifica si hay o no jugadores en puntajes.json. Si hay muestra los 3 mejores, si no hay muestra un
        mensaje especificandolo.
        
        pantalla: El display donde se dibujará la pantalla de puntajes.
        sonidos: Lista de sonidos que serán usados en los eventos como efectos
        fondo: La imagen de fondo a usar en la pantalla de puntajes
        fuente_normal: La fuente utilizada para renderizar el texto normal
        fuente_semi_titulo: La fuente utilizada para renderizar un sub titulo
        color_btn: Tupla con el color de fondo para los botones
        color_txt: Tupla con el color del texto
        estado_mute: Estado actual del sonido, True si está muteado, False si no lo está
    """
    activo = True
    lista = cargar_puntajes()
    
    while activo: 
        pantalla.blit(fondo, (0, 0))

        salir = crear_volver_atras(pantalla, color_btn)
        rect_boton_sonido = crear_boton_sonido(pantalla, color_btn, estado_mute)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if salir.collidepoint(event.pos):
                    sonidos[1].play()
                    activo = False
                    
                if rect_boton_sonido.collidepoint(event.pos):
                    sonidos[1].play()
                    if estado_mute == False:
                        estado_mute = True
                        manejar_musica(sonidos[0], estado_mute)
                    else:
                        estado_mute = False
                        manejar_musica(sonidos[0], estado_mute)

        if len(lista) > 0:
            lista.sort(key = lambda jugador: jugador["puntaje"], reverse = True)
            mejores_jugadores = lista[:3]
            
            texto_titulo = fuente_semi_titulo.render("Tabla de clasificaciones", True, color_txt)
            pantalla.blit(texto_titulo, (318, 100))
            
            jugadores_eje_y = 220

            for jugador in mejores_jugadores:
                texto_puntajes = fuente_normal.render(f"Nombre: {jugador["nombre"]} -  Puntaje: {jugador["puntaje"]}", True, color_txt)
                pantalla.blit(texto_puntajes, (395, jugadores_eje_y))
                jugadores_eje_y += 50
        else: 
            texto_sin_puntajes = fuente_semi_titulo.render("No hay puntajes", True, color_txt)
            pantalla.blit(texto_sin_puntajes, (415, 280))

        pygame.display.flip()


def guardar_puntaje(puntaje: dict):
    """
        Guarda un nuevo puntaje en el archivo puntajes.json
        primero carga los puntajes, recibe por parámetro el nuevo puntaje y lo agrega a una
        nueva lista la cual es guardada en el archivo.
        
        puntaje: Un diccionario que contiene el nombre del jugador y su puntaje.
    """
    lista_puntajes = cargar_puntajes()
    lista_puntajes.append(puntaje)
    
    with open("Programación I/Segundo_parcial/preguntados/puntajes.json", "w") as puntajes:
        json.dump(lista_puntajes, puntajes, indent=4, ensure_ascii=False)


def cargar_puntajes() -> list:
    """
        Carga la lista de puntajes desde el archivo puntajes.json
        se guardan en una variable y se la retorna.
    """
    with open("Programación I/Segundo_parcial/preguntados/puntajes.json", "r") as archivo:
        datos = json.load(archivo)
    return datos