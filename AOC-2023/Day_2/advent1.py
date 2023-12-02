
class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.RedGreenBlueCubes = { 'red':12, 'green':13, 'blue':14 }


  def CalcGamePower(self, text):
    cubeTotals = { 'red':0, 'green':0, 'blue':0 }
    samples = text.split(':')[1].split(';')
    for sample in samples:
      for cube in sample.split(','):
        cube = cube.strip().split(' ')
        count = int(cube[0])
        color = cube[1]
        if count > cubeTotals[color]:
          cubeTotals[color] = count

    power = 1
    for k,v in cubeTotals.items():
      if v > 0:
        power *= v
    return power


  def ExamineGame(self, text):
    game = int(text.split(':')[0].split(' ')[1])
    samples = text.split(':')[1].split(';')
    for sample in samples:
      cubeTotals = { 'red':0, 'green':0, 'blue':0 }
      for cube in sample.split(','):
        cube = cube.strip().split(' ')
        count = int(cube[0])
        color = cube[1]
        cubeTotals[color] = count
      for k,v in cubeTotals.items():
        if v > self.RedGreenBlueCubes[k]:
          return 0
    return game


  def DoWork(self):
    sum = 0
    power = 0

    for line in self.fileGen:
      line = line.strip('\n')
      sum += self.ExamineGame(line)  # Part 1
      power += self.CalcGamePower(line)  # Part 2

    return sum, power


if __name__ == '__main__':
  # ans1, ans2 = AdventOfCode('sample.txt').DoWork()
  ans1, ans2 = AdventOfCode('input.txt').DoWork()
  print('Answer Part 1:', ans1)
  print('Answer Part 2:', ans2)
