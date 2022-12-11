
class ReadAndSum(object):
  def __init__(self, fileName):
    self.fname = fileName

  def DoWork(self):
    cals = 0
    topThree = [0, 0, 0]

    fileGen = (row for row in open(self.fname, 'r'))
    for line in fileGen:
      line = line.strip('\n')
      if len(line) > 0:
        cals += int(line)
      else:
        for i in range(3):
          if cals > topThree[i]:
            topThree[i] = cals
            topThree.sort()
            #print(str(topThree))
            break
        cals = 0

    if cals > 0:
      for i in range(3):
        if cals > topThree[i]:
          topThree[i] = cals
          topThree.sort()
          #print(str(topThree))
          break

    print('Top three:', str(topThree))
    return sum(topThree)


if __name__ == '__main__':
  cals = ReadAndSum('input-day-1.txt').DoWork()
  print('Sum of top three:', cals)
