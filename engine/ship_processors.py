"""
* Movement
* Collision
* Firing
* Getting hit
* Shield
* Taking hull damage
* Draining power (shield, weapons, afterburner)
* Draining fuel (engine, generator)
* Special effects

All processors only process events posted to the event queue
"""
import pygame
import math


def calculate_ship_body_area(sid, width_factor, length_factor, m):
    sd = m.cfg.world_ships

    ship_body_area = ((sd[sid].cs[0] + sd[sid].wbs[0] + sd[sid].es[0]) * width_factor) * ((sd[sid].cs[1] + sd[sid].wbs[1] + sd[sid].es[1]) * length_factor)
    return ship_body_area


def rotate(sid: int, direction: int, m):
    """
    Rotates ship, and the speed of rotation is determined by the area of the ship body
    Larger area = slower rotation
    Smaller area = faster rotation

    standardized ship area is the base area at which the ship rotates 1 degree per frame
    """
    width_factor = 1
    length_factor = 1.5

    sd = m.cfg.world_ships
    ship_body_area = calculate_ship_body_area(sid, width_factor, length_factor, m)
    standardized_ship_area = 8000

    area_ratio = standardized_ship_area / ship_body_area

    if direction > 0:
        m.event.post(m.event.R_SIDE_THRUST, sid, 0)
    else:
        m.event.post(m.event.L_SIDE_THRUST, 0, sid)

    #print(ship_body_area, area_ratio, area_ratio*1.5)
    sd[sid].angle += direction * (area_ratio * 2) * sd[sid].side_thruster.turn_factor
    #print("Trying rotate", sid, "value:", value, "sd[sid].angle value:", sd[sid].angle)


def animate_side_thrust(sid, side, m):
    ship = m.cfg.world_ships[sid]
    event = m.event

    if side == "left":

        filename_without_png = ship.side_thruster.image_file.split(".")
        image = "".join([filename_without_png[0], "f.png"])
        ship.side_thruster.imagel = image
        event.post(event.SHIP_CHANGED, sid)

    if side == "right":

        filename_without_png = ship.side_thruster.image_file.split(".")
        image = "".join([filename_without_png[0], "f.png"])
        ship.side_thruster.imager = image
        event.post(event.SHIP_CHANGED, sid)


def reset_all_side_thrust(m):
    sd = m.cfg.world_ships

    for sid in sd:
        if hasattr(sd[sid], "side_thruster"):
            sd[sid].side_thruster.imagel = sd[sid].side_thruster.image_file
            sd[sid].side_thruster.imager = sd[sid].side_thruster.image_file


def stop(sid, value, m):
    sd = m.cfg.world_ships

    sd[sid].vel = [0, 0]


def redraw_ship(sid, m):
    sd = m.cfg.world_ships
    sb = m.ship_builder
    ms = sb.make_ship_image
    i = sd[sid].image

    assert sid in sd, "[redraw_ship] Ship ID not in world_ships!"
    i, sd[sid].cs, sd[sid].wbs, sd[sid].wls, sd[sid].es = ms(sd[sid].shipdict, m, return_sizes=True)


def change_weapon_activation(sid, slot, m):
    ship = m.cfg.world_ships[sid]
    event = m.event
    if slot == 1 and ship.weapon1:
        if ship.weapon1.active:
            ship.shipdict["weapons_slot1"].active = False
            ship.shipdict["weapons_slot1"].choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0
        if not ship.weapon1.active:
            ship.weapon1.active = True
            ship.weapon1.choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0
    if slot == 2 and ship.weapon2:
        if ship.weapon2.active:
            ship.weapon2.active = False
            ship.weapon2.choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0
        if not ship.weapon2.active:
            ship.weapon2.active = True
            ship.weapon2.choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0
    if slot == 3 and ship.weapon3:
        if ship.weapon3.active:
            ship.weapon3.active = False
            ship.weapon3.choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0
        if not ship.weapon3.active:
            ship.weapon3.active = True
            ship.weapon3.choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0
    if slot == 4 and ship.weapon4:
        if ship.weapon4.active:
            ship.weapon4.active = False
            ship.weapon4.choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0
        if not ship.weapon4.active:
            ship.weapon4.active = True
            ship.weapon4.choose_image()
            event.post(event.SHIP_CHANGED, sid)
            return 0


def animate_engine_thrust(m):
    """
    Changes image of all engines thrusting and back when no longer thrusting
    """
    ws = m.cfg.world_ships
    event = m.event

    for sid in ws:
        ship = ws[sid]
        engine = ship.engine
        # print("[animate_engine_thrust] engine:", ship.engine.name)
        if ship.thrust > 0:
            # print("[animate_engine_thrust] SID:", sid)
            filename_without_png = engine.image_file.split(".")
            image = "".join([filename_without_png[0], "f.png"])
            engine.image = image
            # print("[animate_engine_thrust] image:", image)
            event.post(event.SHIP_CHANGED, sid)
        if ship.thrust == 0:
            engine.image = engine.image_file
            event.post(event.SHIP_CHANGED, sid)
        if ship.after_burner_thrust > 0:
            filename_without_png = engine.image_file.split(".")
            image = "".join([filename_without_png[0], "ff.png"])
            engine.image = image
            event.post(event.SHIP_CHANGED, sid)


def animate_reverse_thrust(m):
    ws = m.cfg.world_ships
    event = m.event

    for sid in ws:
        ship = ws[sid]
        rthruster = ship.reverse_thruster
        if ship.reverse_thrust > 0:
            filename_without_png = rthruster.image_file.split(".")
            image = "".join([filename_without_png[0], "f.png"])
            rthruster.image = image
            event.post(event.SHIP_CHANGED, sid)
            # print("[animate_reverse_thrust] changing to thrusting image")
        if ship.reverse_thrust == 0:
            rthruster.image = rthruster.image_file
            event.post(event.SHIP_CHANGED, sid)
            # print("[animate_reverse_thrust] changing to normal image")


def reset_all_ships_thrust(m):
    """
    call this before ship update and before add_thrust
    :param m:
    :return:
    """
    for s in m.cfg.world_ships:
        m.cfg.world_ships[s].thrust = 0
        m.cfg.world_ships[s].reverse_thrust = 0
        m.cfg.world_ships[s].after_burn_thrust = 0


def nullify_thrust(sid, m):
    m.cfg.world_ships[sid].thrust = 0


def remake_ship_surface(sid, m):
    """
    Redraws the ship surface after a change
    """
    m.cfg.world_ships[sid].remake_ship_surface()


def add_thrust(sid, value, m):
    """
    Base thrust is the value of the engine
    Larger ships require more thrust, they get a penalty
    """
    # factors of penalty based on length and width
    width_factor = 1
    length_factor = 1

    sd = m.cfg.world_ships
    base_thrust = sd[sid].engine.thrust

    ship_body_area = calculate_ship_body_area(sid, width_factor, length_factor, m)
    standardized_ship_area = 8000
    area_ratio = standardized_ship_area / ship_body_area

    actual_thrust = (base_thrust / 1000) * area_ratio

    sd[sid].thrust += actual_thrust


def add_reverse_thrust(sid, not_used, m):
    """
    Actually adds negative thrust to the ships thrust based on the thrusters' thrust (lol)
    """
    # factors of penalty based on length and width
    width_factor = 1
    length_factor = 1

    sd = m.cfg.world_ships
    base_reverse_thrust = sd[sid].reverse_thruster.thrust

    ship_body_area = calculate_ship_body_area(sid, width_factor, length_factor, m)
    standardized_ship_area = 8000
    area_ratio = standardized_ship_area / ship_body_area

    actual_reverse_thrust = (base_reverse_thrust / 1000) * area_ratio

    sd[sid].reverse_thrust += actual_reverse_thrust


def add_after_burn_thrust(sid, not_used, m):
    """
    Base thrust is the value of the engine
    Larger ships require more thrust, they get a penalty
    """
    # factors of penalty based on length and width
    width_factor = 1
    length_factor = 1

    sd = m.cfg.world_ships
    base_thrust = sd[sid].engine.thrust
    ship_body_area = calculate_ship_body_area(sid, width_factor, length_factor, m)
    standardized_ship_area = 8000
    area_ratio = standardized_ship_area / ship_body_area

    actual_thrust = (base_thrust / 1000) * area_ratio
    sd[sid].thrust += (actual_thrust * 2)