import sys
import math

class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))


  def ComputeDiffs(self, text):
    readings = list(map(int, text.split()))
    rows = [ readings ]
    while not all(v==0 for v in rows[-1]):
      diffs = [ ]
      prev = None
      for x in rows[-1]:
        if prev != None:
          diffs.append(x - prev)
        prev = x
      rows.append(diffs)
    return rows


  def ProcLineP1(self, rows):
    for r in rows:
      r.append(0)

    prev = None
    for r in reversed(rows):
      if prev != None:
        r[-1] = r[-2] + prev[-1]
      prev = r

    retVal = rows[0][-1]
    return retVal


  def ProcLineP2(self, rows):
    for r in rows:
      r.insert(0, 0)

    prev = None
    for r in reversed(rows):
      if prev != None:
        r[0] = r[1] - prev[0]
      prev = r

    retVal = rows[0][0]
    return retVal


  def DoWork(self):
    p1_result = 0
    p2_result = 0

    for line in self.fileGen:
      line = line.strip('\n').strip()
      rowsP1 = self.ComputeDiffs(line)
      rowsP2 = rowsP1
      # Part 1
      p1_result += self.ProcLineP1(rowsP1)

      # Part 2
      p2_result += self.ProcLineP2(rowsP2)

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
