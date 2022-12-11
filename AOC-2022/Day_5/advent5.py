
from collections import deque

class ReadAndWork(object):
  def __init__(self, partOne, fileName):
    self.partOne = partOne
    self.fname = fileName

  def DoWork(self):
    initState = True
    stateLines = [ ]
    stacks = [ ]
    score = None

    fileGen = (row for row in open(self.fname, 'r'))
    for line in fileGen:
      line = line.strip('\n')

      if initState:
        if len(line) > 0:
          stateLines.append(line)
        else:
          initState = False
          stackList = stateLines.pop().split()
          stacks = [ deque() for i in stackList ]
          lineLength = len(stateLines[0])

          for x in reversed(stateLines):
            meh=[ x[i] for i in range(1,lineLength,4) ]
            for i in range(len(meh)):
              c = meh[i]
              if c != ' ':
                stacks[i].append(c)


      else:
        #print('1', stacks)
        s = line.split()
        moveItems = int(s[1])
        moveFrom = int(s[3]) - 1
        moveTo = int(s[5]) - 1
        if self.partOne:
          for i in range(moveItems):
            stacks[moveTo].append(stacks[moveFrom].pop())
            #print('2', stacks)
        else:
          l = [ ]
          for i in range(moveItems):
            l.append(stacks[moveFrom].pop())
          for i in reversed(l):
            stacks[moveTo].append(i)


    #print('3', stacks)
    score = ''
    for s in stacks:
      score += s[-1]

    return score


if __name__ == '__main__':
  partOne = False
  fileIndex = 1
  inputFile = ('sample.txt', 'advent5.txt')

  score = ReadAndWork(partOne, inputFile[fileIndex]).DoWork()
  print('Score:', score)
