
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
    def activate_next( cls, event ):
        cls.units.rotate(1)

        cls.end_of_turn -= 1
        #print cls.end_of_turn
        if cls.end_of_turn <= 0:
            e.Event( e.END_TURN )
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
        up = self.terrain.up_terrain()
        is_up = up is None or up.contains_unit( unit_type )

        down = self.terrain.down_terrain()
        is_down = down is None or down.contains_unit( unit_type )

        left = self.terrain.left_terrain()
        is_left = left is None or left.contains_unit( unit_type )

        right = self.terrain.right_terrain()
        is_right = right is None or right.contains_unit( unit_type )

        return (is_up and is_down and is_left and is_right)

    def update( self, dt ):
        pass

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
    flower.Flower( Terrain.grid[0][0] )

    import rabbit
    rabbit.Rabbit( Terrain.grid[8][9] )
    rabbit.Rabbit( Terrain.grid[9][8] )

    #Unit.end_of_turn = 2
    manager.restore_default()
    manager.update_current( Unit.active().active_listeners )

def all():
    return Unit.units

def end_turn( event ):
    for unit in all():
        unit.end_turn()

