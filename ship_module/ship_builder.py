import pygame
from ship_module import ship_parts as sp
"""
Finished:
* On-the-fly creation of ship surface by just supplying shipdict
* On-the-fly adding/removing weapons to the wings by just supplying shipdict

Not finished:
- Addons for cockpit, wingbody, engine just like the wings above
    -- Make sure addons from different parts dont collide with eachother on top/on the side of the ship
"""


def make_ship_surface(shipdict, m, return_sizes=False):
    """
    FULLY FUNCTIONING - I THINK

    Puts all the parts together in one single surface
    * create empty surface
    * blit the ship parts correctly
    * adjusts automatically so parts fit together and aligns them
    * return the surface

    :return: pygame surface
    """
    cockpit = shipdict["cockpit"]
    wingbody = shipdict["wingbody"]
    powerplant = shipdict["power_plant"]
    engine = shipdict["engine"]

    image_mod = m.image
    render = m.render
    imgld = image_mod.load

    # surfaces of all parts
    c = make_cockpit_with_addon(shipdict, m)
    wb = imgld(wingbody.image)
    pp = imgld(powerplant.image)
    e = imgld(engine.image)  # TODO check if ship is afterburning
    wl, wr = make_wings_with_weapons(shipdict, m)


    # size of every part
    cs = c.get_size()
    wbs = wb.get_size()
    pps = pp.get_size()
    es = e.get_size()
    wls = wl.get_size()
    wrs = wr.get_size()

    """
    Calculate needed surface size to contain ship
    """
    total_width = wls[0] + wrs[0] + wbs[0]  # wings + wing body
    total_height = cs[1] + wbs[1] + es[1]  # total height of ship body

    """
    Determine where each part should be,
    start x should be at the end of 1 wing length
    start y should be 0 for cockpit, then work downwards
    
    Need to check where center is of every body part to align them correctly
    """

    cockpit_start = ((total_width / 2) - (cs[0] / 2), 0)  # cockpit starts in the middle of x axis, 0 y axis
    wb_offset = (cs[0] - wbs[0]) / 2  # half the difference in width is the offset required for centering next part
    pp_offset = (wbs[0] - pps[0]) / 2
    e_offset = (pps[0] - es[0]) / 2  # half the difference in width is the offset required for centering next part

    wb_start = (cockpit_start[0] + wb_offset, cs[1])
    pp_start = (wb_start[0] + pp_offset, wb_start[1] + wbs[1])
    e_start = (pp_start[0] + e_offset, pp_start[1] + pps[1])

    # this offsets wings on long wingbodies
    wing_offset = 0
    if wbs[1] > 1.5 * wrs[1]:
        wing_offset = wbs[1] / 3

    lwing = (wb_start[0] - wls[0], wb_start[1] + wing_offset)  # offset wing depending on size of wingbody
    rwing = (wb_start[0] + wbs[0], wb_start[1] + wing_offset)  # offset wing depending on size of wingbody

    shipsurf = render.make_transparent_surface((total_width, total_height))

    shipsurf.blit(c, cockpit_start)
    shipsurf.blit(wb, wb_start)
    shipsurf.blit(pp, pp_start)
    shipsurf.blit(e, e_start)
    shipsurf.blit(wl, lwing)
    shipsurf.blit(wr, rwing)

    if not return_sizes:
        return shipsurf
    if return_sizes:
        return shipsurf, cs, wbs, wls, es


def make_wings_with_weapons(shipdict, m) -> tuple:
    """
    Puts together weapons and wings and returns them as 2 surfaces (left wing, right wing)
    """
    render = m.render
    imgld = m.image.load
    wings = shipdict["wings"]

    """
    POSITIONING (on left win, counts from right edge)
    """
    SLOT1_POSITION = 24
    SLOT2_POSITION = 44
    SLOT3_POSITION = 64
    SLOT4_POSITION = 84  # wingtip, always at the left lower corner!

    """
    Now to the actual body
    """
    wslot1 = shipdict.get("weapons_slot1")
    wslot2 = shipdict.get("weapons_slot2")
    wslot3 = shipdict.get("weapons_slot3")
    wslot4 = shipdict.get("weapons_slot4")
    # load weapon images into surfaces and determine sizes
    w1, w2, w3, w4 = None, None, None, None
    w1s, w2s, w3s, w4s = None, None, None, None

    if wslot1:
        w1 = imgld(wslot1.image)
        w1s = w1.get_size()
    if wslot2:
        w2 = imgld(wslot2.image)
        w2s = w2.get_size()
    if wslot3:
        w3 = imgld(wslot3.image)
        w3s = w3.get_size()
    if wslot4:
        w4 = imgld(wslot4.image)
        w4s = w4.get_size()

    # determine which weapon is the longest
    max_width = 0
    max_height = 0

    if w1s:
        max_width = w1s[0]
        max_height = w1s[1]
    if w2s:
        if w2s[0] > max_width:
            max_width = w2s[0]
        if w2s[1] > max_height:
            max_height = w2s[1]
    if w3s:
        if w3s[0] > max_width:
            max_width = w3s[0]
        if w3s[1] > max_height:
            max_height = w3s[1]
    if w4s:
        if w4s[0] > max_width:
            max_width = w4s[0]
        if w4s[1] > max_height:
            max_height = w4s[1]

    # left wing
    wl = imgld(wings.image)  # left wing
    wls = wl.get_size()

    # make surface for wings
    # make room for weapon if it is larger than wing
    total_wing_area = (wls[0] + max_width, wls[1] + max_height)
    left_wing = render.make_transparent_surface(total_wing_area)

    # blit the wing on the newly made surface
    left_wing.blit(wl, (max_width, max_height))
    lws = left_wing.get_size()

    # add reverse thrusters (9 wide 16 long when rotated 90 degrees)
    thruster_image = pygame.transform.rotate(imgld(shipdict["reverse_thruster"].image), 0)
    tsx = thruster_image.get_size()[0]
    tsy = thruster_image.get_size()[1]

    if "weapons_slot1" in shipdict:
        left_wing.blit(thruster_image, (lws[0] - tsx, lws[1] - tsy))
    else:
        left_wing.blit(thruster_image, (lws[0] - tsx, lws[1] - tsy))

    # blit weapons if any
    if isinstance(w1, pygame.Surface):
        left_wing.blit(w1, (wls[0] + max_width - SLOT1_POSITION, wls[1]))
    if isinstance(w2, pygame.Surface):
        left_wing.blit(w2, (wls[0] + max_width - SLOT2_POSITION, wls[1]))
    if isinstance(w3, pygame.Surface):
        left_wing.blit(w3, (wls[0] + max_width - SLOT3_POSITION, wls[1]))
    if isinstance(w4, pygame.Surface):
        left_wing.blit(w4, (wls[0] + max_width - SLOT4_POSITION, wls[1]))


    # right wing is really just a transform.rotated left wing
    right_wing = pygame.transform.flip(left_wing, True, False)  # right wing
    return left_wing, right_wing


def make_cockpit_with_addon(ship_image_dict, m):
    """
    Adds shield generator to the cockpit image if present
    """
    sd = ship_image_dict
    imgld = m.image.load
    render = m.render

    cockpit = sd["cockpit"]
    c = imgld(cockpit.image)
    cs = c.get_size()

    # add side thrusters before shield (easier to calculate width of cockpit before a potentially wide shield is added)
    if "side_thruster" in sd:
        c = cockpit_add_side_thruster(cockpit, sd["side_thruster"], m)

    # add shield if present, pass only c.
    # TODO FIX code in add shield to allow passing of c
    if "shield" in sd:
        return cockpit_add_shield(c, sd["shield"], m)

    else:
        return c


def cockpit_add_side_thruster(cockpit, side_thruster, m):
    imgld = m.image.load
    render = m.render

    c = imgld(cockpit.image)
    sl = imgld(side_thruster.imagel)
    sr = imgld(side_thruster.imager)

    # get sizes of cockpit and shield
    cs = c.get_size()
    ss = sr.get_size()

    # make room for 2 side thrusters on surface
    c_surf = render.make_transparent_surface((cs[0]+(2 * ss[0]), cs[1]))

    # adjust position of cockpit 1 side thruster to the right
    c_surf.blit(c, (ss[0], 0))

    # blit left side thruster (they are drawn right-facing)
    c_surf.blit(pygame.transform.rotate(sl, 180), (0, cs[1] - ss[1]))

    # blit right side thruster
    c_surf.blit(sr, (cs[0]+ss[0], cs[1] - ss[1]))

    return c_surf


def cockpit_add_shield(c, shield, m):
    """
    Pass c as a surface!
    :param c: pygame.Surface
    """
    imgld = m.image.load
    render = m.render

    s = imgld(shield.image)

    # get sizes of cockpit and shield
    cs = c.get_size()
    ss = s.get_size()

    # make surface big enough for cockpit+shield
    if ss[0] > cs[0]:
        x_diff = (ss[0] - cs[0]) / 2  # to center the part, it must be displaced by half the difference in width
    else:
        x_diff = (cs[0] - ss[0]) / 2  # see above, if ss is smaller than cs it must be calculated the opposite

    c_surf = render.make_transparent_surface((cs[0], cs[1] + ss[1]))
    c_surf.blit(c, (0, ss[1]))
    c_surf.blit(s, (x_diff, 0))

    return c_surf


def make_engine_with_addon(shipdict, m):
    pass


# BASE PARAMETERS ARE: IMAGE; DURABILITY; POWER DRAIN; SLOTS

"""
# wings
wings1 = sp.Wings("wings1.png", "not_used")
wings2 = sp.Wings("wings2.png", "not_used")
wings3 = sp.Wings("wings3.png", "not_used")
wings4 = sp.Wings("wings4.png", "not_used")
wings5 = sp.Wings("wings5.png", "not_used")

# cockpit
cockpit1 = sp.Cockpit("cockpit1.png", 0)
cockpit2 = sp.Cockpit("cockpit2.png", 0)
cockpit3 = sp.Cockpit("cockpit3.png", 0)
cockpit4 = sp.Cockpit("cockpit4.png", 0)
cockpit5 = sp.Cockpit("cockpit5.png", 0)

# wing body
wingbody1 = sp.Wingbody("wingbody1.png", 0)
wingbody2 = sp.Wingbody("wingbody2.png", 0)
wingbody3 = sp.Wingbody("wingbody3.png", 0)

# engine
engine1 = sp.Engine("engine1.png", 2, 1)
engine2 = sp.Engine("engine2.png", 5, 2)
engine3 = sp.Engine("engine3.png", 10, 5)
"""