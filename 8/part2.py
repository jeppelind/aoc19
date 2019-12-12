# -*- coding: utf-8 -*-
WIDTH = 25
HEIGHT = 6

inputStr = open('data.txt').read()
layerSize = WIDTH * HEIGHT

def getCombinedLayer():
  combinedLayer = ['2'] * layerSize
  idx = 0
  while idx < len(inputStr):
    layer = inputStr[idx:idx+layerSize]
    for i in range(layerSize):
      if layer[i] != '2' and combinedLayer[i] == '2':
        combinedLayer[i] = layer[i]
    idx += layerSize
  return combinedLayer

def printLayer(layer):
  idx = 0
  while idx < layerSize:
    row = layer[idx:idx+WIDTH]
    print(''.join(row).replace('1', '█').replace('0', ' '))
    idx += WIDTH

printLayer(getCombinedLayer())
