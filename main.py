import sys, pygame, random
from pygame.locals import *
pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (120, 125, 240)

fish_image = pygame.image.load("fish.png")
#fish_imgage = pygame.transform.smoothscale(fish_image(80, 80))
fish_rect = fish_image.get_rect()
fish_rect.center = (width//2, height//2)

speed = pygame.math.Vector2(0,3)
rotation = random.randint(0,360)
speed.rotate_ip(rotation)

def move_fish():
	fish_rect.move_ip(speed)

def main():
	while True:
		clock.tick(60)
		move_fish()
		pygame.display.flip()
		screen.fill(color)
		screen.blit(fish_image, fish_rect)

if __name__ == '__main__ ':
	main()