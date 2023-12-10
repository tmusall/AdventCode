import sys

class Map(object):
  def __init__(self, name):
    self.name = name
    self.rules = [ ]

  def Name(self):
    return self.name

  def Add(self, newRule):
    self.rules.append(newRule)

  def Convert(self, inputNum):
    returnNum = inputNum
    for r in self.rules:
      srcRange = range(r[1], r[1]+r[2])
      if inputNum in srcRange:
        returnNum = r[0] + (inputNum - r[1])
        break
    return returnNum

  def InverseConvert(self, inputNum):
    returnNum = inputNum
    for r in self.rules:
      srcRange = range(r[0], r[0]+r[2])
      if inputNum in srcRange:
        returnNum = r[1] + (inputNum - r[0])
        break
    return returnNum

  def Print(self):
    print(self.name)
    print(self.rules)


class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.maps = [ ]


  def BuildMap(self, text):
    name = text.split()[0]
    newMap = Map(name)
    for line in self.fileGen:
      line = line.strip('\n').strip()
      if len(line) == 0:
        break
      newMap.Add([ int(x) for x in line.split() ])
    #newMap.Print()
    self.maps.append(newMap)


  def SeedInRange(self, seed):
    for r in self.seedRanges:
      if seed in r:
        return True
    return False


  def DoWork(self):
    # Make a seed list
    line = next(self.fileGen)
    line = line.strip('\n').strip()
    self.seeds = [ int(x) for x in line.split()[1:] ]
    self.seedRanges = [ ]
    i = 0;
    while True:
      if i >= len(self.seeds):
        break
      n = self.seeds[i]
      c = self.seeds[i+1]
      self.seedRanges.append(range(n, n+c))
      i += 2

    for line in self.fileGen:
      line = line.strip('\n').strip()
      if (len(line) > 0) and (':' in line):
        self.BuildMap(line)  # Part 1

    p1minLoc = 99999999999999
    for seed in self.seeds:
      val = seed
      for map in self.maps:
        val = map.Convert(val)
      if val < p1minLoc:
        p1minLoc = val

    p2minLoc = 0
    startLoc = 0
    for loc in range(0, 9999999999, 1000):
      val = loc
      for map in self.maps.__reversed__():
        val = map.InverseConvert(val)
      if self.SeedInRange(val):
        startLoc = loc - 1000
        break

    for loc in range(startLoc, startLoc+1001):
      val = loc
      for map in self.maps.__reversed__():
        val = map.InverseConvert(val)
      if self.SeedInRange(val):
        p2minLoc = loc
        break;

    return p1minLoc, p2minLoc


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Please provide input file name on command line.')
    exit(1)
  inputFile = sys.argv[1]
  print('Input file is:', inputFile)
  ans1, ans2 = AdventOfCode(inputFile).DoWork()
  print('Answer Part 1:', ans1)
  print('Answer Part 2:', ans2)
