import pygame
from time import time


def start_up(modules):
    cfg = modules.cfg
    render = modules.render

    cfg.screen = render.init_screen(1024, 768, "SVENSPACE - Main Menu")
    return main_menu


def main_menu(m):
    render = m.render
    image_module = m.image
    cfg = m.cfg
    button = m.button.mouse_over_clickable

    done = False
    click_cd = 0.5
    last_click = 0
    while not done:
        pygame.event.poll()
        render.blit_image_as_background(cfg.menu_bg_image, m)
        if button("t_new_game.png", (000, 100), m):
            return 2
        if button("t_load.png", (000, 200), m):
            return 1
        if button("t_quit.png", (832, 0), m):
            return 0
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            done = True

        render.draw_to_screen(m)
        render.update()


