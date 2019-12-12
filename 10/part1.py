import math

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
for pos in astroidPosList:
  viewAngles = {}
  for otherObject in astroidPosList:
    if pos != otherObject:
      angle = math.atan2(pos[0]-otherObject[0], pos[1]-otherObject[1])
      viewAngles.update({angle: [otherObject]})
  if maxUnobtrusedViews < len(viewAngles):
    maxUnobtrusedViews = len(viewAngles)
    bestPos = pos

print(bestPos, maxUnobtrusedViews)
