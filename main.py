#!/usr/bin/env python3
# coding=utf-8
import logging

import pygame
from pygame.locals import *

_logger = logging.getLogger(__name__)


# A physicsy-thing that can topple over
class Toppleable():
    # A position in ???-space? 0-1? Should just keep this data in Bear for now?
    # infact it probably should be calculated depend on bears current squish?
    centre_of_mass = None

    # "If an object is tilted it will topple over if a vertical line from its
    # centre of gravity falls outside its base."


class Material():
    # probably just need mass (for 1m**3).
    mass = None


class BearPart():
    # aabb is in Bear-space.
    aabb = None
    material = None
    name = "left arm"
    texture = None


class Bear(pygame.sprite.Sprite):
    # Bears are a really simple 2-level geometry hierarchies.
    # The geom of the BearParts are the actual hit-targets.
    # aabb = None
    # geom = None
    # bear_parts = []
    # name = "TI Bear"

    def __init__(self, texture_path="assets/crap_ti_bear.png"):
        super().__init__()
        self.image = pygame.image.load(texture_path).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, *args):
        None


def main(args):
    _logger.info("main")

    pygame.init()
    screen_surface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Bear Tower Tumble')

    def clear_background(surf, rect):
        surf.fill((100, 149, 237), rect)

    clear_background(screen_surface, screen_surface.get_rect())

    bear_sprite = Bear()

    all_sprites = pygame.sprite.Group([bear_sprite])
    all_sprites.clear(screen_surface, clear_background)

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == QUIT or (
                            event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                return

        all_sprites.update()
        all_sprites.draw(screen_surface)
        # FIXME Not sure if I should use flip() or update() with groups
        pygame.display.flip()


def _main_setup_log(args):
    if args.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level,
                        format='[%(asctime)s] %(levelname)s - %(message)s')
    _logger.info("log started")
    if args.verbose:
        _logger.debug("args.verbose level: %s", args.verbose)


def _main_process_argv():
    """
    Constructs ArgumentParser and parses argv
    Returns:
        Namespace: output of parse_args()
    """
    import argparse

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--verbose', '-v', action='count',
                            help="Emit more data to log")

    return arg_parser.parse_args()


if __name__ == '__main__':
    _main_args = _main_process_argv()
    _main_setup_log(_main_args)
    main(_main_args)
