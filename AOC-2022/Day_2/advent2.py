
class ReadAndSum(object):
  def __init__(self, fileName):
    self.fname = fileName

  def DoWork(self):
    # A/X - Rock
    # B/Y - Paper
    # C/Z - Scissors
    score = 0
    ties = { 'A': 'X',
             'B': 'Y',
             'C': 'Z' }

    wins = { 'A': 'Y',
             'B': 'Z',
             'C': 'X' }

    losses = { 'A': 'Z',
             'B': 'X',
             'C': 'Y' }

    points = { 'X':1, 'Y':2, 'Z':3 }

    trans = { 'X': 1, 'Y': 2, 'Z': 3 }

    fileGen = (row for row in open(self.fname, 'r'))
    for line in fileGen:
      line = line.strip('\n').split(' ')

      if line[1] == 'Z':
        counter = points[wins[line[0]]]
        score += counter + 6
      elif line[1] == 'Y':
        print(wins[line[0]])
        counter = points[ties[line[0]]]
        score += counter + 3
      else:
        counter = points[losses[line[0]]]
        score += counter + 0

      # for w in wins:
      #   if line == w:
      #     print(6 + points[line[1]])
      #     score += 6 + points[line[1]]
      #     flag = True
      #     break

      # tie
      # for t in ties:
      #   if line == t:
      #     print(3 + points[line[1]])
      #     score += 3 + points[line[1]]
      #     flag = True
      #     break

      # lose
      # print(0 + points[line[1]])
      # score += points[line[1]]

    return score


if __name__ == '__main__':
  # score = ReadAndSum('sample2.txt').DoWork()
  score = ReadAndSum('advent2.txt').DoWork()
  print('Score:', score)
