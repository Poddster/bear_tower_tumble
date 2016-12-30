#!/usr/bin/env python3
# coding=utf-8
import logging

import pygame
from pygame.locals import *

_logger = logging.getLogger(__name__)


def AxisAlignedBoundingBox():
    pass


AABB = AxisAlignedBoundingBox


# A physicsy-thing that can topple over
def Toppleable():
    # A position in ???-space? 0-1? Should just keep this data in Bear for now?
    # infact it probably should be calculated depend on bears current squish?
    centre_of_mass = None

    # "If an object is tilted it will topple over if a vertical line from its
    # centre of gravity falls outside its base."


def Material():
    # probably just need mass (for 1m**3).
    mass = None

def Bear():
    # Bears are a really simple 2-level AABB hierarchies.
    # The AABBs of the BearParts are the actual hit-targets.
    aabb = None
    bear_parts = []
    name = "TI Bear"


def BearPart():
    # aabb is in Bear-space.
    aabb = None
    material = None
    name = "left arm"
    texture = None


def main(args):
    _logger.info("main")

    pygame.init()
    screen_surface = pygame.display.set_mode((640, 480))

    bear_sprite = pygame.image.load("assets/crap_ti_bear.png").convert_alpha()

    pygame.display.set_caption('Hello World')
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == QUIT or (
                            event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                return

        screen_surface.fill((100, 149, 237))
        sprite_pos = (0, 0)
        screen_surface.blit(bear_sprite, sprite_pos)
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
