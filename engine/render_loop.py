def update(m):
    r = m.render
    u = m.in_game_ui

    #  background
    r.render_black_space(m)
    r.draw_to_screen(m)

    #  sprites
    m.cfg.shipgroup.update()
    m.cfg.shipgroup.draw(m.cfg.screen)

    #  blit ui
    r.draw_ui_to_screen(m.cfg)

    # finalize rendering

    r.update()
