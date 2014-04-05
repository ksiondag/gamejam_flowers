
import unit
from terrain import Terrain

class Flower( unit.Unit ):

    def action_direction( self, action_terrain ):
        if action_terrain.contains_unit( type(self) ):
            return False
        else:
            Flower( action_terrain )
            return True

    def action_up( self ):
        action_terrain = self.terrain.up_terrain()
        return self.action_direction( action_terrain )

    def action_down( self ):
        action_terrain = self.terrain.down_terrain()
        return self.action_direction( action_terrain )

    def action_left( self ):
        action_terrain = self.terrain.left_terrain()
        return self.action_direction( action_terrain )

    def action_right( self ):
        action_terrain = self.terrain.right_terrain()
        return self.action_direction( action_terrain )
    
    def action_skip( self ):
        return True

    def action_attack( self ):
        return True

    def action_defend( self ):
        return True

def init_unit():
    Flower( Terrain.grid[0][0] )
