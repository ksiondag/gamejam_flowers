
from collections import deque
import unit #remove
import pygame

import colors
import event as e
from terrain import Terrain

import manager

class Unit( object ):
    
    units  = deque()
    end_of_turn = 0

    @classmethod
    def activate_next( cls ):
        cls.units.rotate(1)

        cls.end_of_turn -= 1
        #print cls.end_of_turn
        if cls.end_of_turn <= 0:
            end_turn( None )
            cls.end_of_turn = len( cls.units )

        manager.restore_default()
        manager.update_current( cls.active().active_listeners )

    @classmethod
    def active( cls ):
        return Unit.units[0]
    
    def __init__( self, terrain ):
        Unit.units.appendleft( self )

        self.terrain = terrain
        self.terrain.add_unit( self )
        self.active_listeners = {
        }

        self.specific_listeners = {
            e.DEATH: self.delete
        }

    def add_listener( event_key, function ):
        self.specific_listeners[ event_key ] = function
    
    def delete( self, event ):
        self.terrain.remove_unit( self )
        Unit.units.remove( self )

        manager.restore_default()
        manager.update_current( Unit.active().active_listeners )

    def is_surrounded( self, unit_type=None ):
        return (self.terrain.up_terrain()   .contains_unit(unit_type) and
                self.terrain.down_terrain() .contains_unit(unit_type) and
                self.terrain.left_terrain() .contains_unit(unit_type) and
                self.terrain.right_terrain().contains_unit(unit_type)    )

    def update( self, dt ):
        if self.is_surrounded( type(self) ):
            e.Event( e.DEATH, target=self )

    def end_turn( self ):
        pass

    def draw_number( self, screen ):
        return
        myfont = pygame.font.SysFont("monospace", 20)

        # render text
        label = myfont.render("%i" % self.growth, 1, colors.BLACK)
        screen.blit(label, self.terrain)

    def draw( self, screen ):
        if self is Unit.active():
            self.terrain.draw_border(screen, colors.RED)

def init():
    import flower
    flower.Flower( Terrain.grid[4][4] )

    import rabbit
    rabbit.Rabbit( Terrain.grid[5][5] )

    Unit.end_of_turn = 2
    Unit.activate_next()

def all():
    return Unit.units

def end_turn( event ):
    for unit in all():
        unit.end_turn()

