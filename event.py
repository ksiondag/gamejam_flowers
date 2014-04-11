
# AI events
AI_LEFT  = 1000
AI_RIGHT = 1001
AI_UP    = 1002
AI_DOWN  = 1003
AI_MOVE  = 1004
AI_SKIP  = 1005

# Turn events
END_TURN    = 1006
DEATH       = 1007
NEXT_ACTIVE = 1008

# FLOWER actions
FLOWER_UP     = 1009
FLOWER_DOWN   = 1010
FLOWER_LEFT   = 1011
FLOWER_RIGHT  = 1012
FLOWER_SKIP   = 1013
FLOWER_SEED   = 1014
FLOWER_THORN  = 1015
FLOWER_CANCEL = 1016
FLOWER_POISON = 1017

class Event(object):

    _events = []

    @classmethod
    def get( cls ):
        events = cls._events
        cls._events = []

        return events

    def __init__( self, type, target=None, **kwargs ):
        self.type = type
        self.target = target

        for k, v in kwargs.items():
            setattr(self, k, v )

        Event._events.append( self )

