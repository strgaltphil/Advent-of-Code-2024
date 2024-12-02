def is_increasing(l: list):
   return all(i < j for i, j in zip(l, l[1:]))

def is_decreasing(l: list):
   return all(i > j for i, j in zip(l, l[1:]))

with open('input.txt', 'r') as file:
   data = [[int(x) for x in line.split()] for line in file.read().split('\n')]

safe_reports = 0

for d in data:
    if is_increasing(d):
        if all([(b - a) <= 3 for a, b in zip(d, d[1:])]):
            safe_reports += 1
 
    if is_decreasing(d):
        if all([(a - b) <= 3 for a, b in zip(d, d[1:])]):
            safe_reports += 1

print(safe_reports)