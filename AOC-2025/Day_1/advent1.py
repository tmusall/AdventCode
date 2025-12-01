import sys

class AdventOfCode(object):
  def __init__(self, fileName):
    self.fileGen = (row for row in open(fileName, 'r'))


  def DoWork(self):
    ansPart1 = 0
    ansPart2 = 0
    pos = 50

    for line in self.fileGen:
      line = line.strip('\n')
      direction = line[0]
      clicks = int(line[1:]) * (-1 if 'L' in direction else 1)
      pos = (pos + clicks) % 100
      ansPart1 += (1 if pos == 0 else 0)
      
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
