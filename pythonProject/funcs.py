from tabnanny import check

import pygame
import random
stars = []
for _ in range(1400):
    star = (random.randint(0, 1400), random.randint(0, 800))
    if star not in stars:
        stars.append(star)
def draw_space(screen):
    screen.fill("Black")
    for s in stars:
        pygame.draw.circle(screen, "White", s, 1)


class Menu:
    star_game_polygon = pygame.Rect(550, 400, 300, 100)

    def __init__(self):
        self.menu_image = pygame.image.load("images/menu.png")

        self.menu_font = pygame.font.Font("fonts/menu_f.ttf", 150)
        self.name_game = self.menu_font.render('Space Fighter', True, "White")

        self.start_font = pygame.font.Font("fonts/menu_f.ttf", 60)
        self.start_game = self.start_font.render('Start Game', True, "White")

    def menu(self, screen, start_change):
        screen.blit(self.menu_image, (0, 0))
        screen.blit(self.name_game, (300, 100))
        if start_change:
            pygame.draw.rect(screen, (50, 50, 50), (550, 400, 300, 100))
        pygame.draw.rect(screen, "White", (550, 400, 300, 100), 5)
        screen.blit(self.start_game, (570, 405))


class Ship:
    ship_polygon = pygame.Rect(50, 360, 151, 100)
    def __init__(self):
        self.ship_image = pygame.image.load("images/ships/1.png")
        self.x = 50
        self.y = 360
        self.hp = 200
        self.bullets = []

    def draw_ship(self, screen):
        self.ship_polygon = pygame.Rect(self.x, self.y, 151, 100)
        screen.blit(self.ship_image, (self.x, self.y))

    def go_to(self, right, left, up, down):
        if right and self.x + 151 <= 1400:
            self.x += 2
        if left and self.x >= 0:
            self.x -= 2
        if up and self.y >= 0:
            self.y -= 2
        if down and self.y + 100 <= 800:
            self.y += 2

    def shot(self):
        self.bullets.append(Bullet(self.x + 30, self.y + 70))

    def change_bullets(self, screen):
        self.check_bullets()
        for i in self.bullets:
            i.button_motion(screen)

    def check_bullets(self):
        k = []
        for i in self.bullets:
            if i.check() < 1400:
                k.append(i)
        self.bullets = k

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button_poligon = pygame.Rect(self.x, self.y, 15, 5)

    def button_motion(self, screen):
        self.x += 5
        self.button_poligon = pygame.Rect(self.x, self.y, 15, 5)
        pygame.draw.rect(screen, "White", (self.x, self.y, 15, 5))

    def check(self):
        return self.x


class Sniper:
    def __init__(self, x, y):
        self.sniper_image = pygame.image.load("images/ships/2.png")
        self.x = x
        self.y = y
        self.sniper_polygon = pygame.Rect(x, y, 120, 46)
        self.hp = 200
        self.bullets = []

    def draw_ship(self, screen):
        screen.blit(self.sniper_image, (self.x, self.y))
