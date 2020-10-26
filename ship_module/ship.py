"""
Ship class
* Per-pixel collision detection (maybe)?
* Use sprites
* Ship surface = sprite image is made by ship_module
* Keep track of all parts of the ship
* Ship and player is separate, easy changing of ships
* Player is it's own sprite, a small human in a space suit
"""
# TODO pass in ship dict and not separate parts and change the function creating the ship surface

import pygame
import math


class Ship(pygame.sprite.Sprite):
    def __init__(self, sid, shipdict, m, alive=False, visible=False):
        super().__init__()
        self.m = m  # dependencies
        self.sid = sid  # ship id
        self.shipdict = shipdict

        """
        Vectorized movement
        """
        self.angle = 0
        self.vel = [0, 0]  # velocity x and y
        self.thrust = 0
        self. reverse_thrust = 0
        self.after_burner_thrust = 0

        """
        Position
        """
        self.pos = [512, 374]

        """
        Ship parts
        """
        self.cockpit = self.shipdict["cockpit"]
        self.wingbody = self.shipdict["wingbody"]
        self.wings = self.shipdict["wings"]
        self.engine = self.shipdict["engine"]

        self.shield = self.shipdict.get("shield")
        self.power_plant = self.shipdict.get("power_plant")

        self.weapon1 = self.shipdict.get("weapons_slot1")
        self.weapon2 = self.shipdict.get("weapons_slot2")
        self.weapon3 = self.shipdict.get("weapons_slot3")
        self.weapon4 = self.shipdict.get("weapons_slot4")

        self.reverse_thruster = self.shipdict.get("reverse_thruster")
        self.side_thruster = self.shipdict.get("side_thruster")

        """
        Ship states
        """
        self.after_burning = False
        """
        Ship stats, comes from ship parts (not implemented) 
        """
        # TODO
        self.shield = 1
        self.hp = 1

        self.image, self.cs, self.wbs, self.wls, self.es = m.ship_builder.make_ship_surface(self.shipdict,
                                                                                            m,
                                                                                            return_sizes=True)

        self.weight = 0  # calculate this from the area of the ship body. Heavier = slower turn rate
        self.bkp_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.mask = pygame.mask.from_surface(self.image)

        self.alive = alive
        self.visible = visible
        self.group_update = False

        print("[ship]", self.sid, "created")
        if self.visible:
            self.add(m.cfg.shipgroup)
            print("[ship]", self.sid, "added to group")

    def update(self):
        self.rotate_sprite()
        self.apply_thrust()

        if self.group_update:
            if self.visible:
                if self not in self.m.cfg.shipgroup:
                    self.add(self.m.cfg.shipgroup)
                    self.group_update = False
                    print(self.sid, "added to", self.m.cfg.shipgroup)
            if not self.visible:
                if self in self.m.cfg.shipgroup:
                    self.remove(self.m.cfg.shipgroup)
                    self.group_update = False
                    print(self.sid, "removed from", self.m.cfg.shipgroup)

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.friction()  # apply friction
        self.decrease_thrust()  # nullify thrust at the end of update or accelerate indefinately

        self.rect.center = self.pos[0], self.pos[1]

    def rotate_sprite(self):
        # TODO sprite pivots around engine, which is not intended... fix
        # TODO all engines are 92 y, which offsets the center with the invisible surface area
        old_rect = self.rect.centerx, self.rect.centery
        correction_image = pygame.transform.rotate(self.bkp_image, -90)
        self.image = pygame.transform.rotate(correction_image, self.angle)
        self.rect = self.image.get_rect()

        # compensate for different sizes of parts to get true center y
        true_center_offset = -(self.es[1] + (self.wbs[1] / 2))

        # TODO still not working
        self.rect.center = old_rect[0], old_rect[1] + true_center_offset

    def apply_thrust(self):
        angle = math.radians(self.angle)  # convert to radians or .math's sin/cos won't work
        thrust_x = -self.thrust * math.cos(angle)
        thrust_y = -self.thrust * math.sin(angle)

        reverse_thrust_x = -self.reverse_thrust * math.cos(angle)
        reverse_thrust_y = self.reverse_thrust * math.sin(angle)

        #print(thrust_x, thrust_y)
        self.vel[0] += -thrust_x + reverse_thrust_x
        self.vel[1] += thrust_y + reverse_thrust_y

    def apply_after_burner_thrust(self):
        angle = math.radians(self.angle)  # convert to radians or .math's sin/cos won't work
        thrust_x = -self.after_burner_thrust * math.cos(angle)
        thrust_y = -self.after_burner_thrust * math.sin(angle)
        # print(thrust_x, thrust_y)
        self.vel[0] += -thrust_x
        self.vel[1] += thrust_y

    def decrease_thrust(self):
        self.thrust = 0

    def friction(self):
        constant = 0.0001
        if -0.0001 < abs(self.vel[0]) < 0.0001:
            self.vel[0] = 0
        if -0.0001 < abs(self.vel[1]) < 0.0001:
            self.vel[1] = 0

        if self.vel[0] > 0:
            self.vel[0] -= constant
        if self.vel[0] < 0:
            self.vel[0] += constant
        if self.vel[1] > 0:
            self.vel[1] -= constant
        if self.vel[1] < 0:
            self.vel[1] += constant

    def remake_ship_surface(self):
        """
        Need to change bkp_image to make permanent changes, it's the surface that gets rotated to give self.image

        Used mainly to animate ship parts, if a ship part is changed this is not the correct way to do it.
        Then use remake_ship_from_dict.
        """
        # print("[ship][remake_ship_surface]")
        # TODO this is called every frame. IF NEEDED optimize
        m = self.m
        self.bkp_image, self.cs, self.wbs, self.wls, self.es = m.ship_builder.make_ship_surface(self.shipdict,
                                                                                            m,
                                                                                            return_sizes=True)

    def self_delete(self, m):
        self.group_update = True
        self.visible = False

"""
SHIP FUNCS
"""


def remake_ship_from_dict(sid, shipdict, m):
    """
    Changes parts of an already existing ship
    """
    print("[remake_ship_from_dict] SID:", sid)
    cfg = m.cfg
    cfg.world_ships[sid].self_delete(m)
    cfg.world_ships[sid] = Ship(sid,
                                shipdict,
                                m,
                                alive=True,
                                visible=True)


def make_ship_from_dict(shipdict, m):
    """
    Creates a new ship
    """
    cfg = m.cfg
    sb = m.ship_builder

    sid = 0
    while sid in cfg.world_ships:
        sid += 1

    assert sid not in cfg.world_ships, "[make_ship_from_dict] key error - key already exists"

    cfg.world_ships[sid] = Ship(sid,
                                shipdict,
                                m,
                                alive=True,
                                visible=True)

    # create inventory for ship
    make_new_ship_inventory(shipdict, sid, m)


def make_new_ship_inventory(shipdict, sid, m):
    """
    Creates inventory for ship, erases old if there is one (to prevent duping)
    """
    cfg = m.cfg
    inv = m.cfg.all_ship_inventories
    sd = shipdict
    il = m.inventory

    inv[sid] = {}
    si = inv[sid]

    si["cockpit"] = {"equipped": [],
                     "stash": []}
    si["wingbody"] = {"equipped": [],
                     "stash": []}
    si["wings"] = {"equipped": [],
                     "stash": []}
    si["power_plant"] = {"equipped": [],
                     "stash": []}
    si["engine"] = {"equipped": [],
                     "stash": []}
    si["side_thruster"] = {"equipped": [],
                     "stash": []}
    si["reverse_thruster"] = {"equipped": [],
                     "stash": []}
    si["shield"] = {"equipped": [],
                     "stash": []}
    si["weapons"] = {"equipped": [],
                     "stash": []}

    si["cockpit"]["equipped"] = [sd["cockpit"]]
    si["wingbody"]["equipped"] = [sd["wingbody"]]
    si["wings"]["equipped"] = [sd["wings"]]
    si["power_plant"]["equipped"] = [sd["power_plant"]]
    si["engine"]["equipped"] = [sd["engine"]]
    si["reverse_thruster"]["equipped"] = [sd["reverse_thruster"]]
    si["side_thruster"]["equipped"] = [sd["side_thruster"]]
    si["shield"]["equipped"] = [sd["shield"]]
    si["weapons"]["equipped"] = []

    if "wslot1" in sd: si["weapons"]["equipped"].append(sd["wslot1"])
    if "wslot2" in sd: si["weapons"]["equipped"].append(sd["wslot2"])
    if "wslot3" in sd: si["weapons"]["equipped"].append(sd["wslot3"])
    if "wslot4" in sd: si["weapons"]["equipped"].append(sd["wslot4"])

    print("[create_new_ship_inventory] Created inventory for SID:", sid, si)


def get_ship(sid, m):
    try:
        return m.cfg.world_ships[sid]
    except KeyError:
        print("[get_ship] KEY ERROR. SID NOT IN WORLD_SHIPS")


def get_ship_dict(sid, m):
    try:
        ship = get_ship(sid, m)
        return ship.shipdict
    except KeyError:
        print("[get_ship_dict] KEY ERROR. SID NOT IN WORLD_SHIPS OR DOESN'T HAVE SHIPDICT")
