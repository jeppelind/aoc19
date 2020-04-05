# -*- coding: utf-8 -*-
from intcomp import IntComp

inputStr = open('data.txt').read()
BASELIST = [int(i) for i in inputStr.split(',')]

# extend program input list with zeros
BASELIST = BASELIST + [0] * len(BASELIST)

def run():
  intComp = IntComp()
  intComp.data = list(BASELIST)
  blockCount = 0
  while not intComp.isDone:
    intComp.executeIntCode()
    intComp.executeIntCode()
    tileId = intComp.executeIntCode()
    if tileId == 2:
      blockCount += 1
  print(blockCount)

run()
