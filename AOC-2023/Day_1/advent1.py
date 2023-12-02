
class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.digitWords = (('one', 'o1e'),
                       ('two', 't2o'),
                       ('three', 't3ree'),
                       ('four', 'f4ur'),
                       ('five', 'f5ve'),
                       ('six', 's6x'),
                       ('seven', 's7ven'),
                       ('eight', 'e8ght'),
                       ('nine', 'n9ne'))

  def MungeText(self, text):
    for word in self.digitWords:
      text = text.replace(word[0], word[1])
    return text

  def GetDigit(self, text, forward=True):
    iter = enumerate(text if forward else reversed(text))
    for k,c in iter:
      if c.isdigit():
        return c

  def DoWork(self):
    sum = 0

    for line in self.fileGen:
      line = line.strip('\n')
      line = self.MungeText(line)   # Part 2
      sum += int(self.GetDigit(line) + self.GetDigit(line, False))

    return sum


if __name__ == '__main__':
  # ans = AdventOfCode('sample.txt').DoWork()  # Part 1 sample
  # ans = AdventOfCode('sample2.txt').DoWork()  # Part 2 sample
  ans = AdventOfCode('input.txt').DoWork()
  print('Answer:', ans)
