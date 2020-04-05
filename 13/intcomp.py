class Mode:
  POSITION = 0
  IMMEDIATE = 1
  RELATIVE = 2

class Operation:
  ADDITION = 1
  MULTIPLICATION = 2
  INPUT = 3
  OUTPUT = 4
  JUMP_IF_TRUE = 5
  JUMP_IF_FALSE = 6
  LESS_THAN = 7
  EQUALS = 8
  ADJUST_RELATIVE_BASE = 9

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

def getParamIdx(idx, relativeBase, operation, data, mode1, mode2, mode3):
  param1 = getIdxByMode(idx+1, relativeBase, data, mode1)
  if operation == Operation.INPUT or operation == Operation.OUTPUT:
    return param1, None, None
  param2 = getIdxByMode(idx+2, relativeBase, data, mode2)
  if operation == Operation.JUMP_IF_FALSE or operation == Operation.JUMP_IF_TRUE:
    return param1, param2, None
  param3 = getIdxByMode(idx+3, relativeBase, data, mode3)
  return param1, param2, param3

def getIdxByMode(idx, relativeBase, data, mode):
  if mode == Mode.IMMEDIATE:
    return idx
  elif mode == Mode.POSITION:
    return data[idx]
  elif mode == Mode.RELATIVE:
    return data[idx] + relativeBase

def calculateValue(operation, param1, param2):
  return param1 + param2 if operation == Operation.ADDITION else param1 * param2

def getIdxIncreaseAmount(operation):
  if operation == Operation.JUMP_IF_FALSE or operation == Operation.JUMP_IF_TRUE:
    return 0
  elif operation == Operation.INPUT or operation == Operation.OUTPUT or operation == Operation.ADJUST_RELATIVE_BASE:
    return 2
  return 4

class IntComp:
  def __init__(self):
    self.data = []
    self.idx = 0
    self.isDone = False
    self.relativeBase = 0
    self.stopOnOutput = True
    self.input = None
    self.output = []

  def executeIntCode(self):
    while self.data[self.idx] != 99:
      operation, mode1, mode2, mode3 = getOperationAndModes(self.data[self.idx])
      idx1, idx2, idx3 = getParamIdx(self.idx, self.relativeBase, operation, self.data, mode1, mode2, mode3)
      if operation == Operation.ADDITION or operation == Operation.MULTIPLICATION:
        self.data[idx3] = calculateValue(operation, self.data[idx1], self.data[idx2])
      elif operation == Operation.INPUT:
        self.data[idx1] = self.input
      elif operation == Operation.OUTPUT:
        if self.stopOnOutput:
          self.idx += 2
          return self.data[idx1]
        else:
          self.output.append(self.data[idx1])
      elif operation == Operation.JUMP_IF_TRUE:
        self.idx = self.data[idx2] if self.data[idx1] != 0 else self.idx + 3
      elif operation == Operation.JUMP_IF_FALSE:
        self.idx = self.data[idx2] if self.data[idx1] == 0 else self.idx + 3
      elif operation == Operation.LESS_THAN:
        self.data[idx3] = 1 if self.data[idx1] < self.data[idx2] else 0
      elif operation == Operation.EQUALS:
        self.data[idx3] = 1 if self.data[idx1] == self.data[idx2] else 0
      elif operation == Operation.ADJUST_RELATIVE_BASE:
        self.relativeBase += self.data[idx1]
      self.idx += getIdxIncreaseAmount(operation)
    self.isDone = True
