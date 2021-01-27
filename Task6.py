from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

r = 0
for el in cycle("HEH"):
    if r > 15:
        break
    print(el)
    r += 1
