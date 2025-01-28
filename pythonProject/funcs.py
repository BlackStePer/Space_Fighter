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

    def change_bullets(self, screen, sheep=False):
        self.check_bullets(sheep)
        for i in self.bullets:
            i.button_motion(screen)

    def check_bullets(self, sheep):
        k = []
        if sheep:
            for i in self.bullets:
                if i.check()[0] < 1400 and not(sheep.ret_p().collidepoint(i.check())):
                    k.append(i)
                elif sheep.ret_p().collidepoint(i.check()):
                    sheep.dammaged()
        else:
            for i in self.bullets:
                if i.check()[0] < 1400:
                    k.append(i)
        self.bullets = k

    def dammaged(self):
        self.hp -= 20

    def ret_hp(self):
        return self.hp

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
        return [self.x, self.y]


class Sniper:
    def __init__(self, x, y):
        self.sniper_image = pygame.image.load("images/ships/2.png")
        self.x = x
        self.y = y
        self.sniper_polygon = pygame.Rect(x, y, 120, 46)
        self.hp = 140
        self.bullets = []

    def draw_ship(self, screen):
        screen.blit(self.sniper_image, (self.x, self.y))

    def shot(self):
        if random.randint(1, 1001) <= 3:
            self.bullets.append(Anti_Bullet(self.x, self.y + 40))

    def change_bullets(self, screen, sheep):
        self.check_bullets(sheep)
        for i in self.bullets:
            i.button_motion(screen)

    def check_bullets(self, sheep):
        k = []
        for i in self.bullets:
            if i.check()[0] > 0 and not(sheep.ship_polygon.collidepoint(i.check())):
                k.append(i)
            elif sheep.ship_polygon.collidepoint(i.check()):
                sheep.dammaged()
        self.bullets = k

    def dammaged(self):
        self.hp -= 20

    def ret_hp(self):
        return self.hp

    def ret_p(self):
        return self.sniper_polygon


class Anti_Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button_poligon = pygame.Rect(self.x, self.y, 15, 5)

    def button_motion(self, screen):
        self.x -= 5
        self.button_poligon = pygame.Rect(self.x, self.y, 15, 5)
        pygame.draw.rect(screen, "Red", (self.x, self.y, 15, 5))

    def check(self):
        return [self.x, self.y]


class Level_1:
    def __init__(self):
        self.wave_1 = [Sniper(1000, 100), Sniper(1000, 700), Sniper(1100, 250), Sniper(1100, 400), Sniper(1100, 550)]
        self.wave_2 = [Sniper(700, 250), Sniper(700, 550), Sniper(700, 700), Sniper(1000, 350), Sniper(1000, 450)]
        self.wave_3 = [Sniper(800, 150), Sniper(750, 350), Sniper(800, 500), Sniper(1000, 550), Sniper(1000, 700)]
        self.wave_4 = [Sniper(1100, y) for y in range(50, 751, 100)]
        self.waves = [self.wave_1, self.wave_2, self.wave_3, self.wave_4]
    def stand_wave(self, screen, sheep):
        for i in range(len(self.waves)):
            if self.waves[i]:
                k = []
                for wrag in self.waves[i]:
                    sheep.change_bullets(screen, wrag)
                    if wrag.ret_hp() > 0:
                        k.append(wrag)
                self.waves[i] = k
                for wrag in self.waves[i]:
                    wrag.draw_ship(screen)
                for wrag in self.waves[i]:
                    wrag.shot()
                for wrag in self.waves[i]:
                    wrag.change_bullets(screen, sheep)
                break
            else:
                sheep.change_bullets(screen)
