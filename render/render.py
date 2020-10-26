import pytmx
import pygame
import os


def init_screen(width: int, height: int, caption: str):
    tile_buffer_size = 2
    print("[init_screen] width, height:", width, height)
    # background is the scrolled surface
    background = pygame.Surface((width, height))
    #self.background.fill((255, 255, 255))

    # ...caption?
    pygame.display.set_caption(caption)

    return pygame.display.set_mode((width, height))


def blit_image_as_background(file_name, m):
    """
    Takes FILE NAME of image and blits it
    """
    image_module = m.image
    cfg = m.cfg
    pgsurface = cfg.background

    pgsurface.blit(image_module.load(file_name), (0, 0))


def blit_image_on_background(file_name, pos, m, rotate=0):
    """
    Takes FILE NAME of image and blits it
    """
    image_module = m.image
    cfg = m.cfg
    pgsurface = cfg.background
    rot = pygame.transform.rotate

    pgsurface.blit(rot(image_module.load(file_name), rotate), (pos[0], pos[1]))


def blit_surface_on_background(source, pos, m):
    """
    Takes SURFACE of image and blits it
    """
    cfg = m.cfg
    bg = cfg.background
    bg.blit(source, pos)


def make_transparent_surface(size: tuple) -> pygame.Surface:
    """

    :param size: tuple
    :return:
    """
    new_surf = pygame.Surface(size)
    new_surf.set_colorkey((123, 123, 123))
    new_surf.fill((123, 123, 123))

    return new_surf


def blit_surface_centered(surface: pygame.Surface, pos: tuple, m):
    """
    Centers the surface, making the center of surface stay in the same place regardless of size
    """
    ss = surface.get_size()

    offsetx = ss[0] / 2
    offsety = ss[1] / 2

    blit_pos = (pos[0] - offsetx, pos[1] - offsety)

    blit_surface_on_background(surface, blit_pos, m)


def render_black_space(m):
    bg = m.cfg.background

    bgs = pygame.Surface((1024, 768))
    bgs.fill((0, 0, 0))
    bg.blit(bgs, (0, 0))


def blit_tiles(cfg):
    map_size = self.map_data.width * self.map_data.tilewidth,\
               self.map_data.height * self.map_data.tileheight

    # Get world coordinates of start and end point of screen area (+buffer)
    start, end = scrolling_funcs.get_tile_area_to_blit(self.tile_size, self.tile_buffer_size, map_size)

    start_x = start[0]
    end_x = end[0]

    start_y = start[1]
    end_y = end[1]

    # blit column for column
    for x in range(start_x, end_x, self.tile_size[0]):
        for y in range(start_y, end_y, self.tile_size[1]):
            # Fetch tile
            tile_image = scrolling_funcs.fetch_tile((x, y), self.tile_size, self.map_data)

            # Translate to screen coordinate
            screen_coordinate = scrolling_funcs.translate_world_to_screen((x, y),
                                                                          cfg.camera_pos,
                                                                          self.width,
                                                                          self.height,
                                                                          self.tile_size)

            # Blit to screen
            self.background.blit(tile_image,
                                 screen_coordinate)


def draw_ui_to_screen(cfg):
    cfg.screen.blit(cfg.ui_surface, (0, 0))


def update_on_demand_queue(cfg):
    """
    Pops items from update queue and updates them

    :return:
    """

    # temp storage of all sprites to update
    update_list = list()

    while len(update_queue.update_queue) > 0:
        next_sprite = update_queue.update_queue.pop()
        update_list.append(next_sprite)
        #print("[update_on_demand_queue] Found in on demand queue:", next_sprite.name)

    #print("[update_on_demand_queue] Updating on demand queue with contents:", update_list)

    for s in update_list:
        s.update()


def draw_to_screen(m):
    cfg = m.cfg

    cfg.screen.blit(cfg.background, (0, 0))


def draw_sprites(cfg, state):
    # Blit sprites in correct positions

    for spr in cfg.sprite_group:
        # Translate world to screen coords
        wc = spr.pos

        sc = scrolling_funcs.translate_world_to_screen(wc,
                                                       cfg.camera_pos,
                                                       cfg.screen_width,
                                                       cfg.screen_height,
                                                       self.tile_size)

        # Blit sprite to screen
        self.background.blit(spr.image, sc)


def update():
    pygame.display.update()
    pygame.display.flip()


def update_old(cfg, state):
    # update cfg.map_size var
    self.store_map_size(state)

    # blit the tiles real-time
    self.blit_tiles()

    # blit the sprites, before UI (or they will overlap)
    self.draw_sprites(state)

    # only update on demand queue if it has contents
    if len(update_queue.update_queue) > 0:
        self.update_on_demand_queue()

    # blit the UI
    self.blit_ui()

    # blit everything onto the screen surface
    self.draw_to_screen(state)

    # update and flip double buffer
    pygame.display.update()
    pygame.display.flip()