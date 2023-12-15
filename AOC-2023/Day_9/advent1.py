import sys
import math

class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))


  def ProcLine(self, text):
    readings = text.split()
    readings = [ int(x) for x in readings ]
    rows = [ readings ]
    while (sum(rows[-1]) != 0) or (len(set(rows[-1])) != 1):
      diffs = [ ]
      prev = None
      for x in rows[-1]:
        if prev != None:
          diffs.append(x - prev)
        prev = x
      rows.append(diffs)

    #print(rows)
    for r in rows:
      r.append(0)

    prev = None
    for r in rows.__reversed__():
      if prev != None:
        r[-1] = r[-2] + prev[-1]
      prev = r

    print()
    for r in rows:
      print(r)
    retVal = rows[0][-1]
    return retVal


  def DoWork(self):
    sumTotal = 0

    for line in self.fileGen:
      line = line.strip('\n').strip()
      sumTotal += self.ProcLine(line)

    # Part 1
    p1_result = sumTotal

    # Part 2
    p2_result = 0
    return p1_result, p2_result


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Please provide input file name on command line.')
    exit(1)
  inputFile = sys.argv[1]
  print('Input file is:', inputFile)
  ans1, ans2 = AdventOfCode(inputFile).DoWork()
  print('Answer Part 1:', ans1)
  print('Answer Part 2:', ans2)
