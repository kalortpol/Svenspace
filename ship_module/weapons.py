"""
Weapons module
* A weapon has a projectile, shield damage and hull damage
* It has an image that is blited inside the ships surface (might change later if it need to be animated)
* It also has a power drain and a minimum power requirement (which is to be able to fire 1 shot)
"""
import os


class Laserwep:
    """
    Each weapon needs 2 images, and need to be named this way:
    weapon_name + a .png (without + or whitespace) -> active image
    weapon_name + i .png (without + or whitespace) -> inactive image
    """
    def __init__(self, image_file, sdmg, hdmg, power_drain):
        self.active = True
        self.image_file = image_file
        self.sdmg = sdmg
        self.hdmg = hdmg
        self.powerdr = power_drain

        def choose_image(self):
            filename_without_png = self.image_file.split(".")

            if self.active:
                image = "".join([filename_without_png[0], "a.png"])
                return image
            if not self.active:
                image = "".join([filename_without_png[0], "i.png"])
                return image

        self.image = choose_image(self)

    def choose_image(self):
        filename_without_png = self.image_file.split(".")

        if self.active:
            image = "".join([filename_without_png[0], "a.png"])
            self.image = image
        if not self.active:
            image = "".join([filename_without_png[0], "i.png"])
            self.image = image


def make_weapon(weapon_name: str):
    wd = {"laser1": {"classname": Laserwep,
                     "image": "laser1.png",
                     "sdmg": 10,
                     "hdmg": 10,
                     "power_drain": 10}
          }

    assert weapon_name in wd, "[make_weapon] tried to make non-existent weapon!"
    w = wd[weapon_name]

    print("[make_weapon] New weapon:", weapon_name)
    return w["classname"](w["image"], w["sdmg"], w["hdmg"], w["power_drain"])


laser1 = Laserwep("laser1.png", 10, 10, 10)
