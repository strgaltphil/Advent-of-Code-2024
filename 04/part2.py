import re
from operator import mul

with open('input.txt', 'r') as file:
   data = file.read()

mask = len(data) * '1'

dont_len = len("don't()")

dos = [element for element in re.finditer(r'do\(\)', data)]
donts = [element for element in re.finditer(r"don't\(\)", data)]


for dont in donts:
   next_do = next((do for do in dos if do.start() > dont.start()), None)
   
   start = dont.start()
   end = None
   if (next_do == None):
      end = len(data) - 1
   else:
      end = next_do.start()

   mask = ('0' * (end - start)).join([mask[:start], mask[end:]])

data = ''.join([z[0] for z in zip(list(data), list(mask)) if z[1] != '0'])

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
print(sum([int(match[0]) * int(match[1]) for match in matches]))