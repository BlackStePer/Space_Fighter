import pygame
import random


class Ship:
    ship_polygon = pygame.Rect(50, 360, 151, 100)
    def __init__(self):
        self.ship_image = pygame.image.load("images/ships/1.png")
        self.x = 50
        self.y = 360
        self.hp = 202
        self.angle = 0
        self.bullets = []

    def draw_ship(self, screen):
        self.ship_polygon = pygame.Rect(self.x, self.y, 151, 100)
        screen.blit(pygame.transform.rotate(self.ship_image, self.angle), (self.x, self.y))
        pygame.draw.rect(screen, "RED", (self.x + 30, self.y - 30, 0.5 * self.hp, 5))

    def go_to(self, right, left, up, down):
        if right and self.x + 151 <= 1400:
            self.x += 3
        if left and self.x >= 0:
            self.x -= 3
        if up and self.y >= 0:
            if self.angle < 15:
                self.angle += 0.4
            self.y -= 3
        if down and self.y + 100 <= 800:
            if self.angle > -10:
                self.angle -= 0.2
                if self.angle > 1:
                    self.angle -= 0.2
            self.y += 3
        if not(any([right, left, up, down])):
            if self.angle < -1:
                self.angle += 0.8
            elif self.angle > 1:
                self.angle -= 0.8
            else:
                ...

    def shot(self):
        self.bullets.append(Bullet(self.x + 30, self.y + 70))

    def change_bullets(self, screen):
        for i in self.bullets:
            i.button_motion(screen)

    def check_bullets(self, sheep):
        k = []
        if sheep.ret_p().colliderect([self.x, self.y, 151, 100]):
            sheep.dammaged()
        for i in self.bullets:
            if i.check()[0] < 1400 and not(sheep.ret_p().collidepoint(i.check())):
                k.append(i)
            elif sheep.ret_p().collidepoint(i.check()):
                sheep.dammaged()
        self.bullets = k

    def dammaged(self):
        self.hp -= 20

    def ret_hp(self):
        return self.hp

    def ret_cords(self):
        return self.x, self.y

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


class AntiBullet(Bullet):
    def button_motion(self, screen):
        self.x -= 5
        self.button_poligon = pygame.Rect(self.x, self.y, 15, 5)
        pygame.draw.rect(screen, "Red", (self.x, self.y, 15, 5))


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
        pygame.draw.rect(screen, "RED", (self.x + 20, self.y - 30, 0.5 * self.hp, 5))

    def shot(self):
        if random.randint(1, 1001) <= 3:
            self.bullets.append(AntiBullet(self.x, self.y + 40))

    def change_bullets(self, screen, sheep):
        self.check_bullets(sheep)
        for i in self.bullets:
            i.button_motion(screen)

    def check_bullets(self, sheep):
        k = []
        if sheep.ship_polygon.colliderect(self.sniper_polygon):
            sheep.dammaged()
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

    def ret_type(self):
        return "sniper"


class HardSniper(Sniper):
    def __init__(self, x, y):
        self.sniper_image = pygame.image.load("images/ships/4.png")
        self.x = x
        self.y = y
        self.sniper_polygon = pygame.Rect(x, y, 120, 46)
        self.hp = 400
        self.bullets = []

    def shot(self):
        if random.randint(1, 1001) <= 5:
            self.bullets.append(AntiBullet(self.x, self.y))
            self.bullets.append(AntiBullet(self.x, self.y + 20))
            self.bullets.append(AntiBullet(self.x, self.y + 40))

    def draw_ship(self, screen):
        screen.blit(self.sniper_image, (self.x, self.y))
        pygame.draw.rect(screen, "RED", (self.x + 20, self.y - 30, 0.2 * self.hp, 5))

class Breaker:
    def __init__(self, x, y):
        self.breaker_image = pygame.image.load("images/ships/3.png")
        self.x = x
        self.y = y
        self.breaker_polygon = pygame.Rect(x, y, 120, 120)
        self.hp = 1000

    def draw_ship(self, screen):
        screen.blit(self.breaker_image, (self.x, self.y))
        pygame.draw.rect(screen, "RED", (self.x + 10, self.y - 30, 0.1 * self.hp, 5))

    def dammaged(self):
        self.hp -= 20

    def ret_hp(self):
        return self.hp

    def ret_p(self):
        return self.breaker_polygon

    def ret_type(self):
        return "breaker"

    def check_bullets(self, sheep):
        if sheep.ship_polygon.colliderect(self.breaker_polygon):
            sheep.dammaged()


class UFO:
    def __init__(self, x, y):
        self.ufo_image = pygame.image.load("images/ships/5.png")
        self.x = x
        self.y = y
        self.UFO_polygon = pygame.Rect(x, y, 326, 200)
        self.hp = 4000
        self.bullets = []
        self.timer = 0

    def draw_ship(self, screen):
        screen.blit(self.ufo_image, (self.x, self.y))
        pygame.draw.rect(screen, "RED", (self.x + 10, self.y - 30, 0.15 * 0.5 * self.hp, 5))

    def shot(self):
        if self.timer // 60 == 1:
            self.bullets.append(AntiBullet(self.x, self.y + 20))
            self.bullets.append(AntiBullet(self.x, self.y + 45))
            self.bullets.append(AntiBullet(self.x, self.y + 70))
            self.timer = 0
        else:
            self.timer += 1

    def shot_2(self):
        for y in range(50, 800, 20):
            if random.randint(1, 1001) <= 1:
                self.bullets.append(AntiBullet(self.x, y))
    def shot_3(self):
        for y in range(50, 800, 30):
            if random.randint(1, 1001) <= 2:
                self.bullets.append(AntiBullet(1050, y))

    def change_bullets(self, screen, sheep):
        self.check_bullets(sheep)
        for i in self.bullets:
            i.button_motion(screen)

    def check_bullets(self, sheep):
        k = []
        if sheep.ship_polygon.colliderect(self.UFO_polygon):
            sheep.dammaged()
        for i in self.bullets:
            if i.check()[0] > 0 and not(sheep.ship_polygon.collidepoint(i.check())):
                k.append(i)
            elif sheep.ship_polygon.collidepoint(i.check()):
                sheep.dammaged()
        self.bullets = k

    def motion(self, sheep):
        x, y = sheep.ret_cords()
        if self.y > y + 5:
            self.y -= 1.8
        elif self.y < y - 5:
            self.y += 1.8
        self.UFO_polygon = pygame.Rect(self.x, self.y, 326, 200)

    def motion_3(self, sheep):
        x, y = sheep.ret_cords()
        if self.y > y + 5:
            self.y -= 1.4
        elif self.y < y - 5:
            self.y += 1.4
        if self.x > x + 5:
            self.x -= 1.4
        elif self.x < x - 5:
            self.x += 1.4
        self.UFO_polygon = pygame.Rect(self.x, self.y + 100, 326, 50)

    def mot_to(self, x, y):
        if self.y > y + 5:
            self.y -= 1.4
        elif self.y < y - 5:
            self.y += 1.4
        if self.x > x + 5:
            self.x -= 1.4
        elif self.x < x - 5:
            self.x += 1.4
        self.UFO_polygon = pygame.Rect(self.x, self.y + 100, 326, 50)
    def ret_hp(self):
        return self.hp

    def dammaged(self):
        self.hp -= 20

    def ret_p(self):
        return self.UFO_polygon

    def st_2(self, screen):
        screen.blit(self.ufo_image, (self.x, self.y))
        pygame.draw.rect(screen, "RED", (self.x + 10, self.y - 30, 0.15 * 0.5 * self.hp, 5))
        self.UFO_polygon = pygame.Rect(self.x, self.y, 326, 200)

class Level1:
    def __init__(self):
        self.wave_1 = [Sniper(1000, 100), Sniper(1000, 700), Sniper(1100, 250),
                       Sniper(1100, 400), Sniper(1100, 550)]
        self.wave_2 = [Sniper(700, 250), Sniper(700, 550), Sniper(700, 700),
                       Sniper(1000, 350), Sniper(1000, 450)]
        self.wave_3 = [Sniper(800, 150), Sniper(750, 350), Sniper(800, 500),
                       Sniper(1000, 550), Sniper(1000, 700)]
        self.wave_4 = [Sniper(1100, y) for y in range(50, 751, 100)]
        self.waves = [self.wave_1, self.wave_2, self.wave_3, self.wave_4]

    def stand_wave(self, screen, sheep):
        for i in range(len(self.waves)):
            if self.waves[i]:
                k = []
                sheep.change_bullets(screen)
                for wrag in self.waves[i]:
                    sheep.check_bullets(wrag)
                    if wrag.ret_hp() > 0:
                        k.append(wrag)
                self.waves[i] = k
                for wrag in self.waves[i]:
                    wrag.draw_ship(screen)
                for wrag in self.waves[i]:
                    if wrag.ret_type() != "breaker":
                        wrag.shot()
                for wrag in self.waves[i]:
                    if wrag.ret_type() != "breaker":
                        wrag.change_bullets(screen, sheep)
                    else:
                        wrag.check_bullets(sheep)
                break

    def check_waves(self):
        return any(self.waves)


class Level2(Level1):
    def __init__(self):
        self.wave_1 = [Breaker(800, 310), Breaker(800, 430), Sniper(1000, 400), Sniper(1000, 500),
                       Sniper(1000, 300)]
        self.wave_2 = [Breaker(600, 210), Breaker(900, 680), Breaker(700, 450), Sniper(800, 230),
                       Sniper(840, 520), Sniper(1050, 680), Sniper(1100, 100)]
        self.wave_3 = [Breaker(500, 0), Breaker(500, 90), Sniper(600, 60), Breaker(500, 600),
                       Breaker(500, 690), Sniper(600, 660), Breaker(800, 350), Sniper(900, 380),
                       Breaker(1000, 150), Sniper(1100, 180),
                       Breaker(1000, 550), Sniper(1100, 580)]
        self.waves = [self.wave_1, self.wave_2, self.wave_3]


class Level3(Level1):
    def __init__(self):
        self.wave_1 = ([Sniper(1100, y) for y in range(50, 751, 100)] +
                       [Sniper(1000, 100), Sniper(1000, 700),
                       Sniper(1100, 400), Sniper(700, 250), Sniper(700, 550),
                       Sniper(700, 700), Sniper(1000, 350), Sniper(1000, 450)])
        self.wave_2 = [Sniper(50, 100), Breaker(960, 450), Sniper(1100, 460),
                       Sniper(1020, 620), Sniper(1020, 700)]
        self.wave_3 = [Sniper(900, 100), Sniper(1000, 720), Sniper(1090, 540),
                       Sniper(950, 320), Sniper(1300, 620), Sniper(1250, 250)]
        self.waves = [self.wave_1, self.wave_2, self.wave_3]


class Level4(Level1):
    def __init__(self):
        self.wave_1 = [HardSniper(1000,100), HardSniper(1100, 300), HardSniper(1100, 500),
                       HardSniper(1000, 700)]
        self.wave_2 = [Breaker(800, 670), HardSniper(900, 750), HardSniper(900, 650),
                       HardSniper(1000, 100), Sniper(1100, 350), Sniper(700, 500)]
        self.wave_3 = [Sniper(820, 100), HardSniper(980, 120), Sniper(1100, 110),
                       HardSniper(900, 310), HardSniper(1080, 270), Sniper(1100, 500),
                       HardSniper(960, 550), Sniper(1010, 600), HardSniper(1100, 700)]
        self.waves = [self.wave_1, self.wave_2, self.wave_3]

class Level5:
    def __init__(self):
        self.ufo = UFO(1050, 400)

    def stand_wave(self, screen, sheep):
        if self.ufo.ret_hp() > 0:
            self.ufo.draw_ship(screen)
            sheep.change_bullets(screen)
            sheep.check_bullets(self.ufo)
            if self.ufo.ret_hp() > 3000:
                self.ufo.motion(sheep)
                self.ufo.shot()
                self.ufo.change_bullets(screen, sheep)
            elif self.ufo.ret_hp() > 2000:
                self.ufo.mot_to(1050, 400)
                self.ufo.st_2(screen)
                self.ufo.shot_2()
                self.ufo.change_bullets(screen, sheep)
            elif self.ufo.ret_hp() > 1000:
                self.ufo.motion_3(sheep)
                self.ufo.change_bullets(screen, sheep)
            else:
                self.ufo.mot_to(1050, 400)
                self.ufo.st_2(screen)
                self.ufo.shot_3()
                self.ufo.change_bullets(screen, sheep)

    def check_waves(self):
        return self.ufo.ret_hp() > 0