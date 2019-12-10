items = {}

with open('data.txt') as data:
  for line in data:
    parentId, childId = line.rstrip().split(')')
    parent = items.get(parentId)
    if parent == None:
      parent = {parentId: {'parent': None, 'children': [childId]}}
    else:
      childList = parent.get('children', [])
      childList.append(childId)
      parent = {parentId: {'parent': parent.get('parent'), 'children': childList}}

    child = items.get(childId)
    if child == None:
      child = {childId: {'parent': parentId, 'children': []}}
    else:
      child = {childId: {'parent': parentId, 'children': child.get('children')}}

    items.update(parent)
    items.update(child)

def stepsBetweenItems(source, target):
  sourceParents = getIndirectParentList(source)
  targetStepsToCommonParent = stepsToCommonParent(sourceParents, target)
  commonParent = targetStepsToCommonParent.pop()
  sourceCommonParentIdx = sourceParents.index(commonParent)
  sourceStepsToCommonParent = sourceParents[:sourceCommonParentIdx]
  return len(sourceStepsToCommonParent) + len(targetStepsToCommonParent)

def getIndirectParentList(name):
  parentList = []
  item = items.get(name)
  while item.get('parent'):
    parentName = item.get('parent')
    parentList.append(item.get('parent'))
    item = items.get(parentName)
  return parentList

def stepsToCommonParent(sourceParents, target):
  targetParents = []
  parentId = None
  item = items.get(target)
  while parentId not in sourceParents:
    parentId = item.get('parent')
    targetParents.append(parentId)
    item = items.get(parentId)
  return targetParents

print(stepsBetweenItems('YOU', 'SAN'))
