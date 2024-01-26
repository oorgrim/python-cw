import pygame as pg 
import player 
 
def check(object: player.Player): 
    keys = pg.key.get_pressed() 
    for control in object.controls: 
        code = control['key'] 
        name = control['animation'] 
        if keys[code]: 
            object.set_animation(name)
