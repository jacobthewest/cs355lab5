from gl_base import Renderer
import numpy as np


class Lab5Renderer(Renderer):
    title = "Lab 5: 3D Rendering (OpenGL)"

    xpos = 0
    ypos = 0
    zpos = -20
    theta = 0
    ortho = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def poll_keys(self):
        if self.key_pressed[self.keys.A]: # Move left
            self.xpos -= np.cos(self.theta) * 0.1
            self.zpos -= np.sin(self.theta) * 0.1
        elif self.key_pressed[self.keys.D]: # Move right
            self.xpos += np.cos(self.theta) * 0.1
            self.zpos += np.sin(self.theta) * 0.1
        elif self.key_pressed[self.keys.S]: # Move back
            self.zpos -= 0.2
            if self.theta < 0:
                self.xpos -= 0.1
            elif self.theta > 0:
                self.xpos += 0.1
        elif self.key_pressed[self.keys.W]: # Move forward
            self.zpos += 0.2
            if self.theta < 0:
                self.xpos += 0.1
            elif self.theta > 0:
                self.xpos -= 0.1
        elif self.key_pressed[self.keys.Q]: # Turn left
            self.theta += 0.05
        elif self.key_pressed[self.keys.E]: # Turn right
            self.theta -= 0.05
        elif self.key_pressed[self.keys.R]: # Move up
            self.ypos += 0.1
        elif self.key_pressed[self.keys.F]: # Move down
            self.ypos -= 0.1
        elif self.key_pressed[self.keys.P]: # perspective mode
            self.ortho = False
        elif self.key_pressed[self.keys.O]: # orthographic mode
            self.ortho = True
        elif self.key_pressed[self.keys.H]: # return home
            self.xpos = 0
            self.ypos = 0
            self.zpos = -20
            self.theta = 0

    def get_projection(self): # Gets the projection matrix

        if(self.ortho): # Return the orthographic projection
            projection = np.array([[1 / 10, 0, 0, 0],
                                   [0, 1 / 10, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 1]])
        else: # Return the perspective projection
            projection = np.array([[1, 0, 0, 0],
                                   [0, 1, 0, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 1, 0]])
        return np.transpose(projection)

    def get_view(self): #Gets the view matrix
        theta = self.theta
        translation = np.array([[1, 0, 0, -self.xpos],
                                [0, 1, 0, -self.ypos],
                                [0, 0, 1, -self.zpos],
                                [0, 0, 0, 1]])
        rotation = np.array([[np.cos(theta), 0, np.sin(theta), 0],
                               [0, 1, 0, 0],
                               [-np.sin(theta), 0, np.cos(theta), 0],
                               [0, 0, 0, 1]])
        transform = np.matmul(rotation, translation)
        return np.transpose(transform)


if __name__ == "__main__":
    Lab5Renderer.run()
