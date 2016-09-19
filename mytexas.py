#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GLU import *

from math import *
import mymaintest
import sys
from Image import *

#begin from mymaintest.main
lastx=0
lasty=0
# set up a light 
lightOnePosition = (40.0, 40, 100.0, 0.0)
lightOneColor = (0.99, 0.99, 0.99, 1.0) 

lightTwoPosition = (-40.0, 40, 100.0, 0.0)
lightTwoColor = (0.99, 0.99, 0.99, 1.0) 
#end from mymaintest.main


SCALE = 0.8
TSCALE = 4

brand_points = map(lambda x: (0, 0, TSCALE*x), (0.1, 0.0, -5.0, -5.1))
brand_colors = ((1.0, 0.3, 0.0),)*4

points = ((-1.5, 2.0), (-0.75, 2.0), (-0.75, 1.38), (-0.5, 1.25), (0.88, 1.12), (1.0, 0.62), (1.12, 0.1), (0.5, -0.5), (0.2, -1.12),
          (0.3, -1.5), (-0.25, -1.45), (-1.06, -0.3), (-1.38, -0.3), (-1.65, -0.6), (-2.5, 0.5), (-1.5, 0.5), (-1.5, 2.0), (-0.75, 2.0))

tspine = map(lambda x: (TSCALE*x[0], TSCALE*x[1], 0), points)

texas_xsection = map(lambda x: (SCALE*x[0], SCALE*x[1]), points[1:])

tcolors = []

for i in range(len(texas_xsection)):
	tcolors.append((((i*33) % 255)/255.0, ((i*47) % 255)/255.0, ((i*89) % 255)/255.0))


texas_normal = []

for i in range(1, len(texas_xsection)):
	ax = texas_xsection[i][0] - texas_xsection[i-1][0]
	ay = texas_xsection[i][1] - texas_xsection[i-1][1]
	alen = sqrt (ax*ax + ay*ay)
	texas_normal.append((-ay / alen, ax / alen))

texas_normal.insert(0, texas_normal[-1])

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

texture = 0


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	# If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    sys.exit()

def LoadTexture():
	#image = open("test2.bmp")
	#image = open("bluecloth08.bmp")
	image = open("bluecloth09.bmp")
	ix = image.size[0]
	print ix
	iy = image.size[1]
	print iy
	image = image.tostring("raw","RGBX", 0, -1)
	
	# Create Texture
	glBindTexture(GL_TEXTURE_2D, glGenTextures(1))	# 2d texture (x and y size)
	glPixelStorei(GL_UNPACK_ALIGNMENT,1)
	glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def DrawGLScene():
	global texas_xsection, texas_normal, tspine, tcolors, brand_points, brand_colors
	global lastx, lasty
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	# Clear The Screen And The Depth Buffer
	####glLoadIdentity()					# Reset The View
	glTranslatef(0.0,-0.25,-2.8)			# Move Into The Screen
	####
	##### Note there does not seem to be support for this call.
	#glBindTexture(GL_TEXTURE_2D,texture)	# Rotate The Pyramid On It's Y Axis
	
	glBegin(GL_QUADS)			    # Start Drawing The Cube

	# Front Face (note that the texture's corners have to match the quad's corners)
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	# Top Right Of The Texture and Quad
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Left Of The Texture and Quad
	
	
	glEnd(); #done drawing the face.
	#  since this is double buffered, swap the buffers to display what just got drawn. 
	#glutSwapBuffers()


	#from mytexas.py:
	#glEnable(GL_LINE_SMOOTH)
	#glEnable(GL_POLYGON_SMOOTH)
	#glEnable(GL_POINT_SMOOTH)
	#glHint(GL_LINE_SMOOTH_HINT|GL_POLYGON_SMOOTH_HINT, GL_NICEST)
	
	#glEnable(GL_BLEND)							# Enable Blending
	#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)			

	# set up some matrices so that the object spins with the mouse


	#xxxxx gleSetJoinStyle(TUBE_NORM_FACET | TUBE_JN_ANGLE | TUBE_CONTOUR_CLOSED | TUBE_JN_CAP)
	#xxxxx glPushMatrix ()
	#xxxxx glTranslatef (0.0, 0.0, -80.0)
	#xxxxx glRotatef (lastx, 0.0, 1.0, 0.0)
	#xxxxx glRotatef (lasty, 1.0, 0.0, 0.0)

	#xxxxx gleExtrusion(texas_xsection, texas_normal, None, tspine, tcolors)
	#xxxxx gleExtrusion(texas_xsection, texas_normal, None, brand_points, brand_colors)

	#xxxxx glPopMatrix ()

	glutSwapBuffers ()

# get notified of mouse motions
def MouseMotion (x, y):
	global lastx, lasty
	lastx = x
	lasty = y
	glutPostRedisplay ()


def JoinStyle (msg):
	sys.exit(0)

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
####	# initialize GL */
####	glClearDepth (1.0)
####	glEnable (GL_DEPTH_TEST)
####	glClearColor (0.0, 0.0, 0.0, 0.0)
####	glShadeModel (GL_SMOOTH)
####
####	glMatrixMode (GL_PROJECTION)
####	# roughly, measured in centimeters */
####	glFrustum (-9.0, 9.0, -9.0, 9.0, 50.0, 150.0)
####	glMatrixMode(GL_MODELVIEW)
####
####	# initialize lighting */
####	glLightfv (GL_LIGHT0, GL_POSITION, lightOnePosition)
####	glLightfv (GL_LIGHT0, GL_DIFFUSE, lightOneColor)
####	glEnable (GL_LIGHT0)
####	glLightfv (GL_LIGHT1, GL_POSITION, lightTwoPosition)
####	glLightfv (GL_LIGHT1, GL_DIFFUSE, lightTwoColor)
####	glEnable (GL_LIGHT1)
####	glEnable (GL_LIGHTING)
####	glColorMaterial (GL_FRONT_AND_BACK, GL_DIFFUSE)
####	glEnable (GL_COLOR_MATERIAL)




	LoadTexture()
	glEnable(GL_TEXTURE_2D)
	glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
	glMatrixMode(GL_PROJECTION)
#	glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
	#the following messes up texas display
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

	glMatrixMode(GL_MODELVIEW)
	# roughly, measured in centimeters */
	glFrustum (-9.0, 9.0, -9.0, 9.0, 50.0, 150.0)

	# initialize lighting */
	glLightfv (GL_LIGHT0, GL_POSITION, lightOnePosition)
	glLightfv (GL_LIGHT0, GL_DIFFUSE, lightOneColor)
	glEnable (GL_LIGHT0)
	glLightfv (GL_LIGHT1, GL_POSITION, lightTwoPosition)
	glLightfv (GL_LIGHT1, GL_DIFFUSE, lightTwoColor)
	glEnable (GL_LIGHT1)
	glEnable (GL_LIGHTING)
	glColorMaterial (GL_FRONT_AND_BACK, GL_DIFFUSE)
	glEnable (GL_COLOR_MATERIAL)



# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
	if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
		Height = 1

	glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)


def mymaintestmain(DrawGLScene):
	global glutDisplayFunc, glutMotionFunc
	global window
	# initialize glut 
	glutInit(sys.argv)

	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_ALPHA)
	
	# get a 640 x 480 window 
	#glutInitWindowSize(640, 480)
	# the window starts at the upper left corner of the screen 
	#glutInitWindowPosition(0, 0)

	glutCreateWindow("pretty picture")
	glutDisplayFunc(DrawGLScene)
	# Uncomment this line to get full screen.
	#glutFullScreen()
	# Register the function called when our window is resized.
	#glutReshapeFunc(ReSizeGLScene)
	
	glutMotionFunc(MouseMotion)
	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)


	# create popup menu */
#	glutCreateMenu (JoinStyle)
#	glutAddMenuEntry ("Exit", 99)
#	glutAttachMenu (GLUT_MIDDLE_BUTTON)

	# Initialize our window. 
	InitGL(640, 480)

	# Start Event Processing Engine	
	glutMainLoop ()

mymaintestmain(DrawGLScene)
