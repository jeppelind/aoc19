import re, math

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

class ResourceTracker:
  def __init__(self):
    self.patterns = {}
    self.excess = {}

  def loadPatterns(self, source):
    self.patterns = source
    for resource in source:
      self.excess[resource] = 0

  def calculateOreNeeded(self, name, amountRequested):
    if name == 'ORE':
      return amountRequested

    recipe = self.patterns[name]
    totalOreUsed = 0
    amountNeededToProduce = amountRequested - self.excess[name]
    if amountNeededToProduce <= 0:
      self.excess[name] -= amountRequested
      return 0

    runsToProduceRequestedAmount = math.ceil(amountNeededToProduce / recipe['amount'])
    amountProduced = runsToProduceRequestedAmount * recipe['amount'] + self.excess[name]
    excessProduce = amountProduced - amountRequested
    self.excess[name] = int(excessProduce)
    
    for resource in recipe['resources']:
      resourceName = resource[0]
      resourceAmount = resource[1]
      totalOreUsed += int(self.calculateOreNeeded(resourceName, resourceAmount * runsToProduceRequestedAmount))
    
    return totalOreUsed

  def calculateAmountOfFuelFromOre(self, oreAmount):
    low, mid, high = 0, 0, oreAmount
    while low <= high:
      mid = (low + high) // 2
      oreNeeded = self.calculateOreNeeded('FUEL', mid)
      if oreNeeded < oreAmount:
        low = mid + 1
      else:
        high = mid -1
    print('Fuel form {0} ore: {1}'.format(oreAmount, high))

resourceTracker = ResourceTracker()
resourceTracker.loadPatterns(parseResources('data.txt'))
resourceTracker.calculateAmountOfFuelFromOre(1000000000000)
# totalOreNeeded = resourceTracker.calculateOreNeeded('FUEL', 1)
# print('Total ore needed: {0}'.format(totalOreNeeded))
