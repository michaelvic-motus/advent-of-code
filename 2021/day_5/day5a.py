
import numpy as np

# Run problem
# -----------

with open('test1_input.txt') as f:
    data = f.readlines()

dataNew = []
for line in data:
    dataNew.append(line.split('->')) 
    dataNew = [[x[0].strip(), x[1].strip()] for x in dataNew]

fromPoint = []
toPoint = []
for line in dataNew:
    fromPoint.append(line[0].split(','))
    fromPoint = [[int(x[0]), int(x[1])] for x in fromPoint]

    toPoint.append(line[1].split(','))
    toPoint = [[int(x[0]), int(x[1])] for x in toPoint]

print(fromPoint)
print(toPoint)

# Draw grid
# ---------
# Find max and min x and y
xMin = fromPoint[0][0]; xMax = fromPoint[0][0]
yMin = fromPoint[0][1]; yMax = fromPoint[0][1]
for point in fromPoint[1:]:
    xMin = min(xMin, point[0])
    xMax = max(xMax, point[0])
    yMin = min(yMin, point[1])
    yMax = max(yMax, point[1])

for point in toPoint[0:]:
    xMin = min(xMin, point[0])
    xMax = max(xMax, point[0])
    yMin = min(yMin, point[1])
    yMax = max(yMax, point[1])

# Grid
grid = np.zeros((xMax - xMin, yMax - yMin))

# Process Lines horizontal and vertical only
delta = [0, 0]
for i in range(len(fromPoint)):
    delta[0] = toPoint[i][0] - fromPoint[i][0]
    delta[1] = toPoint[i][1] - fromPoint[i][1]
    

    if 0 in delta:
        print(toPoint[i], fromPoint[i])

    # Draw lines