#!/usr/bin/python

import pygame

import collections
import sys

import colors
import terrain as t
import unit as u
import flower as f
import manager

TITLE = 'Units activate!'

def do_nothing( event ):
    return

def quit( event ):
    pygame.quit()
    sys.exit()

def mouse_motion( event ):
    result = t.collision( event.pos )
    if result is not None:
        result.set_highlight()

def mouse_button_down( event ):
    result = t.collision( event.pos )
    if result is not None:
        return
        u.Unit( result )

def key_down( event ):

    if manager.listens_for( event.key ):
        if manager.process( event ):
            u.Unit.activate_next()

def init():
    pygame.init()

    manager.init()

    t.init()
    u.init()
        
def main():
    init()

    # Setup the screen
    size = t.screen_size()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # Initialize clock
    clock = pygame.time.Clock()

    # Initialize background
    screen.fill(colors.BLACK)
    pygame.display.flip()

    # Event managing dictionary
    # For events we do not process, we are defaulting to doing nothing
    process = collections.defaultdict( lambda: do_nothing )
    process.update( [
        (pygame.QUIT,               quit),
        (pygame.MOUSEMOTION,        mouse_motion),
        (pygame.MOUSEBUTTONDOWN,    mouse_button_down),
        (pygame.KEYDOWN,            key_down)
    ] )

    while True:
        # Handle events and change state as necessary
        for event in pygame.event.get():
            process[event.type]( event )

        # Redraw screen
        screen.fill(colors.BLACK)
        for terrain in t.all():
            terrain.draw(screen)
        for unit in u.all():
            unit.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()

