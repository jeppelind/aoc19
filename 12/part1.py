import re

moons = []
with open('data.txt') as source:
  for line in source:
    x, y, z = map(int, re.findall(r'-?\d+', line))
    moons.append({
      'pos': {'x': x, 'y': y, 'z': z},
      'velocity': {'x': 0, 'y': 0, 'z': 0}
    })

def getVelocityChange(num1, num2):
  if num1 > num2:
    return -1
  elif num1 < num2:
    return 1
  return 0

def applyGravity(idx):
  moon = moons[idx]
  otherMoons = list(moons)
  del otherMoons[idx]
  for other in otherMoons:
    moon['velocity']['x'] += getVelocityChange(moon['pos']['x'], other['pos']['x'])
    moon['velocity']['y'] += getVelocityChange(moon['pos']['y'], other['pos']['y'])
    moon['velocity']['z'] += getVelocityChange(moon['pos']['z'], other['pos']['z'])

def calculateVelocity():
  for idx in range(len(moons)):
    applyGravity(idx)

def applyVelocity():
  for moon in moons:
    moon['pos']['x'] += moon['velocity']['x']
    moon['pos']['y'] += moon['velocity']['y']
    moon['pos']['z'] += moon['velocity']['z']

def getEnergy():
  combinedEnergy = 0
  for moon in moons:
    potential = abs(moon['pos']['x']) + abs(moon['pos']['y']) + abs(moon['pos']['z'])
    kinetic = abs(moon['velocity']['x']) + abs(moon['velocity']['y']) + abs(moon['velocity']['z'])
    total = potential * kinetic
    combinedEnergy += total
  return combinedEnergy

def getEneryAfterNSteps(steps):
  for _ in range(steps):
    calculateVelocity()
    applyVelocity()
  energy = getEnergy()
  return energy

print(getEneryAfterNSteps(1000))