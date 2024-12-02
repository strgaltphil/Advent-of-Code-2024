def is_increasing(l: list):
   return all(i < j for i, j in zip(l, l[1:]))

def is_decreasing(l: list):
   return all(i > j for i, j in zip(l, l[1:]))

with open('input.txt', 'r') as file:
   data = [[int(x) for x in line.split()] for line in file.read().split('\n')]

safe_reports = 0

for d in data:
    for i in range(len(d)):
        d_copy = list(d)
        del d_copy[i]
        found_solution = False

        if is_increasing(d_copy):
            if all([(b - a) <= 3 for a, b in zip(d_copy, d_copy[1:])]):
                found_solution = True
    
        if is_decreasing(d_copy):
            if all([(a - b) <= 3 for a, b in zip(d_copy, d_copy[1:])]):
                found_solution = True

        if found_solution:
            safe_reports += 1
            break

print(safe_reports)