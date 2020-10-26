"""
Startup script

Keep game loop and menu separate
Save state globally in cfg module

Use ECS type of system

Use as much functional programming as possible
"""
import pygame
pygame.init()

from config import cfg
from config import menus
from render import render
from events import event
from events import event_sorter
from maps import maps
from assets import image
from engine import shipyard
from ship_module import ship_builder
from ship_module import ship
from ship_module import ship_parts
from ship_module import weapons
from ship_module import inventory
from ship_module import ship_part_loader
from engine import main_loop
from engine import render_loop
from engine import ship_processors
from engine import new_frame_events
from ui import button
from ui import input
from ui import in_game_ui
from flow_control import new_game


class Dependencies:
    """
    This is to simplify dependency injection.
    Maybe it's ugly, but it speeds up programming
    """
    def __init__(self,
                 render,
                 maps,
                 image,
                 ship_builder,
                 button,
                 cfg,
                 event,
                 shipyard,
                 ship,
                 main_loop,
                 render_loop,
                 event_sorter,
                 input,
                 ship_processors,
                 ship_parts,
                 weapons,
                 inventory,
                 new_frame_events,
                 ship_part_loader,
                 new_game,
                 in_game_ui):
        self.render = render
        self.meps = maps
        self.image = image
        self.ship_builder = ship_builder
        self.button = button
        self.cfg = cfg
        self.event = event
        self.shipyard = shipyard
        self.ship = ship
        self.main_loop = main_loop
        self.render_loop = render_loop
        self.event_sorter = event_sorter
        self.input = input
        self.ship_processors = ship_processors
        self.ship_parts = ship_parts
        self.weapons = weapons
        self.inventory = inventory
        self.new_frame_events = new_frame_events
        self.ship_part_loader = ship_part_loader
        self.new_game = new_game
        self.in_game_ui = in_game_ui

m = Dependencies(render,
                 maps,
                 image,
                 ship_builder,
                 button,
                 cfg,
                 event,
                 shipyard,
                 ship,
                 main_loop,
                 render_loop,
                 event_sorter,
                 input,
                 ship_processors,
                 ship_parts,
                 weapons,
                 inventory,
                 new_frame_events,
                 ship_part_loader,
                 new_game,
                 in_game_ui)  # pass this around instead of all separate dependencies


def main():
    main_menu = menus.start_up(m)
    choice = main_menu(m)

    # init modules
    in_game_ui.init(m)
    ship_part_loader.init_all_ship_parts(m)
    new_game.init_new_game(m)
    inventory.give_new(0, "cockpit", "cockpit2", m)
    inventory.give_new(0, "cockpit", "cockpit3", m)
    inventory.give_new(0, "cockpit", "cockpit4", m)
    inventory.give_new(0, "wingbody", "wingbody2", m)
    inventory.give_new(0, "wingbody", "wingbody3", m)
    inventory.give_new(0, "power_plant", "power_plant2", m)
    inventory.give_new(0, "power_plant", "power_plant3", m)
    inventory.give_new(0, "engine", "engine2", m)
    inventory.give_new(0, "engine", "engine3", m)
    inventory.give_new(0, "wings", "wings2", m)
    inventory.give_new(0, "wings", "wings3", m)
    inventory.give_new(0, "wings", "wings4", m)
    inventory.give_new(0, "wings", "wings5", m)
    if choice == 2:
        m.main_loop.main_loop(m)


    print("|| END OF MAIN ||")


if __name__ == "__main__":
    main()
