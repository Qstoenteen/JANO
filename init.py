
from settings import *
from biome import *
from ui import*
from debug import debug
from monster import*
from card import*
from button import*

from player import Player
from monster import Monster
from battle import Eventy




# Init
player = Player()
charUi = CharUi()
player.init()
player.point_init()      
biome = Biome() # type: ignore
biome.tree_init()
biome.gex_text()
monster = Monster()
monster.init()



######CARD#######
    
        
    


