import pygame, random as r
from settings import *
#from init import *

battle = False
event = False
start = (200,200)
biome = 'forest'

class Gex():
    def __init__(self):
        global biome
        self.biome = 'forest'
        self.image = pygame.image.load(('assets/gex/forest.png'))
        self.tree_sprite = pygame.image.load(('assets/tree/tree.png'))
        
            
    def gex_draw(self):
        if self.biome == 'forest':
            self.image = pygame.image.load(('assets/gex/forest.png'))
            
        if self.biome == 'winter':
            self.image = pygame.image.load(('assets/gex/winter.png'))
            
        if self.biome == 'vulkan':
            self.image = pygame.image.load(('assets/gex/vulkan.png'))
            
        sc.blit(self.image,(start))
        
    def gex_random(self):
        n = r.randint(0,2)
        if n == 0:
            self.biome = 'forest'
            biome == 'forest'
        if n == 1:
            self.biome = 'winter'
            biome == 'winter'
        if n == 2:
            self.biome = 'vulkan'
    def tree_init(self):
        if self.biome == 'forest':
            self.tree_sprite = pygame.image.load(('assets/tree/tree.png'))
        if self.biome == 'winter':
            self.tree_sprite = pygame.image.load(('assets/tree/winter_tree.png'))
        if self.biome == 'vulkan':
            self.tree_sprite = pygame.image.load(('assets/tree/vulkan_tree.png'))
        print(self.biome)
        self.n1 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n2 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n3 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n4 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n5 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n6 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n7 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n8 = ((r.randint(200,500)),(r.randint(200,500)))
        self.n9 = ((r.randint(200,500)),(r.randint(200,500)))
    
    def tree_draw(self):
        sc.blit(self.tree_sprite,(self.n1))
        sc.blit(self.tree_sprite,(self.n2))
        sc.blit(self.tree_sprite,(self.n3))
        sc.blit(self.tree_sprite,(self.n4))
        sc.blit(self.tree_sprite,(self.n5))
        sc.blit(self.tree_sprite,(self.n6))
        sc.blit(self.tree_sprite,(self.n7))
        sc.blit(self.tree_sprite,(self.n8))
        sc.blit(self.tree_sprite,(self.n9))
     
        
        
class Player():
    def __init__ (self):
        self.image = [pygame.image.load('assets/char_animation/char1.png'),
                 pygame.image.load('assets/char_animation/char2.png'),
                 pygame.image.load('assets/char_animation/char3.png'),
                 pygame.image.load('assets/char_animation/char4.png')]
    def init(self):
        self.hp = 100
        self.damage = 1
        self.xp = 0
        self.coin = 0
        self.agility = 1
        self.strength = 1
        self.intelligence = 1
        self.luck = 1
        
        self.position = 1
        self.counter = 0
        self.point_radius = 10
        
    def point_init(self):
        self.p1 = start[0]+40,start[1]*2
        self.p2 = self.p1[0] + self.point_radius*2+(r.randint(1,15)), self.p1[1] + r.randint(-30,25)
        self.p3 = self.p2[0] + self.point_radius*2+(r.randint(1,15)), self.p2[1] + r.randint(-30,25)
        self.p4 = self.p3[0] + self.point_radius*2+(r.randint(1,15)), self.p3[1] + r.randint(-35,25)
        self.p5 = self.p4[0] + self.point_radius*2+(r.randint(1,15)), self.p4[1] + r.randint(-35,25)
        self.p6 = self.p5[0] + self.point_radius*2+(r.randint(1,15)), self.p5[1] + r.randint(-35,25)
        self.p7 = self.p6[0] + self.point_radius*2+(r.randint(1,15)), self.p6[1] + r.randint(-35,25)
        self.p8 = self.p7[0] + self.point_radius*2+(r.randint(1,15)), self.p7[1] + r.randint(-35,25)
        self.p9 = self.p8[0] + self.point_radius*2+(r.randint(1,15)), self.p8[1] + r.randint(-35,25)
        self.p10 = self.p9[0] + self.point_radius*2+(r.randint(1,15)), self.p9[1] + r.randint(-35,25)
    
    def points_draw(self):
        pygame.draw.circle(sc,(255,255,255),(self.p1),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p2),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p3),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p4),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p5),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p6),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p7),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p8),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p9),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p10),self.point_radius,1)
        
        pygame.draw.line(sc,(255,255,255),(self.p1[0],self.p1[1]),(self.p2[0],self.p2[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p2[0],self.p2[1]),(self.p3[0],self.p3[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p3[0],self.p3[1]),(self.p4[0],self.p4[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p4[0],self.p4[1]),(self.p5[0],self.p5[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p5[0],self.p5[1]),(self.p6[0],self.p6[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p6[0],self.p6[1]),(self.p7[0],self.p7[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p7[0],self.p7[1]),(self.p8[0],self.p8[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p8[0],self.p8[1]),(self.p9[0],self.p9[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p9[0],self.p9[1]),(self.p10[0],self.p10[1]),1)

    def move_up(self):
            if self.position < 10:
                self.position += 1
    
    def move_down(self):
        if self.position > 1:
            self.position -= 1       
    
    def player_draw (self):
        if self.counter == 9:
            self.counter = 0 
        self.counter += 1
        if self.position == 1:
            sc.blit(self.image[self.counter//3],(self.p1[0]-self.point_radius*2,self.p1[1]-self.point_radius*2))
        if self.position == 2:
            sc.blit(self.image[self.counter//3],(self.p2[0]-self.point_radius*2,self.p2[1]-self.point_radius*2))
        if self.position == 3:
            sc.blit(self.image[self.counter//3],(self.p3[0]-self.point_radius*2,self.p3[1]-self.point_radius*2))
        if self.position == 4:
            sc.blit(self.image[self.counter//3],(self.p4[0]-self.point_radius*2,self.p4[1]-self.point_radius*2))
        if self.position == 5:
            sc.blit(self.image[self.counter//3],(self.p5[0]-self.point_radius*2,self.p5[1]-self.point_radius*2))
        if self.position == 6:
            sc.blit(self.image[self.counter//3],(self.p6[0]-self.point_radius*2,self.p6[1]-self.point_radius*2))
        if self.position == 7:
            sc.blit(self.image[self.counter//3],(self.p7[0]-self.point_radius*2,self.p7[1]-self.point_radius*2))
        if self.position == 8:
            sc.blit(self.image[self.counter//3],(self.p8[0]-self.point_radius*2,self.p8[1]-self.point_radius*2))
        if self.position == 9:
            sc.blit(self.image[self.counter//3],(self.p9[0]-self.point_radius*2,self.p9[1]-self.point_radius*2))
        if self.position == 10:
            sc.blit(self.image[self.counter//3],(self.p10[0]-self.point_radius*2,self.p10[1]-self.point_radius*2))
        
        
    def info(self):
        print (self.hp,
              self.xp,
              self.damage,
              self.agility,
              self.strength,
              self.intelligence)
        

        
def hpbar():
    hpbar = pygame.image.load('assets/ui/hp.png')
    sc.blit(hpbar,(5,5))