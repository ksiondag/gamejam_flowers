#!/usr/bin/python

import pygame

import colors
import flower as f
import event as e
import manager as m
import rabbit as r
import terrain as t
import unit as u

TITLE = "It's Game Time!"

FPS = 60

def init():
    pygame.init()

    m.init()
    t.init()
    u.init()
        
def main():
    # Initialize everything
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


    while True:
        dt = clock.tick( FPS ) / 1000.

        # Handle events and change state as necessary
        for event in pygame.event.get():
            m.process( event )

        for event in e.Event.get():
            m.process( event )

        # Update all units
        for unit in u.all():
            unit.update( dt )

        flower_count = 0
        rabbit_count = 0
        for unit in u.all():
            if isinstance(unit, f.Flower):
                flower_count += 1
            if isinstance(unit, r.Rabbit):
                rabbit_count += 1

        # Redraw screen
        screen.fill(colors.BLACK)
        for terrain in t.all():
            terrain.draw(screen)
        for unit in u.all():
            unit.draw(screen)
        pygame.display.flip()

        # End game condition
        if rabbit_count == 0:
            pygame.font.init()
            font = pygame.font.SysFont("Monospace",100)
            win = font.render("You win!!!",1,colors.BLUE)
            screen.blit(win,(0,0))#self.terain
            pygame.display.flip()
            pygame.time.wait(5000)
            m.quit( None )
        if flower_count == 0:
            pygame.font.init()
            font = pygame.font.SysFont("Monospace",100)
            lose = font.render("You lose!!!",1,colors.RED)
            screen.blit(lose,(0,0))#self.terain
            pygame.display.flip()
            pygame.time.wait(5000)
            m.quit( None )

if __name__ == '__main__':
    main()

