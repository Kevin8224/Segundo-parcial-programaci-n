import pygame

pygame.init()

fuente = pygame.font.Font("Programación I/Segundo_parcial/preguntados/assets/Roboto-Regular.ttf", 36)
fuente_semi_titulo = pygame.font.Font("Programación I/Segundo_parcial/preguntados/assets/Roboto-Regular.ttf", 60)
fuente_titulo = pygame.font.Font("Programación I/Segundo_parcial/preguntados/assets/Roboto-Regular.ttf", 85)

musica_inicio = pygame.mixer.Sound("Programación I/Segundo_parcial/preguntados/assets/musica_inicio.mp3")
musica_jugando = pygame.mixer.Sound("Programación I/Segundo_parcial/preguntados/assets/musica_jugando.mp3")
musica_puntaje = pygame.mixer.Sound("Programación I/Segundo_parcial/preguntados/assets/musica_puntaje.mp3")

sonido_resp_correcta = pygame.mixer.Sound("Programación I/Segundo_parcial/preguntados/assets/respuesta_correcta.wav")
sonido_de_click = pygame.mixer.Sound("Programación I/Segundo_parcial/preguntados/assets/sonido_de_click.wav")
sonido_resp_incorrecta = pygame.mixer.Sound("Programación I/Segundo_parcial/preguntados/assets/sonido_incorrecta.mp3")
