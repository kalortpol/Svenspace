import pygame
from time import time
"""
Template:
if button.clickable(image_file_name, (posx, posy), (sizex, sizey), cfg_module, render_module, image_module)
"""


def clickable(image, pos, m):
    """
    Principle:
    Draws itself on the screen at position when called (do so every frame it is supposed to exist)
    When clicked, it will return "True"

    Use like this:
    if button("image.png", (100, 100), (64, 64), cfg, render):
        * action when button is clicked *

    Dependencies:
    * Render to blit itself
    * cfg to access background
    * image to load image
    """
    render = m.render
    image_module = m.image
    cfg = m.cfg

    image = image_module.load(image)
    size = image.get_size()

    render.blit_surface_on_background(image, pos, m)
    button_area = pos[0] + size[0], pos[1] + size[1]
    rangex = range(pos[0], button_area[0])
    rangey = range(pos[1], button_area[1])
    if pygame.mouse.get_pressed()[0]:
        if cfg.last_click + cfg.click_cd < time():
            if pygame.mouse.get_pos()[0] in rangex and pygame.mouse.get_pos()[1] in rangey:
                cfg.last_click = time()
                return True
    else:
        return False


def clickable_ui(image, pos, m):
    """
    Principle:
    Draws itself on the screen at position when called (do so every frame it is supposed to exist)
    When clicked, it will return "True"

    Use like this: !!!!!!! OLD !!!!!!!!!!!!!
    if button("image.png", (100, 100), (64, 64), cfg, render):
        * action when button is clicked *

    Dependencies:
    * Render to blit itself
    * cfg to access background
    * image to load image
    """
    render = m.render
    image_module = m.image
    cfg = m.cfg

    image = image_module.load(image)
    size = image.get_size()

    cfg.ui_surface.blit(image, pos)
    button_area = pos[0] + size[0], pos[1] + size[1]
    rangex = range(pos[0], button_area[0])
    rangey = range(pos[1], button_area[1])
    if pygame.mouse.get_pressed()[0]:
        if cfg.last_click + cfg.click_cd < time():
            if pygame.mouse.get_pos()[0] in rangex and pygame.mouse.get_pos()[1] in rangey:
                cfg.last_click = time()
                return True
    else:
        return False


def mouse_over_clickable(image, pos, m, color=(255, 255, 255)):
    render = m.render
    image_module = m.image
    cfg = m.cfg

    normal_image = image_module.load(image)
    size = normal_image.get_size()
    surf = cfg.background

    surf.blit(normal_image, pos)
    button_area = pos[0] + size[0], pos[1] + size[1]
    rangex = range(pos[0], button_area[0])
    rangey = range(pos[1], button_area[1])

    if pygame.mouse.get_pos()[0] in rangex and pygame.mouse.get_pos()[1] in rangey:
        # make a border around the button
        pygame.draw.rect(surf, color, pygame.Rect((pos[0] - 2, pos[1] - 2), (size[0] + 4, size[1] + 4)))
        surf.blit(normal_image, pos)

    if pygame.mouse.get_pressed()[0]:
        if cfg.last_click + cfg.click_cd < time():
            if pygame.mouse.get_pos()[0] in rangex and pygame.mouse.get_pos()[1] in rangey:
                cfg.last_click = time()
                return True
    else:
        return False


def mouse_over_clickable_ui(image, pos, m, color=(255, 255, 255)):
    render = m.render
    image_module = m.image
    cfg = m.cfg

    normal_image = image_module.load(image)
    size = normal_image.get_size()
    surf = cfg.ui_surface

    surf.blit(normal_image, pos)
    button_area = pos[0] + size[0], pos[1] + size[1]
    rangex = range(pos[0], button_area[0])
    rangey = range(pos[1], button_area[1])

    if pygame.mouse.get_pos()[0] in rangex and pygame.mouse.get_pos()[1] in rangey:
        # make a border around the button
        pygame.draw.rect(surf, color, pygame.Rect((pos[0] - 2, pos[1] - 2), (size[0] + 4, size[1] + 4)))
        surf.blit(normal_image, pos)

    if pygame.mouse.get_pressed()[0]:
        if cfg.last_click + cfg.click_cd < time():
            if pygame.mouse.get_pos()[0] in rangex and pygame.mouse.get_pos()[1] in rangey:
                cfg.last_click = time()
                return True
    else:
        return False