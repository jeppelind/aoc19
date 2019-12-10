inputStr = open('data.txt').read()
data = [int(i) for i in inputStr.split(',')]

class Mode():
  position = 0
  immediate = 1

class Operation():
  addition = 1
  multiplication = 2
  inputValue = 3
  outputValue = 4
  jumpIfTrue = 5
  jumpIfFalse = 6
  lessThan = 7
  equals = 8

def executeIntCode(userInput):
  idx = 0
  while data[idx] != 99:
    operation, mode1, mode2, mode3 = getOperationAndModes(data[idx])
    idx1, idx2, idx3 = getParamIdx(idx, operation, mode1, mode2, mode3)
    if operation == Operation.addition or operation == Operation.multiplication:
      data[idx3] = calculateValue(operation, data[idx1], data[idx2])
    elif operation == Operation.inputValue:
      data[idx1] = userInput
    elif operation == Operation.outputValue:
      print(data[idx1])
    elif operation == Operation.jumpIfTrue:
      idx = data[idx2] if data[idx1] != 0 else idx + 3
    elif operation == Operation.jumpIfFalse:
      idx = data[idx2] if data[idx1] == 0 else idx + 3
    elif operation == Operation.lessThan:
      data[idx3] = 1 if data[idx1] < data[idx2] else 0
    elif operation == Operation.equals:
      data[idx3] = 1 if data[idx1] == data[idx2] else 0
    idx += getIdxIncreaseAmout(operation)

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

def getParamIdx(idx, operation, mode1, mode2, mode3):
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

executeIntCode(5)
