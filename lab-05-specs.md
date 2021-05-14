# Lab 5: 3D Graphics with OpenGL
This lab intrduces you to simple 3D graphics by having you set up the world-to-camera, projection (perspective and orhographic), and viewport transformations.  In this lab, we will not IPython Notebooks but will use command line Python to make a viewing window.

In this lab, you will move around a *very* simple virtual world that consists of a wireframe model of a small house--if you wish, you may play around with the model to render other scenes.  In this world, you can turn left or right in the *xz* plane of the world; move up or down in the *y* direction, or move forward, backward, left, or right ***relative to the direction you are facing***.  You should be able to switch the projection between perspective and orthographic.

When moving, you should move one unit in the world coordinates ***relative to the direction you are currently facing***. When turning, you should turn one degree left or right.

---

## User Interface
Your only interaction will be thorugh the keyboard. Each of the following keys should perform the corresponding actions.

Key | Action
:---: | :---
a  | Move left
d  | Move right
w  | Move forward
s  | Move backward
q  | Turn left
e  | Turn right
r  | Move up
f  | Move down
h  | Return to the original "home" position and orientation
o  | Switch to orthographic projection
p  | Swtich to perspective projection

---

## Implementation Notes
You are given two files that you will **not** need to edit (`gl_base.py` and `gl_models.py`) and a file that you will edit and turn in (`lab5.py`).  `gl_base.py` contains a class that you will inherit from called `Renderer`, which handles a lot of the boilerplate code involved with OpenGL.  `gl_models.py` contain the actual 3d geometry needed for this lab and the next including a house, a car, and a tire.  `lab5.py` is the file you will edit.

Already provided in `lab5.py` is a class called `Lab5Renderer` that inherits from `Renderer` and provides methods that you will override including `poll_keys`, `get_projection` and `get_view`.   `poll_keys` handles the keyboard input and an example of how to detect key presses is provided for the `a` key.  `get_projection` is the method where you will implement your projection matrix and should return an orthographic projection matrix if you are in orthographic mode and a perspective matrix if you are in perspective mode.  `get_view` should return the view matrix.  Both `get_projection` and `get_view` should return row ordered numpy arrays representing their respecitve matrices.
