import pygame
from settings import*

def hpbar():
    hpbar = pygame.image.load('assets/ui/hp.png')
    sc.blit(hpbar,(5,420))
 
def tableSprite():
    table = pygame.image.load('assets/ui/table.png')
    sc.blit(table,(530,35))
    
def inventory():
    inventory = pygame.image.load('assets/ui/inventory.png')
    sc.blit(inventory,(150,280))
 

class Card ():
    def __init__(self,name,x,sprite):
        self.sprite = sprite
        self.name = name
        self.x = x
        self.y = 420
        self.text = myfont.render(self.name,False,(255,255,255))
    def drawtest(self):
        mPos = pygame.mouse.get_pos()
        xx = mPos[0] - self.x 
        yy = mPos[1] - self.y
        if xx >= 0 :
            xx //= 2
            
            if xx > 50:
                # Изменение направления роста
                xx = 100 - xx
                if xx < 0:
                    xx -= xx
            sc.blit(self.sprite, (self.x, self.y+80 - xx))
            sc.blit(self.text,(self.x + 60, self.y + 280 - xx))
            
        if xx < 0 :
            sc.blit(self.sprite, (self.x, self.y + 80))
            sc.blit(self.text,(self.x + 60, self.y + 280))
        
        

    
        