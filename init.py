from settings import *
from classes import *
from biome import *
from ui import*

# Init
player = Player()
player.init()
player.point_init()      
biome = Biome()
biome.tree_init()
biome.gex_text()



######CAR#######
card1 = Card('Рука Мидаса',550,pygame.image.load('assets/ui/card_04.png'))
card2 = Card('Отмычка',650,pygame.image.load('assets/ui/card_04.png'))
card3 = Card('Пинок',750,pygame.image.load('assets/ui/card_04.png'))
card4 = Card('Внезапный удар',850,pygame.image.load('assets/ui/card_04.png'))
card5 = Card('Рык',950,pygame.image.load('assets/ui/card_04.png'))



def card_target():
    pos = pygame.mouse.get_pos()
    if pos [0] < 600:
        card1.drawtest()
        card2.drawtest()
        card3.drawtest()
        card4.drawtest()
        card5.drawtest()
    if pos[0]>=600:
        card2.drawtest()
        card3.drawtest()
        card4.drawtest()
        card5.drawtest()
        card1.drawtest()
    if pos[0]>=700:
        card3.drawtest()
        card4.drawtest()
        card5.drawtest()
        card1.drawtest()
        card2.drawtest()
    if pos[0]>=800:
        card4.drawtest()
        card5.drawtest()
        card1.drawtest()
        card2.drawtest()
        card3.drawtest()
    if pos[0]>=900:
        card5.drawtest()
        card1.drawtest()
        card2.drawtest()
        card3.drawtest()
        card4.drawtest()
    if pos[0]>=1000:
        card1.drawtest()
        card2.drawtest()
        card3.drawtest()
        card4.drawtest()
        card5.drawtest()
    
        
    


