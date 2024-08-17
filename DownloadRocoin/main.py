import pygame
from sys import exit
import random
import time

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Rocoin')
icon = pygame.image.load('coin.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font('Pixeltype.ttf',50)
r_speed = 6
c_speed = 4
score = 0



bg_surf = pygame.image.load('bg.png').convert_alpha()
dead_surf = pygame.Surface((600,600))
dead_surf.fill('Red')

player_surf = pygame.image.load('stickfigure.gif').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (300,495))

rockX = random.randint(80,520)
rock_surf = pygame.image.load('rock.png').convert_alpha()
rock_rect = rock_surf.get_rect(center = (rockX, -50))

coinX = random.randint(13,587)
coin_surf = pygame.image.load('coin.png').convert_alpha()
coin_rect = coin_surf.get_rect(center = (coinX, -12.5))

start_txt_surf = font.render('Play', False, 'Red')
start_txt_rect = start_txt_surf.get_rect(center = (300,267.5))

exit_txt_surf = font.render('Exit', False, 'Red')
exit_txt_rect = exit_txt_surf.get_rect(center = (300,337.5))

cover_start_surf = pygame.Surface((100,50))
cover_start_surf.fill('Black')
cover_start_rect = cover_start_surf.get_rect(center = (300,265))
cover_start_surf2 = pygame.Surface((90,40))
cover_start_surf2.fill('White')
cover_start_rect2 = cover_start_surf.get_rect(center = (305,270))

cover_exit_surf = pygame.Surface((100,50))
cover_exit_surf.fill('Black')
cover_exit_rect = cover_start_surf.get_rect(center = (300,335))
cover_exit_surf2 = pygame.Surface((90,40))
cover_exit_surf2.fill('White')
cover_exit_rect2 = cover_start_surf.get_rect(center = (305,340))

cover_dead_surf = pygame.Surface((325,50))
cover_dead_surf.fill('Black')
cover_dead_rect = cover_start_surf.get_rect(center = (190,300))
cover_dead_surf2 = pygame.Surface((315,40))
cover_dead_surf2.fill('White')
cover_dead_rect2 = cover_start_surf.get_rect(center = (195,305))

def score_():
	global score
	cover_surf = pygame.Surface((200,50))
	cover_surf.fill('Black')
	cover_rect = cover_surf.get_rect(center = (300,50))
	cover_surf2 = pygame.Surface((190,40))
	cover_surf2.fill('White')
	cover_rect2 = cover_surf.get_rect(center = (305,55))
	score_surf = font.render('Coins = '+ str(score), False, 'Red')
	score_rect = score_surf.get_rect(center = (300,52.5))
	screen.blit(cover_surf, cover_rect)
	screen.blit(cover_surf2, cover_rect2)
	screen.blit(score_surf, score_rect)
	if player_rect.colliderect(coin_rect):
		coin_rect.top = -25
		coin_rect.left = random.randint(0,575)
		score += 1

game_on = False
dead = False
menu = True

while True:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

	keys = pygame.key.get_pressed()
	mouse = pygame.mouse.get_pos()
	screen.blit(bg_surf, (0,0))

	if game_on == True:
		if keys[pygame.K_a]:
			player_rect.x -= 7
		if keys[pygame.K_d]:
			player_rect.x += 7

		screen.blit(player_surf, player_rect)
		screen.blit(rock_surf, rock_rect)
		screen.blit(coin_surf, coin_rect)
		score_()

		rock_rect.y += r_speed
		coin_rect.y += c_speed
		r_speed += .005
		c_speed += .0025

		if coin_rect.top >= 601: 
			coin_rect.top = -25
			coin_rect.left = random.randint(0,575)
		if rock_rect.top >= 601: 
			rock_rect.top = -101
			rock_rect.left = random.randint(0,500)

		if player_rect.colliderect(rock_rect):
			game_on = False
			dead = True

	elif dead == True:
		dead_txt_surf = font.render('Game Over! Coins = ' + str(score), False, 'White')
		dead_txt_rect = dead_txt_surf.get_rect(center = (300,302.5))
		screen.blit(dead_surf,(0,0))
		#screen.blit(cover_dead_surf, cover_dead_rect)
		#screen.blit(cover_dead_surf2, cover_dead_rect2)
		screen.blit(dead_txt_surf, dead_txt_rect)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				time.sleep(1)
				dead = False
				menu = True

	elif menu == True:
		screen.blit(cover_start_surf, cover_start_rect)
		screen.blit(cover_start_surf2, cover_start_rect2)
		screen.blit(start_txt_surf, start_txt_rect)
		screen.blit(cover_exit_surf, cover_exit_rect)
		screen.blit(cover_exit_surf2, cover_exit_rect2)
		screen.blit(exit_txt_surf, exit_txt_rect)
		player_rect.centerx = 300
		screen.blit(player_surf, player_rect)

		if event.type == pygame.MOUSEBUTTONDOWN:
			if exit_txt_rect.collidepoint(event.pos) or cover_exit_rect2.collidepoint(event.pos):
				pygame.quit()
				exit()
			if start_txt_rect.collidepoint(event.pos) or cover_start_rect2.collidepoint(event.pos):
				game_on = True
				menu = False
				score = 0
				r_speed = 6
				c_speed = 4
				coin_rect.bottom = 0
				coin_rect.left = random.randint(0,575)
				rock_rect.bottom = 0
				rock_rect.left = random.randint(0,500)

	pygame.display.update()
	clock.tick(60)