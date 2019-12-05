MIN, MAX = 264360, 746325

def isAscending(numList):
  return numList == sorted(numList)

def hasDoubleAdjacentDigit(numList):
  return len(numList) != len(set(numList))

def noMoreThanTwoMatchingAdjacentDigits(numSequence):
  numOfAdjacentDigits = 1
  previous = numSequence[0]
  for num in numSequence[1:]:
    if num == previous:
      numOfAdjacentDigits += 1
    elif numOfAdjacentDigits == 2:
      return True
    else:
      numOfAdjacentDigits = 1
    previous = num
  return numOfAdjacentDigits == 2

cnt = 0
for number in range(MIN, MAX+1):
  numSequence = [int(i) for i in str(number)]
  if isAscending(numSequence):
    if hasDoubleAdjacentDigit(numSequence):
      if noMoreThanTwoMatchingAdjacentDigits(numSequence):
        cnt += 1

print(cnt)
