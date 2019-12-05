total = 0
with open('data.txt') as list:
  for line in list:
    basevalue = int(line)
    value = (basevalue / 3) - 2
    total += value
print(total)
