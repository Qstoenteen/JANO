import pygame, random as r
from settings import *
#from init import *

sizeGex = 384
class Biome():
    def __init__(self):
        global biome
        self.biome = 'forest'
        self.image = pygame.image.load(('assets/gex/forest.png'))
        self.tree_sprite = pygame.image.load(('assets/tree/tree.png'))
        self.text = self.biome
        self.table_biome = pygame.image.load(('assets/ui/map_table.png'))
            
    def biome_draw(self):
        if self.biome == 'forest':
            self.image = pygame.image.load(('assets/gex/forest.png'))
            self.text = 'Лес'
            
        if self.biome == 'winter':
            self.image = pygame.image.load(('assets/gex/winter.png'))
            self.text = 'Зима'
            
        if self.biome == 'vulkan':
            self.image = pygame.image.load(('assets/gex/vulkan.png'))
            self.text = 'Вулкан'
        sc.blit(self.table_biome,(start[0]-10,start[1]-13))  
        sc.blit(self.image,(start))
        
        
    def biome_random(self):
        n = r.randint(0,2)
        if n == 0:
            self.biome = 'forest'
        if n == 1:
            self.biome = 'winter'
        if n == 2:
            self.biome = 'vulkan'
    def tree_init(self):
        if self.biome == 'forest':
            self.tree_sprite = pygame.image.load(('assets/tree/tree.png'))
        if self.biome == 'winter':
            self.tree_sprite = pygame.image.load(('assets/tree/winter_tree.png'))
        if self.biome == 'vulkan':
            self.tree_sprite = pygame.image.load(('assets/tree/vulkan_tree.png'))

        self.n1 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n2 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n3 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n4 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n5 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n6 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n7 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n8 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))
        self.n9 = ((r.randint(start[0],sizeGex-50)),(r.randint(start[1],sizeGex)))

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
    
    def gex_text(self):
        gexText = myfont.render(self.text, False,(255,255,255))
        sc.blit(gexText,(200,40))