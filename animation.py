import pygame

#definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):
	# definir les choses á faire á la création de l'entité
	def __init__(self, sprite_name, size=(200,200)):
		super().__init__()
		self.size = size
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.image = pygame.transform.scale(self.image, size)
		self.current_image = 0 # commence l'anim á l'image 0
		self.images = animation.get(sprite_name)
		self.animation = False

	#definir une methode pour démarrer l'animation
	def start_animation(self):
		self.animation = True

	#definir une methode pour animer le prite
	def animate(self, loop=False):
		#verifier si l'animation est active
		if self.animation:
			#passer à l'image suivante
			self.current_image += 1

			#veridier si on a atteint la fi de l'animation
			if self.current_image >= len(self.images):
				#remettre l'animation au départ
				self.current_image = 0

				#verifier si l'animation n'est pas en mode boucle
				if loop is False:
					#desactivation de l'animation
					self.animation = False

			#modifier l'image précedente par la suivante
			self.image = self.images[self.current_image]
			self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
	# charger les 24 images de ce sprite dans le soddier correspondant
	images = []
	#recuperer le chemin du dossier pour ce sprite
	path = f"assets/{sprite_name}/{sprite_name}"

	#boucler sur chaque image dans ce sossier
	for num in range(1, 24):
		image_path = path + str(num) + '.png'
		images.append(pygame.image.load(image_path))

	# renvoyer le contenuy de la liste d'images
	return images


#definir un dictionaire qui va contenir les images de chaque sprite
animation = {
	'mummy': load_animation_images('mummy'),
	'player': load_animation_images('player'),
	'alien': load_animation_images('alien')
}