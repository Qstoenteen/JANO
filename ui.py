import pygame
from settings import*

def hpbar():
    hpbar = pygame.image.load('assets/ui/hp.png')
    sc.blit(hpbar,(38,600))
 
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
        


class Button():
    
    def __init__(self,x,y,text):
        self.text = text
        self.x = x
        self.y = y
        self.sprite = pygame.image.load('assets/ui/button_01_01.png')
        self.w = 198
        self.h = 90
        self.outlite = 1
    def draw(self):
        global button_push
        self.target = False
        
        pos = pygame.mouse.get_pos()
        
    
            
        if self.x < pos[0] < self.x + self.w and self.y<pos[1]< self.y + self.h:
            self.target = True
        if self.target == False:
            self.sprite = pygame.image.load('assets/ui/button_01_01.png')
        if self.target == True:
            self.sprite = pygame.image.load('assets/ui/button_01_02.png')
        if self.target == True and button_push == True:
            self.sprite = pygame.image.load('assets/ui/button_01_03.png')
    
            
            
        #pygame.draw.rect(sc,(255,255,255),(self.x, self.y, self.w, self.h),self.outlite)
        button_text = myfont.render((self.text),False,(255,255,255))
        sc.blit(self.sprite,(self.x,self.y))
        sc.blit(button_text,(self.x+50,self.y+40))
        
        
class CharUi():
        def __init__(self):
            self.stat = False
            self.inventory = False
            self.buff = False
            self.think = False
            self.sprite = pygame.image.load('assets/ui/null.png')
            self.push = False
            
        def init_null(self):
            self.stat = False
            self.inventory = False
            self.buff = False
            self.think = False
            self.sprite = pygame.image.load('assets/ui/null.png')
        
        def init_stat(self):
            if self.stat == False:
                self.stat = True
            elif self.stat == True:
                self.stat = False
                print(self.stat)
            
            self.inventory = False
            self.buff = False
            self.think = False
            
            self.sprite = pygame.image.load('assets/ui/char_ui_01.png')
            
        def init_inventory(self):
            self.stat = False
            self.inventory = True
            self.buff = False
            self.think = False
            
            
            self.sprite = pygame.image.load('assets/ui/char_ui_02.png')
        def init_buff(self):
            self.stat = False
            self.inventory = True
            self.buff = True
            self.think = False
            
            self.sprite = pygame.image.load('assets/ui/char_ui_03.png')
        def init_think(self):
            self.stat = False
            self.inventory = False
            self.buff = False
            self.think = True
            
            self.sprite = pygame.image.load('assets/ui/char_ui_04.png')
                
        def draw(self):
            sc.blit(self.sprite,(143,423))
        
        def info(self):
            print(self.push)
        #def close(self):
            