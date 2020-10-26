import pygame
from time import time


def shipyard_menu_OLD(m):
    ship_builder = m.ship_builder
    render = m.render
    image_module = m.image
    cfg = m.cfg
    button = m.button
    weapons = m.weapons
    ship_addons = m.ship_addons

    done = False
    click_cd = 0.5
    last_click = 0

    print("|| SHIPYARD ||")
    menu_choice = None

    current_ship_choices = {"engine": ship_builder.engine1,
                            "wingbody": ship_builder.wingbody1,
                            "cockpit": ship_builder.cockpit1,
                            "wings": ship_builder.wings1,
                            "shield": ship_addons.shield1,
                            "reverse_thruster": ship_addons.reverse_thruster1,
                            "side_thruster": ship_addons.side_thruster1,
                            "power_plant": ship_addons.power_plant3}

    while not done:
        pygame.event.poll()
        render.blit_image_as_background(cfg.menu_bg_image, m)

        # create background color for the ship parts
        bggrey = pygame.Surface((192, 1000))
        bggrey.fill((20, 20, 20))
        cfg.background.blit(bggrey, (0, 0))

        bggrey2 = pygame.Surface((500, 1000))
        bggrey.fill((30, 30, 30))
        cfg.background.blit(bggrey, (192, 0))

        # build ship button
        render.blit_image_on_background("t_build_ship.png", (0, 0), m)

        # buttons to select ship parts

        """
        COCKPIT
        """
        if button.clickable("t_cockpit.png", (0, 64), m):
            menu_choice = "cockpit"

        if menu_choice == "cockpit":
            if button.clickable(ship_builder.cockpit1.image, (200, 100), m):
                current_ship_choices["cockpit"] = ship_builder.cockpit1
            if button.clickable(ship_builder.cockpit2.image, (300, 100), m):
                current_ship_choices["cockpit"] = ship_builder.cockpit2
            if button.clickable(ship_builder.cockpit3.image, (200, 200), m):
                current_ship_choices["cockpit"] = ship_builder.cockpit3
            if button.clickable(ship_builder.cockpit4.image, (300, 200), m):
                current_ship_choices["cockpit"] = ship_builder.cockpit4
            if button.clickable(ship_builder.cockpit5.image, (200, 300), m):
                current_ship_choices["cockpit"] = ship_builder.cockpit5

        """
        WINGBODY
        """
        if button.clickable("t_wingbody.png", (0, 128), m):
            menu_choice = "wingbody"

        if menu_choice == "wingbody":
            if button.clickable(ship_builder.wingbody1.image, (200, 100), m):
                current_ship_choices["wingbody"] = ship_builder.wingbody1
            if button.clickable(ship_builder.wingbody2.image, (300, 100), m):
                current_ship_choices["wingbody"] = ship_builder.wingbody2
            if button.clickable(ship_builder.wingbody3.image, (200, 200), m):
                current_ship_choices["wingbody"] = ship_builder.wingbody3

        """
        WINGS
        """
        if button.clickable("t_wings.png", (0, 192), m):
            menu_choice = "wings"

        if menu_choice == "wings":
            if button.clickable(ship_builder.wings1.image, (200, 100), m):
                current_ship_choices["wings"] = ship_builder.wings1
            if button.clickable(ship_builder.wings2.image, (300, 100), m):
                current_ship_choices["wings"] = ship_builder.wings2
            if button.clickable(ship_builder.wings3.image, (200, 200), m):
                current_ship_choices["wings"] = ship_builder.wings3
            if button.clickable(ship_builder.wings4.image, (200, 300), m):
                current_ship_choices["wings"] = ship_builder.wings4
            if button.clickable(ship_builder.wings5.image, (200, 400), m):
                current_ship_choices["wings"] = ship_builder.wings5
        """
        ENGINE
        """
        if button.clickable("t_engine.png", (0, 256), m):
            menu_choice = "engine"

        if menu_choice == "engine":
            if button.clickable(ship_builder.engine1.image, (200, 100), m):
                current_ship_choices["engine"] = ship_builder.engine1
            if button.clickable(ship_builder.engine2.image, (300, 100), m):
                current_ship_choices["engine"] = ship_builder.engine2
            if button.clickable(ship_builder.engine3.image, (200, 200), m):
                current_ship_choices["engine"] = ship_builder.engine3

        """
        WEAPONS
        """
        if button.clickable("t_weapons.png", (0, 500), m):
            menu_choice = "weapons"

        if menu_choice == "weapons":
            if current_ship_choices["wings"].slots == 1:
                # this means only 1 slot on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"

            if current_ship_choices["wings"].slots == 2:
                # this means 2 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"

            if current_ship_choices["wings"].slots == 3:
                # this means 3 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"

            if current_ship_choices["wings"].slots == 4:
                # this means 4 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"
                if button.clickable("t_slot4.png", (192, 692), m):
                    menu_choice = "weapons_slot4"

        """
        Slot submenus
        """

        if menu_choice == "weapons_slot1":
            # weapons go here, copy paste this into all other weapon slot sub-routines
            if button.clickable(weapons.laser1.image, (200, 100), m):
                current_ship_choices[menu_choice] = weapons.make_weapon("laser1")

            # below is terrible but necessary
            if current_ship_choices["wings"].slots == 1:
                # this means only 1 slot on each wing
                if button.clickable("t_slot1p.png", (192, 500), m):
                    menu_choice = "weapons_slot1"

            if current_ship_choices["wings"].slots == 2:
                # this means 2 slots on each wing
                if button.clickable("t_slot1p.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"

            if current_ship_choices["wings"].slots == 3:
                # this means 3 slots on each wing
                if button.clickable("t_slot1p.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"

            if current_ship_choices["wings"].slots == 4:
                # this means 4 slots on each wing
                if button.clickable("t_slot1p.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"
                if button.clickable("t_slot4.png", (192, 692), m):
                    menu_choice = "weapons_slot4"

        if menu_choice == "weapons_slot2":
            # weapons go here, copy paste this into all other weapon slot sub-routines
            if button.clickable(weapons.laser1.image, (200, 100), m):
                current_ship_choices[menu_choice] = weapons.make_weapon("laser1")

            # below is terrible but necessary
            if current_ship_choices["wings"].slots == 1:
                # this means only 1 slot on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"

            if current_ship_choices["wings"].slots == 2:
                # this means 2 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2p.png", (192, 564), m):
                    menu_choice = "weapons_slot2"

            if current_ship_choices["wings"].slots == 3:
                # this means 3 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2p.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"

            if current_ship_choices["wings"].slots == 4:
                # this means 4 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2p.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"
                if button.clickable("t_slot4.png", (192, 692), m):
                    menu_choice = "weapons_slot4"

        if menu_choice == "weapons_slot3":
            # weapons go here, copy paste this into all other weapon slot sub-routines
            if button.clickable(weapons.laser1.image, (200, 100), m):
                current_ship_choices[menu_choice] = weapons.make_weapon("laser1")

            # below is terrible but necessary
            if current_ship_choices["wings"].slots == 1:
                # this means only 1 slot on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"

            if current_ship_choices["wings"].slots == 2:
                # this means 2 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"

            if current_ship_choices["wings"].slots == 3:
                # this means 3 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3p.png", (192, 628), m):
                    menu_choice = "weapons_slot3"

            if current_ship_choices["wings"].slots == 4:
                # this means 4 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3p.png", (192, 628), m):
                    menu_choice = "weapons_slot3"
                if button.clickable("t_slot4.png", (192, 692), m):
                    menu_choice = "weapons_slot4"

        if menu_choice == "weapons_slot4":
            # weapons go here, copy paste this into all other weapon slot sub-routines
            if button.clickable(weapons.laser1.image, (200, 100), m):
                current_ship_choices[menu_choice] = weapons.make_weapon("laser1")

            # below is terrible but necessary
            if current_ship_choices["wings"].slots == 1:
                # this means only 1 slot on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"

            if current_ship_choices["wings"].slots == 2:
                # this means 2 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"

            if current_ship_choices["wings"].slots == 3:
                # this means 3 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"

            if current_ship_choices["wings"].slots == 4:
                # this means 4 slots on each wing
                if button.clickable("t_slot1.png", (192, 500), m):
                    menu_choice = "weapons_slot1"
                if button.clickable("t_slot2.png", (192, 564), m):
                    menu_choice = "weapons_slot2"
                if button.clickable("t_slot3.png", (192, 628), m):
                    menu_choice = "weapons_slot3"
                if button.clickable("t_slot4p.png", (192, 692), m):
                    menu_choice = "weapons_slot4"

        """
        QUIT
        """
        if button.clickable("t_quit.png", (832, 0), m):
            print("quit")
            break

        """
        MAKE SHIP SURFACE
        """

        sps = ship_builder.make_ship_surface(current_ship_choices, m)

        """
        BLIT IT
        """
        render.blit_surface_centered(sps, (768, 374), m)

        # continue button
        if button.clickable("t_go.png", (832, 704), m):
            return current_ship_choices
        # update screen
        render.draw_to_screen(m)
        render.update()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            done = True


def shipyard_menu(shipdict, m, cheats=False):
    render = m.render
    cfg = m.cfg
    button = m.button.mouse_over_clickable
    inv = m.inventory.get(cfg.playerdict["current_ship"], m)
    sid = cfg.playerdict["current_ship"]

    sd = shipdict

    # menu loop
    done = False

    while not done:
        # background
        menu_bg(m)
        top_blackish_border(m)
        left_blackish_border(m)

        # ship preview
        ship_preview(sd, m)

        # debug/testing/cheat button
        if button("t_debug_give_all.png", (400, 0), m):
            print("Not implemented ;)")

        # buttons

        if button("t_cockpit.png", (0, 68), m):
            sd = part_equip_ui(sd, "cockpit", m)
        if button("t_wingbody.png", (0, 68*2), m):
            sd = part_equip_ui(sd, "wingbody", m)
        if button("t_wings.png", (0, 68*3), m):
            sd = part_equip_ui(sd, "wings", m)
        if button("t_power_plant.png", (0, 68*4), m):
            sd = part_equip_ui(sd, "power_plant", m)
        if button("t_engine.png", (0, 68*5), m):
            sd = part_equip_ui(sd, "engine", m)
        if button("t_weapons.png", (0, 68*6), m):
            menu_choice = "weapon_selection"

        # flow buttons
        if button("t_quit.png", (832, 0), m):
            pygame.quit()

        if button("t_go.png", (832, 704), m):
            done = True

        # update

        menu_update(m)

    # return the shipdict
    return sd


def ship_preview(shipdict, m):
    render = m.render
    sb = m.ship_builder
    cfg = m.cfg
    rot = pygame.transform.rotate



    ship_surface = rot(sb.make_ship_surface(shipdict, m), m.cfg.world_ships[cfg.playerdict["current_ship"]].angle - 90)
    ship_surface_size = ship_surface.get_size()

    render.blit_surface_centered(ship_surface, (1024/2, 748/2), m)

    # service ships
    render.blit_image_on_background("service_ship1.png", (1024/2 - ship_surface_size[0], 748/2), m)
    render.blit_image_on_background("service_ship1.png", (1024 / 2 + ship_surface_size[0], 748 / 2), m, rotate=180)

    render.blit_image_on_background("service_ship1.png", (1024 / 2, 748 / 2 - ship_surface_size[1] -100), m, rotate=-90)
    render.blit_image_on_background("service_ship1.png", (1024 / 2, 748 / 2 + ship_surface_size[0]), m, rotate=90)
"""
SUB MENU TEMPLATE:

def submenu(shipdict, m):
    render = m.render
    cfg = m.cfg
    sd = shipdict

    done = False

    while not done:
        menu_bg(m)
        done = submenu_standard_top(sd, m)
        
        [[[ BODY OF SUBMENU HERE ]]]
        
        menu_update(m)

    return sd
    
///
Call submenu with sd = submenu() to allow changing of ship dict.
/// 

!!! 
Sub-submenus can be called from a submenu the same way
!!!
"""


def wingbody_selection(shipdict, m, cheats=False):
    render = m.render
    cfg = m.cfg
    inv = m.inventory
    sd = shipdict

    # this is universal
    available_parts = inv.get_stash_part(cfg.playerdict["current_ship"], "wingbody", m)
    if cheats:
        available_parts = m.cfg.all_ship_parts["wingbody"]

    done = False

    while not done:
        menu_bg(m)
        done = submenu_standard_elems(sd, m)

        # [[[BODY OF SUBMENU HERE]]]
        for p in available_parts:
            print(p)

        menu_update(m)

    return sd


def weapon_selection(current_ship_choices, m):

    render = m.render
    cfg = m.cfg
    button = m.button.clickable

    done = False

    while not done:

        if current_ship_choices["wings"].slots == 1:
            if button("t_slot1.png", (192, 500), m):
                weapon_slot_select(1, m)

        if current_ship_choices["wings"].slots == 2:
            if button("t_slot1.png", (192, 500), m):
                weapon_slot_select(1, m)
            if button("t_slot2.png", (192, 564), m):
                menu_choice = "weapons_slot2"

        if current_ship_choices["wings"].slots == 3:
            # this means 3 slots on each wing
            if button("t_slot1.png", (192, 500), m):
                weapon_slot_select(1, m)
            if button("t_slot2.png", (192, 564), m):
                menu_choice = "weapons_slot2"
            if button("t_slot3.png", (192, 628), m):
                menu_choice = "weapons_slot3"

        if current_ship_choices["wings"].slots == 4:
            # this means 4 slots on each wing
            if button("t_slot1.png", (192, 500), m):
                weapon_slot_select(1, m)
            if button("t_slot2.png", (192, 564), m):
                menu_choice = "weapons_slot2"
            if button("t_slot3.png", (192, 628), m):
                menu_choice = "weapons_slot3"
            if button("t_slot4p.png", (192, 692), m):
                menu_choice = "weapons_slot4"


def menu_bg(m):
    """
    Displays menu background, also polls pygame event
    """
    render = m.render
    cfg = m.cfg

    pygame.event.poll()
    render.blit_image_as_background(cfg.menu_bg_image, m)


def weapon_slot_select(slot, m):
    pass


def top_blackish_border(m):
    cfg = m.cfg

    bggrey = pygame.Surface((1080, 64))
    bggrey.fill((20, 20, 20))
    cfg.background.blit(bggrey, (0, 0))


def left_blackish_border(m):
    cfg = m.cfg

    bggrey = pygame.Surface((192, 1000))
    bggrey.fill((20, 20, 20))
    cfg.background.blit(bggrey, (0, 0))


def submenu_standard_elems(shipdict, m):
    render = m.render
    cfg = m.cfg
    mobutton = m.button.mouse_over_clickable
    sd = shipdict

    top_blackish_border(m)
    left_blackish_border(m)

    if mobutton("t_back.png", (0, 0), m):
        return True

    if mobutton("t_quit.png", (832, 0), m):
        pygame.quit()


def menu_update(m):
    render = m.render
    cfg = m.cfg

    m.in_game_ui.init(m)
    render.draw_to_screen(m)
    render.draw_ui_to_screen(cfg)
    render.update()


def get_player_ship(m):
    return m.cfg.world_ships[m.cfg.playerdict["current_ship"]]


def part_equip_ui(shipdict, ship_part, m):
    render = m.render
    cfg = m.cfg
    button = m.button.clickable
    mobutton = m.button.mouse_over_clickable
    sid = cfg.playerdict["current_ship"]
    ui = m.in_game_ui
    imod = m.inventory

    sd = shipdict

    # menu loop
    done = False

    while not done:

        # update inventory if it changes in an iteration
        inv = m.inventory.get(cfg.playerdict["current_ship"], m)

        # background
        menu_bg(m)
        top_blackish_border(m)
        left_blackish_border(m)

        # ship preview
        ship_preview(sd, m)

        # buttons
        # determine if there are parts to show
        stash = imod.get_stash_part(sid, ship_part, m)

        if len(stash) > 0:

            position = 0
            counter = 0
            for p in stash:

                # determine position based on number after the name. ONLY SUPPORTS 9 PARTS
                # TODO fix so it supports unlimited amounts of parts
                for s in p.name:
                    if s.isdigit():
                        position = int(s)

                # create a button and offset it with position
                if mobutton(p.image, (64, 100 * position), m):
                    # print(sid, "trying to equip:", p.name, "stash:", [s.name for s in stash])
                    sd = imod.equip(sid, ship_part, p.name, shipdict, m)  # must pass part as string -> p.name!



        # flow buttons
        if mobutton("t_quit.png", (832, 0), m):
            pygame.quit()

        if mobutton("t_back.png", (0, 0), m):
            done = True

        # update

        menu_update(m)

    # return the shipdict
    return sd

