import sys
import math

class Tracker(object):
  def __init__(self, name, pipes, start, moveDirs, rowRange, colRange):
    self.name = name
    self.pipes = pipes
    self.start = start
    self.moveDirs = moveDirs
    self.rowRange = rowRange
    self.colRange = colRange
    self.curPos = start
    self.curDir = None
    self.stepCnt = 0


  def Print(self):
    print()
    print('Tracker\t', self.name)
    print('Start\t', self.start)
    print('CurDir\t', self.curDir)
    print('CurPos\t', self.curPos)
    print('Steps\t', self.stepCnt)


  def __eq__(self, other):
    return self.curPos == other.curPos


  def GetSteps(self):
    return self.stepCnt


  def GetPosition(self):
    return self.curPos


  def IsAtStartPos(self):
    return self.curPos == self.start


  def TakeFirstStep(self, takenPos=(None,None)):
    self.stepCnt += 1
    for dir in self.moveDirs:
      nextPos = self.CheckMove(self.curPos, dir)
      if (None not in nextPos) and (nextPos != takenPos):
        self.curPos = nextPos
        self.curDir = dir
        break
    return self.curPos


  def IsOppositeDir(self, dir):
    opposites = { 'U':'D', 'D':'U', 'L':'R', 'R':'L' }
    return dir == opposites[self.curDir]


  def TakeNextStep(self):
    self.stepCnt += 1
    dir = self.GetNextDir()
    nextPos = self.CheckMove(self.curPos, dir)
    if (None not in nextPos):
      self.curPos = nextPos
      self.curDir = dir
    else:
      print()
      print()
      print('Next step failed')
      self.Print()
    return self.curPos


  def CheckMove(self, pos, dir):
    row, col = pos
    if dir == 'U':
      if row-1 in self.rowRange:
        row -= 1
        if self.pipes[row][col] in self.moveDirs[dir]:
          return (row, col)
    elif dir == 'D':
      if row+1 in self.rowRange:
        row += 1
        if self.pipes[row][col] in self.moveDirs[dir]:
          return (row, col)
    elif dir == 'L':
      if col-1 in self.colRange:
        col -= 1
        if self.pipes[row][col] in self.moveDirs[dir]:
          return (row, col)
    else: # dir == 'R'
      if col+1 in self.colRange:
        col += 1
        if self.pipes[row][col] in self.moveDirs[dir]:
          return (row, col)
    return (None, None)


  def GetNextDir(self):
    dirMap = { '-':('L','R'), '|':('U','D'), 'F':('D','R'), '7':('D','L'), 'J':('U','L'), 'L':('U','R') }
    curChar = self.pipes[self.curPos[0]][self.curPos[1]]
    possibleDirs = dirMap[curChar]
    if self.IsOppositeDir(possibleDirs[0]):
      return possibleDirs[1]
    return possibleDirs[0]


class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.pipes = [ ]
    self.rowRange = None
    self.colRange = None
    self.moveDirs = { 'U':('|','F','7'), 'D':('|','L','J'),
                      'L':('-','L','F'), 'R':('-','7','J') }


  def ProcPuzzle(self, start):
    # Track pipe loop in both directions
    trackers = ( Tracker('Trkr_1', self.pipes, start, self.moveDirs, self.rowRange, self.colRange),
                 Tracker('Trkr_2', self.pipes, start, self.moveDirs, self.rowRange, self.colRange) )

    firstPos = (None,None)
    for tracker in trackers:
      firstPos = tracker.TakeFirstStep(firstPos)
      #tracker.Print()

    loopCnt = 100000
    retVal = 0
    while True:
      for tracker in trackers:
        tracker.TakeNextStep()
        #tracker.Print()
      if trackers[0] == trackers[1]:
        retVal = max(trackers[0].GetSteps(), trackers[1].GetSteps())
        break
      if trackers[0].IsAtStartPos() or trackers[1].IsAtStartPos():
        print('Trkr_1 full loop, steps', trackers[0].GetSteps(), trackers[0].GetPosition())
        print('Trkr_2 full loop, steps', trackers[1].GetSteps(), trackers[1].GetPosition())
        break
      loopCnt -= 1
      if loopCnt == 0:
        print('Max loop count reached')
        print('Trkr_1 steps', trackers[0].GetSteps(), trackers[0].GetPosition())
        print('Trkr_2 steps', trackers[1].GetSteps(), trackers[1].GetPosition())
        break
    return retVal


  def FindStart(self):
    for i,r in enumerate(self.pipes):
      for j,c in enumerate(r):
        if c == 'S':
          return (i, j)
    return (None, None)


  def DoWork(self):
    p1_result = 0
    p2_result = 0

    for line in self.fileGen:
      line = line.strip('\n').strip()
      self.pipes.append(line)

    self.rowRange = range(0, len(self.pipes))
    self.colRange = range(0, len(self.pipes[0]))
    start = self.FindStart()

    # Part 1
    p1_result = self.ProcPuzzle(start)

    # Part 2

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
