
import colors
import event
import manager
import unit

DIRECTION = 0
ACTION = 1

def decision( current ):
    return ( current + 1 ) % 2

class Action( unit.Unit ):

    def __init__( self, terrain, executor ):
        unit.Unit.__init__( self, terrain )

        self.executor = executor

        self.active_listeners = {
            event.AI_MOVE: self.action_move
        }

        manager.restore_default()
        manager.update_current( unit.Unit.active().active_listeners )

        self.wait = 1

    def action_move( self, event ):
        self.executor.terrain.remove_unit( self.executor )

        self.executor.terrain = self.terrain
        self.terrain.add_unit( self.executor )

        self.delete()
        unit.Unit.activate_next()

    def update( self, dt ):
        self.wait -= dt

        if self.wait < 0:
            event.Event( event.AI_MOVE )

    def draw( self, screen ):
        if self is unit.Unit.active():
            self.terrain.draw_border(screen, colors.BLUE)
            self.executor.terrain.draw_border(screen, colors.RED)

