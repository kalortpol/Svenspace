image_library = {}
import pygame
import os


def load(image: str) -> pygame.Surface:
    """

    :param image: string
    :return: pygame surface
    """
    if image not in image_library:
        try:
            path = "assets/"
            image_path = os.path.join(path, image)
            image_library[image] = pygame.image.load(image_path).convert_alpha()

        except FileNotFoundError:
            print("[load_image] File not found! File:", image, "path:", image_path)

    if image in image_library:
        return image_library[image]
