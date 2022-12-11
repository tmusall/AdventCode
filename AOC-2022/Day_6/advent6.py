
class ReadAndWork(object):
  def __init__(self, partOne, fileName):
    self.partOne = partOne
    self.fname = fileName

  def DoWork(self):
    score = None
    winSize = 4 if self.partOne else 14
    fileGen = (row for row in open(self.fname, 'r'))
    for line in fileGen:
      line = line.strip('\n')

      limit = len(line) - winSize
      idx = 0

      for i in range(limit):
        s = set(line[idx:idx+winSize:1])
        if len(s) == winSize:
          score = idx+winSize
          break
        idx += 1

    return score


if __name__ == '__main__':
  partOne = True
  fileIndex = 1
  inputFile = ('sample.txt', 'advent6.txt')

  score = ReadAndWork(True, inputFile[fileIndex]).DoWork()
  print('Part 1 Score:', score)
  score = ReadAndWork(False, inputFile[fileIndex]).DoWork()
  print('Part 2 Score:', score)
