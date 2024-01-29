import pygame as pg 
import player 
from player import Player 
FPS = 60 
bg = pg.image.load('resources/background.jpeg') 
pg.init() 
clock = pg.time.Clock() 
screen = pg.display.set_mode((1024, 768)) 
 
me = Player(screen, (64, 64), (512-40, 284-40), ( 
    {"key": pg.K_UP, "animation": "up"}, 
    {"key": pg.K_DOWN, "animation": "down"}, 
    {"key": pg.K_LEFT, "animation": "left"}, 
    {"key": pg.K_RIGHT, "animation": "right"} 
)) 
 
bro = Player(screen, (64, 64), (612-40, 484-50), ( 
    {"key": pg.K_w, "animation": "up"}, 
    {"key": pg.K_s, "animation": "down"}, 
    {"key": pg.K_a, "animation": "left"}, 
    {"key": pg.K_d, "animation": "right"} 
)) 
 
gameover = False 
while not gameover: 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            gameover = True 
    
    screen.blit(bg, (0, 0)) 
    me.check() 
    bro.check() 
    pg.display.update() 
    clock.tick(FPS)
