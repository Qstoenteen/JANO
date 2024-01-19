import pygame,sys
from settings import *
from debug import debug
from classes import *
from init import *

class Game:
    def __init__(self):
        # general setup
        pygame.init()
    def run(self):
        while True:
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
                        tree.init()
                        stone.init()
                        gex.random()
                    
            sc.fill((20,20,40))
            gex.draw()
            stone.draw()
            tree.draw()
            player.points_draw()
            player.player_draw()
            
            pygame.display.update()
            clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()