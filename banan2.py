
from re import A
from tkinter import Scale
from typing import Literal
from  ursina import *
import time
score=0
points=1
speed=4

app = Ursina()
me = Animation(
    'assets\player',
    Collider='box',y=5
)
Sky()
camera.orthographic = True
camera.fov = 20
me = Entity(
    model='cube',
    texture='unicorn',
    scale=1.5,
    collider = "box"
)
# hinder
fly = Entity(
    model='cube',
    texture= 'anka',
    collider='box',
    scale=1.5,
    x=20,
    y=-10
)
flies = []
def newfly():
    a = 9
    new = duplicate(
        fly,
        y=(random.random()*a*2)-a
    )
    flies.append(new)
    invoke(newfly, delay=1)

game_over = False

def update(): # inte del av hinder 
    global score, speed,game_over

    for fly in flies:
         
        fly.x -= speed*time.dt # hinder slutar
    me.y += held_keys['up arrow']*6*time.dt
    me.y -= held_keys['down arrow']*6*time.dt
    a = held_keys['up arrow']*-10
    b = held_keys['down arrow']*10
    if a != 0:
        me.rotation_z = a
    else:
        me.rotation_z = b

    
    t = me.intersects()
    if t.hit:
        game_over = True

    for fly in flies:
        fly.x -= 4*time.dt
        touch = fly.intersects()
        if touch.hit:
            print("Hit")
            flies.remove(fly)
            destroy(fly)
            score +=points
            print(score)
            if score % 20 == 0:
                speed *= 1.4 
            
    if game_over:
        for x in scene.entities:
            destroy(x)

def input(key):
    if key == 'space':
        e = Entity(
            y=me.y,
            x=me.x+2,
            model='cube',
            texture='banan',
            collider='cube'
        )
        e.animate_x(
            30,
            duration=2,
            curve=curve.linear
        )
        invoke(destroy, e,
                delay=2)    

newfly()
EditorCamera()
app.run() 
  