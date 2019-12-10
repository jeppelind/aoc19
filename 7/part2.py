import itertools
inputStr = open('data.txt').read()
BASELIST = [int(i) for i in inputStr.split(',')]

class Mode:
  position = 0
  immediate = 1

class Operation:
  addition = 1
  multiplication = 2
  inputValue = 3
  outputValue = 4
  jumpIfTrue = 5
  jumpIfFalse = 6
  lessThan = 7
  equals = 8

class Adapter:
  def __init__(self, name):
    self.name = name
    self.data = list(BASELIST)
    self.idx = 0
    self.handledInputCnt = 0
    self.isDone = False
    self.outputVal = None

  def executeIntCode(self, phaseVal, signalVal):
    while self.data[self.idx] != 99:
      operation, mode1, mode2, mode3 = getOperationAndModes(self.data[self.idx])
      idx1, idx2, idx3 = getParamIdx(self.idx, operation, self.data, mode1, mode2, mode3)
      if operation == Operation.addition or operation == Operation.multiplication:
        self.data[idx3] = calculateValue(operation, self.data[idx1], self.data[idx2])
      elif operation == Operation.inputValue:
        self.data[idx1] = phaseVal if self.handledInputCnt == 0 else signalVal
        self.handledInputCnt += 1
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
      self.idx += getIdxIncreaseAmout(operation)
    self.isDone = True
    return self.outputVal

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

def getParamIdx(idx, operation, data, mode1, mode2, mode3):
  param1 = idx+1 if mode1 == Mode.immediate else data[idx+1]
  if operation == Operation.inputValue or operation == Operation.outputValue:
    return param1, None, None
  param2 = idx+2 if mode2 == Mode.immediate else data[idx+2]
  if operation == Operation.jumpIfFalse or operation == Operation.jumpIfTrue:
    return param1, param2, None
  param3 = idx+3 if mode3 == Mode.immediate else data[idx+3]
  return param1, param2, param3

def calculateValue(operation, param1, param2):
  return param1 + param2 if operation == Operation.addition else param1 * param2

def getIdxIncreaseAmout(operation):
  if operation == Operation.jumpIfFalse or operation == Operation.jumpIfTrue:
    return 0
  elif operation == Operation.inputValue or operation == Operation.outputValue:
    return 2
  return 4

def runAdapters(phaseList):
  adapterA = Adapter('A')
  adapterB = Adapter('B')
  adapterC = Adapter('C')
  adapterD = Adapter('D')
  adapterE = Adapter('E')
  signalInput = 0
  while not adapterE.isDone:
    signalInput = adapterA.executeIntCode(phaseList[0], signalInput)
    signalInput = adapterB.executeIntCode(phaseList[1], signalInput)
    signalInput = adapterC.executeIntCode(phaseList[2], signalInput)
    signalInput = adapterD.executeIntCode(phaseList[3], signalInput)
    signalInput = adapterE.executeIntCode(phaseList[4], signalInput)
  del adapterA
  del adapterB
  del adapterC
  del adapterD
  del adapterE
  return signalInput

maxVal = 0
maxCombination = 0
combinations = list(itertools.permutations([5,6,7,8,9]))
for combination in combinations:
  adapterOutput = runAdapters(combination)
  if adapterOutput > maxVal:
    maxVal = adapterOutput
    maxCombination = combination

print('Max output', maxVal)
print('Max combination', maxCombination)
