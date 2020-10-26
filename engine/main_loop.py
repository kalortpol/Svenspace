import pygame


def main_loop(m):
    """
    * Input
    * Event engine
        - Event queue
        - Event processors
        - Event order
    * Render world
        - Procedural generation
        - Scrolling
        - Special effects
    * Getting in and out of ship
    * Docking with stations/planets
    * Traveling through wormholes and gates
    """
    r = m.render

    running = True
    while running:
        pygame.event.poll()  # or it stops responding. No other use.

        # new frame events (what should happen at start of each frame?
        m.new_frame_events.update(m)

        # render ui
        m.in_game_ui.ui("normal", m)

        # input
        m.input.update_keyboard(m)

        # events
        m.event_sorter.update(m)

        # render - included here is update of sprite images and positions
        m.render_loop.update(m)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
