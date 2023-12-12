import sys

class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.dirString = ''
    self.nodes = { }


  def DirGen(self):
    while True:
      for c in self.dirString:
        yield (0 if c == 'L' else 1)


  def ProcLine(self, text):
    temp = text.split('=')
    key = temp[0].strip()
    temp = temp[1].split(',')
    lval = temp[0].strip(' (')
    rval = temp[1].strip(' )')
    self.nodes[key] = (lval,rval)


  def FindEndNode(self, startNode, endNode, dirGen):
    stepCnt = 0
    node = startNode

    for nextDir in dirGen:
      if node == endNode:
        break
      node = self.nodes[node][nextDir]
      stepCnt += 1
    return stepCnt


  def FindStartNodes(self, endsWith):
    nodeList = [ ]
    for k in self.nodes:
      if k[-1] == endsWith:
        nodeList.append(k)
    return nodeList


  def AllNodesEndWith(self, nodeList, endsWith):
    for n in nodeList:
      if n[-1] != endsWith:
        return False
    return True


  def FindEndNodes(self, startNodes, endsWith, dirGen):
    stepCnt = 0
    nodes = startNodes

    for nextDir in dirGen:
      if self.AllNodesEndWith(nodes, endsWith):
        break
      for i,n in enumerate(nodes):
        nodes[i] = self.nodes[n][nextDir]
      stepCnt += 1

    return stepCnt


  def DoWork(self):
    self.dirString = next(self.fileGen).strip('\n').strip()
    dirGen = self.DirGen()

    for line in self.fileGen:
      line = line.strip('\n').strip()
      if len(line) > 0:
        self.ProcLine(line)

    # Part 1
    p1_result = 0
    #p1_result = self.FindEndNode('AAA', 'ZZZ', dirGen)

    # Part 2
    startNodes = self.FindStartNodes('A')
    print(startNodes)
    p2_result = self.FindEndNodes(startNodes, 'Z', dirGen)

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
