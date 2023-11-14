#include <glut.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int windowWidth = 800;
int windowHeight = 600;
int xStart, yStart, xEnd, yEnd;
int lineSpots;

void init()
{
  glClearColor(1.0f, 1.0f, 1.0f, 0.0f);
}

void drawLine(int x1, int y1, int x2, int y2)
{
  int dx = abs(x2 - x1);
  int dy = abs(y2 - y1);
  int sx = (x1 < x2) ? 1 : -1;
  int sy = (y1 < y2) ? 1 : -1;
  int err = dx - dy;

  while (1)
  {
    glVertex2i(x1, y1);

    if (x1 == x2 && y1 == y2)
      break;
    int e2 = 2 * err;
    if (e2 > -dy)
    {
      err = err - dy;
      x1 = x1 + sx;
    }
    if (e2 < dx)
    {
      err = err + dx;
      y1 = y1 + sy;
    }
  }
}

void displayFunc()
{
  glClear(GL_COLOR_BUFFER_BIT);

  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(0, windowWidth, 0, windowHeight);

  if (lineSpots == 2)
  {
    glBegin(GL_POINTS);
    drawLine(xStart, yStart, xEnd, yEnd);
    glEnd();
    glutSwapBuffers();
    lineSpots = 0;
  }

  glFlush();
}

void mouseClick(int button, int state, int x, int y)
{
  if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
  {
    if (lineSpots == 0)
    {
      xStart = x;
      yStart = windowHeight - y; // Inverte o eixo Y
    }
    else
    {
      xEnd = x;
      yEnd = windowHeight - y;
    }
    lineSpots++;
    glutPostRedisplay();
  }
}

int main(int argc, char *argv[])
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
  glutInitWindowPosition(50, 50);
  glutInitWindowSize(windowWidth, windowHeight);
  glutCreateWindow("Viewing 2D");
  glutDisplayFunc(displayFunc);
  glutMouseFunc(mouseClick);
  init();
  glutMainLoop();
  return 0;
}
