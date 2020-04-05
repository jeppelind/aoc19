# -*- coding: utf-8 -*-
from intcomp import IntComp

inputStr = open('data.txt').read()
BASELIST = [int(i) for i in inputStr.split(',')]

# extend program input list with zeros
BASELIST = BASELIST + [0] * len(BASELIST)

class Orientation:
  north = 0
  east = 1
  south = 2
  west = 3

def getNewOrientation(orientation, turn):
  modifier = -1 if turn == 0 else 1
  newOrientation = orientation + modifier
  if newOrientation < 0:
    newOrientation = Orientation.west
  elif newOrientation > Orientation.west:
    newOrientation = Orientation.north
  return newOrientation

def run():
  intComp = IntComp(list(BASELIST))
  orientation = Orientation.north
  x, y = 0, 0
  positions = { (x, y): 1 }
  minX, maxX, minY, maxY = 0, 0, 0, 0
  while not intComp.isDone:
    previousColor = positions[(x, y)] if (x, y) in positions else 0
    color = intComp.executeIntCode(previousColor)
    turn = intComp.executeIntCode(previousColor)
    if not intComp.isDone:
      positions[(x, y)] = color
      orientation = getNewOrientation(orientation, turn)
      if orientation == Orientation.north:
        y += 1
        maxY = y if y > maxY else maxY
      elif orientation == Orientation.east:
        x += 1
        maxX = x if x > maxX else maxX
      elif orientation == Orientation.south:
        y -= 1
        minY = y if y < minY else minY
      elif orientation == Orientation.west:
        x -= 1
        minX = x if x < minX else minX
  print(len(positions))
  
  outputStr = ''
  for row in range(maxY+1, minY-1, -1):
    for column in range(minX, maxX):
      isWhite = positions[(column, row)] if (column, row) in positions else 0
      outputStr += '█' if isWhite else ' '
    outputStr += '\n'
  print(outputStr)

run()
