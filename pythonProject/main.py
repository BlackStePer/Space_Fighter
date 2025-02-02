from funcs import *
from Interfaises import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('Космические войны')
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    menu = Menu()
    lev_menu = LevelMenu()
    deth_menu = DethMenu()
    ship = Ship()

    running = True
    start_vis = False
    men = False
    l1 = False
    l2 = False
    level = "menu"
    lvl1 = Level1()
    lvl2 = Level2()

    down = False
    up = False
    left = False
    righ = False

    while running:
        pygame.display.flip()
        if level == "1_lvl":
            draw_space(screen)
            ship.draw_ship(screen)
            lvl1.stand_wave(screen, ship)
        if level == "2_lvl":
            draw_space(screen)
            ship.draw_ship(screen)
            lvl2.stand_wave(screen, ship)
        if level == "menu":
            menu.menu(screen, start_vis)
        if level == "ch_lvl":
            lev_menu.menu(screen, l1, l2)
        if level == "deth_menu":
            deth_menu.menu(screen, men)
        ship.go_to(righ, left, up, down)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if ship.ret_hp() <= 0:
                level = "deth_menu"
            if event.type == pygame.MOUSEMOTION:
                start_vis = True if menu.star_game_polygon.collidepoint(event.pos) and level == "menu" else False
                l1 = True if lev_menu.l1_polygon.collidepoint(event.pos) and level == "ch_lvl" else False
                l2 = True if lev_menu.l2_polygon.collidepoint(event.pos) and level == "ch_lvl" else False
                men = True if deth_menu.back_polygon.collidepoint(event.pos) and level == "deth_menu" else False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if level == "menu" and menu.star_game_polygon.collidepoint(event.pos):
                    level = "ch_lvl"
                elif level == "ch_lvl" and lev_menu.l1_polygon.collidepoint(event.pos):
                    level = "1_lvl"
                elif level == "ch_lvl" and lev_menu.l2_polygon.collidepoint(event.pos):
                    level = "2_lvl"
                elif level == "deth_menu" and deth_menu.back_polygon.collidepoint(event.pos):
                    ship = Ship()
                    lvl1 = Level1()
                    lvl2 = Level2()
                    level = "menu"
                elif level != "menu" and level != "ch_lvl" and level != "deth_menu":
                    ship.shot()
            if event.type == pygame.KEYDOWN:
                if level != "menu" and level != "ch_lvl":
                    down = event.key == pygame.K_s or down
                    up = event.key == pygame.K_w or up
                    righ = event.key == pygame.K_d or righ
                    left = event.key == pygame.K_a or left
            if event.type == pygame.KEYUP:
                if level != "menu" and level != "ch_lvl":
                    down = False if event.key == pygame.K_s else down
                    up = False if event.key == pygame.K_w else up
                    righ = False if event.key == pygame.K_d else righ
                    left = False if event.key == pygame.K_a else left
    pygame.quit()