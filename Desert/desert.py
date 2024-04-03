import pygame, random
from random import randint
from pathlib import Path

WIDTH = 800
HEIGHT = 550
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desert")
clock = pygame.time.Clock()
current_path = Path.cwd()
file_path = current_path / 'highscore.txt'

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/player.png").convert(),(100,100))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = self.rect.width
		self.rect.bottom = HEIGHT - 30
		self.speed_x = 0
		self.shield = 100
		self.jumping = False
		self.Y_GRAVITY = 1
		self.JUMP_HEIGHT = 20
		self.Y_VELOCITY = self.JUMP_HEIGHT

	def update(self):
		self.shield += 1/24
		self.speed_x = 0
		if self.shield > 100:
			self.shield = 100
		if self.shield < 0:
			self.shield = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -10
		if keystate[pygame.K_d]:
			self.speed_x = 10
		if keystate[pygame.K_f]:
			self.jumping = True
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

class Rock(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		num1 = randint(1,100)
		print(num1)
		if num1 == 1:
			self.image = rock_images[4]
		elif num1 == 2:
			self.image = rock_images[3]
		elif num1 >= 3 and num1 <= 4:
			self.image = rock_images[1]
		elif num1 >= 5 and num1 <= 98:
			self.image = rock_images[0]
		elif num1 >= 99:
			self.image = rock_images[2]
		
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3)
		self.rect.y = random.randrange(300,450)
		self.speedx = -5

	def update(self):
		self.rect.x += self.speedx

		if self.rect.right < -self.rect.width:
			num1 = randint(1,100)
			if num1 == 1:
				self.image = rock_images[4]
			elif num1 == 2:
				self.image = rock_images[3]
			elif num1 >= 3 and num1 <= 4:
				self.image = rock_images[1]
			elif num1 >= 5 and num1 <= 98:
				self.image = rock_images[0]
			elif num1 >= 99:
				self.image = rock_images[2]
			self.image.set_colorkey(WHITE)
			self.rect.y = random.randrange(300,450)
			self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3)

class Rock1(Rock):
	def __init__(self):
		super().__init__()
		
class Rock2(Rock):
	def __init__(self):
		super().__init__()

class Rock3(Rock):
	def __init__(self):
		super().__init__()
		
class Rock4(Rock):
	def __init__(self):
		super().__init__()

class Rock5(Rock):
	def __init__(self):
		super().__init__()

class Rock6(Rock):
	def __init__(self):
		super().__init__()

class Cactus(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		num7 = randint(1,10)
		if num7 == 1:
			self.image = cactus_images[2]
		if num7 == 2:
			self.image = cactus_images[1]
		if num7 >= 3 :
			self.image = cactus_images[0]
		
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3)
		self.rect.y = 450
		self.speedx = -5

	def update(self):
		self.rect.x += self.speedx
		if self.rect.right < -self.rect.width - 20:
			num7 = randint(1,10)
			if num7 == 1:
				self.image = cactus_images[2]
			if num7 == 2:
				self.image = cactus_images[1]
			if num7 >= 3 :
				self.image = cactus_images[0]
			self.image.set_colorkey(WHITE)
			self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3)
			self.rect.y = 450

class Jarra(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = jarra_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 2)
		self.rect.y = random.randrange(350,490)
		self.speedx = -5

	def update(self):
		self.rect.x += self.speedx
		if self.rect.left < -self.rect.width:
			self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 2)
			self.rect.y = 430

def show_go_screen():
	
	screen.blit(background, [0,0])
	draw_text2(screen, "Desert", 65, WIDTH // 2, HEIGHT // 4)
	draw_text2(screen, "Esquiva obstáculos y colecta jarras", 20, WIDTH // 2, HEIGHT // 2)
	draw_text2(screen, "Press Key Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text2(screen, "Created by: Francisco Carvajal", 10,  60, 500)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

rock_images = []
rock_list = ["img/1.png", "img/2.png", "img/3.png", "img/22.png", "img/33.png"]
for img in rock_list:
	rock_images.append(pygame.image.load(img).convert())

cactus_images = []
cactus_list = ["img/cac.png", "img/cac2.png","img/cac3.png"]
for img in cactus_list:
	cactus_images.append(pygame.image.load(img).convert())

jarra_images = []
jarra_list = ["img/jarra.png"]
for img in jarra_list:
	jarra_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(50,50)))

num_list = [0,0,1,1,1,1]

def get_high_score():
	with open(file_path,'r') as file:
		return file.read()

def show_game_over_screen():
	screen.blit(background, [0,0])
	if highest_score <= score:
		draw_text2(screen, "¡high score!", 60, WIDTH  // 2, HEIGHT * 1/4)
		draw_text2(screen, "score: "+str(score), 30, WIDTH // 2, HEIGHT // 2)
		draw_text2(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 4/5)
	else:
		draw_text2(screen, "score: "+str(score), 60, WIDTH // 2, HEIGHT * 1/3)
		draw_text2(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 2/3)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

# Cargar imagen de fondo
background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(800,600))

### high score

try:
	highest_score = int(get_high_score())
except:
	highest_score = 0

game_over = False
running = True
start = True
while running:
	if game_over:

		show_game_over_screen()

		game_over = False
		all_sprites = pygame.sprite.Group()
		rock_list = pygame.sprite.Group()
		cactus_list = pygame.sprite.Group()
		jarra_list = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)

		rock1 = Rock1()		
		rock2 = Rock2()		
		rock3 = Rock3()		
		rock4 = Rock4()		
		rock5 = Rock5()		
		rock6 = Rock6()

		all_sprites.add(rock1, rock2, rock3, rock4, rock5, rock6)			
		
		rock_list.add(rock1, rock2, rock3, rock4, rock5, rock6)			
		
		cactus = Cactus()
		all_sprites.add(cactus)
		cactus_list.add(cactus)

		for i in range(3):
			jarra = Jarra()
			all_sprites.add(jarra)
			jarra_list.add(jarra)
			
		score = 0

	if start:
		show_go_screen()
		start = False
		all_sprites = pygame.sprite.Group()
		rock_list = pygame.sprite.Group()
		cactus_list = pygame.sprite.Group()
		jarra_list = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)

		rock1 = Rock1()		
		rock2 = Rock2()		
		rock3 = Rock3()		
		rock4 = Rock4()		
		rock5 = Rock5()		
		rock6 = Rock6()

		all_sprites.add(rock1, rock2, rock3, rock4, rock5, rock6)			
		
		rock_list.add(rock1, rock2, rock3, rock4, rock5, rock6)			
		
		cactus = Cactus()
		all_sprites.add(cactus)
		cactus_list.add(cactus)

		for i in range(3):
			jarra = Jarra()
			all_sprites.add(jarra)
			jarra_list.add(jarra)
			
		score = 0

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	if player.jumping:
		player.rect.bottom -= player.Y_VELOCITY
		player.Y_VELOCITY -= player.Y_GRAVITY
		if player.Y_VELOCITY < - player.JUMP_HEIGHT:
			player.jumping = False
			player.Y_VELOCITY = player.JUMP_HEIGHT
		
	all_sprites.update()

	if player.shield == 0:
		game_over = True
	
	#colisiones - rock - player
	hits = pygame.sprite.spritecollide(player, rock_list, False)
	for hit in hits:
		player.shield -= 2
		
	#colisiones - cactus - player
	hits2 = pygame.sprite.spritecollide(player, cactus_list, False )
	for hit in hits2:
		player.shield -= 2
		
	#colisiones - jarra - player
	hits = pygame.sprite.spritecollide(player, jarra_list, True)
	for hit in hits:
		score += 100
		player.shield += randint(5,10)
		
		jarra = Jarra()
		all_sprites.add(jarra)
		jarra_list.add(jarra)

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	draw_text2(screen, str(score), 25, WIDTH // 2, 10)

	# Escudo.
	draw_shield_bar(screen, 5, 5, player.shield)
	draw_text2(screen, str(int(player.shield)) + "/100", 10, 55, 5)
	draw_shield_bar(screen, player.rect.x, player.rect.y - 10, player.shield)
	draw_text2(screen, str(int(player.shield)) + "/100", 10, player.rect.centerx, player.rect.y - 10)
	pygame.display.flip()