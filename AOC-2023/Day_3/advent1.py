import re
from collections import deque

def NumberGen(text):
  txt = text
  while True:
    x = re.search('\d+', txt)
    if x != None:
      z = x.span()
      yield (z, x.group())
      txt = txt[:z[0]] + '.' * (z[1] - z[0]) + txt[z[1]:]  # Overwrite number with periods
    else:
      break


class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    # Anything NOT in this list considered a symbol
    self.periodDigits = ( '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' )
    self.window = deque([ ])  # Holds a 3 line window being examined
    self.lineLen = 0
    self.lineNum = 0
    self.gears = { }


  def WindowAdjust(self, text):
    if len(self.window) == 3:
      self.window.popleft()  # Remove oldest line
    self.window.append(text) # Add new line
    return True if len(self.window) == 3 else False


  def SymbolFound(self, pos, num):
    startIdx = (pos[0] - 1) if pos[0] > 0 else pos[0]
    endIdx = (pos[1] + 1) if pos[1] < self.lineLen else pos[1]
    for i in range(startIdx, endIdx):
      for w in range(0, 3):
        if self.window[w][i] not in self.periodDigits:
          if self.window[w][i] == '*':
            lNum = self.lineNum + (w - 1)
            key = (lNum, i)
            if key in self.gears.keys():
              self.gears[key].append(num)
            else:
              self.gears[key] = [num]
          return True
    return False


  def ExamineLine(self, text):
    self.lineLen = len(text)
    self.lineNum += 1
    lineTotal = 0
    if self.WindowAdjust(text):
      for pos,num in NumberGen(self.window[1]):
        if self.SymbolFound(pos,num):
          lineTotal += int(num)
    return lineTotal


  def CalcGearRatio(self):
    sum = 0
    for v in self.gears.values():
      mul = 1
      if len(v) > 1:
        for i in v:
          mul *= int(i)
        sum += mul
    return sum


  def DoWork(self):
    sum = 0

    for line in self.fileGen:
      line = line.strip('\n')
      sum += self.ExamineLine(line)  # Part 1
                                     # Part 2
    gearRatio = self.CalcGearRatio()
    return sum, gearRatio


if __name__ == '__main__':
  #inputFile = 'sample.txt'
  inputFile = 'input.txt'
  ans1, ans2 = AdventOfCode(inputFile).DoWork()
  print('Answer Part 1:', ans1)
  print('Answer Part 2:', ans2)
