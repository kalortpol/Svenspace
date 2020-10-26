"""
Inventory management
"""


def get(sid, m):
    """
    Get inventory of SID
    Returns empty dict if no inventory is found
    """
    si = m.cfg.all_ship_inventories

    try:
        return si[sid]
    except KeyError:
        return {}


def get_stash_part(sid, part, m):
    stash = m.cfg.all_ship_inventories[sid][part]["stash"]

    return stash


def has_part(sid, part, part_name, m, return_it=False):
    """
    Checks if SID has particular ship part.
    Optionally returns the part
    """
    inv = m.cfg.all_ship_inventories[sid]

    if len(inv[part]["stash"]) > 0:
        for p in inv[part]["stash"]:
            # print("[has_part] p.name:", p.name, "part_name:", part_name)
            if p.name == part_name and not return_it:
                return True
            if p.name == part_name and return_it:
                temp = p
                return temp

        print("[has_part] sid:", sid, "does not have part", part_name)
        print("[has_part] sid stash:", [s.name for s in inv[part]["stash"]])
        return False


def give_new(sid, part, part_name, m):
    """
    Creates a new part and puts it in SID inventory
    ** If nothing is equipped in the slot, item is automatically equipped **
    """
    cfg = m.cfg
    spl = m.ship_part_loader
    inv = m.cfg.all_ship_inventories[sid]
    ship = m.cfg.world_ships[sid]

    assert sid in cfg.world_ships, "[give_new] SID does not exist!"
    assert part in cfg.all_ship_parts, "[give_new] part does not exist!"

    new_part = spl.get_ship_part(part, part_name, m)

    if len(inv[part]["equipped"]) == 0:
        inv[part]["equipped"] = [new_part]
        # setattr(ship, part, inv[part]["equipped"][0])
        ship.shipdict[part] = inv[part]["equipped"][0]
        m.event.post(m.event.SHIP_CHANGED, sid)
    else:
        inv[part]["stash"].append(new_part)

    # print("[give_new]", part_name, "given to SID", sid)
    # print("[give_new] inventory of SID", sid, get(sid, m))


def remove(sid, part, part_name, m):
    cfg = m.cfg
    inv = cfg.all_ship_inventories

    if part_name in inv[sid][part]["stash"]:
        inv[sid][part]["stash"].remove(part_name)
        print("[remove]", part_name, "removed from inventory of SID:", sid)
    elif part_name in inv[sid][part]["equipped"]:
        print("[remove] cannot remove equipped part", part_name, "of SID:", sid)
    else:
        print("[remove] should not be reached. Check code.")


def equip(sid, part, part_name, shipdict, m):
    """
    Equips new item, moves old equipped item to stash
    """
    print("[equip] part_name:", part_name)

    assert has_part(sid, part, part_name, m), "[equip] tried to equip item SID does not have"
    ship = m.cfg.world_ships[sid]
    inv = get(sid, m)

    eq = inv[part]["equipped"]
    stash = inv[part]["stash"]

    # print("[equip] equip before changes [equip]:", [s.name for s in inv[part]["equipped"]])
    # print("[equip] stash before changes [equip]:", [s.name for s in inv[part]["stash"]])

    old_eq = inv[part]["equipped"][0]
    # put old item in stash
    inv[part]["stash"].append(old_eq)
    # remove old item from equipped
    inv[part]["equipped"].remove(old_eq)

    # print("[equip] equip old item stashed [equip]:", [s.name for s in inv[part]["equipped"]])
    # print("[equip] stash old item stashed [equip]:", [s.name for s in inv[part]["stash"]])

    # add new item to equipped if it's in stash
    new_equip = has_part(sid, part, part_name, m, return_it=True)
    inv[part]["equipped"].append(new_equip)

    # remove new item from stash
    inv[part]["stash"].remove(new_equip)

    # TODO trying to not modify ship.shipdict directly from this func
    # TODO instead this func returns a modified shipdict

    shipdict[part] = inv[part]["equipped"][0]  # index because it's a list

    # print("[equip] equip at end of [equip]:", [s.name for s in inv[part]["equipped"]])
    # print("[equip] stash at end of [equip]:", [s.name for s in inv[part]["stash"]])
    m.event.post(m.event.SHIP_EQUIP_CHANGED, sid)  # easily forgotten in calling function
    return shipdict


def part_class(part, m):
    sp = m.ship_part_loader

    td = {"cockpit": sp.Cockpit,
          "wingbody": sp.Wingbody,
          "wings": sp.Wings,
          "power_plant": sp.PowerPlant,
          "engine": sp.Engine,
          "reverse_thruster": sp.ReverseThruster,
          "side_thruster": sp.SideThruster,
          "shield": sp.ShieldGen}

    return td[part]
