import pygame, math, random as r, sys,time
import input_data
import file



print(input_data.config)
pygame.init()
clock = pygame.time.Clock()
WIDTH = 1280
HEIGHT = 720
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame MyGame')
icon = pygame.image.load('assets/character_default.png')
FPS = 60
running = True
myfont = pygame.font.Font(None,25)
text_surface = myfont.render('Forest biome',False,(255,255,255))

GexInit = False
class Gex ():
    global GexInit
    def __init__(self,biome,x,y,width,height):
        self.biome = biome
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.rect(sc,(255,255,255),(50,50,self.width,self.height),1)
        
class Point ():
    def __init__(self,x,y,scale):
        self.x = x
        self.y = y
        self.scale = scale
    def draw (self):
        pygame.draw.circle(sc,(255,255,255),(self.x,self.y),self.scale,1)



class Player ():
    global position
    def __init__(self, x, y, position, hp, damage, level, counter = int):
        self.x = x
        self.y = y
        self.position = position
        self.hp = hp
        self.damage = damage
        self.level = level
        self.counter = counter
    def draw(self):
        if self.counter == 9:
            self.counter = -1
        self.counter += 1
        
forest = Gex('forest',50,50,400,400)    
    
    
    
def gex_init():
    forest.draw()
    
    
    
while running:

    sc.fill((25,25,50))
    
    
    
    forest.draw()
    forest.point()
    pygame.display.update()
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(FPS)