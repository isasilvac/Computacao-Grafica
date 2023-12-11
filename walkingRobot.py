##Projeto: Robô em movimento com textura
#Isabela Cristina Silva Pedro

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from math import sin, pi

varX = 0.0
varY = 0.0
movY = 0
movX = 0

posicaoRobo = [0.0, 0.0, 0.0]
velocidadeRobo = 0.01
texturas = []


def obter_textura(file_name):
    image = Image.open(file_name)
    width, height = image.size
    image_data = image.tobytes("raw", "RGB", 0, -1)
    texture_id = glGentexturas(1)

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id

def cubo():
    glEnable(GL_TEXTURE_2D)
    
    # Face 1
    glBindTexture(GL_TEXTURE_2D, texturas[0])
    glBegin(GL_POLYGON)
    glNormal3f(0, 0, 1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, -0.25, 0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, 0.25)
    glEnd()

    # Face 2
    glBindTexture(GL_TEXTURE_2D, texturas[1])
    glBegin(GL_POLYGON)
    glNormal3f(0, 0, -1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, 0.25, -0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, -0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, -0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, -0.25)
    glEnd()

    # Face 3
    glBindTexture(GL_TEXTURE_2D, texturas[2])
    glBegin(GL_POLYGON)
    glNormal3f(1, 0, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, 0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0.25, -0.25, -0.25)
    glEnd()

    # Face 4
    glBindTexture(GL_TEXTURE_2D, texturas[3])
    glBegin(GL_POLYGON)
    glNormal3f(-1, 0, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-0.25, 0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, -0.25)
    glEnd()

    # Face 5
    glBindTexture(GL_TEXTURE_2D, texturas[4])
    glBegin(GL_POLYGON)
    glNormal3f(0, 1, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, 0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, 0.25, -0.25)
    glEnd()

    # Face 6
    glBindTexture(GL_TEXTURE_2D, texturas[5])
    glBegin(GL_POLYGON)
    glNormal3f(0, -1, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, -0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, -0.25)
    glEnd()

    glDisable(GL_TEXTURE_2D)


    glEnable(GL_TEXTURE_2D)

    # Face 1 
    glBindTexture(GL_TEXTURE_2D, texturas[2])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, -0.25, 0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, 0.25)
    glEnd()

    # Face 2 
    glBindTexture(GL_TEXTURE_2D, texturas[3])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, 0.25, -0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, -0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, -0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, -0.25)
    glEnd()

    # Face 3 
    glBindTexture(GL_TEXTURE_2D, texturas[4])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, 0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0.25, -0.25, -0.25)
    glEnd()

    # Face 4 
    glBindTexture(GL_TEXTURE_2D, texturas[5])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-0.25, 0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, -0.25)
    glEnd()

    # Face 5 
    glBindTexture(GL_TEXTURE_2D, texturas[0])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, 0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, 0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, 0.25, -0.25)
    glEnd()

    # Face 6
    glBindTexture(GL_TEXTURE_2D, texturas[1])
    glBegin(GL_POLYGON)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.25, -0.25, 0.25)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.25, -0.25, -0.25)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.25, -0.25, -0.25)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def iluminacao():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
   
    glLightfv(GL_LIGHT0,GL_POSITION, (-4, 4, -4))
    glLightfv(GL_LIGHT0,GL_AMBIENT, (0, 0, 0))
    glLightfv(GL_LIGHT0,GL_DIFFUSE,(1, 1, 1))

def cabeca():
        glPushMatrix()
        glTranslatef(0.0, 0.5, 0.0)
        glScalef(0.5, 0.5, 0.4)
        cubo() #cabeca
        glPopMatrix()

def corpo():
    glPushMatrix()
    glTranslatef(0.0, 0.1, 0.0)
    glScalef(0.5, 0.9, 0.3)
    cubo() #corpo
    glPopMatrix()

def bracoEsq():
    glPushMatrix()
    glTranslatef(0.185, 0.23, 0.0)
    glScalef(0.17, 0.3, 0.16)
    cubo() #bracoEsq
    glPopMatrix()

def bracoDir():
    glPushMatrix()
    glTranslatef(-0.18, 0.23, 0.0)
    glScalef(0.17, 0.3, 0.16)
    cubo() #bracoDir
    glPopMatrix()

def anteBracoEsq():
    glPushMatrix()
    glTranslatef(0.185, 0.05, 0.0)
    glScalef(0.17, 0.3, 0.15)
    cubo() # anteBracoEsq
    glPopMatrix()

def anteBracoDir():
    glPushMatrix()
    glTranslatef(-0.18, 0.05, 0.0)
    glScalef(0.17, 0.3, 0.15)
    cubo() #anteBracoDir
    glPopMatrix()

def pernaEsq():    
    glPushMatrix()
    glTranslatef(0.08, -0.23, 0.0)
    glScalef(0.17, 0.34, 0.2)
    cubo() #pernaEsq
    glPopMatrix()

def pernaDir():
    glPushMatrix()
    glTranslatef(-0.08, -0.23, 0.0)
    glScalef(0.17, 0.34, 0.2)
    cubo() #pernaDir
    glPopMatrix()

def pernaInfEsq():
    glPushMatrix()
    glTranslatef(0.08, -0.43, 0.0)
    glScalef(0.17, 0.34, 0.18)
    cubo() #pernaInfEsq
    glPopMatrix()

def pernaInfDir():
    glPushMatrix()
    glTranslatef(-0.08, -0.43, 0.0)
    glScalef(0.17, 0.34, 0.18)
    cubo() #pernaInfDir
    glPopMatrix()

def grupoBracoDir():
    global movY
    glPushMatrix()
    glTranslatef(0, 0.28, 0)
    glRotatef(movY*20, 1, 0, 0)
    glTranslatef(0, -0.28, 0)
    bracoDir()
    glTranslatef(0, 0.14, 0)
    glRotatef(20+movY*20, 1, 0, 0)
    glTranslatef(0, -0.14, 0)
    anteBracoDir()
    
    glPopMatrix()

def grupoBracoEsq():
    global movY
    glPushMatrix()
    glTranslatef(0, 0.28, 0)
    glRotatef(movY*-20, 1, 0, 0)
    glTranslatef(0, -0.28, 0)
    bracoEsq()    
    glTranslatef(0, 0.14, 0)
    glRotatef(20+movY*-20, 1, 0, 0)
    glTranslatef(0, -0.14, 0)
    anteBracoEsq()
    
    glPopMatrix()

def grupoPernaEsq():
    global movY
    glPushMatrix()
    glTranslatef(0, -0.1, 0)
    glRotatef(movY*+20, 1, 0, 0)
    glTranslatef(0, 0.1, 0)
    pernaEsq()
    glTranslatef(0, -0.3, 0)
    if movX >= pi*3/2 or movX <= pi/2:
        glRotatef(-40+abs(movY*40), 1, 0, 0)
    glTranslatef(0, 0.3, 0)
    pernaInfEsq()
    
    glPopMatrix()

def grupoPernaDir():
    global movY, movX
    glPushMatrix()
    glTranslatef(0, -0.1, 0)
    glRotatef(movY*-20, 1, 0, 0)
    glTranslatef(0, 0.1, 0)
    pernaDir()
    glTranslatef(0, -0.3, 0)
    if pi/2 <= movX <= pi*3/2:
        glRotatef(-40+abs(movY*40), 1, 0, 0)
    glTranslatef(0, 0.3, 0)
    pernaInfDir()
    
    glPopMatrix()

def desenha():
    global varY, movX, movY

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 0.10)  
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    gluLookAt(0.15, -0.10, 0.10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
 
    glTranslatef(posicaoRobo[0], posicaoRobo[1], posicaoRobo[2])
    
    glTranslatef(0, 1/20-abs(movY)/20, 0)
    glRotatef(varY, 0, 1, 0)
    grupoBracoDir()
    grupoBracoEsq()
    grupoPernaEsq()
    grupoPernaDir()
    cabeca()
    corpo()
    
    movX += velocidadeRobo*5
    if movX >= 2*pi:
        movX = 0
    movY = sin(movX)

    glutSwapBuffers()

def tecladoEspecial(tecla, x, y):
    global varY, movY
    global posicaoRobo

    # Move o robô para a frente
    if tecla == GLUT_KEY_RIGHT:
        posicaoRobo[2] -= velocidadeRobo*(0.6*abs(movY)+0.4)
        varY = 0

    # Move o robô para trás
    elif tecla == GLUT_KEY_LEFT:
        posicaoRobo[2] += velocidadeRobo*(0.6*abs(movY)+0.4)
        varY = -180

    glutPostRedisplay()

def init():
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.7, 0.2, 0.4, 1.0)  
    glEnable(GL_DEPTH_TEST)  
    glShadeModel(GL_SMOOTH)
    glEnable(GL_NORMALIZE)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    gluPerspective(45.0, 1.0, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    gluLookAt(4.0, 2.0, 1.0,  
              0.0, 0.0, 0.0, 
              0.0, 1.0, 0.0)  

    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity() 
    glViewport(0, 0, 500, 500)

    iluminacao()

def main():
    global texturas
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Robo")
    glutDisplayFunc(desenha)
    glutIdleFunc(desenha)
    glutReshapeFunc(reshape)
    glutSpecialFunc(tecladoEspecial)
    init()
    
    texturas.append(obter_textura(r"C:\Users\isabe\Downloads\metal.jpg"))
    texturas.append(obter_textura(r"C:\Users\isabe\Downloads\rosa.jpg"))
    texturas.append(obter_textura(r"C:\Users\isabe\Downloads\metal.jpg"))
    texturas.append(obter_textura(r"C:\Users\isabe\Downloads\rosa.jpg"))
    texturas.append(obter_textura(r"C:\Users\isabe\Downloads\metal.jpg"))
    texturas.append(obter_textura(r"C:\Users\isabe\Downloads\rosa.jpg"))

    glutMainLoop()

def reshape(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

if __name__ == "__main__":
    main()