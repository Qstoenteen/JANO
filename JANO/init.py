from settings import *
from classes import *

# Init
player = Player()
player.init()
player.point_init()      
tree = Decor(pygame.image.load(('assets/tree/tree.png')))
stone = Decor(pygame.image.load(('assets/tree/stone_01.png')))
stone.init()
tree.init()
gex = Gex()