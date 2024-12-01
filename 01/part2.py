with open('input.txt', 'r') as file:
   data = [line.split() for line in file.read().split('\n')]

left_list = []
right_list = []

for element in data:
    left, right = element
    left_list.append(int(left))
    right_list.append(int(right))

print(sum([right_list.count(number) * number for number in left_list]))