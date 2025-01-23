import pygame

from funcs import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('Космические войны')
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    menu = Menu()
    ship = Ship()

    running = True
    ground = False
    down = False
    up = False
    left = False
    righ = False
    level = 0

    while running:
        pygame.display.flip()
        if level == "1_lvl":
            draw_space(screen)
            ship.draw_ship(screen)
        if not ground:
            menu.menu(screen, False)
            ground = True
            level = "menu"
        if down:
            ship.go_down()
        if up:
            ship.go_up()
        if left:
            ship.go_left()
        if righ:
            ship.go_right()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if level == "menu" and event.type == pygame.MOUSEMOTION:
                if menu.star_game_polygon.collidepoint(event.pos):
                    menu.menu(screen,True)
                else:
                    menu.menu(screen, False)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if level == "menu" and menu.star_game_polygon.collidepoint(event.pos):
                    level = "1_lvl"
                    draw_space(screen)
                    ship.draw_ship(screen)
            if event.type == pygame.KEYDOWN:
                if level != "menu" and event.key == pygame.K_s:
                    down = True
                if level != "menu" and event.key == pygame.K_w:
                    up = True
                if level != "menu" and event.key == pygame.K_d:
                    righ = True
                if level != "menu" and event.key == pygame.K_a:
                    left = True
            if event.type == pygame.KEYUP:
                if level != "menu" and event.key == pygame.K_s:
                    down = False
                if level != "menu" and event.key == pygame.K_w:
                    up = False
                if level != "menu" and event.key == pygame.K_d:
                    righ = False
                if level != "menu" and event.key == pygame.K_a:
                    left = False


    pygame.quit()