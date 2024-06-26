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
            player.player_draw() 
            biome.tree_draw()
            #123
            monster.draw()
            #button1.draw()
            #button2.draw()
            debug(dt)

         
            
            ##### UI #####
            hpbar()
            charUi.draw()
            
            biome.gex_text()
            #inventory()
            card_target()
            ################

            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit ()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.move_down()
                    if event.key == pygame.K_RIGHT:
                        player.move_up()
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