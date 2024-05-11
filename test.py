import pygame,sys
pygame.init()

button_push = False
myfont = pygame.font.Font(None,25)

WIDTH   = 1280
HEIGTH  = 720
FPS     = 60
sc = pygame.display.set_mode((WIDTH,HEIGTH))
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('JANO ADVENTURE')
clock = pygame.time.Clock()



class Square(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

square = Square('crimson',500,300)
square2 = Square('crimson',600,200)
squares = pygame.sprite.Group()
squares.add(square)
squares.add(square2)
print(squares)

#####input####
##############

class Game:
    def __init__(self):
        pygame.init()
        clock.tick(FPS)
    def run(self):
        while True:
            mpos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit ()
                    sys.exit()
            
            sc.fill((20,20,40))
            squares.draw(sc)
            
            
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()