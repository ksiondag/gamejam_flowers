
import collections
import sys

import pygame

import event as e
import unit

def do_nothing( event ):
    return

def process( event ):
    return _current[ event.type ]( event )

def special_delivery( event ):
    if event.type in event.target.specific_listeners:
        event.target.specific_listeners[event.key](event)

def init_listener( ):
    return collections.defaultdict( lambda: do_nothing )

_DEFAULT = None
_current = None

def quit( event ):
    pygame.quit()
    sys.exit()

_KEYBOARD_TRANSLATE = {
    pygame.K_UP:        e.FLOWER_UP,
    pygame.K_DOWN:      e.FLOWER_DOWN,
    pygame.K_LEFT:      e.FLOWER_LEFT,
    pygame.K_RIGHT:     e.FLOWER_RIGHT,
    pygame.K_SPACE:     e.FLOWER_SKIP,
    pygame.K_s:         e.FLOWER_SEED,
    pygame.K_t:         e.FLOWER_THORN,
    pygame.K_p:         e.FLOWER_POISON,
    pygame.K_BACKSPACE: e.FLOWER_CANCEL,
}
def key_down( event ):
    print event
    if event.key in _KEYBOARD_TRANSLATE:
        e.Event( _KEYBOARD_TRANSLATE[ event.key ] )

def update_current( E ):
    global _current
    for k in E:
        _current[k] = E[k]

def restore_default():
    global _current
    _current = init_listener()
    _current.update( _DEFAULT )

def init():

    # Event managing dictionary for events that are always listened for
    # For events we do not process, we are defaulting to doing nothing
    # TODO: add listening for controllers

    global _DEFAULT
    _DEFAULT =  init_listener()

    # TODO: add controller listening
    _DEFAULT.update( [
        (pygame.QUIT,       quit),
        (pygame.KEYDOWN,    key_down),
        (e.END_TURN,        unit.end_turn),
        (e.NEXT_ACTIVE,     unit.Unit.activate_next)
    ] )

