with open('input.txt', 'r') as file:
   data = [line.split() for line in file.read().split('\n')]

print(data)