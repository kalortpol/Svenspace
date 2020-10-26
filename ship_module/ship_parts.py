class SPart:
    """
    Used to store image+stats of each ship part
    Every part has a non-unique name which is used in inventory management
    """
    def __init__(self, image_file):
        self.image_file = image_file  # image of the part (file name)

        # override to change image
        self.image = image_file

        self.name = self.image_file.split(".")[0]



class Cockpit(SPart):
    """
    Specific slot(s): Shield
    Specific stat: Crew
    """
    def __init__(self, image_file, crew):
        super().__init__(image_file)
        self.crew = crew


class Wingbody(SPart):
    """
    Specific slot(s): Power plant
    Specific stat: Cargo
    """
    def __init__(self, image_file, cargo):
        super().__init__(image_file)
        self.cargo = cargo


class Engine(SPart):
    """
    Specific slot(s): Afterburner
    Specific stat: Thrust
    """
    def __init__(self, image_file, thrust):
        super().__init__(image_file)
        self.thrust = thrust


class Wings(SPart):
    """
    Specific slot(s): Weapons
    """
    def __init__(self, image_file, not_used):
        super().__init__(image_file)


class ShieldGen(SPart):
    def __init__(self, image_file, power):
        super().__init__(image_file)
        self.power = power


class PowerPlant(SPart):
    def __init__(self, image_file, output):
        super().__init__(image_file)
        self.output = output


class SideThruster(SPart):
    def __init__(self, image_file, turn_factor):
        super().__init__(image_file)
        self.image_file = image_file
        self.imagel = self.image_file
        self.imager = self.image_file
        self.turn_factor = turn_factor


class ReverseThruster(SPart):
    def __init__(self, image_file, thrust):
        super().__init__(image_file)
        self.thrust = thrust



