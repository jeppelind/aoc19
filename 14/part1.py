import re

def getNameAndAmount(pattern):
  name = ''.join(re.findall(r'[A-Z]', pattern))
  amount = int(re.findall(r'\d+', pattern).pop())
  return name, amount

def parseResources(filename):
  with open(filename) as source:
    patterns = {}
    for line in source:
      pattern, result = line.split('=>')
      resName, resAmount = getNameAndAmount(result)
      
      resources = []
      ingredients = pattern.split(',')
      for ingredient in ingredients:
        name, amount = getNameAndAmount(ingredient)
        resources.append([name, amount])

      patterns[resName] = {
        'amount': resAmount,
        "resources": resources
      }
    return patterns

def calculateOreNeeded(name, amountRequested, patterns, excess = {}):
  recipe = patterns[name]
  totalOreUsed = 0
  amountProduced = 0
  while amountProduced < amountRequested:
    if name in excess and excess[name] + amountProduced >= amountRequested:
      amountRemovedFromExcess = amountRequested - amountProduced
      excess[name] -= amountRemovedFromExcess
      amountProduced = amountRequested
      continue
    
    for resource in recipe['resources']:
      resourceName = resource[0]
      resourceAmount = resource[1]
      if resourceName in excess and excess[resourceName] >= resourceAmount:
        excess[resourceName] -= resourceAmount
      elif resourceName == 'ORE':
        totalOreUsed += resourceAmount
      else:
        oreUsed, excess = calculateOreNeeded(resourceName, resourceAmount, patterns, excess)
        totalOreUsed += oreUsed
    amountProduced += recipe['amount']
    
  excessProduce = amountProduced - amountRequested
  if excessProduce > 0:
    excess[name] = excess[name] + excessProduce if name in excess else excessProduce
  
  return totalOreUsed, excess


patterns = parseResources('data.txt')
totalOreNeeded, excessResources = calculateOreNeeded('FUEL', 1, patterns)
print('Total ore needed: {0}'.format(totalOreNeeded))
print('Output excess materials: {0}'.format(excessResources))
