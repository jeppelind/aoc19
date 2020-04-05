inputStr = open('data.txt').read()
data = [int(i) for i in inputStr.split(',')]

# extend program input list with zeros
data = data + [0] * len(data)

class Mode:
  position = 0
  immediate = 1
  relative = 2

class Operation:
  addition = 1
  multiplication = 2
  inputValue = 3
  outputValue = 4
  jumpIfTrue = 5
  jumpIfFalse = 6
  lessThan = 7
  equals = 8
  adjustRelativeBase = 9

def getOperationAndModes(operationCode):
  fullCode = appendMissingDigits(str(operationCode))
  operation = int(fullCode[3:5])
  mode1 = int(fullCode[2])
  mode2 = int(fullCode[1])
  mode3 = int(fullCode[0])
  return operation, mode1, mode2, mode3

def appendMissingDigits(strValue):
  missingDigits = 5 - len(strValue)
  for _ in range(0, missingDigits):
    strValue = '0' + strValue
  return strValue

def getParamIdx(idx, relativeBase, operation, mode1, mode2, mode3):
  param1 = getIdxByMode(idx+1, relativeBase, mode1)
  if operation == Operation.inputValue or operation == Operation.outputValue:
    return param1, None, None
  param2 = getIdxByMode(idx+2, relativeBase, mode2)
  if operation == Operation.jumpIfFalse or operation == Operation.jumpIfTrue:
    return param1, param2, None
  param3 = getIdxByMode(idx+3, relativeBase, mode3)
  return param1, param2, param3

def getIdxByMode(idx, relativeBase, mode):
  if mode == Mode.immediate:
    return idx
  elif mode == Mode.position:
    return data[idx]
  elif mode == Mode.relative:
    return data[idx] + relativeBase

def calculateValue(operation, param1, param2):
  return param1 + param2 if operation == Operation.addition else param1 * param2

def getIdxIncreaseAmount(operation):
  if operation == Operation.jumpIfFalse or operation == Operation.jumpIfTrue:
    return 0
  elif operation == Operation.inputValue or operation == Operation.outputValue or operation == Operation.adjustRelativeBase:
    return 2
  return 4

class IntComp:
  def __init__(self, indata):
    self.data = indata
    self.idx = 0
    self.isDone = False
    self.outputVal = None
    self.relativeBase = 0

  def executeIntCode(self, inputValue):
    while self.data[self.idx] != 99:
      operation, mode1, mode2, mode3 = getOperationAndModes(self.data[self.idx])
      idx1, idx2, idx3 = getParamIdx(self.idx, self.relativeBase, operation, mode1, mode2, mode3)
      if operation == Operation.addition or operation == Operation.multiplication:
        self.data[idx3] = calculateValue(operation, self.data[idx1], self.data[idx2])
      elif operation == Operation.inputValue:
        self.data[idx1] = inputValue
      elif operation == Operation.outputValue:
        self.outputVal = self.data[idx1]
        self.idx += 2
        return self.outputVal
      elif operation == Operation.jumpIfTrue:
        self.idx = self.data[idx2] if self.data[idx1] != 0 else self.idx + 3
      elif operation == Operation.jumpIfFalse:
        self.idx = self.data[idx2] if self.data[idx1] == 0 else self.idx + 3
      elif operation == Operation.lessThan:
        self.data[idx3] = 1 if self.data[idx1] < self.data[idx2] else 0
      elif operation == Operation.equals:
        self.data[idx3] = 1 if self.data[idx1] == self.data[idx2] else 0
      elif operation == Operation.adjustRelativeBase:
        self.relativeBase += self.data[idx1]
      self.idx += getIdxIncreaseAmount(operation)
    self.isDone = True
    return self.outputVal

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
  inputs = []
  outputs = []
  intComp = IntComp(data[:])
  orientation = Orientation.north
  x, y = 0, 0
  positions = { (x, y): 0 }
  while not intComp.isDone:
    previousColor = positions[(x, y)] if (x, y) in positions else 0
    inputs.append(previousColor)
    color = intComp.executeIntCode(previousColor)
    turn = intComp.executeIntCode(previousColor)
    if not intComp.isDone:
      outputs.append((color, turn))
      positions[(x, y)] = color
      orientation = getNewOrientation(orientation, turn)
      # print(x, y, color, turn, orientation)
      if orientation == Orientation.north:
        y += 1
      elif orientation == Orientation.east:
        x += 1
      elif orientation == Orientation.south:
        y -= 1
      elif orientation == Orientation.west:
        x -= 1
  # print(inputs)
  # print(outputs)
  print(len(inputs), len(outputs))
  print(len(positions))

run()
