import pygame
import random as r
pygame.init()

#SOUND####################################
pygame.mixer.init()
pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)  # Установка громкости
#/SOUND###################################

button_push = False
myfont = pygame.font.Font(None,25)
start = (60,80)
WIDTH   = 1280
HEIGTH  = 720
FPS     = 30

sc = pygame.display.set_mode((WIDTH,HEIGTH))
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('JANO ADVENTURE')

clock = pygame.time.Clock()