# 1: +
# 2: *
# 3: takes a single integer as input and saves it to the address given by its only parameter
# 4: outputs the value of its only parameter

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

def executeIntList(userInput):
  idx = 0
  while data[idx] != 99:
    operation, mode1, mode2, mode3 = getOperationModes(data[idx])
    if operation == Operation.addition or operation == Operation.multiplication:
      param1 = data[idx+1] if mode1 == Mode.immediate else data[data[idx+1]]
      param2 = data[idx+2] if mode2 == Mode.immediate else data[data[idx+2]]
      targetIdx = idx+3 if mode3 == Mode.immediate else data[idx+3]
      data[targetIdx] = calculateValue(operation, param1, param2)
    if operation == Operation.inputValue:
      targetIdx = idx+3 if mode1 == Mode.immediate else data[idx+3]
      data[targetIdx] = userInput
    if operation == Operation.outputValue:
      param = data[idx+1]
      value = param if mode1 == Mode.immediate else data[param]
      print(value)
    idx += 4 if operation < 3 else 2

def getOperationModes(operationCode):
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

def calculateValue(operation, param1, param2):
  return param1 + param2 if operation == Operation.addition else param1 * param2

executeIntList(1)
