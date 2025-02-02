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


class LevelMenu:
    l1_polygon = pygame.Rect(100, 250, 200, 100)
    l2_polygon = pygame.Rect(600, 250, 200, 100)
    def __init__(self):
        self.menu_image = pygame.image.load("images/menu.png")

        self.l_font = pygame.font.Font("fonts/menu_f.ttf", 60)
        self.l1 = self.l_font.render('Level 1', True, "White")
        self.l2 = self.l_font.render('Level 2', True, "White")

        self.main_font = pygame.font.Font("fonts/menu_f.ttf", 150)
        self.name_game = self.main_font.render('Change level', True, "White")

    def menu(self, screen, l_1, l_2):
        screen.blit(self.menu_image, (0, 0))
        screen.blit(self.name_game, (300, -10))
        if l_1:
            pygame.draw.rect(screen, (50, 50, 50), (100, 250, 200, 100))
        if l_2:
            pygame.draw.rect(screen, (50, 50, 50), (600, 250, 200, 100))
        pygame.draw.rect(screen, "White", (100, 250, 200, 100), 5)
        pygame.draw.rect(screen, "White", (600, 250, 200, 100), 5)
        screen.blit(self.l1, (120, 255))
        screen.blit(self.l2, (620, 255))

class DethMenu:
    back_polygon = pygame.Rect(305, 465, 225, 150)
    def __init__(self):
        self.menu_image = pygame.image.load("images/deth.jpg")

        self.menu_font = pygame.font.Font("fonts/menu_f.ttf", 120)
        self.name_game = self.menu_font.render('You are died!', True, (7, 237, 229))

        self.back_font = pygame.font.Font("fonts/menu_f.ttf", 60)
        self.back = self.back_font.render('Menu', True, "White")
    def menu(self, screen, men):
        screen.blit(self.menu_image, (0, -60))
        screen.blit(self.name_game, (370, 100))
        if men:
            pygame.draw.rect(screen, (50, 50, 50), (305, 465, 225, 150))
        pygame.draw.rect(screen, "White", (305, 465, 225, 150), 5)
        screen.blit(self.back, (350, 490))