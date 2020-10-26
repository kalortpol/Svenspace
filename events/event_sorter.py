import pygame


def first_updates(m):
    event = m.event
    sp = m.ship_processors

    if event.RESET_ALL_SHIPS_THRUST in event.event_queue:
        sp.reset_all_ships_thrust(m)
        del event.event_queue[event.RESET_ALL_SHIPS_THRUST]

    if event.RESET_ALL_SIDE_THRUST in event.event_queue:
        sp.reset_all_side_thrust(m)
        del event.event_queue[event.RESET_ALL_SIDE_THRUST]

    while event.exists(event.WEAPON_ACTIVATION):
        sid, value = event.pop_type(event.WEAPON_ACTIVATION)
        sp.change_weapon_activation(sid, value, m)


def middle_updates(m):
    event = m.event
    sp = m.ship_processors

    while event.exists(event.REVERSE_THRUST):
        sid, value = event.pop_type(event.REVERSE_THRUST)
        sp.add_reverse_thrust(sid, value, m)

    while event.exists(event.THRUST):
        sid, value = event.pop_type(event.THRUST)
        sp.add_thrust(sid, value, m)

    while event.exists(event.AFTER_BURN_THRUST):
        sid, value = event.pop_type(event.AFTER_BURN_THRUST)
        sp.add_after_burn_thrust(sid, value, m)

    if event.ANIMATE_ALL_THRUST in event.event_queue:
        sp.animate_engine_thrust(m)
        del event.event_queue[event.ANIMATE_ALL_THRUST]

    if event.ANIMATE_ALL_REVERSE_THRUST in event.event_queue:
        sp.animate_reverse_thrust(m)
        del event.event_queue[event.ANIMATE_ALL_REVERSE_THRUST]

    while event.exists(event.TURN):
        sid, value = event.pop_type(event.TURN)
        sp.rotate(sid, value, m)

    while event.exists(event.L_SIDE_THRUST):
        sid, value = event.pop_type(event.L_SIDE_THRUST)
        sp.animate_side_thrust(sid, "left", m)

    while event.exists(event.R_SIDE_THRUST):
        sid, value = event.pop_type(event.R_SIDE_THRUST)
        sp.animate_side_thrust(sid, "right", m)

    while event.exists(event.STOP):
        sid, value = event.pop_type(event.STOP)
        sp.stop(sid, 0, m)


def last_updates(m):
    event = m.event
    sp = m.ship_processors
    shipmod = m.ship

    # TODO implement
    while event.exists(event.SHIP_EQUIP_CHANGED):
        sid, value = event.pop_type(event.SHIP_EQUIP_CHANGED)
        shipmod.remake_ship_from_dict(sid, shipmod.get_ship_dict(sid, m), m)

    while event.exists(event.SHIP_CHANGED):
        sid, value = event.pop_type(event.SHIP_CHANGED)
        ship = shipmod.get_ship(sid, m)
        ship.remake_ship_surface()

def update(m):
    """
    SPLIT all events into different functions that can be executed in a pre-determined order,
    to make the events happen at the correct relative times
    """
    event = m.event
    sp = m.ship_processors

    # events ordered in three sequential functions
    first_updates(m)
    middle_updates(m)
    last_updates(m)

    if event.QUIT in event.event_queue:
        pygame.quit()
