import pygame, math, random as r, sys,time
### ОСНОВНЫЕ ИМПУТЫ

pygame.init()
clock = pygame.time.Clock()
WIDTH = 1280
HEIGHT = 720
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame MyGame')
icon = pygame.image.load('assets/character_default.png')

### ИМПОРТ КОНТЕНТА
characterIdle = [pygame.image.load('assets/char_animation/char1.png'),
                 pygame.image.load('assets/char_animation/char2.png'),
                 pygame.image.load('assets/char_animation/char3.png'),
                 pygame.image.load('assets/char_animation/char4.png')]

wolfSprite = [pygame.image.load('assets/wolf_animation/wolf_01.png'),
                 pygame.image.load('assets/wolf_animation/wolf_02.png'),
                 pygame.image.load('assets/wolf_animation/wolf_03.png'),
                 pygame.image.load('assets/wolf_animation/wolf_04.png')]

bearSprite = [pygame.image.load('assets/bear_animation/bear_01.png'),
                 pygame.image.load('assets/bear_animation/bear_02.png'),
                 pygame.image.load('assets/bear_animation/bear_03.png'),
                 pygame.image.load('assets/bear_animation/bear_04.png')]

goulSprite = [pygame.image.load('assets/char_animation/char1.png'),
                 pygame.image.load('assets/char_animation/char2.png'),
                 pygame.image.load('assets/char_animation/char3.png'),
                 pygame.image.load('assets/char_animation/char4.png')]

forest_gex = pygame.image.load('assets/gex_forest.png')
forest_gex = pygame.transform.scale(forest_gex,(512,512))
pygame.display.set_icon(icon)
running = True
FPS = 30

enemyList = ('wolf','bear','goul')
enemy_Counter = 0
image_counter = 0
position = 1

battle = False

### ВХОДНЫЕ ПЕРЕМЕННЫЕ
myfont = pygame.font.Font(None,25)
text_surface = myfont.render('Forest biome',False,(255,255,255))

class Player ():
    global position
    
    def __init__(self, name, scale, corX, corY, position, hp, damage, level):
        self.name = name
        self.scale = scale
        self.corX = corX
        self.corY = corY
        self.position = position
        self.hp = hp
        self.damage = damage
        self.level = level
        
    def draw(self):
        self.damage = self.level + 1 
        global image_counter
        
        self.name = characterIdle
        if image_counter == 9:
            image_counter = -1

        image_counter += 1
        #if position == 1 and battle == True: 
            #pygame.draw.circle(sc,(255, 0, 0),(point1.corX, point1.corY), 20,2)
        if position == 2 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point2.corX, point2.corY), 20,2)
        if position == 3 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point3.corX, point3.corY), 20,2)
        if position == 4 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point4.corX, point4.corY), 20,2)
        if position == 5 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point5.corX, point5.corY), 20,2)
        if position == 6 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point6.corX, point6.corY), 20,2)
        if position == 7 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point7.corX, point7.corY), 20,2)
        if position == 8 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point8.corX, point8.corY), 20,2)
        if position == 9 and battle == True: 
            pygame.draw.circle(sc,(255, 0, 0),(point9.corX, point9.corY), 20,2)

        if position == 1:
            sc.blit(self.name[image_counter//3],(point1.corX-20, point1.corY-20))
        if position == 2:
            sc.blit(self.name[image_counter//3],(point2.corX-20, point2.corY-20))
        if position == 3:
            sc.blit(self.name[image_counter//3],(point3.corX-20, point3.corY-20))
        if position == 4:
            sc.blit(self.name[image_counter//3],(point4.corX-20, point4.corY-20))
        if position == 5:
            sc.blit(self.name[image_counter//3],(point5.corX-20, point5.corY-20)) 
        if position == 6:
            sc.blit(self.name[image_counter//3],(point6.corX-20, point6.corY-20))
        if position == 7:
            sc.blit(self.name[image_counter//3],(point7.corX-20, point7.corY-20))
        if position == 8:
            sc.blit(self.name[image_counter//3],(point8.corX-20, point8.corY-20)) 
        if position == 9:
            sc.blit(self.name[image_counter//3],(point9.corX-20, point9.corY-20))
class Monster():
    global position
    def __init__(self, name, level, hp, damage, sprite):
        self.level = level
        self.name = name
        self.hp = hp
        self.damage = damage
        self.sprite = sprite
    def init(self):
        random = r.randint(0,(len(enemyList)-1))
        self.name = enemyList[random]
        self.level = r.randint(0,3) + position
        self.hp = self.level + position + 2
        self.damage = self.level + position 
        #№№№ УСЛОВИЯ ДЛЯ ОТРИСОВКИ СПРАЙТА ПРОТИВНИКАМ:
        if self.name == 'wolf':
            self.sprite = wolfSprite
        if self.name == 'bear':
            self.sprite = bearSprite
        if self.name == 'goul':
            self.sprite = goulSprite 
    def draw(self): 
        global enemy_Counter
        if enemy_Counter == 9:
            enemy_Counter == -1
        enemy_Counter += 1
        
        sc.blit(self.sprite[image_counter//3],(900,350 ))
class Gex ():
    def __init__(self, biome, corX, corY):
        self.biome = biome
        self.corX = corX
        self.corY = corY
    def draw(self):
        sc.blit(self.biome,(self.corX-50,self.corY - 50))
    def info(self):
        if gex1.biome == forest_gex:
            print('ЛЕС')
class Point ():
    def __init__(self, name, corX, corY, scale):
        self.name = name
        self.corX = corX
        self.corY = corY
        self.scale = scale
    def draw(self):
        pygame.draw.circle(sc,(255,255,255),(self.corX,self.corY),self.scale,1)
class Button():
    def __init__(self,color,cor1x,cor1y,button_weight,button_heigh,outline,text):
        self.color = color
        self.cor1x = cor1x
        self.cor1y = cor1y
        self.button_weight = button_weight
        self.button_heigh = button_heigh
        self.outline = outline
        self.text = text
    
    def draw(self):
        pygame.draw.rect(sc,(self.color),(self.cor1x,self.cor1y,self.button_weight,self.button_heigh),self.outline)
        buttonText = myfont.render((self.text),False,(self.color))
        sc.blit(buttonText,(self.cor1x+15,self.cor1y+15))

#battleText = myfont.render(('Вы встретили врага: '+ str(enemy.name)),False,(255,255,255))   

button1 = Button((255,0,0),795,480,150,50,1,'Атаковать')
button2 = Button((255,0,0),945,480,150,50,1,'Бежать')


#ЭКЗЕМПЛЯРЫ    
player = Player('player',50,WIDTH/2,HEIGHT/2,1,100,3,1)

enemy = Monster('null',5,100,10,'wolf')

gex1 = Gex(forest_gex,150,150)





point1 = Point('point1',150,400,15)
point2 = Point('point2',point1.corX+30,point1.corY+30,15)
point3 = Point('point3',point2.corX+r.randint(30,90),point2.corY-r.randint(-50,50),15)
point4 = Point('point3',point3.corX+r.randint(30,70),point3.corY-r.randint(-50,50),15)
point5 = Point('point3',point4.corX+r.randint(30,70),point4.corY-r.randint(-50,50),15)
point6 = Point('point3',point5.corX+r.randint(30,70),point5.corY-r.randint(-50,50),15)
point7 = Point('point3',point6.corX+r.randint(30,70),point6.corY-r.randint(-50,50),15)
point8 = Point('point3',point7.corX+r.randint(30,70),point7.corY-r.randint(-50,50),15)
point9 = Point('point3',point8.corX+r.randint(30,70),point8.corY-r.randint(-50,50),15)
point10 = Point('point3',point9.corX+r.randint(30,70),point9.corY-r.randint(-50,50),15)


timeTest = pygame.time.get_ticks()
print('ТЕСТ ТАЙМЕР ВНЕ ЦИКЛА',timeTest)

### ТЕСТ ОКНО ИНПУТ####
while running:
    battleText = myfont.render(('Противник: '+ str(enemy.name)),False,(255,255,255))
    enemyHpText = myfont.render(('Здоровье противника: '+ str(enemy.hp)),False,(255,255,255))
    enemyDamageText = myfont.render(('Урон противника : '+ str(enemy.damage)+' урона'),False,(255,255,255))
    enemyLevelText = myfont.render(('Уровень противника: '+ str(enemy.level)),False,(255,255,255))
    
        
    #ОСНОВНОЙ БЛОК ОТРИСОВКИ
    
    hpBar = myfont.render('Ваше Здоровье: '+(str(player.hp)),False,(255,255,255))
    damageBar = myfont.render('Ваш урон: '+(str(player.damage)),False,(255,255,255))
    levelBar = myfont.render('Ваш уровень: '+(str(player.level)),False,(255,255,255)) 
    pos = pygame.mouse.get_pos()

    sc.fill((25,25,50))
    sc.blit(text_surface,(300,620))
    sc.blit(levelBar,(10,20))
    sc.blit(hpBar,(10,40))
    sc.blit(damageBar,(10,60))
    
    

   
    gex1.draw()
    
    pygame.draw.line(sc,(255,255,255),(point1.corX,point1.corY),(point2.corX,point2.corY),1)
    pygame.draw.line(sc,(255,255,255),(point2.corX,point2.corY),(point3.corX,point3.corY),1)
    pygame.draw.line(sc,(255,255,255),(point3.corX,point3.corY),(point4.corX,point4.corY),1)
    pygame.draw.line(sc,(255,255,255),(point4.corX,point4.corY),(point5.corX,point5.corY),1)
    pygame.draw.line(sc,(255,255,255),(point5.corX,point5.corY),(point6.corX,point6.corY),1)
    pygame.draw.line(sc,(255,255,255),(point6.corX,point6.corY),(point7.corX,point7.corY),1)
    pygame.draw.line(sc,(255,255,255),(point7.corX,point7.corY),(point8.corX,point8.corY),1)
    pygame.draw.line(sc,(255,255,255),(point8.corX,point8.corY),(point9.corX,point9.corY),1)
    pygame.draw.line(sc,(255,255,255),(point9.corX,point9.corY),(point9.corX,point9.corY),1)
    point1.draw()
    point2.draw()
    point3.draw()
    point4.draw()
    point5.draw()
    point6.draw()
    point7.draw()
    point8.draw()
    point9.draw()
    
    ##################################ТЕСТ ДВИГАЮЩЕГОСЯ ОКНА #################
    basespeed = 0.01
    finalPos = 800
    window = pygame.Surface((150,150))
    button = pygame.Surface((50,50))
    button.fill((255,0,0))
    window.blit(button,(0,0))
    

    
    
 
    #######################################################################
    
    
    player.draw()
    
    
    if enemy.name is not 'null' and battle == True:
        button1.draw()
        button2.draw()
        enemy.draw()

        sc.blit(battleText,(800,40))
        sc.blit(enemyLevelText,(800,60))
        sc.blit(enemyHpText,(800,80))
        sc.blit(enemyDamageText,(800,100))
        pygame.draw.rect(sc, (255, 255, 255),(790,35,310,500), 1)
    pygame.display.update()
    
    
    #ТЕХНИЧЕСКИЙ ЦИКЛ ИГРЫ
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                if button1.cor1x <= pos[0] <= button1.cor1x + button1.button_weight and button1.cor1y <= pos[1] <= button1.cor1y + button1.button_heigh:
                    if battle == True:
                        print('Вы совершили атаку и нанесли: ', player.damage,' урона')
                        enemy.hp -= player.damage
                        player.hp -= enemy.damage
                        if enemy.hp <= 0:
                            player.level += 1
                            enemy.init()
                            battle = False
                        if player.hp <= 0:
                            position = 1
                            player.level = 1
                            player.hp = 100
                            battle = False
                            print('XXXXX')
                            print("ВЫ ПОГИБЛИ")
                            print('XXXXX')
                    

                if button2.cor1x <= pos[0] <= button2.cor1x + button2.button_weight and button2.cor1y <= pos[1] <= button2.cor1y + button2.button_heigh:
                    if battle == True:
                        if player.hp <= 0:
                            position = 1
                            player.hp = 100
                            player.level = 1
                            battle = False
                        away = r.randint(1,5)
                        if away >= 4:
                            print('Вам удалось сбежать')
                            battle = False
                            position -= 1
                        else:
                            print('НЕ УДАЛОСЬ УБЕЖАТЬ')
                            player.hp -= enemy.damage
                            print('Вам нанесли', enemy.damage,'урона')

   
        if event.type == pygame.KEYDOWN:
                #ВЛЕВО
                if event.key == pygame.K_LEFT:
                    if position > 1:
                        if battle == False:
                            if player.hp < 100:
                                player.hp += 15
                                if player.hp > 100:
                                    player.hp = 100
                            position -= 1
                            
                            
                #ВПРАВО
                if event.key == pygame.K_RIGHT:
                    if position < 9:
                        cycleEvent = r.randint(1,3)
                        if battle == False and cycleEvent == 1: #БОЙ
                            battle = True
                            enemy.init()
                            position += 1
                        if battle == False and cycleEvent == 2:
                            position += 1
                            print('Произошел ивент')
                        if battle == False and cycleEvent == 3:
                            position += 1
                            print('Вы нашли сокровищницу')
       
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(FPS)
            
