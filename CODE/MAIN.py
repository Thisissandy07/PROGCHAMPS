import pygame
from sys import exit
import random


pygame.init()
pygame.display.set_caption('desmond the moon bear')
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1300
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
width = 40
height = 40

#images background
background = pygame.image.load('Assets/BACKGROUND.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#images of desmond
walking = [pygame.image.load('Assets/walk img/walk1.png').convert_alpha(), pygame.image.load(
    'Assets/walk img/walk2.png'), pygame.image.load(
    'Assets/walk img/walk3.png'), pygame.image.load('Assets/walk img/walk4.png'), pygame.image.load(
    'Assets/walk img/walk5.png'), pygame.image.load(
    'Assets/walk img/walk6.png')]
for pic in walking:
    pic = pygame.transform.scale(pic, (20, 20)).convert_alpha()

idle = pygame.image.load('Assets/desmond_idle.png')
jumping = [pygame.image.load('Assets/jump img/jump1.png'), pygame.image.load('Assets/jump img/jump2.png'), pygame.image.load(
    'Assets/jump img/jump3.png'), pygame.image.load('Assets/jump img/jump4.png'), pygame.image.load(
    'Assets/jump img/jump5.png'), pygame.image.load(
    'Assets/jump img/jump6.png'), pygame.image.load('Assets/jump img/jump7.png'), pygame.image.load(
    'Assets/jump img/jump8.png')]

attack = [pygame.image.load('Assets/attack img/attack1.png'),pygame.image.load('Assets/attack img/attack2.png'),pygame.image.load('Assets/attack img/attack3.png'),pygame.image.load('Assets/attack img/attack4.png'),pygame.image.load('Assets/attack img/attack5.png'),pygame.image.load('Assets/attack img/attack6.png')]


#obstacles and stuff
ships = [pygame.image.load('Assets/SHIPS/ship1.png'), pygame.image.load('Assets/SHIPS/ship2.png'), pygame.image.load(
    'Assets/SHIPS/ship3.png')]
for ship in ships:
    ship = pygame.transform.scale(ship, (40, 40)).convert_alpha()
clouds = [pygame.image.load('Assets/CLOUDS/clouds1.png'), pygame.image.load('Assets/CLOUDS/clouds2.png')]
rock_small = [pygame.image.load('Assets/Rock2.png'), pygame.image.load('Assets/smallRock3.png'), pygame.image.load(
    'Assets/small Rock4.png')]
for rock in rock_small:
    rock = pygame.transform.scale(rock, (40, 40)).convert_alpha()
rockk1 = pygame.image.load('Assets/Rock1.png')
rockk1 = pygame.transform.scale(rockk1, (90, 70)).convert_alpha()
rockk2 = pygame.image.load('Assets/LargeRock5.png')
rockk2 = pygame.transform.scale(rockk2, (100, 100)).convert_alpha()
rock_large = [rockk1, rockk2]




class Desmond:
    X_POS = 80
    Y_POS = 550
    Y_POS_DUCK = 950
    JUMP_VEL = 11


    def __init__(self):


        self.run_img = walking

        self.jump_img = jumping

        self.desmond_run = True
        self.desmond_jump = False


        self.step_index = 0
        self.jump_index = 0
        self.jump_vel  = self.JUMP_VEL
        self.image = self.run_img[0]
        self.desmond_rect = self.image.get_rect()
        self.desmond_rect.x = self.X_POS
        self.desmond_rect.y = self.Y_POS





    def update(self,user_input):
        if self.desmond_run:
            self.run()
        if self.desmond_jump:
            self.jump()


        if self.step_index == len(self.run_img)*5:
            self.step_index = 0

        if self.jump_index == len(self.jump_img)*5:
            self.jump_index = 0


        if user_input[pygame.K_SPACE] and not self.desmond_jump:
            self.desmond_jump = True
            self.desmond_run = False

        elif not self.desmond_jump or user_input[pygame.K_DOWN] :
            self.desmond_jump = False
            self.desmond_run = True


    def jump(self):
        self.image = self.jump_img[self.jump_index//5]
        if self.desmond_jump:
            self.desmond_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            self.jump_index += 1
        if self.jump_vel < - self.JUMP_VEL:
            self.desmond_jump = False
            self.jump_vel = self.JUMP_VEL



    def run(self):
        self.image = self.run_img[self.step_index//5]
        self.desmond_rect = self.image.get_rect()
        self.desmond_rect.x = self.X_POS
        self.desmond_rect.y = self.Y_POS
        self.step_index += 1


    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.desmond_rect.x,self.desmond_rect.y))






class Clouds():
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800,1000)
        self.y = SCREEN_HEIGHT + random.randint(50,100)
        self.image = clouds[random.randint(0,1)]
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed*1.5
        if self.x < -self.width:
            self.image = clouds[random.randint(0,1)]
            self.x = SCREEN_WIDTH + random.randint(2500,3000)
            self.y = random.randint(50,100)



    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.x,self.y))


class Obstacle():
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()





    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallRock(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 650

class LargeRock(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 650

class SpaceShip(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 400





def main(SCREEN):
    global game_speed,x_pos_bg,y_pos_bg,points,obstacles
    run = True
    clock = pygame.time.Clock()
    player = Desmond()
    CLOUD = Clouds()
    game_speed = 15
    x_pos_bg = 0
    y_pos_bg = 750
    points = 0
    font = pygame.font.SysFont('comicsans', 30)
    obstacles = []
    death_count = 0


    def score():
        global points, game_speed
        points += 0.5
        if points % 200 == 0:
            game_speed *= 1.3


        text = font.render('Score: ' + str(points), True, (255,255,255))
        textRect = text.get_rect()
        textRect.centerx = 1150
        textRect.centery = 100
        SCREEN.blit(text, textRect)









    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        SCREEN.blit(background, (0, 0))
        user_input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(user_input)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallRock(rock_small))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeRock(rock_large))
            elif random.randint(0, 2) == 2:
                obstacles.append(SpaceShip(ships))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.desmond_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)


        CLOUD.draw(SCREEN)
        CLOUD.update()

        score()

        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(walking[0], (SCREEN_WIDTH // 2-100 , SCREEN_HEIGHT // 2 - 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main(SCREEN)


menu(death_count=0)




