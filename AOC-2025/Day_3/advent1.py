import sys

class AdventOfCode(object):
  def __init__(self, fileName: str):
    self.fileGen = (row for row in open(fileName, 'r'))

  def CalcJoltage(self, bank: str) -> int:
    ans = 0

    for idx,digit in enumerate(bank):
      for x in (int(c) for c in bank[idx+1:]):
        prod = int(digit) * 10 + x
        ans = prod if prod > ans else ans

    return ans

  def CalcBigJoltage(self, bank: str) -> int:
    print(bank)
    ans = 0
    hitCnt = 0
    digiDict = { '9':[], '8':[],'7':[], '6':[], '5':[], '4':[], '3':[], '2':[], '1':[] }
    digiList = [ -1 for x in range(12) ]
    for d in '987654321':
      pos = 0
      while True:
        pos = bank.find(d, pos)
        if pos != -1:
          hitCnt += 1
          digiDict[d].append(pos)
          print(pos)
          digiList[pos] = d
          pos += 1
          if hitCnt == 12:
            break
        else:
          break
    print(digiList)
    return ans

  def DoWork(self):
    ansPart1 = 0
    ansPart2 = 0

    for line in self.fileGen:
      line = line.strip('\n')
      ansPart1 += self.CalcJoltage(line)
      ansPart2 += self.CalcBigJoltage(line)

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
