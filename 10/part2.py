import math
import collections

astroidPosList = []
with open('data.txt') as list:
  y = 0
  for line in list:
    x = 0
    for char in line:
      if char == '#':
        astroidPosList.append([x,y])
      x += 1
    y += 1

bestPos = None
maxUnobtrusedViews = 0
astroidsByAngle = {}
for pos in astroidPosList:
  viewAngles = {}
  for otherObject in astroidPosList:
    if pos != otherObject:
      angle = math.atan2(pos[0]-otherObject[0], pos[1]-otherObject[1])
      if angle <= 0:
        angle = abs(angle) * 180 / math.pi
      else:
        angle = 360 - angle * 180 / math.pi

      angleList = viewAngles.get(angle)
      if angleList == None:
        angleList = [otherObject]
      else:
        angleList += [otherObject]
      viewAngles.update({angle: angleList})
  if maxUnobtrusedViews < len(viewAngles):
    maxUnobtrusedViews = len(viewAngles)
    bestPos = pos
    astroidsByAngle = collections.OrderedDict(sorted(viewAngles.items()))

def getAsteroidByDeletionOrder(num):
  cnt = 0
  while len(astroidsByAngle) > 0:
    for angle in astroidsByAngle:
      cnt += 1
      deletedAsteroid = None
      asteroids = astroidsByAngle.get(angle)
      if len(asteroids) == 1:
        deletedAsteroid = astroidsByAngle.pop(angle)[0]
      else:
        closestIdx = None
        shortestDist = 99999
        idx = 0
        for pos in asteroids:
          dist = pos[0] - bestPos[0] + pos[1] - bestPos[1]
          if dist < shortestDist:
            closestIdx = idx
            shortestDist = dist
          idx += 1
        deletedAsteroid = asteroids.pop(closestIdx)
        astroidsByAngle.update({angle: asteroids})
      if cnt == num:
        return deletedAsteroid

deletedAsteroid200 = getAsteroidByDeletionOrder(200)
print(deletedAsteroid200[0] * 100 + deletedAsteroid200[1])
