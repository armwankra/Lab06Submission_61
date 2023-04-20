import sys 
import pygame as pg
pg.init()

win_x = 800
win_y = 400
screen = pg.display.set_mode((win_x, win_y))
check_w = False
check_a = False
check_s = False
check_d = False
pos_SX = 400
pos_SY = 200
w = 0 
a = 0 
s = 0 
d = 0 
while(1):
    screen.fill((255,255,255))
    pg.draw.rect(screen,(0,255,255),(pos_SX+d-a,pos_SY-w+s,100,100))
    if check_w:
        w+=1
        pg.time.delay(1)
    if check_a:
        a+=1
        pg.time.delay(1)
    if check_s:
        s+=1
        pg.time.delay(1)
    if check_d:
        d+=1
        pg.time.delay(1)


    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            print("Key D down")
            check_d = True
        if event.type == pg.KEYUP and event.key == pg.K_d:
            print("Key D up")
            check_d = False
        
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            print("Key A down")
            check_a = True
        if event.type == pg.KEYUP and event.key == pg.K_a:
            print("Key A up")
            check_a = False

        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            print("Key s down")
            check_s = True
        if event.type == pg.KEYUP and event.key == pg.K_s:
            print("Key s up")
            check_s = False

        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            print("Key w down")
            check_w = True
        if event.type == pg.KEYUP and event.key == pg.K_w:
            print("Key w up")
            check_w = False
        