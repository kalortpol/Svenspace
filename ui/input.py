import pygame
from time import time

def update_keyboard(m):
    k = pygame.key.get_pressed()
    event = m.event
    weapons = m.weapons


    if k[pygame.K_ESCAPE]:
        event.post(event.QUIT)

    """
    ship controls
    """
    if k[pygame.K_a]:
        event.post(event.TURN, 0, 1)
    if k[pygame.K_d]:
        event.post(event.TURN, 0, -1)
    if k[pygame.K_w]:
        event.post(event.THRUST, 0, 0)
    if k[pygame.K_s]:
        event.post(event.REVERSE_THRUST, 0, 0)

    """
    Weapon controls
    """
    if k[pygame.K_1]:
        if kcd(m):
            event.post(event.WEAPON_ACTIVATION, 0, 1)
    if k[pygame.K_2]:
        if kcd(m):
            event.post(event.WEAPON_ACTIVATION, 0, 2)
    if k[pygame.K_3]:
        if kcd(m):
            event.post(event.WEAPON_ACTIVATION, 0, 3)
    if k[pygame.K_4]:
        if kcd(m):
            event.post(event.WEAPON_ACTIVATION, 0, 4)



def kcd(m):
    lc = m.cfg.last_keyboard_press
    cd = m.cfg.keyboard_cd

    if time() > lc + cd:
        m.cfg.last_keyboard_press = time()
        return True
    else:
        return False
