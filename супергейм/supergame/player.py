import pygame as pg  
 
class Player: 
    size = (0,0)  
    position = (0,0)  
    sprite = None  
    frame = 0  
    layer: pg.Surface = None 
    current_animation = "" 
    controls = () 
    frame_lines = {  
        'up': 0,  
        'down': 2,  
        'right': 3,  
        'left': 1  
    }  
    surface: pg.Surface = None 
  
    def __init__(self, layer, size, position, controls):  
        self.layer = layer 
        self.size = size  
        self.position = position  
        self.controls = controls  
        self.sprite = pg.image.load("resources/sprite.png") 
        self.current_animation = 'right'  
        self.surface = pg.Surface(size)  
        # self.me.set_colorkey((0,0,0))  
        self.update()  
  
    def update(self):  
        self.surface.fill((0,0,0))  
        self.surface.blit(self.sprite,   
                (0,0),   
                (self.size[0]*self.frame, self.frame_lines[self.current_animation] * self.size[1], self.size[0]*(self.frame+1),self. size[1])), 
                # self.size[1], 
                # self.size[0] 
                  
        #        ^^^^^^^^ x1 ^^^^^^^  y1 ^^^^^^^^^ x2 ^^^^^^^^^^  ^^^ y2 ^^^  
         
         
  
    def next_frame(self):  
        self.frame += 1  
        if self.frame > 8:  
            self.frame = 0 
        self.update() 
     
    def move(self, dx, dy):  
        self.position = (self.position[0]+dx, self.position[1]+dy)  
        self.next_frame()  
     
    def set_animation(self, name):  
        if name in self.frame_lines: 
            self.current_animation = name 
        match name: 
            case 'up': 
                self.move(0, -10) 
            case 'down': 
                self.move(0, 10) 
            case 'left': 
                self.move(-10, 0) 
            case 'right': 
                self.move(10, 0) 
            
    def check(self): 
        keys = pg.key.get_pressed() 
        for control in self.controls: 
            code = control['key'] 
            name = control['animation'] 
            if keys[code]: 
                self.set_animation(name) 
        self.layer.blit(self.surface, self.position)
