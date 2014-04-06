
import pygame

import action
import colors
import unit
from terrain import Terrain

class Flower( unit.Unit ):

    def __init__( self, terrain ):
        unit.Unit.__init__( self, terrain )

        self.active_listeners = {
            pygame.K_UP:    self.action_up,
            pygame.K_DOWN:  self.action_down,
            pygame.K_LEFT:  self.action_left,
            pygame.K_RIGHT: self.action_right,
            pygame.K_SPACE: self.action_skip,
        }

    def _action_direction( self, action_terrain ):
        action.Action( action_terrain, self )
        return False

    def action_up( self, event ):
        action_terrain = self.terrain.up_terrain()
        return self._action_direction( action_terrain )

    def action_down( self, event ):
        action_terrain = self.terrain.down_terrain()
        return self._action_direction( action_terrain )

    def action_left( self, event ):
        action_terrain = self.terrain.left_terrain()
        return self._action_direction( action_terrain )

    def action_right( self, event ):
        action_terrain = self.terrain.right_terrain()
        return self._action_direction( action_terrain )
    
    def action_skip( self, event):
        return True

    def draw( self, screen ):
        pygame.draw.rect( screen, colors.GREEN, self.terrain )
        self.draw_number( screen )
        unit.Unit.draw( self, screen )
