import pygame
"""
State vars
"""

current_menu = "start_up"


"""
Renderer vars
"""

# the following vars are initialized when passed to render.init()
screen = None
map_data = None
tile_size = None

width, height = 1024, 768  # screen size

background = pygame.Surface((width, height))  # this is the actual background. Blit anything on top of it
ui_surface = None
"""
Map_vars
"""
current_map = "test_map.tmx"

"""
Menu vars
"""
menu_bg_image = "spaceblue.png"

"""
Ship vars
"""
world_ships = {}
starting_shipdict = {"cockpit": "cockpit1",
                     "wingbody": "wingbody1",
                     "wings": "wings1",
                     "power_plant": "power_plant1",
                     "engine": "engine1",
                     "shield": "shield1",
                     "side_thruster": "side_thruster1",
                     "reverse_thruster": "reverse_thruster1",
                     "wslot1": None,
                     "wslot2": None,
                     "wslot3": None,
                     "wslot4": None}

"""
Ship part vars
"""

# ALL the ship parts!
# Initialized from ship_part_loader
all_ship_parts = {"cockpit": {},
                  "wingbody": {},
                  "wings": {},
                  "power_plant": {},
                  "engine": {},
                  "shield": {},
                  "side_thruster": {},
                  "reverse_thruster": {},
                  "weapons": {}
                  }


# every SID has its own inventory
all_ship_inventories = {}

"""
Sprite vars
"""
shipgroup = pygame.sprite.Group()

"""
Player vars
"""
playerdict = {"current_ship": 0}
"""
Mouse vars
"""
last_click = 0
click_cd = 0.5

"""
Keyboard vars
"""
last_keyboard_press = 0
keyboard_cd = 0.5

"""
Text vars
"""
font = pygame.font.Font(pygame.font.get_default_font(), 36)
