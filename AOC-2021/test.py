import numpy as np

field = np.array(list(map(list, """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".strip().split())))

moved = [True]
while any(moved[-2:]):
  for who,axis in ((">",1), ("v",0)):
    allowed_moves = (np.roll(field, -1, axis) == ".") & (field == who)
    moved.append(np.any(allowed_moves))
    field[allowed_moves] = "."
    field[np.roll(allowed_moves, 1, axis)] = who

print(len(moved)//2)
