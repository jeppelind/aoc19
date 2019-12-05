MIN, MAX = 264360, 746325

def isAscending(numList):
  return numList == sorted(numList)

def hasDoubleAdjacentDigit(numList):
  return len(numList) != len(set(numList))

cnt = 0
for number in range(MIN, MAX+1):
  numSequence = [int(i) for i in str(number)]
  if isAscending(numSequence):
    if hasDoubleAdjacentDigit(numSequence):
      cnt += 1

print(cnt)
