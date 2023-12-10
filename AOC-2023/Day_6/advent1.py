import sys

class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))


  def ComputeRace(self, time, distance):
    ways2win = 0
    for v in range(1, time):
      d = v * (time - v)
      if d > distance:
        ways2win += 1
    return ways2win


  def DoWork(self):
    times = next(self.fileGen).strip('\n').strip().split()[1:]
    times_p2 = int(''.join(times))
    times = [ int(x) for x in times ]
    distances = next(self.fileGen).strip('\n').strip().split()[1:]
    distances_p2 = int(''.join(distances))
    distances = [ int(x) for x in distances ]

    p1_result = 1
    for idx, time in enumerate(times):
      p1_result *= self.ComputeRace(time, distances[idx])

    p2_result = self.ComputeRace(times_p2, distances_p2)

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
