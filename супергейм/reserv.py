import pygame as pg

my_size = (0,0)
my_position = (0,0)
my_color = "green"
my_sprite = None
my_frame = 0
my_current_animation = 0

my_frame_lines = {
    'up': 0,
    'down': 2,
    'right': 3,
    'left': 1
}

def init(size, position, color):
    global my_size, my_position, my_color, my_sprite, my_current_animation
    my_size = size
    my_position = position
    my_color = color
    my_sprite = pg.image.load("resources/sprite.png")
    me = pg.Surface(my_size)
    me.set_colorkey((0,0,0))
    my_current_animation = 'left'
    update(me)
    return me

def update(me):
    me.fill((0,0,0))
    me.blit(my_sprite, 
            (0,0), 
            (my_size[0]*my_frame, my_frame_lines[my_current_animation] * my_size[1], my_size[0]*(my_frame+1), my_size[1]))
    #        ^^^^^^^^ x1 ^^^^^^^  y1 ^^^^^^^^^ x2 ^^^^^^^^^^  ^^^ y2 ^^^

def next_frame():
    global my_frame
    my_frame += 1
    if my_frame > 8:
        my_frame = 0

def move(dx, dy):
    global my_position
    my_position = (my_position[0]+dx, my_position[1]+dy)
    next_frame()

def set_animation(name):
    global my_current_animation 

    if name in my_frame_lines:
        my_current_animation  = name
        