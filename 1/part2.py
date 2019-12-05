total = 0
moduleArr = []

def calcFuel(n):
  return (n / 3) -2

with open('data.txt') as list:
  for line in list:
    moduleTotal = 0
    fuel = calcFuel(int(line))
    while fuel > 0:
      moduleTotal += fuel
      fuel = calcFuel(fuel)
    moduleArr.append(moduleTotal)

for module in moduleArr:
  total += module

print(total)
