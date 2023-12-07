import pygame
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, radians

pygame.init()
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -3.0)
glEnable(GL_DEPTH_TEST)

viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glGetFloatv(GL_MODELVIEW_MATRIX)

#glEnable(GL_LIGHTING)

#glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
#glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 0, 1, 1))
#glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 0, 1))
#glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))

#glEnable(GL_LIGHT0)
# Change path name to suit your directory structure

mesh = Cube()

def LineDraw():
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0, 0, 0)
    glVertex3f(100, 0, 0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0, 0, 0)
    glVertex3f(0,100, 0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 100)
    glEnd()

def XMove(mesh, i):
    mesh.vertices = [(vertex[0] + 0.1 * i, vertex[1], vertex[2]) for vertex in mesh.vertices]
def YMove(mesh, i):
    mesh.vertices = [(vertex[0], vertex[1] + 0.1 * i, vertex[2]) for vertex in mesh.vertices]
def ZMove(mesh, i):
    mesh.vertices = [(vertex[0], vertex[1], vertex[2] + 0.1 * i) for vertex in mesh.vertices]
def XScale(mesh, i):
    if i > 0:
        mesh.vertices = [(vertex[0] * 1.1, vertex[1], vertex[2]) for vertex in mesh.vertices]
    else:
        mesh.vertices = [(vertex[0] * 0.9, vertex[1], vertex[2]) for vertex in mesh.vertices]
def YScale(mesh, i):
    if i > 0:
        mesh.vertices = [(vertex[0], vertex[1] * 1.1, vertex[2]) for vertex in mesh.vertices]
    else:
        mesh.vertices = [(vertex[0], vertex[1] * 0.9, vertex[2]) for vertex in mesh.vertices]
def ZScale(mesh, i):
    if i > 0:
        mesh.vertices = [(vertex[0], vertex[1], vertex[2] * 1.1) for vertex in mesh.vertices]
    else:
        mesh.vertices = [(vertex[0], vertex[1], vertex[2] * 0.9 * i) for vertex in mesh.vertices]
def XRot(mesh, i):
    rad_angle = radians(5.0 * i)
    cos_a, sin_a = cos(rad_angle), sin(rad_angle)
    mesh.vertices = [(vertex[0],vertex[1] * cos_a - vertex[2] * sin_a,vertex[1] * sin_a + vertex[2] * cos_a) for vertex in mesh.vertices]
def YRot(mesh, i):
    rad_angle = radians(5.0 * i)
    cos_a, sin_a = cos(rad_angle), sin(rad_angle)
    mesh.vertices = [(vertex[0] * cos_a - vertex[2] * sin_a,vertex[1], vertex[0] * sin_a + vertex[2] * cos_a) for vertex in mesh.vertices]
def ZRot(mesh, i):
    rad_angle = radians(5.0 * i)
    cos_a, sin_a = cos(rad_angle), sin(rad_angle)
    mesh.vertices = [(vertex[0] * cos_a + vertex[1] * sin_a,-vertex[0] * sin_a + vertex[1] * cos_a,vertex[2]) for vertex in mesh.vertices]

done = False
left_p = False
right_p = False
forward_p = False
backward_p = False
up_p = False
down_p = False
mouse_l = False
mouse_r = False
mode_1 = False
mode_2 = False
mode_3 = False
up_down_angle = 0.0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            if(pygame.mouse.get_pressed()[0] == 1):
                mouse_l = True
            if(pygame.mouse.get_pressed()[2] == 1):
                pygame.mouse.set_visible(False)

                if mouse_r:
                    mouse_r = True
                else:
                    pygame.mouse.get_rel()
                    mouse_r = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode_1 = True
                mode_2 = False
                mode_3 = False
            if event.key == pygame.K_2:
                mode_2 = True
                mode_1 = False
                mode_3 = False
            if event.key == pygame.K_3:
                mode_3 = True
                mode_1 = False
                mode_2 = False
            if event.key == pygame.K_a:
                left_p = True
            if event.key == pygame.K_d:
                right_p = True
            if event.key == pygame.K_w:
                forward_p = True
            if event.key == pygame.K_s:
                backward_p = True
            if event.key == pygame.K_e:
                up_p = True
            if event.key == pygame.K_q:
                down_p = True

        if event.type==pygame.MOUSEBUTTONUP:
                mouse_l = False
                mouse_r = False
                pygame.mouse.set_visible(True)
                mode_1 = False
                mode_2 = False
                mode_3 = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left_p = False
            if event.key == pygame.K_d:
                right_p = False
            if event.key == pygame.K_w:
                forward_p = False
            if event.key == pygame.K_s:
                backward_p = False
            if event.key == pygame.K_e:
                up_p = False
            if event.key == pygame.K_q:
                down_p = False
    if mouse_r:
        glLoadIdentity()
        mouseMove = pygame.mouse.get_rel()
        up_down_angle += mouseMove[1]*0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        glPushMatrix() #행렬 저장 위아래로 회전한 각(축)을 저장해놈

        glLoadIdentity()

        if left_p:
            glTranslatef(0.1,0,0)
        if right_p:
            glTranslatef(-0.1,0,0)
        if forward_p:
            glTranslatef(0,0,0.1)
        if backward_p:
            glTranslatef(0,0,-0.1)
        if up_p:
            glTranslatef(0,-0.1,0)
        if down_p:
            glTranslatef(0,0.1,0)

        glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

        glMultMatrixf(viewMatrix) #현재 모델뷰 행렬에 인자값을 곱함
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glPopMatrix()

        glMultMatrixf(viewMatrix)
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if mouse_l:
        if mode_1:
            if left_p:
                XMove(mesh, 1)
            if right_p:
                XMove(mesh, -1)
            if forward_p:
                ZMove(mesh, 1)
            if backward_p:
                ZMove(mesh, -1)
            if up_p:
                YMove(mesh, -1)
            if down_p:
                YMove(mesh, 1)
        elif mode_2:
            if left_p:
                XRot(mesh, 1)
            if right_p:
                XRot(mesh, -1)
            if forward_p:
                ZRot(mesh, 1)
            if backward_p:
                ZRot(mesh, -1)
            if up_p:
                YRot(mesh, -1)
            if down_p:
                YRot(mesh, 1)
        elif mode_3:
            if left_p:
                XScale(mesh, 1)
            if right_p:
                XScale(mesh, -1)
            if forward_p:
                ZScale(mesh, 1)
            if backward_p:
                ZScale(mesh, -1)
            if up_p:
                YScale(mesh, -1)
            if down_p:
                YScale(mesh, 1)

        mesh.drawPivot()

    glColor3f(1.0, 1.0, 1.0)
    mesh.draw()
    LineDraw()
    pygame.display.flip()
    pygame.time.wait(50)

pygame.quit()
