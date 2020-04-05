# -*- coding: utf-8 -*-
import time
from intcomp import IntComp

inputStr = open('data.txt').read()
BASELIST = [int(i) for i in inputStr.split(',')]

# extend program input list with zeros
BASELIST = BASELIST + [0] * 9999999

class Item:
  BLANK = 0
  WALL = 1
  BLOCK = 2
  PADDLE = 3
  BALL = 4

def getChar(id):
  if id == Item.BLANK:
    return ' '
  elif id == Item.WALL:
    return '☐'
  elif id == Item.BLOCK:
    return '█'
  elif id == Item.PADDLE:
    return '─'
  elif id == Item.BALL:
    return '●'

def paintScreen(data, score):
  outputStr = ''
  for row in data:
    for item in row:
      outputStr += getChar(item)
    outputStr += '\n'
  print(outputStr + 'SCORE: {0}'.format(score))

def getStatus(data):
  ballX, paddleX = 0, 0
  for row in data:
    for i, item in enumerate(row):
      if item == Item.BALL:
        ballX = i
      elif item == Item.PADDLE:
        paddleX = i
  return ballX, paddleX

def adjustJoystick(ball, paddle):
  if (ball > paddle):
    return 1
  elif (ball < paddle):
    return -1
  return 0

def initGame(intComp, screenData):
  initialized = False
  while not intComp.isDone and not initialized:
    x = intComp.executeIntCode()
    y = intComp.executeIntCode()
    value = intComp.executeIntCode()
    if x == -1 and y == 0 or intComp.isDone:
      initialized = True
    else:
      screenData[y][x] = value

def run(intComp, screenData, joystickInput):
  intComp.input = joystickInput
  paused = False
  while not intComp.isDone and not paused:
    x = intComp.executeIntCode()
    y = intComp.executeIntCode()
    value = intComp.executeIntCode()
    if intComp.isDone:
      return None
    elif x == -1 and y == 0:
      return value
    else:
      screenData[y][x] = value
      paused = True

def startArcade():
  BASELIST[0] = 2 #infinite quarters
  intComp = IntComp()
  intComp.data = list(BASELIST)
  score, rows, columns = 0, 20, 44
  screenData = [[0 for x in range(columns)] for x in range(rows)]

  initGame(intComp, screenData)
  paintScreen(screenData, score)
  ballX, paddleX = getStatus(screenData)

  while not intComp.isDone:
    joystickInput = adjustJoystick(ballX, paddleX)
    gameOutput = run(intComp, screenData, joystickInput)
    score = gameOutput if gameOutput != None else score
    ballX, paddleX = getStatus(screenData)
    if paddleX > 0 and ballX > 0:
      paintScreen(screenData, score) 
      time.sleep(0.01)
  
  print('GAME OVER - SCORE: {0}'.format(score))

startArcade()
