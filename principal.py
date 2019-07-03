import sys, pygame, util
from pygame.locals import *
from Pelota import *

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game():
      pygame.init()
      pygame.mixer.init()
      screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
      jugando = True
      pygame.display.set_caption( "Pelota" )
      background_image = util.cargar_imagen('imagenes/fondo.jpg');
      fuente = pygame.font.Font(None, 30)
      pygame.mouse.set_visible( False )
      temporizador = pygame.time.Clock()
      pelota = Pelota()      
      while jugando:
          pelota.update()
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()
          screen.blit(background_image, (0,0))
          screen.blit(pelota.imagen, pelota.rect)

          pygame.display.update()
          pygame.time.delay(20)


if __name__ == '__main__':
      game()
