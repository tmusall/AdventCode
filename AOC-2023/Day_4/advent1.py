
class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.cards = [ (0,0,0) ]


  def ExamineLine(self, text):
    cardNum = int(text.split(':')[0].split()[1])
    winning_player = text.split(':')[1].split('|')
    winning = winning_player[0].strip().split()
    player = winning_player[1].strip().split()
    matches = 0
    cardTotal = 0
    for n in player:
      if n in winning:
        cardTotal = 1 if cardTotal == 0 else cardTotal * 2
        matches += 1
    self.cards.append((matches, range(cardNum+1,cardNum+matches+1),cardNum))
    return cardTotal


  def CountCards(self, rng):
    cardCnt = 1
    for c in rng:
      nextRange = self.cards[c][1]
      cardCnt += self.CountCards(nextRange)
    return cardCnt


  def DoWork(self):
    sum = 0

    for line in self.fileGen:
      line = line.strip('\n')
      sum += self.ExamineLine(line)  # Part 1
                                     # Part 2
    cardCnt = self.CountCards(range(1, len(self.cards)))
    return sum, cardCnt-1


if __name__ == '__main__':
  #inputFile = 'sample.txt'
  inputFile = 'input.txt'
  ans1, ans2 = AdventOfCode(inputFile).DoWork()
  print('Answer Part 1:', ans1)
  print('Answer Part 2:', ans2)
