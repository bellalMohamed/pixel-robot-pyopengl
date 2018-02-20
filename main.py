from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from helpers import *

def draw():
    #background
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    drawShape([
        [-35, 95],
        [-35, 83],
        [35, 83],
        [35, 95]
    ], 'black');

    drawShape([
        [-48, 35],
        [-48, 47],
        [48, 47],
        [48, 35]
    ], 'black');

    drawShape([
        [35, 95],
        [35, 35],
        [23, 35],
        [23, 95]
    ], 'black');

    drawShape([
        [-35, 95],
        [-35, 35],
        [-23, 35],
        [-23, 95]
    ], 'black');

    drawShape([
        [-23, 83],
        [-23, 47],
        [23, 47],
        [23, 83]
    ], 'gray');


    drawShape([
        [-35, 35],
        [-35, 0],
        [35, 0],
        [35, 35]
    ], 'gray');

    drawShape([
        [47, 24],
        [47, 0],
        [35, 0],
        [35, 24],
    ], 'gray');

    drawShape([
        [47.75, 36],
        [47.75, 24],
        [35, 24],
        [35, 36],
    ], 'black');

    drawShape([
        [58, 36],
        [58, 0],
        [47, 0],
        [47, 36],
    ], 'black');

    drawShape([
        [-59, 36],
        [-35, 36],
        [-35, 0],
        [-59, 0],
    ], 'black');

    drawShape([
        [-11, 71],
        [1, 71],
        [1, 59],
        [-11, 59],
    ], 'red');

    drawShape([
        [13, 71],
        [25, 71],
        [25, 59],
        [13, 59],
    ], 'red');

    #bottom
    drawShape([
        [-59, 0],
        [-59, -70],
        [-48, -70],
        [-48, 0],
    ], 'black');

    drawShape([
        [-48, -46],
        [-35, -46],
        [-35, 0],
        [-48, 0],
    ], 'black');

    #Points convention top-lef => top-right => bottom-right => bottom-left

    drawShape([
        [-35, 0],
        [47, 0],
        [47, -35],
        [-35, -35],
    ], 'gray');

    drawShape([
        [-59, -35],
        [70, -35],
        [70, -47],
        [-59, -47],
    ], 'black');

    drawShape([
        [58, 0],
        [70, 0],
        [70, -35],
        [58, -47],
    ], 'black');

    drawShape([
        [47, -12],
        [59, -12],
        [59, -35],
        [47, -35],
    ], 'gray');

    drawShape([
        [47, 0],
        [58, 0],
        [58, -12],
        [47, -12],
    ], 'black');

    drawShape([
        [-25, -47],
        [-2, -47],
        [-2, -71],
        [-13, -71],
        [-13, -94],
        [-25, -94],
    ], 'black');

    drawShape([
        [22, -47],
        [46, -47],
        [46, -71],
        [34, -71],
        [34, -94],
        [22, -94],
    ], 'black');

    drawShape([
        [22, -12],
        [34, -12],
        [34, -23],
        [22, -23],
    ], 'black');

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"first opengl program")
glutDisplayFunc(draw)
glutMainLoop()
