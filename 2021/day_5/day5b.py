import numpy as np
import math


#TODO: sumething is not right with my indexes, just made them bigger

def minMax(data):
    xMin = data[0][0]; xMax = data[0][0]
    yMin = data[0][1]; yMax = data[0][1]
    
    for point in data[1:]:
        xMin = min(xMin, point[0])
        xMax = max(xMax, point[0])
        yMin = min(yMin, point[1])
        yMax = max(yMax, point[1])

    return [xMin, xMax, yMin, yMax]


def findStraightLines(fromPoint, toPoint):
    
    entries = len(fromPoint)

    fromPoints = []
    toPoints = []
    for line in range(entries):
        if (toPoint[line][0] - fromPoint[line][0] == 0) or (toPoint[line][1] - fromPoint[line][1] == 0):
            fromPoints.append(fromPoint[line])
            toPoints.append(toPoint[line])

    return fromPoints, toPoints

def findIncrement(fromPoints, toPoints):

    increment = []
    entries = len(fromPoints)
    for line in range(entries):
        # find increment
        dx = toPoints[line][0] - fromPoints[line][0]
        if dx != 0:
            dx = dx/abs(dx)

        dy = toPoints[line][1] - fromPoints[line][1]
        if dy != 0:
            dy = dy/abs(dy)

        increment.append([int(dx), int(dy)])

    return increment

# Read and prepare data
# ---------------------

with open('input.txt') as f:
    data = f.readlines()

dataNew = []
for line in data:
    dataNew.append(line.split('->')) 
    dataNew = [[x[0].strip(), x[1].strip()] for x in dataNew]

fromPoints = []
toPoints = []
for line in dataNew:
    fromPoints.append(line[0].split(','))
    fromPoints = [[int(x[0]), int(x[1])] for x in fromPoints]

    toPoints.append(line[1].split(','))
    toPoints = [[int(x[0]), int(x[1])] for x in toPoints]

# Draw grid
# ---------
# Find max and min x and y
xMinFrom, xMaxFrom, yMinFrom, yMaxFrom = minMax(fromPoints)
xMinTo, xMaxTo, yMinTo, yMaxTo = minMax(toPoints)

xMin = min(xMinFrom, xMinTo)
xMax = max(xMaxFrom, xMaxTo)
yMin = min(yMinFrom, yMinTo)
yMax = max(yMaxFrom, yMaxTo)

# Grid
grid = np.zeros(((yMax - yMin + 100), (xMax - xMin + 100)))

# Filter to straight lines only
fromPoints, toPoints = findStraightLines(fromPoints, toPoints)  

# Find increments
increments = findIncrement(fromPoints, toPoints)

# Plot lines
for i in range(len(fromPoints)):

    print('Line:', i)

    point = fromPoints[i]

    run = True
    while run:
        print(toPoints[i], point[0], point[1])
        grid[point[1], point[0]] += 1

        if (point[0] == toPoints[i][0]) and (point[1] == toPoints[i][1]):
            run = False
        else:
            point[0] = point[0] + increments[i][0]
            point[1] = point[1] + increments[i][1] 



print(grid)

print('Answer:', len(grid[grid>=2]))