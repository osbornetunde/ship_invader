import sys
import pygame

from rocket_settings import Settings

def run_game():
	pygame.init()
	pa_settings = Settings()
	screen = pygame.display.set_mode((pa_settings.screen_width, pa_settings.screen_height))
	pygame.display.set_caption("Tunde")
	
while True:
		
	screen.fill(pa_settings.bg_color)
	
	
	
	pygame.display.flip()
run_game()
