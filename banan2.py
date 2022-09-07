"""""
# https://www.ursinaengine.org/cheat_sheet.html
# Import everything from my file UrsinaClasses.py so ursina and all my classes are imported
from Ursina.UrsinaClasses import *
# In Ursina you can work with 2D and 3D.


# Import the PlatformerController2d is you want to do a platform game


#Create our Ursina-app
app = Ursina()

#This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = False

# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    pass

# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    pass


#Call the createworld function
createworld()

# Creates a sky with the variable name sky. This is a prefab in Ursina
sky = Sky()

# If you want a first person game you have to create a player with a given position

app.run()
"""""
from re import A
from tkinter import Scale
from  ursina import *
import time

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
    texture='plane.jpg',
    scale=1.5,
    collider = "box"
)
# hinder
fly = Entity(
    model='cube',
    texture='assets\\fly1',
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


def update(): # inte del av hinder 
    for fly in flies:
        fly.x -= 4*time.dt # hinder slutar
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
        quit()

    for fly in flies:
        fly.x -= 4*time.dt
        touch = fly.intersects()
        if touch.hit:
            print("Hit")
            flies.remove(fly)
            destroy(fly)


def input(key):
    if key == 'space':
        e = Entity(
            y=me.y,
            x=me.x+2,
            model='cube',
            texture='assets\Bullet',
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