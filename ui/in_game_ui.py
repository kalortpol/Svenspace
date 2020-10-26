def bottom(m):
    pass


def top(m):
    button = m.button.mouse_over_clickable_ui

    if button("t_build_ship.png", (0, 0), m):
        m.shipyard.shipyard_menu(m.shipyard.get_player_ship(m).shipdict, m)


def left(m):
    pass


def right(m):
    pass


def ui(style, m):
    cfg = m.cfg
    render = m.render
    top(m)


def init(m):
    cfg = m.cfg
    render = m.render
    # print(cfg.width, cfg.height)
    cfg.ui_surface = render.make_transparent_surface((cfg.width, cfg.height))


def text(text, pos, m):
    text_surface = m.cfg.font.render(text, True, (255, 255, 255))
    m.cfg.ui_surface.blit(text_surface, pos)