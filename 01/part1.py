from operator import sub

with open('input.txt', 'r') as file:
   data = [line.split() for line in file.read().split('\n')]

left_list = []
right_list = []

for element in data:
    left, right = element
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

print(sum(map(abs, (map(sub, left_list, right_list)))))