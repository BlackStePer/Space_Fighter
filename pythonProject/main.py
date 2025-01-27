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
    start_vis = False
    level = "menu"

    down = False
    up = False
    left = False
    righ = False

    while running:
        pygame.display.flip()
        if level == "1_lvl":
            draw_space(screen)
            ship.draw_ship(screen)
        if level == "menu":
            menu.menu(screen, start_vis)
        ship.go_to(righ, left, up, down)
        ship.change_bullets(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if level == "menu" and event.type == pygame.MOUSEMOTION:
                start_vis = True if menu.star_game_polygon.collidepoint(event.pos) else False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if level == "menu" and menu.star_game_polygon.collidepoint(event.pos):
                    level = "1_lvl"
                    draw_space(screen)
                    ship.draw_ship(screen)
                if level != "menu":
                    ship.shot()
            if event.type == pygame.KEYDOWN:
                if level != "menu":
                    down = event.key == pygame.K_s or down
                    up = event.key == pygame.K_w or up
                    righ = event.key == pygame.K_d or righ
                    left = event.key == pygame.K_a or left
            if event.type == pygame.KEYUP:
                if level != "menu":
                    down = False if event.key == pygame.K_s else down
                    up = False if event.key == pygame.K_w else up
                    righ = False if event.key == pygame.K_d else righ
                    left = False if event.key == pygame.K_a else left
    pygame.quit()