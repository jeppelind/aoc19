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

# def calculateValue(operation, idxA, idxB):
#   return values[idxA] + values[idxB] if operation == 1 else values[idxA] * values[idxB]

# def executeIntList():
#   idx = 0
#   while values[idx] != 99:
#     operation = values[idx]
#     param1 = values[idx+1]
#     param2 = values[idx+2]
#     targetIdx = values[idx+3]
#     values[targetIdx] = calculateValue(operation, param1, param2)
#     idx += 4
#   return values[0]

# print(executeIntList())
print(Mode.immediate)
print(data)
