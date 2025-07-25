import pygame
import sys
from constants import *
from player import Player
from circleshape import CircleShape 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	while True:
		for event in pygame.event.get():
   			 if event.type == pygame.QUIT:
       				 return
		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.check_collisions(player):
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.check_collisions(shot):
					asteroid.split()
					shot.kill()

		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

