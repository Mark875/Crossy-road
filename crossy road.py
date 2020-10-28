import pygame
import os
import random
pygame.init()
screen_x = 800
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
done = False
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
win = 0
my_image_black = pygame.image.load(os.path.join('images', 'chickena.png'))
my_image_grey = pygame.image.load(os.path.join('images', 'chickengrey.png'))
orange_car_image = pygame.image.load(os.path.join('images', 'orange_car.png'))
orange_car_new = pygame.image.load(os.path.join('images', 'orange_car_dir.png'))
cars_rects = []
def draw_roads():
    for i in range(1, 10):
        pygame.draw.rect(screen, GREY, (0, 700 - i * 70, screen_x, 70))
    for i in range(10):
        pygame.draw.rect(screen, WHITE, (0, 700 - i * 70, screen_x, 5))
class Player():
    def __init__(self):
        self.x = 350
        self.y = 702
        self.vy = 70
        self.vx = 70
        self.image = my_image_black
        self.rect = self.image.get_rect(x=self.x, y=self.y)
    def move(self):
        self.y += self.vy
        self.rect.y += self.vy
        self.x += self.vx
        self.rect.x += self.vx
        if self.y <= 2 or self.y >= 702:
            self.image = my_image_black
        else:
            self.image = my_image_grey            
    def draw(self):       
        screen.blit(self.image, (self.x, self.y))
class Car():
    def __init__(self, direc, y):
        self.x = random.randrange(-120, 920)
        self.y = y
        if direc == 0:
            self.v = 5
            self.image = orange_car_new
            self.original = -120
        else:
            self.image = orange_car_image
            self.v = -5
            self.original = 920
        self.rect = self.image.get_rect(x=self.x, y=self.y)
    def move(self):
        if self.x >= 921 or self.x <= -121:
            self.x = self.original
            self.rect.x = self.original
        self.x += self.v
        self.rect.x += self.v
    def draw(self):       
        screen.blit(self.image, (self.x, self.y))
cars = []
for n in range(1, 10):
    direct_cars = random.randrange(0, 2)
    for j in range(2):
        cars.append(Car(direct_cars, n * 70 + 5))
        cars_rects.append(cars[j].rect)
player = Player()
while not done:
    clock.tick(25)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.vy = -70
                player.vx = 0
                player.move()
            elif event.key == pygame.K_s and player.y <= 702:
                player.vy = 70
                player.vx = 0
                player.move()
            elif event.key == pygame.K_a and player.x >= 50:
                player.vy = 0
                player.vx = -70
                player.move()
            elif event.key == pygame.K_d and player.x <= 730:
                player.vy = 0
                player.vx = 70
                player.move()
    for i in range(len(cars)):
        if cars[i].rect.colliderect(player.rect):
            done = True
    draw_roads()
    player.draw()
    for i in cars:
        i.move()
        i.draw()
    if player.y <= 2:
        done = True
    pygame.display.flip()

pygame.quit()