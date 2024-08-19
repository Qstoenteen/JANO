
from settings import *



        
        
class Player():
    def __init__ (self):
        self.image = [pygame.image.load('assets/char_animation/char1.png'),
                 pygame.image.load('assets/char_animation/char2.png'),
                 pygame.image.load('assets/char_animation/char3.png'),
                 pygame.image.load('assets/char_animation/char4.png')]
    def init(self):
        self.hp = 100
        self.damage = 1
        self.xp = 0
        self.coin = 0
        self.agility = 1
        self.strength = 1
        self.intelligence = 1
        self.luck = 1
        
        self.position = 1
        self.counter = 0
        self.point_radius = 10
        self.is_moving = False
        self.is_moving_back = False
        self.moving_speed = 10
        self.battle = False
        
        
        
    def point_init(self):
        self.p1 = start[0]+r.randint(30,70), start[1]*r.randint(3,5)
        self.p2 = self.p1[0] + self.point_radius*2+(r.randint(1,15)), self.p1[1] + r.randint(-30,25)
        self.p3 = self.p2[0] + self.point_radius*2+(r.randint(1,15)), self.p2[1] + r.randint(-30,25)
        self.p4 = self.p3[0] + self.point_radius*2+(r.randint(1,15)), self.p3[1] + r.randint(-35,25)
        self.p5 = self.p4[0] + self.point_radius*2+(r.randint(1,15)), self.p4[1] + r.randint(-35,25)
        self.p6 = self.p5[0] + self.point_radius*2+(r.randint(1,15)), self.p5[1] + r.randint(-35,25)
        self.p7 = self.p6[0] + self.point_radius*2+(r.randint(1,15)), self.p6[1] + r.randint(-35,25)
        self.p8 = self.p7[0] + self.point_radius*2+(r.randint(1,15)), self.p7[1] + r.randint(-35,25)
        self.p9 = self.p8[0] + self.point_radius*2+(r.randint(1,15)), self.p8[1] + r.randint(-35,25)
        self.p10 = self.p9[0] + self.point_radius*2+(r.randint(1,15)), self.p9[1] + r.randint(-35,25)
        
        self.fpos1 = list(self.p1)
        self.fpos2 = list(self.p2)
        self.fpos3 = list(self.p3)
        self.fpos4 = list(self.p4)
        self.fpos5 = list(self.p5)
        self.fpos6 = list(self.p6)
        self.fpos7 = list(self.p7)
        self.fpos8 = list(self.p8)
        self.fpos9 = list(self.p9)
        self.fpos10 = list(self.p10)
        self.charpos = self.fpos1
    
    def points_draw(self):
        pygame.draw.circle(sc,(255,255,255),(self.p1),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p2),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p3),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p4),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p5),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p6),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p7),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p8),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p9),self.point_radius,1)
        pygame.draw.circle(sc,(255,255,255),(self.p10),self.point_radius,1)
        
        pygame.draw.line(sc,(255,255,255),(self.p1[0],self.p1[1]),(self.p2[0],self.p2[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p2[0],self.p2[1]),(self.p3[0],self.p3[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p3[0],self.p3[1]),(self.p4[0],self.p4[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p4[0],self.p4[1]),(self.p5[0],self.p5[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p5[0],self.p5[1]),(self.p6[0],self.p6[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p6[0],self.p6[1]),(self.p7[0],self.p7[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p7[0],self.p7[1]),(self.p8[0],self.p8[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p8[0],self.p8[1]),(self.p9[0],self.p9[1]),1)
        pygame.draw.line(sc,(255,255,255),(self.p9[0],self.p9[1]),(self.p10[0],self.p10[1]),1)

    def infos (self):
        print('hp =', self.hp)
        print('damage = ', self.damage)
        print('xp = ',self.xp)
        print('coins = ',self.coin)
        print('strength = ',self.strength)
        print('intelligence = ',self.intelligence)
        print('luck = ',self.luck)
        
        
    def start_moving(self):
        self.is_moving = True
    
    def player_draw(self):
        if self.counter == 9:
            self.counter = 0 
        self.counter += 1
        sc.blit(self.image[self.counter//3],(self.charpos[0]-self.point_radius*2,self.charpos[1]-self.point_radius*2))
        
    def player_move (self):
        if self.position == 1:
            self.charpos = self.fpos1
            if self.is_moving == True and self.is_moving_back == False:
                if self.fpos1[0] <= self.fpos2[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos2[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos2[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos2:
                    self.position += 1
                    self.is_moving = False
            if self.is_moving_back == True and self.is_moving == False:
                print('Вы вернулись на базу')
                    
        if self.position == 2:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos3[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos3[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos3[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos3:
                    self.position += 1
                    self.is_moving = False
                    
    
        
        if self.position == 3:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos4[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos4[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos4[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos4:
                    
                    self.position += 1
                    self.is_moving = False
        if self.position == 4:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos5[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos5[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos5[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos5:
                    self.position += 1
                    self.is_moving = False
        if self.position == 5:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos6[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos6[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos6[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos6:
                    self.position += 1
                    self.is_moving = False
        
        if self.position == 6:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos7[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos7[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos7[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos7:
                    self.position += 1
                    self.is_moving = False
        
        if self.position == 7:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos8[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos8[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos8[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos8:
                    self.position += 1
                    self.is_moving = False
        
        if self.position == 8:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos9[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos9[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos9[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos9:
                    self.position += 1
                    self.is_moving = False
        
        if self.position == 9:
            if self.is_moving == True:
                if self.fpos1[0] <= self.fpos10[0]:
                    self.fpos1[0] += self.moving_speed
                if self.fpos1[1] <= self.fpos10[1]:
                    self.fpos1[1] += self.moving_speed
                if self.fpos1[1] >= self.fpos10[1]:
                    self.fpos1[1] -= self.moving_speed
                if self.fpos1 >= self.fpos10:
                    self.position += 1
                    self.is_moving = False
        

                    
            
    


