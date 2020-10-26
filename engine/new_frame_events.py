def update(m):
    """
    what events need to be posted at the start of each frame?
    """
    cfg = m.cfg
    ws = cfg.world_ships
    event = m.event

    # reset all thrust
    event.post(event.RESET_ALL_SHIPS_THRUST, m)
    # animate all thrust
    event.post(event.ANIMATE_ALL_REVERSE_THRUST, m)
    event.post(event.ANIMATE_ALL_THRUST, m)
    event.post(event.RESET_ALL_SIDE_THRUST, m)
    # reset UI background
    m.in_game_ui.init(m)
