import random as r
from player import Player
from monster import Monster
#from biome import biome
class Eventy:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.event_cd = False
        
        
    def eventy_init(self):
        if self.player.battle == False:
            self.eventy = r.randint(1,2)
            print(self.eventy)
            
            if self.eventy == 1:
                self.battle_start()
                
            if self.eventy == 2:
                print('ПРОИЗОШЛО СОБЫТИЕ 2')
                print(self.player.is_moving)
                
                #x = r.randint(1,3)
                #self.player.damage += x
                #print('Вы нашли артефакт, ваш урон увеличен на', x)
                self.event_cd = False
        if self.player.battle == True:
            self.tick()
                
    def battle_start(self):
        self.player.battle = True
        self.monster.init()
        print(self.monster.name)
        print(self.monster.hp)
        print(self.monster.damage)
        
    def battle_end(self):
        self.player.battle = False
        
    def tick(self):
        if self.player.battle == True and self.player.is_moving == False:
            
            if self.player.hp > 0:
                self.player.hp -= self.monster.damage
                self.monster.hp -= self.player.damage
            print('Вы совершили атаку и нанесли ',self.player.damage,' урона')
            print('У него осталось ', self.monster.hp)
            if self.player.hp <= 0:
                print('ВЫ ПОГИБЛИ X___X')
                #self.player.init()
                #self.player.point_init()
                #self.monster.scale = 1
                
                
                
            
            
            if self.monster.hp <= 0:
                print('ВЫ ОДОЛЕЛИ МОНСТРА')
                if self.player.hp < 100:
                    self.player.hp += 2
                    if self.player.hp > 100:
                        self.player.hp = 100
                self.player.damage += 1
                self.player.battle = False
                print('БОЙ ОКОНЧЕН')
                
