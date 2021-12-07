import statistics

def calcCost(distances, reference):
    cost = 0
    for distance in distances:
        cost += abs(distance - reference) 
    return cost


# Run problem
# -----------

with open('input.txt') as f:
    data = f.readlines()
data = [int(i) for i in data[0].split(',')]


# Find optimal value
# ------------------
# check up
loc = statistics.mode(data)
cost = calcCost(data, loc)
run = True
while run:
    loc += 1
    costNew = calcCost(data, loc)
    print(costNew)

    if costNew > cost:
        run = False
    else:
        cost = costNew

print(loc, cost)

# check down
loc = statistics.mode(data)
cost = calcCost(data, loc)
run = True
while run:
    loc -= 1
    costNew = calcCost(data, loc)

    if costNew > cost:
        run = False
    else:
        cost = costNew

print(loc, cost)
