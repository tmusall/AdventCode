import sys

class AdventOfCode(object):
  def __init__(self, fileName: str):
    self.fileGen = (row for row in open(fileName, 'r'))

  def CalcJoltage(self, bank: str) -> int:
    print(bank)
    j1 = [-1, 0]
    j2 = [-1, 0]
    ans = 0

    for digit in range(9, 0, -1):
      pos = bank.find(str(digit))
      if pos > -1 and j1[1] < digit and pos != j2[0]:
        j1[0] = pos
        j1[1] = digit

      pos = bank.rfind(str(digit))
      if pos > -1 and j2[1] < digit and pos > j1[0]:
        j2[0] = pos
        j2[1] = digit

    ans = (j1[1] if j1[0] < j2[0] else j2[1]) * 10 + \
            (j2[1] if j2[0] > j1[0] else j1[1])
    print(j1, '  ', j2, '  ', ans)
    return ans

  def DoWork(self):
    ansPart1 = 0
    ansPart2 = 0

    for line in self.fileGen:
      line = line.strip('\n')
      ansPart1 += self.CalcJoltage(line)

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
