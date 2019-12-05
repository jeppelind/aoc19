inputFile = open('data.txt')
data = inputFile.read()
strList = data.split(',')
values = [int(i) for i in strList]

values[1] = 12
values[2] = 2

def calculateValue(type, idxA, idxB):
  return values[idxA] + values[idxB] if type == 1 else values[idxA] * values[idxB]

def executeIntList():
  idx = 0
  while values[idx] != 99:
    targetIdx = values[idx+3]
    values[targetIdx] = calculateValue(values[idx], values[idx+1], values[idx+2])
    idx += 4
  return values[0]

print(executeIntList())
