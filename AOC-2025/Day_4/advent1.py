import sys

class AdventOfCode(object):
  def __init__(self, fileName: str):
    self.fileGen = (row for row in open(fileName, 'r'))

  def CalcJoltage(self, bank: str) -> int:
    ans = 0

    for idx,digit in enumerate(bank):
      for x in (int(c) for c in bank[idx+1:]):
        prod = int(digit) * 10 + x
        ans = prod if prod > ans else ans

    return ans

  def CalcBigJoltage(self, bank: str) -> int:
    #print(bank)
    num_batteries = 12
    bank_digits = [int(d) for d in bank]  # Convert string to list of integers
    selected = []
    bank_index = -1  # Track the last selected index

    for _ in range(num_batteries):
      # Determine the valid slice: after last selected index, before the last 'remaining' positions
      end = len(bank_digits) - (num_batteries - len(selected)) + 1
      search_slice = bank_digits[bank_index + 1:end]

      # Find the maximum digit in the valid slice
      max_digit = max(search_slice)

      # Find the index of the first occurrence of this digit after the last selected index
      bank_index = bank_digits.index(max_digit, bank_index + 1)
      selected.append(max_digit)

    # Convert selected digits into a single integer
    ans = int("".join(map(str, selected)))
    #print(ans)
    return ans

  def DoWork(self):
    ansPart1 = 0
    ansPart2 = 0

    for line in self.fileGen:
      line = line.strip('\n')
      ansPart1 += self.CalcJoltage(line)
      ansPart2 += self.CalcBigJoltage(line)

    return ansPart1, ansPart2

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Please provide input file name on command line.')
    exit(1)
  inputFile = sys.argv[1]
  print('Input file is:', inputFile)
  ans1, ans2 = AdventOfCode(inputFile).DoWork()
  print('Answer Part 1:', ans1)
  print('Answer Part 2:', ans2)
