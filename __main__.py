#!/usr/bin/python

import pygame

import collections
import sys

import colors
import terrain as t

TITLE = 'Debug mode!'

def turn_end(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            damage(grid)
            grid[row][col].hit = 0
            
            if grid[row][col].color != colors.WHITE:
                grid[row][col].growth += 1

def damage(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col].growth -= grid[row][col].hit

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
        result.change_color()

def key_down( event ):
    # NOTE: Throwaway code to test highlighting and controls
    movement = {
        pygame.K_UP:    t.Terrain.active.up_terrain(),
        pygame.K_DOWN:  t.Terrain.active.down_terrain(),
        pygame.K_LEFT:  t.Terrain.active.left_terrain(),
        pygame.K_RIGHT: t.Terrain.active.right_terrain()
    }
    if event.key in movement:
        movement[ event.key ].set_active()

    elif event.key == pygame.K_q:
        t.Terrain.active.seed = True

    elif event.key == pygame.K_RETURN:
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
        pygame.display.flip()

if __name__ == '__main__':
    main()

