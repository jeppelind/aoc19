WIDTH = 25
HEIGHT = 6

inputStr = open('data.txt').read()

layerSize = WIDTH * HEIGHT
idx = 0
minZeroCount = 99999
minimalZeroLayer = None
while idx < len(inputStr):
  layer = inputStr[idx:idx+layerSize]
  if layer.count('0') < minZeroCount:
    minimalZeroLayer = layer
    minZeroCount = layer.count('0')
  idx += layerSize

print(minimalZeroLayer.count('1') * minimalZeroLayer.count('2'))
