import pygame,sys
from init import *

class Game:
    def __init__(self):
        pygame.init()
    def run(self):
        while True:
            dt = clock.tick(FPS)/1000
            mouse = pygame.mouse.get_pos()
            
                        #### MAIN DRAW ####
            
            sc.fill((20,20,40))
            
            biome.biome_draw()
            tableSprite()  
            player.points_draw()
           
            player.player_move()
            player.player_draw()
            
            biome.tree_draw()
            if player.battle == True:
                monster.draw()
                button1.draw()
                button2.draw()
            
            battle = Eventy(player, monster)
            if player.position == 10:
                biome.biome_random()
                biome.tree_init()
                player.point_init()
                monster.scale += 1
                player.position = 1
            
            if player.hp <= 0:
                biome.biome_random()
                player.init()
                player.point_init()
                biome.tree_init()
                monster.init()
                monster.scale = 1

                
            
            #DEBUG##################################################
            debug('deltatime',dt)
            debug('hp',(player.hp),30,10)
            debug('coin',(player.coin),45,10)
            debug('dmg',(player.damage),60,10)
            debug('str',(player.strength),75,10)
            debug('agil',(player.agility),90,10)
            debug('int',(player.intelligence),105,10)
            debug('xp',(player.xp),120,10)
            debug('pos',(player.position),135,10)
            debug('movspeed',(player.moving_speed),150,10)
            debug('fpos',(player.fpos1),165,10)
            debug('biome',(biome.biome),180,10)
            debug('level',(monster.scale),45,300)
            ######ENEMYDEBUG#####################
            if player.battle == True:
                debug('enemy',(monster.name),30,700)
                debug('level',(monster.level),45,700)
                debug('hp',(monster.hp),60,700)
                debug('damage',(monster.damage),75,700)
                debug('element',(monster.element),90,700)
            #########################################################

            
            ##### UI #####
            
            player.hpbar()
            charUi.draw()
            
            biome.gex_text()
            ############## КАРТЫ #########
            card_target() 
            ################
            #print(player.is_moving)
            pygame.display.update()
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit ()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if player.battle == True:
                            
                            battle.tick()
                        if player.battle == False:
                            print('Нет Активной Цели')
                    if event.key == pygame.K_RIGHT:
                        if player.battle == False:
                            player.start_moving()
                            #battle.tick()
                            if player.is_moving == True:
                                battle.eventy_init()
                            #player.move_down()
                        if player.battle == True:
                            print('Дорогу перегрождает', monster.name)
                    if event.key == pygame.K_SPACE:
                        
                        player.point_init()
                        player.init()
                        biome.biome_random()
                        biome.tree_init()
                        monster.init()
                        

                    if event.key == pygame.K_1:
                        charUi.info()
                        if charUi.stat == False and charUi.inventory == False and charUi.buff == False and charUi.think == False:
                            charUi.init_stat()
                        else:
                            charUi.init_null()
                            
                    if event.key == pygame.K_2:
                        if charUi.stat == False and charUi.inventory == False and charUi.buff == False and charUi.think == False:
                            charUi.init_inventory()
                        else:
                            charUi.init_null()
                        
                    if event.key == pygame.K_3:
                        if charUi.stat == False and charUi.inventory == False and charUi.buff == False and charUi.think == False:
                            charUi.init_buff()
                        else:
                            charUi.init_null()
                        
                    if event.key == pygame.K_4:
                        if charUi.stat == False and charUi.inventory == False and charUi.buff == False and charUi.think == False:
                            charUi.init_think()
                        else:
                            charUi.init_null()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_push = True
                if event.type == pygame.MOUSEBUTTONUP:
                    button_push = False
                    
                    
     
if __name__ == '__main__':
    game = Game()
    game.run()