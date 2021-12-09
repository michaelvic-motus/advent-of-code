import numpy as np


# Run problem
# -----------

# Create board
with open('test1_input.txt') as f:
    data = f.readlines()

dataNew = []
for row in data:
    row = [int(x) for x in row.strip()]
    dataNew.append(row)
data = np.array(dataNew)

print(data)


# Search for lowpoints
# --------------------
score = 0

# Search corners
corners = [data[0, 0], data[-1, 0], data[0, -1], data[-1,-1]]
adjCorners = [
    [data[0, 1], data[1, 0]], # left Top
    [data[-1, 1], data[-2, 0]], # left bottom
    [data[0, -2], data[1, -1]], # right top
    [data[-1, -2], data[-2, -1]]# right bottom
    ] 

for idx, corner in enumerate(corners):
    adj = np.array(adjCorners[idx])
    if len(adj[adj > corner]) == 2:
        score += 1 + corner
        #print(idx, corner, score)

# Search top
topRow = data[0, 1:-1]
print(topRow)

# search bottom

# Search left

# Search right


# Search centre

print('Score:', score)
