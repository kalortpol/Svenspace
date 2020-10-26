event_queue = {}


def post(event_type, sid=None, value=None):
    if event_queue.get(event_type):
        event_queue[event_type].append((sid, value))
    else:
        event_queue[event_type] = []
        event_queue[event_type].append((sid, value))


def len_type(event_type):
    try:
        return len(event_queue[event_type])
    except KeyError:
        print("[queue_len_by_type] no such key:", event_type)
        return 0


def exists(event_type):
    """
    Call to check if event needs to be handled
    """
    if event_type in event_queue and len(event_queue[event_type]) > 0:
        return True
    else:
        return False


def pop_type(event_type):
    try:
        event_tuple = event_queue[event_type].pop()
        return event_tuple
    except KeyError:
        print("[pop_by_type] no such key!")
    except IndexError:
        print("Reached end of list for event", event_type)

"""
Events
"""
# map related
MAP_CHANGE = "map_change"
RELOAD_MAP = "reload_map"

# ship
DMG = "dmg"
SHIELD_DMG = "shield_dmg"
HEAL = "heal"
SHIELD_HEAL = "shield_heal"

SHIELD_ON = "shield_on"
SHIELD_OFF = "shield_off"

SHIELD_INCREASE = "shield_increase"
SHIELD_DECREASE = "shield_decrease"

ENGINE_INCREASE = "engine_increase"
ENGINE_DECREASE = "engine_decrease"
ANIMATE_ALL_THRUST = "animate_all_thrust"
ANIMATE_ALL_REVERSE_THRUST = "animate_all_reverse_thrust"
RESET_ALL_SHIPS_THRUST = "reset_all_ships_thrust"

WEAPONS_INCREASE = "weapons_increase"
WEAPONS_DECREASE = "weapons_decrease"
WEAPON_ACTIVATION = "weapons_activation"

FIRED_GUN_1 = "fired_gun_1"
FIRED_GUN_2 = "fired_gun_2"
FIRED_GUN_3 = "fired_gun_3"
FIRED_GUN_4 = "fired_gun_4"


STARTED_MINING = "started_mining"
STOPPED_MINING = "stopped_mining"

COLLIDED = "collided"
WAS_COLLIDED_WITH = "was_collided_with"

TRY_HIT = "try hit"
HIT_TARGET = "hit_target"
GOT_HIT = "got_hit"

ACCELERATE = "accelerate"
DECELERATE = "decelerate"
THRUST = "thrust"
REVERSE_THRUST = "reverse_thrust"
AFTER_BURN_THRUST = "after_burn_thrust"
FRICTION = "friction"

TURN = "turn"
L_SIDE_THRUST = "l_side_thrust"
R_SIDE_THRUST = "r_side_thrust"
RESET_ALL_SIDE_THRUST = "reset_side_thrust"

STOP = "stop"

LEFT_SHIP = "left_ship"
ENTERED_SHIP = "entered_ship"

SHIP_CHANGED = "ship_changed"
SHIP_EQUIP_CHANGED = "ship_equip_changed"

QUIT = "quit"
