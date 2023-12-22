import sys
import math

pipes = [ ]
rowRange = None
colRange = None
moveDirs = { 'U':('|','F','7'), 'D':('|','L','J'), 'L':('-','L','F'), 'R':('-','7','J') }

class Tracker(object):
  def __init__(self, name, start):
    self.name = name
    self.start = start
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
    for dir in moveDirs:
      nextPos = self.CheckMove(self.curPos, dir)
      if (None not in nextPos) and (nextPos != takenPos):
        self.LeaveBreadCrumb(self.curPos)
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
      self.LeaveBreadCrumb(self.curPos)
      self.curPos = nextPos
      self.curDir = dir
    else:
      print()
      print()
      print('Next step failed')
      self.Print()
    return self.curPos


  def LeaveBreadCrumb(self, pos):
    row, col = pos
    global pipes
    pipes[row] = pipes[row][:col] + '#' + pipes[row][col+1:]


  def CheckMove(self, pos, dir):
    row, col = pos
    if dir == 'U':
      if row-1 in rowRange:
        row -= 1
        if pipes[row][col] in moveDirs[dir]:
          return (row, col)
    elif dir == 'D':
      if row+1 in rowRange:
        row += 1
        if pipes[row][col] in moveDirs[dir]:
          return (row, col)
    elif dir == 'L':
      if col-1 in colRange:
        col -= 1
        if pipes[row][col] in moveDirs[dir]:
          return (row, col)
    else: # dir == 'R'
      if col+1 in colRange:
        col += 1
        if pipes[row][col] in moveDirs[dir]:
          return (row, col)
    return (None, None)


  def GetNextDir(self):
    dirMap = { '-':('L','R'), '|':('U','D'), 'F':('D','R'), '7':('D','L'), 'J':('U','L'), 'L':('U','R') }
    curChar = pipes[self.curPos[0]][self.curPos[1]]
    possibleDirs = dirMap[curChar]
    if self.IsOppositeDir(possibleDirs[0]):
      return possibleDirs[1]
    return possibleDirs[0]


class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))


  def ProcPuzzle(self, start):
    # Track pipe loop in both directions
    trackers = ( Tracker('Trkr_1', start), Tracker('Trkr_2', start) )

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
        trackers[0].LeaveBreadCrumb(trackers[0].GetPosition())
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
    for i,r in enumerate(pipes):
      for j,c in enumerate(r):
        if c == 'S':
          return (i, j)
    return (None, None)


  def DoWork(self):
    p1_result = 0
    p2_result = 0
    origPipes = [ ]

    for line in self.fileGen:
      line = line.strip('\n').strip()
      pipes.append(line)
      origPipes.append(line)


    global rowRange, colRange
    rowRange = range(0, len(pipes))
    colRange = range(0, len(pipes[0]))
    start = self.FindStart()

    # Part 1
    p1_result = self.ProcPuzzle(start)

    # Part 2
    trans = ''.maketrans('|-F7LJ', '......')
    pipeHash = [ ]
    for r in pipes:
      s = r.translate(trans)
      print(r, s)
      pipeHash.append(s)

    #for r in pipeHash:
    #  print(r)

    pipeLoop = [ ]
    for i,r in enumerate(pipeHash):
      origRow = origPipes[i]
      newRow = ''
      for x,c in enumerate(r):
        if c == '#':
          newRow += origRow[x]
        else:
          newRow += c
      pipeLoop.append(newRow)

    print()
    for r in pipeLoop:
      print(r)

    trans = ''.maketrans('S','F')
    pipeLoop[1] = pipeLoop[1].translate(trans)
    insideTiles = 0
    for r in pipeLoop:
      inside = False
      io = ''
      lastCorner = ''
      for c in r:
        if inside and (c == '.'):
          insideTiles += 1
        elif c == '|':
          inside = not inside
        elif c in 'F7LJ':
          if ((c == 'F') and (lastCorner == 'J')) or ((c == 'L') and (lastCorner == '7')):
            inside = not inside
          lastCorner = c
        io += 'I' if inside else 'O'
      print(io)
      #print(r)
    p2_result = insideTiles

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
