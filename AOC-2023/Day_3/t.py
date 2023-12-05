import re

def gen(t):
  txt = t
  while True:
    # txt = txt[i:]
    x = re.search('\d+', txt)
    if x != None:
      z = x.span()
      yield (z, x.group())
      s = ''
      for i in range(z[0],z[1]):
        s = s + '.'
      txt = txt[:z[0]] + s + txt[z[1]:]
    else:
      break

if __name__ == '__main__':
  line = "9....123....45...6"
  print(line)
  g = gen(line)
  for j,k in g:
    print(j,k)
