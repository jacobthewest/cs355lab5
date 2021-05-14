from gl_base import Renderer
import numpy as np


class Lab5Renderer(Renderer):
    title = "Lab 5: 3D Rendering (OpenGL)"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def poll_keys(self):
        if self.key_pressed[self.keys.A]:
            print("A is pressed. Move Left.")
        elif self.key_pressed[self.keys.D]:
            print("D is pressed. Move right.")
        elif self.key_pressed[self.keys.S]:
            print("S is pressed. Move back.")
        elif self.key_pressed[self.keys.W]:
            print("W is pressed. Move forward.")
        elif self.key_pressed[self.keys.Q]:
            print("Q is pressed. Turn Left.")
        elif self.key_pressed[self.keys.E]:
            print("E is pressed. Turn right.")
        elif self.key_pressed[self.keys.R]:
            print("R is pressed. Move up.")
        elif self.key_pressed[self.keys.F]:
            print("F is pressed. Move down.")
        elif self.key_pressed[self.keys.P]:
            print("P is pressed. Cahnge to perspective mode.")
        elif self.key_pressed[self.keys.O]:
            print("O is pressed. Change to orthographic mode.")
        elif self.key_pressed[self.keys.H]:
            print("H is pressed. return 'home'.")

    def get_projection(self):
        """gets the projection matrix
        TODO: if in p state, returns perspective matrix
        TODO: if in o state, returns orthographic matrix
        """
        return np.eye(4)

    def get_view(self):
        """gets the view matrix
        TODO: return the view matrix
        """
        return np.eye(4)


if __name__ == "__main__":
    Lab5Renderer.run()
