posArr = []
with open('data.txt') as data:
  for line in data:
    strSplitList = line.split(',')
    posArr.append(strSplitList)

def calculatePath(positions):
  path = []
  currX, currY = 0, 0
  for pos in positions:
    direction = pos[:1]
    distance = int(pos[1:])
    for _ in range(0, distance):
      if direction == 'R' or direction == 'L':
        currX = currX + 1 if direction == 'R' else currX - 1
      else:
        currY = currY + 1 if direction == 'U' else currY - 1
      path.append([currX, currY])
  return path

def getIntersections(path1, path2):
  map1 = map(tuple, path1)
  map2 = map(tuple, path2)
  return list(set(map1).intersection(set(map2)))

path1 = calculatePath(posArr[0])
path2 = calculatePath(posArr[1])
intersections = getIntersections(path1, path2)

shortestDistance = 99999
for pos in intersections:
  distanceFromCenter = abs(pos[0]) + abs(pos[1])
  if distanceFromCenter < shortestDistance:
    shortestDistance = distanceFromCenter

print(shortestDistance)
