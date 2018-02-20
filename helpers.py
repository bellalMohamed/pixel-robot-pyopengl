from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawShape(nodes, color):
	colors = {
		'black': [0, 0, 0],
		'gray': [0.32, 0.32, 0.32],
		'red': [1, 0, 0]
	}

	glColor(colors[color][0], colors[color][1], colors[color][2])
	glBegin(GL_POLYGON)
	ratio = 1.2 * 95
	for node in nodes:
		glVertex2d(node[0] / ratio, node[1] / ratio)

	glEnd()
