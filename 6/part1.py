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

orbits = 0
for i in items:
  obj = items.get(i)
  while obj.get('parent'):
    orbits += 1
    obj = items.get(obj.get('parent'))

print(orbits)
