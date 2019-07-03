import pygame
from pygame.sprite import Sprite
from pygame import *
import util
from random import randint

class Pelota(Sprite):
        
	def __init__(self):
		Sprite.__init__(self)
		self.imagen = util.cargar_imagen('imagenes/pelota.png')
		self.rect = self.imagen.get_rect()
		self.rect.move_ip(0,200)
		self.velocidad = 1
		self.angulox = 1
		self.anguloy = 1
		
       
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_UP]:
			self.velocidad += 1
		elif teclas[K_DOWN]:
			self.velocidad -= 1
			
		self.movimiento()
		
	def movimiento(self):
		print(self.rect.x)
		print(self.rect.y)

		if self.rect.x <= 3:
			self.anguloy = 1
			self.angulox = 1
		elif self.rect.y <= 3:
			self.anguloy = 1
			self.angulox = -1
		elif self.rect.x >= 447:
			self.anguloy = -1
			self.angulox = -1
		elif self.rect.y >= 447:
			self.angulox = 1
			self.anguloy = -1
			
		self.rect.x+=self.angulox*self.velocidad
		self.rect.y+=self.anguloy*self.velocidad

