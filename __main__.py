#!/usr/bin/python

import pygame

import collections
import sys

import colors
import terrain as t
import unit as u
import flower as f

TITLE = 'Units activate!'

def turn_end(grid):
    dlist = []
    for unit in u.Unit.units:
        if unit.is_surrounded():
            unit.growth -= 2
        unit.growth += 1
        if unit.growth < 1:
            dlist.append(unit)
    for unit in dlist:
       unit.delete()

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

    # NOTE: Throwaway code to test highlighting and controls
    action = [
        pygame.K_UP,
        pygame.K_DOWN,
        pygame.K_LEFT,
        pygame.K_RIGHT,
        pygame.K_SPACE,
        pygame.K_a,
        pygame.K_d
    ]
    if event.key in action:
        if u.Unit.action( event ):
            u.Unit.activate_next()

    if event.key == pygame.K_RETURN:
        turn_end(t.Terrain.grid)

def main():
    # Initialize screen
    size = t.screen_size()
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # Initialize clock
    clock = pygame.time.Clock()

    # Initialize background
    screen.fill(colors.BLACK)
    pygame.display.flip()

    t.init_grid()
    f.init_unit()

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

