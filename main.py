#!/usr/bin/env python3
# coding=utf-8
import logging

import pygame
from pygame.locals import *

_logger = logging.getLogger(__name__)


def main(args):
    _logger.info("main")

    pygame.init()
    screen_surface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Hello World')
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == QUIT or (
                            event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                return
        pygame.display.update()


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
