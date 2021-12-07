import numpy as np

def minMax(data):
    xMin = data[0][0]; xMax = data[0][0]
    yMin = data[0][1]; yMax = data[0][1]
    
    for point in data[1:]:
        xMin = min(xMin, point[0])
        xMax = max(xMax, point[0])
        yMin = min(yMin, point[1])
        yMax = max(yMax, point[1])

    return [xMin, xMax, yMin, yMax]


def findVertLines(fromPoint, toPoint):
    entries = len(fromPoint)
    fromPoints = []
    toPoints = []
    for line in range(entries):
        if (toPoint[line][0] == fromPoint[line][0]):
            fromPoints.append(fromPoint[line])
            toPoints.append(toPoint[line])
    return fromPoints, toPoints

def findHorLines(fromPoint, toPoint):
    entries = len(fromPoint)
    fromPoints = []
    toPoints = []
    for line in range(entries):
        if (toPoint[line][1] == fromPoint[line][1]):
            fromPoints.append(fromPoint[line])
            toPoints.append(toPoint[line])
    return fromPoints, toPoints

def findDiagLines(fromPoint, toPoint):
    entries = len(fromPoint)
    fromPoints = []
    toPoints = []
    for line in range(entries):
        if (toPoint[line][0] != fromPoint[line][0]) and (toPoint[line][1] != fromPoint[line][1]):
            fromPoints.append(fromPoint[line])
            toPoints.append(toPoint[line])
    return fromPoints, toPoints


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

# find and add vertical lines
# ---------------------------
fromPointsV, toPointsV = findVertLines(fromPoints, toPoints)  

entities = len(fromPointsV)
for i in range(0, entities):
    point = fromPointsV[i].copy()
    run = True
    while run:
        grid[point[1], point[0]] += 1
        diff = toPointsV[i][1] - fromPointsV[i][1] 
        dh = int(diff / abs(diff))
        point[1] += dh

        if point[1] == toPointsV[i][1]:
            grid[toPointsV[i][1], toPointsV[i][0]] += 1
            run = False

# find and add horizontal lines
# -----------------------------
fromPointsH, toPointsH = findHorLines(fromPoints, toPoints)  

entities = len(fromPointsH)
for i in range(0, entities):
    point = fromPointsH[i].copy()
    run = True
    while run:
        grid[point[1], point[0]] += 1
        diff = toPointsH[i][0] - fromPointsH[i][0] 
        dh = int(diff / abs(diff))
        point[0] += dh

        if point[0] == toPointsH[i][0]:
            grid[toPointsH[i][1], toPointsH[i][0]] += 1
            run = False

# Find and add diagonal lines
# ---------------------------
# -----------------------------
fromPointsD, toPointsD = findDiagLines(fromPoints, toPoints) 

entities = len(fromPointsD)
for i in range(0, entities):
    point = fromPointsD[i].copy()
    run = True
    while run:
        grid[point[1], point[0]] += 1
        
        diffr = toPointsD[i][0] - fromPointsD[i][0] 
        dhr = int(diffr / abs(diffr))
        point[0] += dhr

        diffc = toPointsD[i][1] - fromPointsD[i][1] 
        dhc = int(diffc / abs(diffc))
        point[1] += dhc

        if (point[0] == toPointsD[i][0]) or (point[1] == toPointsD[i][1]):
            grid[toPointsD[i][1], toPointsD[i][0]] += 1
            run = False
        

print(grid)


print('Answer:', len(grid[grid>=2]))