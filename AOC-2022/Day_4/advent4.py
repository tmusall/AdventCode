
class ReadAndWork(object):
  def __init__(self, partOne, fileName):
    self.partOne = partOne
    self.fname = fileName

  def DoWork(self):
    score = 0

    fileGen = (row for row in open(self.fname, 'r'))
    for line in fileGen:
      line = line.strip('\n').split(',')
      #print(line)
      r1 = line[0].split('-')
      s1 = { i for i in range(int(r1[0]), int(r1[1])+1) }
      r2 = line[1].split('-')
      s2 = { i for i in range(int(r2[0]), int(r2[1])+1) }
      #print(r1, s1)
      #print(r2, s2)

      isSubSet = s1.issubset(s2) or s2.issubset(s1)
      if self.partOne:
        # Part One...
        if isSubSet:
          score += 1
      else:
        # Part Two...
        if isSubSet or s1.intersection(s2) != set():
          score += 1

    return score


if __name__ == '__main__':
  partOne = True
  fileIndex = 1
  inputFile = ('sample.txt', 'advent4.txt')

  score = ReadAndWork(partOne, inputFile[fileIndex]).DoWork()
  print('Score:', score)
