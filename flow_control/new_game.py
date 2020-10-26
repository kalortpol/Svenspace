def init_new_game(m):
    inv = m.inventory
    new = inv.give_new
    equip = inv.equip
    sms = m.ship.make_ship_from_dict
    cfg = m.cfg
    spl = m.ship_part_loader.get_ship_part

    # create a new ship
    cfg.starting_shipdict = {"cockpit": spl("cockpit", "cockpit1", m),
                     "wingbody": spl("wingbody", "wingbody1", m),
                     "wings": spl("wings", "wings1", m),
                     "power_plant": spl("power_plant", "power_plant1", m),
                     "engine": spl("engine", "engine1", m),
                     "shield": spl("shield", "shield1", m),
                     "side_thruster": spl("side_thruster", "side_thruster1", m),
                     "reverse_thruster": spl("reverse_thruster", "reverse_thruster1", m),
                     "wslot1": None,
                     "wslot2": None,
                     "wslot3": None,
                     "wslot4": None}

    sms(cfg.starting_shipdict, m)
