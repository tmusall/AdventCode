import sys

class AdventOfCode(object):
  def __init__(self, fileName):
    self.fileGen = (row for row in open(fileName, 'r'))

  def ValidateId_Part1(self, id):
    ans = 0
    idStr = str(id)
    if len(idStr) % 2:  # Odd number of digits don't count
      return ans
    half = int(len(idStr) / 2)
    if idStr[:half] in idStr[half:]:
      #print(f'Found one: {id}')
      ans = id
    return ans

  def ValidateId_Part2(self, id):
    ans = 0
    idStr = str(id)
    half = int(len(idStr) / 2)
    if idStr[:half] in idStr[half:]:
      print(f'Found one: {id}')
      ans = id
    return ans

  def DoWork(self):
    ansPart1 = 0
    ansPart2 = 0

    idList = next(self.fileGen).strip('\n').split(',')
    print(idList)

    for idRange in idList:
      rangeList = idRange.split('-')
      start = int(rangeList[0])
      stop = int(rangeList[1])
      for id in range(start, stop+1):
        ansPart1 += self.ValidateId_Part1(id)
        ansPart2 += self.ValidateId_Part2(id)

    return ansPart1, ansPart2

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Please provide input file name on command line.')
    exit(1)
  inputFile = sys.argv[1]
  print('Input file is:', inputFile)
  ans1, ans2 = AdventOfCode(inputFile).DoWork()
  print('Answer Part 1:', ans1)
  print('Answer Part 2:', ans2)
