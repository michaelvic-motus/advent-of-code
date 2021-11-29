
with open('directions.txt', 'r') as file:
    directions = file.readlines()
    
floor = 0

ups = directions[0].count('(')
downs = directions[0].count(')')

print('floor is:', ups-downs)