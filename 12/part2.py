import re

#https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

#https://en.wikipedia.org/wiki/Least_common_multiple
def lcm(a, b):
  if b == 0:
    return 0
  return a * b / gcd(a, b)

def getMoonsFromInput(filename):
  res = []
  with open(filename) as source:
    for line in source:
      res.append(map(int, re.findall(r'-?\d+', line)))
  return res

def getVelocityChange(num1, num2):
  if num1 > num2:
    return -1
  elif num1 < num2:
    return 1
  return 0

def calculateVelocity(positions, velocity):
  for i in range(len(positions)):
    for pos in positions:
      velocity[i] += getVelocityChange(positions[i], pos)

def applyVelocity(positions, velocity):
  for i in range(len(positions)):
    positions[i] += velocity[i]

def orbit(positions):
  velocity = [0] * len(positions)
  startPos = list(positions)
  startVelocity = list(velocity)
  loopCount = 0
  isBackAtStart = False
  while not isBackAtStart:
    loopCount += 1
    calculateVelocity(positions, velocity)
    applyVelocity(positions, velocity)
    isBackAtStart = positions == startPos and velocity == startVelocity
  return loopCount

def getNumberOfStepsToReachPreviousState(moons):
  posX = [x for x, _, _ in moons]
  posY = [y for _, y, _ in moons]
  posZ = [z for _, _, z in moons]

  stepsNeededX = orbit(posX)
  stepsNeededY = orbit(posY)
  stepsNeededZ = orbit(posZ)
  stepsNeeded = lcm(stepsNeededX, lcm(stepsNeededY, stepsNeededZ))
  return stepsNeeded

moons = getMoonsFromInput('data.txt')
print('Steps needed: ' + str(getNumberOfStepsToReachPreviousState(moons)))
