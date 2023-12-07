from OpenGL.GL import *


class Mesh3D:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5)]

        self.traingles = [0, 2, 3, 0, 3, 1]        

    def draw(self):
        for t in range(0, len(self.traingles), 3):
            glBegin(GL_POLYGON)
            glVertex3fv(self.vertices[self.traingles[t]])
            glVertex3fv(self.vertices[self.traingles[t + 1]])
            glVertex3fv(self.vertices[self.traingles[t + 2]])
            glEnd()

    def drawPivot(self):
        sum_x = 0.0
        sum_y = 0.0
        sum_z = 0.0
        for vertex in self.vertices:
            sum_x += vertex[0]
            sum_y += vertex[1]
            sum_z += vertex[2]

        pivot = (sum_x / self.vertices.__len__() , sum_y/ self.vertices.__len__() , sum_z/ self.vertices.__len__())

        glLineWidth(3.0)
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(*pivot)
        glVertex3f(pivot[0] + 1, pivot[1],  pivot[2])
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(*pivot)
        glVertex3f(pivot[0], pivot[1] + 1,  pivot[2])
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(*pivot)
        glVertex3f(pivot[0], pivot[1], pivot[2] + 1)
        glEnd()