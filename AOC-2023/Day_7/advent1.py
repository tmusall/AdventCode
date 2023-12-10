import sys

class AdventOfCode(object):
  def __init__(self, fileName):
    self.fname = fileName
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.cardStrength = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2 }
    self.bidList = { }

  def HandValue(self, d):
    if len(d) == 1:
      return 7  # Five of a kind
    elif len(d) == 2:
      for k in d:
        if d[k] == 4:
          return 6  # Four of a kind
        if d[k] == 3:
          return 5  # Full house
    elif len(d) == 3:
      pairs = 0
      for k in d:
        if d[k] == 3:
          return 4  # Three of a kind
        if d[k] == 2:
          pairs += 1
      if pairs == 2:
        return 3  # Two pairs
    elif len(d) == 4:
      return 2  # One pair
    return 1  # High card


  def WildCard(self, d, rank):
    if 'J' in d:
      jokers = d['J']
      if jokers == 1:
        if rank in [6, 5, 1]:
          return rank + 1
        if rank in [4]:
          return 6
        if rank in [2]:
          return 4
        if rank in [3]:
          return 5
      elif jokers == 2:
        if rank in [5, 4]:
          return 7
        if rank in [3]:
          return 6
        if rank in [2]:
          return 4
      elif jokers == 3:
        if rank in [5]:
          return 7
        if rank in [4]:
          return 6
      elif jokers == 4:
        return 7
      elif jokers == 5:
        return 7
    return rank


  def HighCard(self, c1, c2):
    for i,c in enumerate(c1):
      char1 = self.cardStrength[c]
      char2 = self.cardStrength[c2[i]]
      if char1 > char2:
        return True
      if char1 != char2:
        return False


  def InsertBid(self, hand, bid, rank):
    if rank in self.bidList:
      for i, (h, b) in enumerate(self.bidList[rank]):
        if not self.HighCard(hand, h):
          self.bidList[rank].insert(i, (hand, bid))
          return
      self.bidList[rank].append((hand, bid))
    else:
      self.bidList[rank] = [(hand, bid)]


  def RankHand(self, hand, bid, jokerWild=False):
    rank = 1
    d = { }
    for c in hand:
      if c in d:
        d[c] += 1
      else:
        d[c] = 1

    r = self.HandValue(d)
    if jokerWild:
      r = self.WildCard(d, r)
    #print(hand, bid, r)
    self.InsertBid(hand, bid, r)
    #print(self.bidList)


  def DoWork(self):

    for line in self.fileGen:
      hand, bid = line.strip('\n').strip().split()
      bid = int(bid)
      self.RankHand(hand, bid)

    p1_result = 0
    cnt = 1
    sortedKeys = [ k for k in self.bidList.keys() ]
    sortedKeys.sort()

    for k in sortedKeys:
      for h, b in self.bidList[k]:
        p1_result += cnt * b
        cnt += 1

    # Part 2
    self.fileGen = (row for row in open(self.fname, 'r'))
    self.bidList = { }
    self.cardStrength['J'] = 1

    for line in self.fileGen:
      hand, bid = line.strip('\n').strip().split()
      bid = int(bid)
      self.RankHand(hand, bid, jokerWild=True)

    p2_result = 0
    cnt = 1
    sortedKeys = [ k for k in self.bidList.keys() ]
    sortedKeys.sort()

    for k in sortedKeys:
      for h, b in self.bidList[k]:
        p2_result += cnt * b
        cnt += 1

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
