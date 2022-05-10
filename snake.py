"""
Juego: Paint
Programador 1: Josué Fuentes
Programador 2: Alex Flores
Fecha: 10 / mayo / 2022
"""

from random import randrange
from turtle import *
import random

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
cont = 0
colors = ['green','blue','pink','black','orange']
colorFood= random.choice(colors)
colorSnake = random.choice(colors)
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190



def move():
    global cont
    cont += 1
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)
    
        
    #Movemos la comida
    if(cont%10==0):
      food.x += randrange(-10,20,10)
      food.y -= randrange(-10,20,10)
  
    if(food.x < -200): #Si se sale por la izquierda
      food.x += 10 #Se mueve a la derecha

    if(food.x > 190): #Si se sale por la derecha
      food.x -= 10 #Se mueve a la izquierda

    if(food.y < -200): #Si se sale para arriba
      food.y += 10 #Se mueve para abajo

    if(food.y > 190): #Si se sale por abajo
      food.y -= 10 #Se mueve para arriba

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)
    
 


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
