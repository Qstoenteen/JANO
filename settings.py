import pygame


pygame.init()

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