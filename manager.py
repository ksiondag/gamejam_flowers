
import pygame

import event
import unit

_DEFAULT = {

}

_current = {

}

def set_default( E ):
    global _DEFAULT
    _DEFAULT = { k: v for k, v in E.items() }

def restore_default():
    global _current
    _current = { k: v for k, v in _DEFAULT.items() }

def update_current( E ):
    global _current
    for k in E:
        _current[k] = E[k]

def listens_for( event_key ):
    return event_key in _current

def process( event ):
    return _current[ event.key ]( event )

def special_delivery( event ):
    if event.key in event.target.specific_listeners:
        event.target.specific_listeners[event.key](event)

def init():
    default = {
        event.END_TURN: unit.end_turn( event )        
    }
    set_default( default )


