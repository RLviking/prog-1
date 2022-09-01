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
    model='quad',
    Texture='assets\BG',
    Scale=36,z=1
)

def update():
    me.y += held_keys['w']*6*time.dt
    me.y -= held_keys['s']*6*time.dt

app.run()