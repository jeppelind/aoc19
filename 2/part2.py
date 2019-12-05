TARGET = 19690720
INPUT_FILE = open('data.txt')
DATA = INPUT_FILE.read()
STR_LIST = DATA.split(',')
BASELIST = [int(i) for i in STR_LIST]

def findTargetInputs():
  for intA in range(0, 100):
    for intB in range(0, 100):
      testList = list(BASELIST)
      testList[1], testList[2] = intA, intB
      if executeIntList(testList) == TARGET:
        return intA, intB

def executeIntList(arr):
  idx = 0
  while arr[idx] != 99:
    targetIdx = arr[idx+3]
    arr[targetIdx] = calculateValue(arr[idx], arr[idx+1], arr[idx+2], arr)
    idx += 4
  return arr[0]

def calculateValue(type, idxA, idxB, arr):
  return arr[idxA] + arr[idxB] if type == 1 else arr[idxA] * arr[idxB]

inputParamsNeeded = findTargetInputs()
result = 100 * inputParamsNeeded[0] + inputParamsNeeded[1]
print(result)
