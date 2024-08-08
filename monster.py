import pygame, random as r
from init import*
from settings import*


battle = False
class Monster():
    def __init__(self):
        self.name = 'none'
        self.sprite = pygame.image.load('assets/wolf_animation/wolf_01.png')
        self.scale = 1
    def init(self):
        self.level = r.randint(1,3) * self.scale
        self.hp = self.level * r.randint(1,2) * self.scale
        self.damage = self.hp // 3 * self.scale
        enemy_random = r.randint(0,3)
        if enemy_random == 0:
            self.name = 'wolf'
            self.sprite = pygame.image.load('assets/wolf_animation/wolf_01.png')
        if enemy_random == 1:
            self.name = 'bear'
            self.sprite = pygame.image.load('assets/bear_animation/bear_01.png')
        if enemy_random == 2:
            self.name = 'mutant'
            self.sprite = pygame.image.load('assets/wolf_animation/wolf_01.png')
        if enemy_random == 3:
            self.name = 'giant'
            self.sprite = pygame.image.load('assets/wolf_animation/wolf_01.png')
            
        element_random = r.randint(0,3)
        if element_random == 0:
            self.element = 'water'
        if element_random == 1:
            self.element = 'fire'
        if element_random == 2:
            self.element = 'wind'
        if element_random == 3:
            self.element = 'earth'
        print('Ваш противник:', self.name,', Наделенный стихией: ',self.element)
        print('у него:', self.level,' уровень, ',self.hp,' здоровья, ',self.damage,' урона')
        
    def draw(self):
        if self.name == 'wolf':
            self.sprite = pygame.image.load('assets/wolf_animation/wolf_01.png')
        sc.blit(self.sprite,(800,200))
        
    
        
        